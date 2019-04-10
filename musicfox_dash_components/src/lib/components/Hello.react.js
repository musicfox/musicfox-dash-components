import React, {Component} from 'react';
import PropTypes from 'prop-types';
import '../../../assets/intro.js'
import '../../../assets/introjs.css'
import { Steps, Hints } from 'intro.js-react'

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */

var onExit = () => {
    this.setState(() => ({ stepsEnabled: false}));
};

export default class Hello extends Component {
    constructor(props) {
        super(props);
	    this.state = {
        	stepsEnabled: true,
        	initialStep: 0,
    	};
	}
    render() {
        const {id, label, setProps, value, steps} = this.props;
        const { stepsEnabled, initialStep,} = this.state;
        return (
            <div id={id}>
              <Steps               
                enabled={stepsEnabled}
                steps={steps}
                initialStep={0}
                onExit={this.onExit}
              />
            </div>
        );
    }
}

Hello.defaultProps = {
	stepsEnabled: true,
};

Hello.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * A label that will be printed when this component is rendered.
     */
    label: PropTypes.string.isRequired,

    /**
     * The value displayed in the input
     */
    value: PropTypes.string,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func,
    /**
     * List of dictionaries containing each step, with "intro" and "element"
     * keys, at a minimum.
     */
    steps: PropTypes.array,
};
