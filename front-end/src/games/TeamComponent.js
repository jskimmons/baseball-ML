import React from 'react';
import { Popup } from 'semantic-ui-react';

class TeamComponent extends React.Component {

    render() {

        return (
            <Popup 
            	trigger={this.props.triggerComponent}
            	inverted  
            	on='click' 
            	position={this.props.position}
            >
                <Popup.Header>{this.props.teamName}</Popup.Header>
                <Popup.Content>
                    <h1>Stats</h1>
                </Popup.Content>
            </Popup>
        );
    }
}

export default TeamComponent;