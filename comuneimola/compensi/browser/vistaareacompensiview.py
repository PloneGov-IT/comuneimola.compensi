from zope.interface import implements, Interface
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from comuneimola.compensi.interfaces.atareacompensi import IMoneyFormat
from zope.component import getUtility


class IVistaareacompensiView(Interface):
    """
    vistaareacompensi view interface
    """

    def contenuti_folder():
        """ test method"""

    def show_export_button():
        """ policy to decide how can see the button"""


class vistaareacompensiView(BrowserView):
    """
    vistaareacompensi browser view
    """
    implements(IVistaareacompensiView)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.mf = getUtility(IMoneyFormat)

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    def contenuti_folder(self):
        path = '/'.join(self.context.getPhysicalPath())
        query = {'path': {'query': path, 'depth': 1}}
        brains = self.portal_catalog(**query)
        return brains

    def show_export_button(self):
        """
        Right now, everybody can see it
        """
        return True

    def get_money_format(self, value):
        """
        call the money format utility and convert the value
        """
        return self.mf.moneyfmt(value)
