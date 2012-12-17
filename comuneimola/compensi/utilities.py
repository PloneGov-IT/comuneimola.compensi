from zope.interface import implements
from comuneimola.compensi.interfaces.atareacompensi import IMoneyFormat
from decimal import Decimal


class MoneyFormat(object):
    implements(IMoneyFormat)

    def moneyfmt(self, value, places=2, curr='', sep='.', dp=',',
                 pos='', neg='-', trailneg=''):
        """
        directly from python docs:
        http://docs.python.org/2/library/decimal.html#recipes
        Convert Decimal to a money formatted string.

        places:  required number of places after the decimal point
        curr:    optional currency symbol before the sign (may be blank)
        sep:     optional grouping separator (comma, period, space, or blank)
        dp:      decimal point indicator (comma or period)
                 only specify as blank when places is zero
        pos:     optional sign for positive numbers: '+', space or blank
        neg:     optional sign for negative numbers: '-', '(', space or blank
        trailneg:optional trailing minus indicator:  '-', ')', space or blank
        """
        value = Decimal(value)
        q = Decimal(10) ** -places  # 2 places --> '0.01'
        sign, digits, exp = value.quantize(q).as_tuple()
        result = []
        digits = map(str, digits)
        build, next = result.append, digits.pop
        if sign:
            build(trailneg)
        for i in range(places):
            if digits:
                build(next())
            else:
                build(0)
            #build(next() if digits else '0')
        build(dp)
        if not digits:
            build('0')
        i = 0
        while digits:
            build(next())
            i += 1
            if i == 3 and digits:
                i = 0
                build(sep)
        build(curr)
        #build(neg if sign else pos)
        if sign:
            build(neg)
        else:
            build(pos)
        return ''.join(reversed(result))
