"""Definition of the ATAreaCompensi content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from comuneimola.compensi.interfaces.atareacompensi import IATAreaCompensi
from comuneimola.compensi.config import PROJECTNAME
from comuneimola.compensi import compensiMessageFactory as _

ATAreaCompensiSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    atapi.LinesField(name='elenco_uffici',
        widget=atapi.LinesWidget(
            label=_(u"office_list",
                    default=u"Office List"),
            description=_(u"office_list_description",
                          default=u"List here offices for current area"),
            ),
        required=False,
    ),
    atapi.LinesField(name='modalita_affidamento',
        widget=atapi.LinesWidget(
            label=_(u"award_procedures_label",
                    default=u"Procedures for the award"),
            description=_(u"relied_modality_description",
                          default=u"List here the procedures for the award"),
            ),
        required=False,
    ),
    atapi.LinesField(name='natura_importo',
        widget=atapi.LinesWidget(
            label=_(u"type_of_amount_label",
                    default=u"Type of amount"),
            description=_(u"type_of_amount_description",
                          default=u"List here the types of amount"),
            ),
        required=False,
    ),
    atapi.LinesField(name='norma_o_titolo',
        widget=atapi.LinesWidget(
            label=_(u"type_of_norm",
                    default=u"Type of norm or title"),
            description=_(u"type_of_norm_description",
                          default=u"List here the norm or title"),
            ),
        required=False,
    ),

))

ATAreaCompensiSchema['title'].storage = atapi.AnnotationStorage()
ATAreaCompensiSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    ATAreaCompensiSchema,
    folderish=True,
    moveDiscussion=False
)


class ATAreaCompensi(folder.ATFolder):
    """Area Compensi"""
    implements(IATAreaCompensi)

    portal_type = "ATAreaCompensi"
    meta_type = "ATAreaCompensi"
    schema = ATAreaCompensiSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

atapi.registerType(ATAreaCompensi, PROJECTNAME)
