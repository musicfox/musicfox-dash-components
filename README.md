# musicfox-dash-components
Dash components from your favorite music technology company musicfox.io

## Quickstart

Get the goods:
```bash
pip install --user musicfox-dash-components
```

Then import the musicfox.io component library:
```python
>>> import musicfox_dash_components as mdc
```
## `Hello` component: `mdc.Hello`
###### Your first walkthrough
This component narrowly implements a typical web-walkthrough *intro* using a small subset of the `intro.js` component library.

```python
>>> steps = [
>>>     dict(intro='my intro language', element='#selector-by-id1'),
>>>     dict(intro='my other intro language', element='.selector-by-class1'),
>>>     dict(intro="my other other intro language',element='.position-test', position='right'), #whoa...
>>> ]
>>> mdc.Hello(steps=steps) # no HTML-5 attributes necessary as Hello will fire on page load for the given steps
```

![musicfox.io Hello component GIF demo](https://github.com/thinkjrs/musicfox-dash-components/blob/c38b42951557341751595f55d3b28523e10a4c4b/demo_assets/Hello_04092019.gif)

