# AUTO GENERATED FILE - DO NOT EDIT

hello <- function(id=NULL, steps=NULL, nextLabel=NULL, prevLabel=NULL, skipLabel=NULL, doneLabel=NULL, hidePrev=NULL, hideNext=NULL, defaultTooltipPos=NULL, tooltipClass=NULL, highlightClass=NULL, exitOnEsc=NULL, exitOnOverlayClick=NULL, showStepNumbers=NULL, keyboardNavigation=NULL, showProgress=NULL, overlayOpacity=NULL) {
    
    props <- list(id=id, steps=steps, nextLabel=nextLabel, prevLabel=prevLabel, skipLabel=skipLabel, doneLabel=doneLabel, hidePrev=hidePrev, hideNext=hideNext, defaultTooltipPos=defaultTooltipPos, tooltipClass=tooltipClass, highlightClass=highlightClass, exitOnEsc=exitOnEsc, exitOnOverlayClick=exitOnOverlayClick, showStepNumbers=showStepNumbers, keyboardNavigation=keyboardNavigation, showProgress=showProgress, overlayOpacity=overlayOpacity)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Hello',
        namespace = 'musicfox_dash_components',
        propNames = c('id', 'steps', 'nextLabel', 'prevLabel', 'skipLabel', 'doneLabel', 'hidePrev', 'hideNext', 'defaultTooltipPos', 'tooltipClass', 'highlightClass', 'exitOnEsc', 'exitOnOverlayClick', 'showStepNumbers', 'keyboardNavigation', 'showProgress', 'overlayOpacity'),
        package = 'musicfoxDashComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
