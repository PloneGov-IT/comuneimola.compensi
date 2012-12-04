from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName


class IVistacompensiView(Interface):
    """
    vistacompensi view interface
    """

    def test():
        """ test method"""


class vistacompensoView(BrowserView):
    """
    vistacompensi browser view
    """
    implements(IVistacompensiView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

