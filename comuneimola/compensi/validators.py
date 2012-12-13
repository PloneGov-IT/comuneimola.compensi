# -*- coding: utf-8 -*-
from Products.validation.interfaces.IValidator import IValidator
from zope.interface import implements
from comuneimola.compensi import compensiMessageFactory as _
from Products.Archetypes.interfaces import IObjectPostValidation
from comuneimola.compensi.interfaces.atcompenso import IATCompenso
from comuneimola.compensi import compensiMessageFactory as mf
from zope.component import adapts
from zope.i18n import translate
import sys


class FloatValidator:
    """
    Validator for amount
    """
    if sys.version_info[:2] >= (2, 6):
        implements(IValidator)
    else:
        __implements__ = (IValidator,)

    def __init__(self, name):
        self.name = name

    def __call__(self, value, *args, **kwargs):
        """
        Use hardening_tool to check if given file has a valid mimetype
        """
        instance = kwargs.get('instance', None)
        if not instance:
            return True
        try:
            float(value)
        except:
            return translate(mf('wrong_value_error'),
                   context=kwargs.get('instance').REQUEST)
        return True


class CompensiPostValidation(object):
    implements(IObjectPostValidation)
    adapts(IATCompenso)

    def __init__(self, context):
        self.context = context

    def __call__(self, request):
        """Validate the context object. Return a dict with keys of fieldnames
        and values of error strings.
        """
        norm = request.get('norm')
        other_norm = request.get('other_norm')
        if norm == 'other' and other_norm.strip() == '':
            return {'other_norm': _(u"If you select 'other' in the previous form, you must write something here.")}
        return {}
