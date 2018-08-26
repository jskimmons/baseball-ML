import React from 'react';
import TeamComponent from './TeamComponent';
import TeamTriggerComponent from './TeamTrigger';
import {Popup} from 'semantic-ui-react';

class PageContainer extends React.Component {

	render() {
		return (
			<div >
				<TeamComponent 
					position="bottom center"
					teamName="whatevs"
					triggerComponent={<TeamTriggerComponent />}
				/>
			</div>
		);
	}
}

export default PageContainer;