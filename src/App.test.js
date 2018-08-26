import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import renderer from 'react-test-renderer';

import configureStore, { history } from './store'; 

let store;

beforeEach(() => {
  store = configureStore();
});

it('renders without crashing', () => {
  const component = renderer.create(
    <App store={store} history={history}/>
  );
});
