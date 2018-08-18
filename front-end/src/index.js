import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import configureStore, { history } from './store';

const store = configureStore();

ReactDOM.render(<App store={store} history={history} />, document.getElementById('root'));
registerServiceWorker();
