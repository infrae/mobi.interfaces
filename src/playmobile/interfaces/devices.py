from zope.interface import Interface


class IDevice(Interface):

    def get_type():
        """ return a IDeviceType marker interface
        """


class IClassifier(Interface):
    """ Device factory
    """
    def __init__(user_agent_string):
        """ get the user agent string
        """

    def __call__():
        """ return a device
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
