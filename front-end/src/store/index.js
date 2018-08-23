import { createStore, compose, applyMiddleware } from 'redux';
import createHistory from 'history/createBrowserHistory';
import { routerMiddleware } from 'react-router-redux';

import rootReducer from './reducers';
import createLogicMiddleware from '../logic';

export const history = createHistory();

export default function configureStore(initialState = {}, logicDeps) {
  const reactRouterMiddleware = routerMiddleware(history);
  const middlewares = [
    // Add other middleware here...
    createLogicMiddleware(logicDeps),
    reactRouterMiddleware
  ];

  return createStore(rootReducer, initialState, compose(applyMiddleware(...middlewares)));
}