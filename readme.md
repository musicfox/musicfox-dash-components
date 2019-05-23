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
>>>     dict(intro='my other other intro language', element='.position-test', position='right'), #whoa...
>>> ]
>>> mdc.Hello(steps=steps) # no HTML-5 attributes necessary as Hello will fire on page load for the given steps
```

## `ToDo` component: `mdc.ToDo`
![musicfox.io ToDo component static PNG demo](https://github.com/thinkjrs/musicfox-dash-components/blob/6483207bc327d0215f76df0eed59a4c166a2c931/demo_assets/ToDo_2019-05-23.png)

This component narrowly implements a ToDo card with five simple sections: A *Header*, A *Title*, a *Subtitle*, a *ToDo List* and a *Footer*.  
> ###### Weekly todos 
>
> ### Groceries
>
> ##### Things we need to acquire from the market
>
>    - Apples
>    - Pears
>    - Blueberries
>    - Cereal
>    - ...

You get the point. :wink:

###### Usage


```python
>>> mdc.ToDo(id="my-todo-container",
>>>     title="Groceries",
>>>     subtitle="Our weekly list of items to obtain from a grocer.",
>>>     todos=[ # a list of markdown-formatted strings
>>>         "Apples", "Pears", "Blueberries", 
>>>         "Cereal", "Kidney Beans", 
>>>         "Tofu", "Ribeye Steak",
>>>         "Nutella",
>>>     ],
>>>     footer=f"Updated: just {pd.datetime.now()}"
>>> ) # Sometimes, less is more. 
```

We use [Bootstrap cards](https://getbootstrap.com/docs/4.3/components/card/)
and [React-markdown](https://github.com/rexxars/react-markdown) under the hood.  
Visit them for styling info, etc...  
**Required Params**
- `id`: a string id for the composed element
- `todos`: a list of strings or dictionary key:value string:list, a *ToDo List*
    - a todo can always be nested as dictionary string key and value list (and possibly more dictionaries)

**Optional Params**
- `header`: a string *Header* for the todo list
- `title`: a string *Title* for the todo list
- `subtitle`: a string *Subtitle* for the todo list
- `footer`: a string *Footer* for the todo list
