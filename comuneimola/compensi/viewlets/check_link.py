from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class CheckLink(ViewletBase):
    """
    Show alert message if we don't have links
    """
    render = ViewPageTemplateFile('check_link.pt')
