# musicfox-dash-components
Dash components from your favorite music technology company musicfox.io

## Quickstart
```python
>>> import musicfox_dash_components as mdc
```
## `Hello` component: `mdc.Hello`

This component narrowly implements a typical web-walkthrough *intro* using a small subset of the `intro.js` component library.

```python
>>> mdc.Hello() # Will use default data-* attributes when rendered by the React DOM
>>> steps = [
>>>     dict(intro='my intro language', element='selector-by-id1'),
>>>     dict(intro='my other intro language', element='selector-by-id2'),
>>> ]
>>> mdc.Hello(steps=steps) # no HTML-5 attributes necessary as Hello will fire on page load for the given steps
