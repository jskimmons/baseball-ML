import React from 'react';
import PropTypes from 'prop-types';
import { Field, reduxForm } from 'redux-form';

const log = require('simple-console-logger').getLogger('HelloComponent');

/**
 * This is how Redux form Field components allow you to render
 * any custom input component. The "input" props should all be
 * passed to the <input> element. You can pass in 
 */
const renderField = ({
  input,
  label,
  type,
  inputStyle,
  labelStyle,
  meta: { touched, error, warning }
}) => (
  <div>
    <label style={labelStyle}>{label}</label>
    <div>
      <input {...input} placeholder={label} type={type} style={inputStyle} autoComplete="off"/>
      {touched && ((error && <span style={{color:'red'}}>{error}</span>))}
    </div>
  </div>
);

const validate = (values) => {
  let errors = {};
  log.debug('validating form...');
  if (!values.message || values.message.length < 3) {
    errors.message = 'Message must be at least 3 characters';
  }
  return errors;
}

/**
 * Display a simple form with buttons to say hello. The
 * message field uses redux-form as an example of validation.
 */
class HelloComponent extends React.Component {
  static propTyles = {
    message: PropTypes.string,
    pending: PropTypes.bool.isRequired,
    sayHello: PropTypes.func.isRequuired,
    sayHelloAsync: PropTypes.func.isRequuired
  };

  constructor(props) {
    super(props);
    this.state = {message: ''};
  }

  onSubmit = (values) => {
    log.debug('submitting form');
    let fn = values.async ? this.props.sayHelloAsync : this.props.sayHello;
    fn(values.message);
  }

  render() {    
    const { handleSubmit } = this.props

    const buttonStyle={padding:'1em', margin: '1em'};
    const inputStyle={padding: '1em', margin: '1em'};
    const labelStyle={marginLeft: '1em'};
        
    return (
      <div style={{padding:'2em'}}>
        <form onSubmit={handleSubmit(this.onSubmit)}>
          <Field
            inputStyle={inputStyle}
            labelStyle={labelStyle}
            name="message"
            type="text"
            label="Message"
            component={renderField}
          />
          <div style={{marginLeft:'1em'}}>
            Async
            <Field
              name="async"
              id="async"
              component="input"
              type="checkbox"
              style={{marginLeft:'1em'}}
            />
          </div>
          <br/>
          <button style={buttonStyle} disabled={this.props.pending} onClick={this.hello}>Say Hello</button>
        </form>  
        <div style={{padding:'1em'}}>
          {this.props.pending ? 'please wait...': ''}
          {this.props.message ? 'Hello ' + this.props.message : ''}
        </div>           
      </div>
    );            
  }
}

export default reduxForm({
  form: 'HelloForm',
  validate
})(HelloComponent);
