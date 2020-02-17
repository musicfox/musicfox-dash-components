# AUTO GENERATED FILE - DO NOT EDIT

toDo <- function(id=NULL, todos=NULL, title=NULL, subtitle=NULL, footer=NULL, header=NULL, dangerously_allow_html=NULL, loading_state=NULL, containerProps=NULL) {
    
    props <- list(id=id, todos=todos, title=title, subtitle=subtitle, footer=footer, header=header, dangerously_allow_html=dangerously_allow_html, loading_state=loading_state, containerProps=containerProps)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ToDo',
        namespace = 'musicfox_dash_components',
        propNames = c('id', 'todos', 'title', 'subtitle', 'footer', 'header', 'dangerously_allow_html', 'loading_state', 'containerProps'),
        package = 'musicfoxDashComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
