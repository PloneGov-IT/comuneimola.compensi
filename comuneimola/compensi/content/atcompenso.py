"""Definition of the ATCompenso content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.Archetypes.utils import DisplayList
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from comuneimola.compensi.interfaces.atcompenso import IATCompenso
from comuneimola.compensi.config import PROJECTNAME
from comuneimola.compensi import compensiMessageFactory as _

ATCompensoSchema = folder.ATFolderSchema.copy() + atapi.Schema((
    atapi.StringField('fiscal_data',
        required=False,
        widget = atapi.StringWidget(
            label=_(u'fiscal_data_label', default=u'Tax code or VAT number'),
            description=_(u'fiscal_data_help', default=u"Insert your tax code or your VAT number"),
            size=60,
            ),
    ),

    atapi.StringField('amount',
        required=True,
        widget = atapi.StringWidget(
            label=_(u'amount_label', default=u'Amount'),
            description=_(u'amount_help', default=u"Insert the amount of remuneration"),
            size=40,
            ),
    ),

    atapi.StringField('norm',
        required=True,
        storage = atapi.AnnotationStorage(migrate=True),
        widget=atapi.StringWidget(
            label=_(u'norm_label', default=u'Norm'),
            description=_(u'norm_help', default=u"Insert a short text to describe the norm. (max 60 characters)"),
            maxlength=60,
            size=70,
            ),
    ),

    atapi.StringField('office',
        required=True,
        vocabulary='officeVocab',
        widget=atapi.SelectionWidget(
            label=_(u'office_label', default=u'Office'),
            description=_(u'office_help', default=u"Select the office responsible"),
            ),
    ),

    atapi.StringField('responsible',
        required=True,
        widget = atapi.StringWidget(
            label=_(u'responsible_label', default=u'Charge of the procedure'),
            description=_(u'responsible_help', default=u"Specify the name of the charge of the procedure"),
            size=50,
            ),
    ),

    atapi.StringField('award_procedures',
        required=True,
        vocabulary='awardProceduresVocab',
        widget=atapi.SelectionWidget(
            label=_(u'award_procedures_label', default=u'Procedures for the award'),
            description=_(u'award_procedures_help', default=u"Select the award procedures"),
            ),
    ),

    atapi.TextField('note',
        required=False,
        storage = atapi.AnnotationStorage(migrate=True),
        widget = atapi.TextAreaWidget(
            label=_(u'note_label', default=u'Note'),
            rows=4,
            maxlength=256,
            ),
    ),

))

ATCompensoSchema['title'].widget.label = _(u'label_title',default=u'Name of the enterprise')
ATCompensoSchema['description'].widget.visible = False

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.
ATCompensoSchema['title'].storage = atapi.AnnotationStorage()
ATCompensoSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    ATCompensoSchema,
    folderish=True,
    moveDiscussion=False
)

class ATCompenso(folder.ATFolder):
    """AT Compenso"""
    implements(IATCompenso)

    portal_type = "ATCompenso"
    meta_type = "ATCompenso"
    schema = ATCompensoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    def officeVocab(self):
        """ """
        offices = DisplayList()
        offices.add('',_(u'-- not specified --'))
        for office in self.aq_parent.getElenco_uffici():
            offices.add(office, office)
        return offices

    def awardProceduresVocab(self):
        """ """
        award_procedures = DisplayList()
        award_procedures.add('',_(u'-- not specified --'))
        for award_procedure in self.aq_parent.getModalita_affidamento():
            award_procedures.add(award_procedure, award_procedure)
        return award_procedures

atapi.registerType(ATCompenso, PROJECTNAME)
