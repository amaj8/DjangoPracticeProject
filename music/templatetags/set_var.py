from django import template

register = template.Library()

class SetVarNode(template.Node):

    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

    def render(self, context):
        try:
            value = template.Variable(self.var_value).resolve(context)
        except template.VariableDoesNotExist:
            value = ""
        context[self.var_name] = self.var_value
        return u''

def set_var(parser, token):
    """
        {% set <var_name>  = <var_value> %}
    """
    parts = token.split_contents()
    #parts = token.contents.split()
    #parts = token.split(None,3)
    if len(parts) < 4:
        raise template.TemplateSyntaxError("'set' tag must be of the form:  {% set <var_name>  = <var_value> %}")
    return SetVarNode(parts[1], parts[3][1:-1])

register.tag('set', set_var)