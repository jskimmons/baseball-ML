# create-react-app-redux

Starter app based on ```create-react-app``` and adding these components:

* redux
* redux-logic            (middleware for async processing)
* react-router-dom
* react-router-redux
* history
* redux-actions          (reduce boilerplate for actions and reducers)
* redux-form             (simple example in HelloComponent)
* axios
* simple-console-logger  (simple log4j like logger, configured in index.js)

## Usage
```
git clone https://github.com/raythree/create-react-app-redux
cd create-react-app-redux
rm -fr .git
npm install
npm start
```

Everything is wired up, including a sample "hello" component including tests. Just
start by replacing this with your own components. The structure is:

```
store/
  index.js           (exports configureStore, pulls in ducks style reducers from app components)

logic/
  index.js           (sets up redux-logic middleware)

hello/               (A simple starter component - start here and replace with your components)
  hello.js           (ducks style reducer and actions)
  helloLogic.js      (redux-logic for handling async action)
  hello.test.js      (tests actions/reducers/logic)
  HelloContainer.js  (redux container)
  HelloComponent.js  (Component with buttons to say hello and say hello async and redux form validation)
```
