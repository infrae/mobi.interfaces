# Copyright (c) 2010 Infrae. All rights reserved.
# See also LICENSE.txt.
from zope.interface import Interface, Attribute
import logging
logger = logging.getLogger('mobi.interfaces')

try:
    from zope.publisher.interfaces.browser import IBrowserSkinType
except (ImportError,):
    logger.info('zope.publisher package not found, redeclare IBrowserSkinType')
    from zope.interface.interfaces import IInterface
    class IBrowserSkinType(IInterface):
        pass


class IDevice(Interface):
    user_agent = Attribute("User agent attribute")
    type = Attribute("a IDeviceType marker interface")
    platform = Attribute("Platform the device runs on")


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
