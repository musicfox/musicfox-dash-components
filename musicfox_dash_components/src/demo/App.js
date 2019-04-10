/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import { Hello } from '../lib';

class App extends Component {

    constructor() {
        super();
        this.state = {
            value: ''
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return (
            <div>
                <h3 className="myClass">This is a test</h3>
                <h4 className="myClass2">This is another test</h4>
                <Hello
                    setProps={this.setProps}
                    {...this.state}
                    steps={[
                        {'intro':'my intro info', 'element':".myClass"},
                        {'intro':'more intro info', 'element': ".myClass2"},
                    ]}
                    showProgress={true}
                    overlayOpacity={.9}
                    exitOnEsc={false}                    
                />
            </div>
        )
    }
}

export default App;
