
import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux';
import { reducer as formReducer } from 'redux-form';

import helloReducer from '../hello/hello';

const rootReducer = combineReducers({
  routing: routerReducer,
  form: formReducer,
  
  hello: helloReducer,
  // add other reducers here
});

export default rootReducer;

