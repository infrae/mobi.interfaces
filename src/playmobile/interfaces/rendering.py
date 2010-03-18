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

    page = Attribute('')

    def update():
        """ Prepare the view
        """

    def render():
        """ render widget content this method is optional
        """


class IPage(IWidget):
    """ A page
    """

    def register_resource(namespace):
        """ register a resource for the namespace to be rendered later
        """

    def render_resources(namespace):
        """ render resources for the namespace
        """


class IFieldWidget(IWidget):
    """ widget to render a zope.schema field
    """
    def get_value():
        """ return value of the field
        """


class IResource(Interface):

    def __eq__():
        """ method to compare resources to keep them unique
        """

    def __call__():
        """ render the resource
        """


class IHTMLTagResource(IResource):
    """ a resource which is a html tag (e.g: link)
    """


