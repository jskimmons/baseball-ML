import React from 'react';

class ApiTestComponent extends React.Component {

    getGames = () => {
        // get currently saved css
        fetch('/baseball/games')
        //.then(response => response.json())
        .then(response => {
            console.log(response);
        })
    }

  render() { 

    return (
        <div>
            <h2> Get predictions </h2>
            <button onClick={this.getGames}>get'em</button>
        </div>
    );            
  }
}

export default ApiTestComponent;