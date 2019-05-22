import React, {Component} from 'react';
import PropTypes from 'prop-types';
import Markdown from 'react-markdown';
import {omit, propOr, type} from 'ramda';

export default class ToDo extends Component {
    constructor(props) {
        super(props);
//	    this.state = {
//            onExit :()=>{
//                this.setState(() => ({: false}));
//            },
//    	}
	}
    render() {
//        const { stepsEnabled, initialStep, onExit, } = this.state;
        const {
            id, 
            setProps,
//            steps,
//            nextLabel,
//            prevLabel,
//            skipLabel,
//            doneLabel,
//            hidePrev,
//            hideNext,
//            defaultTooltipPos,
//            tooltipClass,
//            highlightClass,
//            exitOnEsc,
//            exitOnOverlayClick,
//            showStepNumbers,
//            keyboardNavigation,
//            showProgress,
//            overlayOpacity
        } = this.props;
//        const options = {};
        const value = this.props;
//        value && (options.value = value)
        return (
//            <div id={id}>
//              <Steps               
//                enabled={stepsEnabled}
//                steps={steps}
//                initialStep={0}
//                onExit={onExit}
//                options={{
//                    nextLabel: this.props.nextLabel,
//                    prevLabel: this.props.prevLabel,
//                    skipLabel: this.props.skipLabel,
//                    doneLabel: this.props.doneLabel,
//                    hidePrev: this.props.hidePrev,
//                    hideNext: this.props.hideNext,
//                    defaultTooltipPos: this.props.defaultTooltipPos,
////                    tooltipClass: this.props.tooltipClass,
////                    highlightClass: this.props.highlightClass,
//                    exitOnEsc: this.props.exitOnEsc,
//                    exitOnOverlayClick: this.props.exitOnOverlayClick,
//                    showStepNumbers: this.props.showStepNumbers,
//                    keyboardNavigation: this.props.keyboardNavigation,
//                    showProgress: this.props.showProgress,
//                    overlayOpacity: this.props.overlayOpacity
//                }}
          <div id={id}>Hello, world.</div>
        );
    }
}

ToDo.defaultProps = {
    /* Define default properties (intro.js options) here */
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

};



