
import { createLogicMiddleware } from 'redux-logic';

import helloLogic from '../hello/helloLogic';
// import all your component's logic here and add to the array

const arrLogic = [
  ...helloLogic
  // add other logic here
];

export default function (deps) {  
  const history = require('../store/').history;
  const logicDeps = { history }; // can be overriden for testing

  const logicMiddleware = createLogicMiddleware(arrLogic, deps || logicDeps);
  return logicMiddleware;
}
