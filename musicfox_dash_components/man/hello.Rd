% Auto-generated: do not edit by hand
\name{hello}

\alias{hello}

\title{Hello component}

\description{
A component that leverages intro.js under the hood to provide the Hello component from musicfox.io. Include the steps you'd like to highlight and more.  This component uses [intro.js](https://intro.js.com/) and thus far most endpoints for Steps are implemented.
}

\usage{
hello(id=NULL, steps=NULL, nextLabel=NULL, prevLabel=NULL, skipLabel=NULL,
doneLabel=NULL, hidePrev=NULL, hideNext=NULL, defaultTooltipPos=NULL,
tooltipClass=NULL, highlightClass=NULL, exitOnEsc=NULL, exitOnOverlayClick=NULL,
showStepNumbers=NULL, keyboardNavigation=NULL, showProgress=NULL,
overlayOpacity=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks}

\item{steps}{Unnamed list. List of dictionaries containing each step, with "intro" and "element"
keys, at a minimum.}

\item{nextLabel}{Character. nextLabel

String label for the "next" button}

\item{prevLabel}{Character. prevLabel

String label for the "prev" button}

\item{skipLabel}{Character. skipLabel 

String label for the "skip" button}

\item{doneLabel}{Character. doneLabel

String label for the "done" button}

\item{hidePrev}{Logical. hidePrev

Boolean true to hide "prev" button in the first step, default is false, 
disabled (grayed-out).}

\item{hideNext}{Logical. hideNext

Boolean true to hide "next" button in the last step, default is false,
disabled (grayed-out).}

\item{defaultTooltipPos}{Character. defaultTooltipPos

String default tooltip position (these can be changed per-step)}

\item{tooltipClass}{Character. tooltipClass

String class of all tooltip CSS}

\item{highlightClass}{Character. highlightClass

String class of all highlight over tooltip CSS (for the helperLayer) in
intro.js}

\item{exitOnEsc}{Logical. exitOnEsc

Boolean true exits with an esc keypress, defaults to true}

\item{exitOnOverlayClick}{Logical. exitOnOverlayClick

Boolean true exits if clicking on the overlay, defaults to false}

\item{showStepNumbers}{Logical. showStepNumbers

Boolean true shows the steps in the red circle, default true}

\item{keyboardNavigation}{Logical. keyboardNavigation

Boolean true allows navigating with the keyboard}

\item{showProgress}{Logical. showProgress


Boolean true shows the progress bar}

\item{overlayOpacity}{Numeric. overlayOpacity

Number between 0 and 1 adjusts the opacity of the overlay layer}
}
