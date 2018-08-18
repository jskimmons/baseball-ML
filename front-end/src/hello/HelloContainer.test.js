import React from 'react';
import ReactDOM from 'react-dom';
import HelloContainer from './HelloContainer';
import { Provider } from 'react-redux';

import configureStore from '../store'; 

let store;

beforeEach(() => {
  store = configureStore();
});

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(
    <Provider store={store}>
      <HelloContainer/>
    </Provider>  
  , div);
  ReactDOM.unmountComponentAtNode(div);
});
