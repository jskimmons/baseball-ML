import React, { Component } from 'react';
import { Provider } from 'react-redux';

import PageContainer from './games/PageContainer';
import ApiTestComponent from './games/ApiTestComponent';


class App extends Component {

  render() {
    return (
      <Provider store={this.props.store}>
      	<div>
              <ApiTestComponent />
              <PageContainer />
        </div>
      </Provider>
    );
  }
}

export default App;
