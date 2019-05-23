# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Hello(Component):
    """A Hello component.
A component that leverages intro.js under the hood to provide the Hello component
from musicfox.io. Include the steps you'd like to highlight and more.

This component uses [intro.js](https://intro.js.com/) and thus far most endpoints for Steps
are implemented.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks
- steps (list; required): List of dictionaries containing each step, with "intro" and "element"
keys, at a minimum.
- nextLabel (string; optional): nextLabel

String label for the "next" button
- prevLabel (string; optional): prevLabel

String label for the "prev" button
- skipLabel (string; optional): skipLabel 

String label for the "skip" button
- doneLabel (string; optional): doneLabel

String label for the "done" button
- hidePrev (boolean; optional): hidePrev

Boolean true to hide "prev" button in the first step, default is false, 
disabled (grayed-out).
- hideNext (boolean; optional): hideNext

Boolean true to hide "next" button in the last step, default is false,
disabled (grayed-out).
- defaultTooltipPos (string; optional): defaultTooltipPos

String default tooltip position (these can be changed per-step)
- tooltipClass (string; optional): tooltipClass

String class of all tooltip CSS
- highlightClass (string; optional): highlightClass

String class of all highlight over tooltip CSS (for the helperLayer) in
intro.js
- exitOnEsc (boolean; optional): exitOnEsc

Boolean true exits with an esc keypress, defaults to true
- exitOnOverlayClick (boolean; optional): exitOnOverlayClick

Boolean true exits if clicking on the overlay, defaults to false
- showStepNumbers (boolean; optional): showStepNumbers

Boolean true shows the steps in the red circle, default true
- keyboardNavigation (boolean; optional): keyboardNavigation

Boolean true allows navigating with the keyboard
- showProgress (boolean; optional): showProgress


Boolean true shows the progress bar
- overlayOpacity (number; optional): overlayOpacity

Number between 0 and 1 adjusts the opacity of the overlay layer"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, steps=Component.REQUIRED, nextLabel=Component.UNDEFINED, prevLabel=Component.UNDEFINED, skipLabel=Component.UNDEFINED, doneLabel=Component.UNDEFINED, hidePrev=Component.UNDEFINED, hideNext=Component.UNDEFINED, defaultTooltipPos=Component.UNDEFINED, tooltipClass=Component.UNDEFINED, highlightClass=Component.UNDEFINED, exitOnEsc=Component.UNDEFINED, exitOnOverlayClick=Component.UNDEFINED, showStepNumbers=Component.UNDEFINED, keyboardNavigation=Component.UNDEFINED, showProgress=Component.UNDEFINED, overlayOpacity=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'steps', 'nextLabel', 'prevLabel', 'skipLabel', 'doneLabel', 'hidePrev', 'hideNext', 'defaultTooltipPos', 'tooltipClass', 'highlightClass', 'exitOnEsc', 'exitOnOverlayClick', 'showStepNumbers', 'keyboardNavigation', 'showProgress', 'overlayOpacity']
        self._type = 'Hello'
        self._namespace = 'musicfox_dash_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'steps', 'nextLabel', 'prevLabel', 'skipLabel', 'doneLabel', 'hidePrev', 'hideNext', 'defaultTooltipPos', 'tooltipClass', 'highlightClass', 'exitOnEsc', 'exitOnOverlayClick', 'showStepNumbers', 'keyboardNavigation', 'showProgress', 'overlayOpacity']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['steps']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Hello, self).__init__(**args)
