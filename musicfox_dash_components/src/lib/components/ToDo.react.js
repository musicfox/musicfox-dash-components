import React, {Component} from 'react';
import PropTypes from 'prop-types';
import Markdown from 'react-markdown';
import {omit, propOr, type} from 'ramda';

// eslint-disable-next-line valid-jsdoc
/**
 * A component that renders a bootstrap card with Github Markdown bullet points, the
 * ToDo component from musicfox.io. Optionally include a title, subtitle, and/or footer.
 *
 * This component uses [react-markdown](https://rexxars.github.io/react-markdown/)
 * under the hood, in the same fashion as the Dash Core Components Markdown component.
 *
 */

export default class ToDo extends Component {
    constructor(props) {
        super(props);
        this.children = new Array(this.props.todos.length);
        // loop through items of array
        // if the types are strings, concatenate them as bullets
        // if they're arrays, keep building
        this.listItems = this.listItems.bind(this); 
	}
    checkString(mystring) {
        /*
         * string type check boolean
         *
         */
        return (typeof mystring === 'string');
    }
    checkArray(array) {
         /*
         * Array type check boolean
         *
         */       
        return (typeof array === 'Array');
    }
    appendString(string, levels) {
        /**
         * Given the levels, append the string. Only one level will be sent, as of 5/22/2019.
         *
         */
        let spaces = ''
        let tabs = ''

        // build spaces
        for (let i = 0; i < levels; i++) {
            spaces += ' ' 
        }
        // build tabs
        for (let i = 0; i < 4; i++) {
            tabs += spaces
        }
//        return tabs+'- '+string+'  \n';
        string += '  \n'
        return (
            <ul>
                <Markdown
                    source={string}
                    escapeHtml={!this.props.dangerously_allow_html}
                />
            </ul>
        )
    }
    toMD(text) {
        return (
            <Markdown
                source={text}
                escapeHtml={!this.props.dangerously_allow_html}
            />
        )
    }
    listItems() {
        return ( 
            <ul 
                style={{
                    listStyleType: 'disc',
                    paddingLeft: 0,
                    marginLeft: '1.25rem'
                }}
                children={this.props.todos.map(todo => (
                    <li todo={todo} key={todo.key}>{this.toMD(todo)}</li>
                ))}
            >
            </ul>
        )
    }
    makeBullets(array, levels=0) {
        /**
         * Construct bullet points for each string in the array.
         *
         */
        this.children = this.listItems()
    }
    checkStringProp(prop) {
        /**
         * If the string prop is defined render its markdown. Otherwise render nothing.
         *
         */
        if (typeof prop === 'string') {
            return (
                this.toMD(prop)
            )
        }
    }
    isString(string) {
        return (typeof string === 'string')
    }
    /**
     * Bootstrap-specific card class manipulations
     *
     */
    makeClass(string, children) {
        /**
         * Return an arbitrary bootstrap class given the string.
         *
         */
        return <div class={string} children={children}></div>
    }
    makeNothing() {
        return <div style={{display:'none'}}></div>
    }

    cardHeader() {
        if (this.isString(this.props.header)) {
            return <strong>
                <h4>
                    {this.makeClass("card-header mb-0 text-secondary", this.toMD(this.props.header))}
                </h4>
            </strong>
        } else {
            return <div style={{display:'none'}}></div>
        }
    }
    cardFooter() {
        if (this.isString(this.props.footer)) {
            return (
                <div class="card-footer bg-light text-muted border-light">
                    <small>
                        {this.toMD(this.props.footer)}
                    </small>
                </div>
            )
        } else {
            return <div style={{display:'none'}}></div>
        }
    }
    cardTitle() {
        if (this.isString(this.props.title)) {
            return <h5>
                {this.makeClass("card-title", this.toMD(this.props.title))}
            </h5>
        } else {
            return <div style={{display:'none'}}></div>
        }
    }
    cardSubtitle() {
        if (this.isString(this.props.subtitle)) {
            return <h6>
                {this.makeClass("card-subtitle text-muted mb-2 mt-2", this.toMD(this.props.subtitle))}
            </h6>
        } else {
            return <div style={{display:'none'}}></div>
        }
    }
    cardText() {
        /**
         * Static PropType checking below should keep us from error, here.
         *
         */
        return this.makeClass("card-text", this.listItems())
    }

    /**
     * Main react render DOM
     *
     */
    render() {
        this.makeBullets(this.props.todos)
        return (
            <div id={this.props.id} class="card w-100 border-light">
                {this.cardHeader()}
                <div class="card-body">
                    {this.cardTitle()}
                    {this.cardSubtitle()}
                    {this.cardText()}
                </div>
                {this.cardFooter()}
            </div>
        );
    }
}

ToDo.defaultProps = {
    /* Define default properties (intro.js options) here */
    dangerously_allow_html: false,
};

ToDo.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func,

    /**
     * A todo list.
     * 
     * Enter the actual "todos" you have here as a list of strings or key-value pairs 
     * consisting of strings=['another list', {'orAnother':['string-key:list-value', 'pairs']}].
     *
     * These will be your "bullet points" in the typical "list".
     *
     * Markdown all the way.
     */
    todos: PropTypes.arrayOf(PropTypes.string),

    /**
     * The string title you'd like to include. Markdown all the way.
     *
     */
    title: PropTypes.string,
    
    /**
     * The string subtitle you'd like to include. Markdown all the way.
     */
    subtitle: PropTypes.string,
    
    /**
     * The string footer you'd like to include. Markdown all the way.
     */
    footer: PropTypes.string,

    /**
     * The string header you'd like to include. Markdown all the way.
     */
    header: PropTypes.string,


    /**
     * Boolean True or False (default)
     *
     * True will allow Markdown HTML rendering but leave your clients exposed to XSS attacks.
     *
     * Don't do this. But I'm into freedom; just don't blame ToDo when things go awry.
     */
    dangerously_allow_html: PropTypes.bool,

    /**
     *
     */
/**
     * Object that holds the loading state object coming from dash-renderer
     */
    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string,
    }),

    /**
     * Append a class name to the class
     */

    /**
     * An object containing custom element props to put on the container
     * element such as id or style
     */
     containerProps: PropTypes.object,
};





