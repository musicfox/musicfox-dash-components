# AUTO GENERATED FILE - DO NOT EDIT

twash <- function(id=NULL, sourceType=NULL, handle=NULL, height=NULL, width=NULL, theme=NULL, linkColor=NULL, borderColor=NULL, noHeader=NULL, noFooter=NULL, noBorders=NULL, noScrollbar=NULL, transparent=NULL, lang=NULL) {
    
    props <- list(id=id, sourceType=sourceType, handle=handle, height=height, width=width, theme=theme, linkColor=linkColor, borderColor=borderColor, noHeader=noHeader, noFooter=noFooter, noBorders=noBorders, noScrollbar=noScrollbar, transparent=transparent, lang=lang)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Twash',
        namespace = 'musicfox_dash_components',
        propNames = c('id', 'sourceType', 'handle', 'height', 'width', 'theme', 'linkColor', 'borderColor', 'noHeader', 'noFooter', 'noBorders', 'noScrollbar', 'transparent', 'lang'),
        package = 'musicfoxDashComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
