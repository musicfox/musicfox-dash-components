# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ToDo(Component):
    """A ToDo component.
A component that renders a bootstrap card with Github Markdown bullet points, the
ToDo component from musicfox.io. Optionally include a title, subtitle, and/or footer.

This component uses [react-markdown](https://rexxars.github.io/react-markdown/)
under the hood, in the same fashion as the Dash Core Components Markdown component.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks
- todos (list; optional): A todo list.

Enter the actual "todos" you have here as a list of strings or key-value pairs 
consisting of strings=['another list', {'orAnother':['string-key:list-value', 'pairs']}].

These will be your "bullet points" in the typical "list".

Markdown all the way.
- title (string; optional): The string title you'd like to include. Markdown all the way.
- subtitle (string; optional): The string subtitle you'd like to include. Markdown all the way.
- footer (string; optional): The string footer you'd like to include. Markdown all the way.
- header (string; optional): The string header you'd like to include. Markdown all the way.
- dangerously_allow_html (boolean; optional): Boolean True or False (default)

True will allow Markdown HTML rendering but leave your clients exposed to XSS attacks.

Don't do this. But I'm into freedom; just don't blame ToDo when things go awry.
- loading_state (optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading
- containerProps (dict; optional): An object containing custom element props to put on the container
element such as id or style"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, todos=Component.UNDEFINED, title=Component.UNDEFINED, subtitle=Component.UNDEFINED, footer=Component.UNDEFINED, header=Component.UNDEFINED, dangerously_allow_html=Component.UNDEFINED, loading_state=Component.UNDEFINED, containerProps=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'todos', 'title', 'subtitle', 'footer', 'header', 'dangerously_allow_html', 'loading_state', 'containerProps']
        self._type = 'ToDo'
        self._namespace = 'musicfox_dash_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'todos', 'title', 'subtitle', 'footer', 'header', 'dangerously_allow_html', 'loading_state', 'containerProps']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ToDo, self).__init__(**args)
