"""Definition of the ATCompenso content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from comuneimola.compensi.interfaces.atcompenso import IATCompenso
from comuneimola.compensi.config import PROJECTNAME
#from comuneimola.compensi import compensiMessageFactory as _


ATCompensoSchema = folder.ATFolderSchema.copy() + atapi.Schema((


))

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

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(ATCompenso, PROJECTNAME)
