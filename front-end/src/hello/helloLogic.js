import { createLogic } from 'redux-logic';
import { sayHelloAsync, sayHelloComplete } from './hello';

const delay = () => {
  return new Promise((resolve) => {
    setTimeout(() => resolve(), process.env.NODE_ENV === 'test' ? 0 : 2000)
  });
}

export default [
  createLogic({
    type: sayHelloAsync,
    //debounce: process.env.NODE_ENV === 'test' ? 0 : 500,
    latest: true,

    process({ action }, dispatch, done) {
      console.log('processing async action');
      delay()
      .then(() => {
        console.log('dispatching complete action');
        dispatch(sayHelloComplete(action.payload));
        done();
      });
    }  
  })

  // Add other action logic here
]; 
