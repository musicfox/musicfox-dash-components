% Auto-generated: do not edit by hand
\name{toDo}

\alias{toDo}

\title{ToDo component}

\description{
A component that renders a bootstrap card with Github Markdown bullet points, the ToDo component from musicfox.io. Optionally include a title, subtitle, and/or footer.  This component uses [react-markdown](https://rexxars.github.io/react-markdown/) under the hood, in the same fashion as the Dash Core Components Markdown component.
}

\usage{
toDo(id=NULL, todos=NULL, title=NULL, subtitle=NULL, footer=NULL, header=NULL,
dangerously_allow_html=NULL, loading_state=NULL, containerProps=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks}

\item{todos}{List of characters. A todo list.

Enter the actual "todos" you have here as a list of strings or key-value pairs 
consisting of strings=['another list', {'orAnother':['string-key:list-value', 'pairs']}].

These will be your "bullet points" in the typical "list".

Markdown all the way.}

\item{title}{Character. The string title you'd like to include. Markdown all the way.}

\item{subtitle}{Character. The string subtitle you'd like to include. Markdown all the way.}

\item{footer}{Character. The string footer you'd like to include. Markdown all the way.}

\item{header}{Character. The string header you'd like to include. Markdown all the way.}

\item{dangerously_allow_html}{Logical. Boolean True or False (default)

True will allow Markdown HTML rendering but leave your clients exposed to XSS attacks.

Don't do this. But I'm into freedom; just don't blame ToDo when things go awry.}

\item{loading_state}{Lists containing elements 'is_loading', 'prop_name', 'component_name'.
those elements have the following types:
  - is_loading (logical; optional): determines if the component is loading or not
  - prop_name (character; optional): holds which property is loading
  - component_name (character; optional): holds the name of the component that is loading. Object that holds the loading state object coming from dash-renderer}

\item{containerProps}{Named list. An object containing custom element props to put on the container
element such as id or style}
}
