import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';
import { Route, Switch } from 'react-router-dom';
import Logger from 'simple-console-logger';

import HelloContainer from './hello/HelloContainer';

Logger.configure({level: 'debug'});

class App extends Component {
  static propTypes = {
    store: PropTypes.object.isRequired,
    history: PropTypes.object.isRequired
  };

  render() {
    return (
      <Provider store={this.props.store}>
        <BrowserRouter>
          <Switch>
            <Route exact path="/hello" render={(props) => (
              <HelloContainer />
            )}/>
            <Route path="/" component={HelloContainer} />
          </Switch>
        </BrowserRouter>  
      </Provider>
    );
  }
}

export default App;
