from zope.interface import Interface
import zope.schema.interfaces
from zope.schema import TextLine


class ILocation(zope.schema.interfaces.ITuple):
    """ GPS location schema field
    """


class IPhoneNumber(zope.schema.interfaces.ITextLine):
    """ Phone number schema field
    """


class IAddress(Interface):
    """ Interface to present an address
    """

    title       = TextLine(title=u"Title", description=u"The title of "\
    u"the address may be used for display")
    street      = TextLine(title=u"Street address and number")
    postal_code = TextLine(title=u"Postal Code")
    city        = TextLine(title=u"City")
    country     = TextLine(title=u"Country")
