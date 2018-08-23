import { sayHello, sayHelloAsync } from './hello';
import configureStore from '../store';

let store;

beforeEach(() => {
  store = configureStore();
});

const delay = (done, cb) => {
  setTimeout(() => { cb(); done(); }, 10);
}

it('should have the correct default state', () => {
  let state = store.getState();
  expect(state.hello.message).toBe('');
  expect(state.hello.pending).toBe(false);
});

it('should handle say hello action', () => {
  store.dispatch(sayHello('Hello World'));
  let state = store.getState();
  expect(state.hello.message).toBe('Hello World');
  expect(state.hello.pending).toBe(false);
});

it('should handle say hello async action', (done) => {
  store.dispatch(sayHelloAsync('Hello World Async'));
  let state = store.getState();  
  expect(state.hello.message).toBe('');
  expect(state.hello.pending).toBe(true);

  delay(done, () => {
    state = store.getState();
    expect(state.hello.message).toBe('Hello World Async');
    expect(state.hello.pending).toBe(false);
  });
});



