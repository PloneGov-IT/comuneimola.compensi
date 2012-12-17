# -*- coding: utf-8 -*-

from zope.interface import implements, Interface
from Products.Five.browser import BrowserView
from Products.CMFPlone.utils import getSiteEncoding
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import normalizeString
from DateTime import DateTime
from zope.interface.interfaces import IInterface
from ZPublisher.Iterators import IStreamIterator
from comuneimola.compensi import compensiMessageFactory as mf
from comuneimola.compensi.interfaces.atareacompensi import IMoneyFormat
from zope.component import getUtility
from zope.i18n import translate
import csv
import os
import tempfile
import shutil
import codecs


class ICsvExport(Interface):

    def get_elements(objects=False):
        """
        @description: this method should return all the element we want export;
        in this poin we can decide to use brains or objects
        """

    def get_query():
        """
        @description: here we decide which object should find in the folder so,
        objects to export
        """

    def write_element(writer, element):
        """
        @description: take an element, a connection to a csv writer and write
        the row for the current element
        """

    def write_elements_to_csv(element_to_export):
        """
        @description: take elements and export them to a csv file
        """

    def get_fields():
        """
        @description: get all the fields we want export
        """


NAME_MAPPING = {'title': 'Titolo',
                'fiscal_data': 'Dati fiscali',
                'amount': 'Importo (€)'.decode('utf-8').encode('utf-8'),
                'amount_type': 'Natura dell\'importo',
                'norm': 'Norma',
                'other_norm': 'Altro',
                'office': 'Ufficio',
                'responsible': 'Responsabile procedimento',
                'award_procedures': 'Modalità di affidamento'.decode('utf-8').encode('utf-8'),
                'effectiveDate': 'Data di pubblicazione',
                'note': 'Note',
                }


class CsvExport(BrowserView):
    implements(ICsvExport)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.response = self.request.RESPONSE
        self.encoding = getSiteEncoding(self.context)
        self.delimiter = ';'
        self.stringdelimiter = '"'
        date = DateTime().strftime("%Y%m%d_%H%M")
        folder_title = normalizeString(self.context.Title(),
                                       encoding=self.encoding)
        self.filename = date + '_' + folder_title + '.csv'
        self.moneyfmt = getUtility(IMoneyFormat)

    def __call__(self):
        tmp = tempfile.mkdtemp()
        tmppath = tempfile.mkdtemp(dir=tmp)
        csvpath = os.path.join(tmppath, self.filename)
        csvstream = open(csvpath, 'w')
        csvstream.write(codecs.BOM_UTF8)

        elements_to_export = self.get_elements(objects=True)
        self.write_elements_to_csv(csvstream, elements_to_export)

        csvstream.flush()
        csvstream.close()

        streamed = EphemeralStreamIterator(csvpath, delete_parent=True,)

        self.response.setHeader('Content-type',
                                'text/csv;charset=' + self.encoding)
        self.response.setHeader('Content-Disposition',
                                "attachment; filename=" + self.filename)

        self.response.setHeader('Content-Length', str(len(streamed)))
        return streamed

    def write_element(self, writer, element):
        values = []
        addvalue = values.append
        for field in self.get_fields:
            value = element.getField(field).get(element)
            if field == 'effectiveDate':
                if value:
                    value = value.strftime('%d/%m/%Y')
            if field == 'amount':
                value = self.moneyfmt.moneyfmt(value)
            if field == 'norm':
                if value == 'other':
                    value = translate(mf('other'), context=self.request)
            if value:
                addvalue(value)
            else:
                addvalue(u"")
        writer.writerow(values)
        return

    def write_elements_to_csv(self, csvstream, elements_to_export):
        writer = csv.writer(csvstream,
                            delimiter=self.delimiter,
                            quotechar=self.stringdelimiter,
                            quoting=csv.QUOTE_NONNUMERIC)

        encoded_field_names = [NAME_MAPPING[field] for field in self.get_fields]
        writer.writerow(encoded_field_names)

        for element in elements_to_export:

            if element == self.context:
                continue

            self.write_element(writer, element)

        return

    @property
    def get_fields(self):
        return ['title',
                'fiscal_data',
                'amount',
                'amount_type',
                'norm',
                'other_norm',
                'office',
                'responsible',
                'award_procedures',
                'effectiveDate',
                'note',
                ]

    @property
    def get_query(self):
        path = '/'.join(self.context.getPhysicalPath())
        return {'portal_type': 'ATCompenso',
                'review_state': 'published',
                'path': {'query': path,
                         'depth': 1}
                }

    def get_elements(self, objects=False):
        pc = getToolByName(self.context, 'portal_catalog')
        brains = pc(**self.get_query)
        if objects:
            return [brain.getObject() for brain in brains]
        return brains


# Next code is taken from Products.csvreplicata. We don't use directly this
# product 'cause I want keep things as simple as possible

# badly stolen ideas from dexterity
# see https://svn.plone.org/svn/plone/plone.dexterity/trunk/plone/dexterity/filerepresentation.py

class FileStreamIterator(object):
    """Simple stream iterator to allow efficient data streaming.
    """

    # Stupid workaround for the fact that on Zope < 2.12, we don't have
    # a real interface
    if IInterface.providedBy(IStreamIterator):
        implements(IStreamIterator)
    else:
        __implements__ = (IStreamIterator,)

    def __init__(self, path, size=None, chunk=1 << 16):
        """Consume data (a str) into a temporary file and prepare streaming.

        size is the length of the data. If not given, the length of the data
        string is used.

        chunk is the chunk size for the iterator
        """
        self.path = path
        self.file = open(path)
        self.file.seek(0)
        self.size = os.stat(path).st_size
        self.chunk = chunk

    def __iter__(self):
        return self

    def next(self):
        data = self.file.read(self.chunk)
        if not data:
            self.file.close()
            raise StopIteration
        return data

    def __len__(self):
        return self.size


class EphemeralStreamIterator(FileStreamIterator):
    """File and maybe its parent directory is deleted when readed"""

    def __init__(self, path, size=None, chunk=1 << 16,
                 delete_parent=False, delete_grand_parent=False):
        FileStreamIterator.__init__(self, path, size, chunk)
        self.delete_parent = delete_parent
        self.delete_grand_parent = delete_grand_parent

    def next(self):
        try:
            return FileStreamIterator.next(self)
        except:
            os.unlink(self.path)
            if self.delete_parent:
                shutil.rmtree(os.path.dirname(self.path))
            if self.delete_grand_parent:
                shutil.rmtree(os.path.dirname(os.path.dirname(self.path)))
            raise
