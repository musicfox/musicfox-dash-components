import React, {Component} from 'react';
import PropTypes from 'prop-types';
import '../../../assets/intro.js'
import '../../../assets/introjs.css'
import { Steps, Hints } from 'intro.js-react'

// eslint-disable-next-line valid-jsdoc
/**
 * A component that leverages intro.js under the hood to provide the Hello component
 * from musicfox.io. Include the steps you'd like to highlight and more.
 *
 * This component uses [intro.js](https://intro.js.com/) and thus far most endpoints for Steps
 * are implemented.
 */

export default class Hello extends Component {
    constructor(props) {
        super(props);
	    this.state = {
        	stepsEnabled: true,
        	initialStep: 0,
            onExit :()=>{
                this.setState(() => ({stepsEnabled: false}));
            },
    	}
	}
    render() {
        const { stepsEnabled, initialStep, onExit, } = this.state;
        const {
            id, 
            setProps,
            steps,
            nextLabel,
            prevLabel,
            skipLabel,
            doneLabel,
            hidePrev,
            hideNext,
            defaultTooltipPos,
            tooltipClass,
            highlightClass,
            exitOnEsc,
            exitOnOverlayClick,
            showStepNumbers,
            keyboardNavigation,
            showProgress,
            overlayOpacity
        } = this.props;
        const options = {};
        const value = this.props;
        value && (options.value = value)
        return (
            <div id={id}>
              <Steps               
                enabled={stepsEnabled}
                steps={steps}
                initialStep={0}
                onExit={onExit}
                options={{
                    nextLabel: this.props.nextLabel,
                    prevLabel: this.props.prevLabel,
                    skipLabel: this.props.skipLabel,
                    doneLabel: this.props.doneLabel,
                    hidePrev: this.props.hidePrev,
                    hideNext: this.props.hideNext,
                    defaultTooltipPos: this.props.defaultTooltipPos,
//                    tooltipClass: this.props.tooltipClass,
//                    highlightClass: this.props.highlightClass,
                    exitOnEsc: this.props.exitOnEsc,
                    exitOnOverlayClick: this.props.exitOnOverlayClick,
                    showStepNumbers: this.props.showStepNumbers,
                    keyboardNavigation: this.props.keyboardNavigation,
                    showProgress: this.props.showProgress,
                    overlayOpacity: this.props.overlayOpacity
                }}
              />
            </div>
        );
    }
}

Hello.defaultProps = {
    /* Define default properties (intro.js options) here */
    nextLabel: "Next", 
    prevLabel: "Previous",
    skipLabel: "Skip tutorial",
    doneLabel: "Done",
    hidePrev: true, 
    hideNext: true,
    defaultTooltipPos: 'bottom',
    exitOnEsc: true,
    exitOnOverlayClick: true,
    showStepNumbers: true,
    keyboardNavigation: true,
    showProgress: true,
    overlayOpacity: .5
};

Hello.propTypes = {
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
     * List of dictionaries containing each step, with "intro" and "element"
     * keys, at a minimum.
     */
    steps: PropTypes.array.isRequired,

    /**
     * nextLabel
     *
     * String label for the "next" button
     *
     */
    nextLabel: PropTypes.string,

    /**
     * prevLabel
     *
     * String label for the "prev" button
     *
     */
    prevLabel: PropTypes.string,

    /**
     * skipLabel 
     *
     * String label for the "skip" button
     *
     */
    skipLabel: PropTypes.string,
    
    /**
     * doneLabel
     *
     * String label for the "done" button
     */
    doneLabel: PropTypes.string,
    
    /**
     *
     * hidePrev
     *
     * Boolean true to hide "prev" button in the first step, default is false, 
     * disabled (grayed-out).
     */
    hidePrev: PropTypes.bool,
     
    /**    
     * hideNext
     *
     * Boolean true to hide "next" button in the last step, default is false,
     * disabled (grayed-out).
     */
    hideNext: PropTypes.bool,
    
    /**
     * defaultTooltipPos
     *
     * String default tooltip position (these can be changed per-step)
     */
    defaultTooltipPos: PropTypes.string,
    
    /**
     * tooltipClass
     *
     * String class of all tooltip CSS
     */
    tooltipClass: PropTypes.string,
    
    /**
     *
     * highlightClass
     *
     * String class of all highlight over tooltip CSS (for the helperLayer) in
     * intro.js
     */
    highlightClass: PropTypes.string,
    
    /**
     *
     * exitOnEsc
     *
     * Boolean true exits with an esc keypress, defaults to true
     */  
    exitOnEsc: PropTypes.bool,
   
    /**
     *
     * exitOnOverlayClick
     *
     * Boolean true exits if clicking on the overlay, defaults to false
     */
    exitOnOverlayClick: PropTypes.bool,
    
    /**
     *
     * showStepNumbers
     *
     * Boolean true shows the steps in the red circle, default true
     *
     */
    showStepNumbers: PropTypes.bool,
   
    /**
     * keyboardNavigation
     *
     * Boolean true allows navigating with the keyboard
     */
    keyboardNavigation: PropTypes.bool,
   
    /**
     * showProgress
     *
     *
     * Boolean true shows the progress bar
     *
     */
    showProgress: PropTypes.bool,
   
    /**
     *
     * overlayOpacity
     *
     * Number between 0 and 1 adjusts the opacity of the overlay layer
     */
    overlayOpacity: PropTypes.number,
};



