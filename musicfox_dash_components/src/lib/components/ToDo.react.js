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
//        return '- '+string+'  \n'
    }
    listItems() {
        return this.props.todos.map(todo => (
            <ul> {todo} </ul>
        ));
    }
    makeBullets(array, levels=0) {
        /**
         * Construct bullet points for each string in the array.
         *
         */
        this.children = this.listItems()
//        for (let i in array) {
//            if (this.checkString(array[i])) {
//                this.children.push(this.appendString(array[i], levels))
//                console.log(this.children)
//                continue;
//            }
//            if (this.checkArray(array[i])) { 
//                // this won't work as of 5/22/2019
//                return this.makeBullets(array[i], levels + 1);
//            }
//        }
    }
    
    render() {
        this.makeBullets(this.props.todos)
        return (
            <div id={this.props.id} class="card" >
                <div class="card-body">
                    <h5 class="card-title">
                        <Markdown
                            source={this.props.title}
                            escapeHtml={!this.props.dangerously_allow_html}
                        />
                    </h5>
                    <h6 class="card-subtitle mb-2 text-muted">
                        <Markdown
                            source={this.props.subtitle}
                            escapeHtml={!this.props.dangerously_allow_html}
                        />
                    </h6>
                    <p class="card-text" children={this.children}></p>
                </div>
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
     *
     */

    /**
     * An object containing custom element props to put on the container
     * element such as id or style
     */
     containerProps: PropTypes.object,
};





