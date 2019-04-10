# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Hello(Component):
    """A Hello component.


Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks
- label (string; required): A label that will be printed when this component is rendered.
- value (string; optional): The value displayed in the input
- steps (list; optional): List of dictionaries containing each step, with "intro" and "element"
keys, at a minimum."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, label=Component.REQUIRED, value=Component.UNDEFINED, steps=Component.UNDEFINED, stepsEnabled=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'label', 'value', 'steps']
        self._type = 'Hello'
        self._namespace = 'musicfox_dash_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'label', 'value', 'steps']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['label']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Hello, self).__init__(**args)