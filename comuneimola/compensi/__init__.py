"""Main product initializer
"""

from comuneimola.compensi import config

from Products.Archetypes import atapi
from Products.CMFCore import utils

from zope.i18nmessageid import MessageFactory
compensiMessageFactory = MessageFactory('comuneimola.compensi')

from Products.validation import validation
from validators import FloatValidator
validation.register(FloatValidator('isFloat'))



def initialize(context):
    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.PROJECTNAME),
        config.PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit('%s: %s' % (config.PROJECTNAME, atype.portal_type),
            content_types=(atype, ),
            permission=config.ADD_PERMISSIONS[atype.portal_type],
            extra_constructors=(constructor,),
            ).initialize(context)
