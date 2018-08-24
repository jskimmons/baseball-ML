import React from 'react';

class TeamTriggerComponent extends React.Component {

    render() {

        return (
            <h1 align="center" onClick={this.props.onClick}> Click </h1>
        );
    }
}

export default TeamTriggerComponent;