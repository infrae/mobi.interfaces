from zope.interface import Interface, Attribute

class IRenderingEngine(Interface):

    name = Attribute('name of the template, [a-zA-Z_] only')

    def get_base_path():
        """ return FS base path for template of the skin
        """

    def lookup_template(widget, name):
        """ return a template path or return None
        """

    def render_widget(widget, request):
        """ render the widget with this skin
        """


class IWidget(Interface):
    """ Widget base interface
    """
    def render():
        """ render widget content
            attributes are added to the first
            tag of the widget
        """


class IFieldWidget(IWidget):
    """ widget to render a zope.schema field
    """
    def get_value():
        """ return value of the field
        """
