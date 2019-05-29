import React, {Component} from 'react';
import PropTypes from 'prop-types';
import { Timeline } from 'react-twitter-widgets'

//eslint-disable-next-line valid-jsdoc
/**
 * Twash, A Twitter Profile Timeline component for Dash from
 * musicfox.io.
 *
 * This component uses react-twitter-widgets under the hood.
 *
 */

export default class Twash extends Component {
    constructor(props) {
        super(props);
        this.twashContainer = React.createRef()
        let options = this.buildOptions()
        this.options = this.buildChromeOptions(options)
    }
    buildOptions() {
        let options = Object.assign({}, this.props.options)
        options = Object.assign({}, options, {
                    theme: this.props.theme,
                    linkColor: this.props.linkColor,
                    borderColor: this.props.borderColor,
                    lang: this.props.lang,
                    height: this.props.height,
                    width: this.props.width
                })

        return options
    }
    buildChromeOptions(options) {
        options.chrome = ''
        if (this.props.noHeader) { options.chrome = options.chrome + ' noheader' }

        if (this.props.noFooter) { options.chrome = options.chrome + ' nofooter' }

        if (this.props.noBorders) { options.chrome = options.chrome + ' noborders' }

        if (this.props.noScrollbar) { options.chrome = options.chrome + ' noscrollbar' }

        if (this.props.transparent) { options.chrome = options.chrome + ' transparent' }

        return options
    }
    render() {
        return (
        <div id={this.props.id}>
    		<Timeline
    			dataSource={{
      				sourceType: this.props.sourceType,
      				screenName: this.props.handle
    			}}
    			options={this.options}
    			onLoad={() => console.log('Timeline is loaded!')}
  			/>
        </div>
        )
    }
}

Twash.defaultProps = {

}

Twash.propTypes = {
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
     * String 'profile' is all for now
     */
    sourceType: PropTypes.string,
    
    /**
     * String user name or public handle, e.g. ArianaGrande
     */
    handle: PropTypes.string.isRequired,

    /**
     *
     * Integer height (in pixels)
    */
    height: PropTypes.number,

    /**
     *
     * Integer width (in pixels)
    */
    width: PropTypes.number,

    //COPY PASTA FROM https://github.com/saurabhnemade/react-twitter-embed/blob/master/src/components/TwitterTimelineEmbed.js
    /**
     *          * Automatically fit into parent container height
     *                   */
    //autoHeight: PropTypes.bool,
    /**
     *          * With dark or light theme
     *                   */
    theme: PropTypes.oneOf(['dark', 'light']),
    /**
     *          * With custom link colors. Note: Only Hex colors are supported.
     *                   */
    linkColor: PropTypes.string,
    /**
     *          * With custom border colors. Note: Only Hex colors are supported.
     *                   */
    borderColor: PropTypes.string,
    /**
     *          * Hide the header from timeline
     *                   */
    noHeader: PropTypes.bool,
    /**
     *          * Hide the footer from timeline
     *                   */
    noFooter: PropTypes.bool,
    /**
     *          * Hide the border from timeline
     *                   */
    noBorders: PropTypes.bool,
    /**
     *          * Hide the scrollbars
     *                   */
    noScrollbar: PropTypes.bool,
    /**
     *          * Enable Transparancy
     *                   */
    transparent: PropTypes.bool,
    /**
     *          * Custom language code. Supported codes here: https://developer.twitter.com/en/docs/twitter-for-websites/twitter-for-websites-supported-languages/overview.html
     *                   */
    lang: PropTypes.string
}
