# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Twash(Component):
    """A Twash component.
Twash, A Twitter Profile Timeline component for Dash from
musicfox.io.

This component uses react-twitter-widgets under the hood.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks
- sourceType (string; optional): String 'profile' is all for now
- handle (string; required): String user name or public handle, e.g. ArianaGrande
- height (number; optional): Integer height (in pixels)
- width (number; optional): Integer width (in pixels)
- theme (a value equal to: 'dark', 'light'; optional): * With dark or light theme
- linkColor (string; optional): * With custom link colors. Note: Only Hex colors are supported.
- borderColor (string; optional): * With custom border colors. Note: Only Hex colors are supported.
- noHeader (boolean; optional): * Hide the header from timeline
- noFooter (boolean; optional): * Hide the footer from timeline
- noBorders (boolean; optional): * Hide the border from timeline
- noScrollbar (boolean; optional): * Hide the scrollbars
- transparent (boolean; optional): * Enable Transparancy
- lang (string; optional): * Custom language code. Supported codes here: https://developer.twitter.com/en/docs/twitter-for-websites/twitter-for-websites-supported-languages/overview.html"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, sourceType=Component.UNDEFINED, handle=Component.REQUIRED, height=Component.UNDEFINED, width=Component.UNDEFINED, theme=Component.UNDEFINED, linkColor=Component.UNDEFINED, borderColor=Component.UNDEFINED, noHeader=Component.UNDEFINED, noFooter=Component.UNDEFINED, noBorders=Component.UNDEFINED, noScrollbar=Component.UNDEFINED, transparent=Component.UNDEFINED, lang=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'sourceType', 'handle', 'height', 'width', 'theme', 'linkColor', 'borderColor', 'noHeader', 'noFooter', 'noBorders', 'noScrollbar', 'transparent', 'lang']
        self._type = 'Twash'
        self._namespace = 'musicfox_dash_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'sourceType', 'handle', 'height', 'width', 'theme', 'linkColor', 'borderColor', 'noHeader', 'noFooter', 'noBorders', 'noScrollbar', 'transparent', 'lang']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['handle']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Twash, self).__init__(**args)
