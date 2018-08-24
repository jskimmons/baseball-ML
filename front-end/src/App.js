import React, { Component } from 'react';
import { Provider } from 'react-redux';

import PageContainer from './games/PageContainer';


class App extends Component {

  render() {
    return (
      <Provider store={this.props.store}>
              <PageContainer />
      </Provider>
    );
  }
}

export default App;
