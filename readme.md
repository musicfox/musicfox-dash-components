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
![musicfox.io Hello component GIF demo](https://github.com/thinkjrs/musicfox-dash-components/blob/ee7dbf50994c07f7e0127f1372882174927ad2ea/demo_assets/Hello_04102019.gif)  

This component narrowly implements a typical web-walkthrough *intro* using a small subset of the `intro.js` component library.

###### Usage 


```python
>>> steps = [
>>>     dict(intro='my intro language', element='#selector-by-id1'),
>>>     dict(intro='my other intro language', element='.selector-by-class1'),
>>>     dict(intro="my other other intro language',element='.position-test', position='right'), #whoa...
>>> ]
>>> mdc.Hello(steps=steps) # no HTML-5 attributes necessary as Hello will fire on page load for the given steps
```

## `ToDo` component: `mdc.ToDo`

This component narrowly implements a ToDo card with four simple sections: A *Title*, a *Subtitle*, a *ToDo List* and a *Footer*.  
Furthermore, the *ToDo List* can have a list of dictionaries to indicate list heirarchy. For example, 
>- Fruits
>    - Apples
>    - Pears
>    - Blueberries
>- Dry
>    - Cereal
>    - ...

You get the point. :wink:

###### Usage


```python
>>> todolist = 
>>> mdc.ToDo(dict(
>>>     title="Groceries",
>>>     subtitle="Our weekly list of items to obtain from a grocer.",
>>>     todolist=[dict(Fruits=["Apples", "Pears", "Blueberries"], Dry=["Cereal", "Kidney Beans"], Protein=["Tofu", "Ribeye Steak"])],
>>>     footer=[
>>> ] 
