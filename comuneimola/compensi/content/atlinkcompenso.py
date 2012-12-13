from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import link

from comuneimola.compensi.interfaces.atlinkcompenso import IATLinkCompenso
from comuneimola.compensi.config import PROJECTNAME

ATLinkCompensoSchema = link.ATLinkSchema.copy()


class ATLinkCompenso(link.ATLink):
    """Area Compensi"""
    implements(IATLinkCompenso)

    portal_type = "ATLinkCompenso"
    meta_type = "ATLinkCompenso"
    schema = ATLinkCompensoSchema


atapi.registerType(ATLinkCompenso, PROJECTNAME)
