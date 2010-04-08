from zope.interface import Interface


class IDevice(Interface):

    user_agent = """ User agent attribute """

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


class IDeviceType(Interface):
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
