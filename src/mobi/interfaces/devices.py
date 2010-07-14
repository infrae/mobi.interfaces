from zope.interface import Interface, Attribute
import logging
logger = logging.getLogger('mobi.devices')

try:
    from zope.publisher.interfaces.browser import IBrowserSkinType
except (ImportError,):
    logger.info('zope.publisher package not found, redeclare IBrowserSkinType')
    from zope.interface.interfaces import IInterface
    class IBrowserSkinType(IInterface):
        pass


class IDevice(Interface):

    user_agent = Attribute(""" User agent attribute """)

    def get_type():
        """ return a IDeviceType marker interface
        """

    def get_platform():
        """ return the platform
        """


class IClassifier(Interface):
    """ Device factory
    """

    def __call__(user_agent):
        """ return a IDevice object
        """


class IDeviceType(IBrowserSkinType):
    """ Base class for device types
    """


class IBasicDeviceType(IDeviceType):
    """ Really basic html browser
    """


class IStandardDeviceType(IBasicDeviceType):
    """ device with decent html/css browser
    """


class IAdvancedDeviceType(IStandardDeviceType):
    """ Full Javascript/XHTML/CSS browser device : Android, iPhone
    """
