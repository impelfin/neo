import React, { Component } from "react";

class App extends Component {
  state = {
    hello : 'Hello App.js!!',
  }


  handleChange = () => {
    this.setState({
      hello : 'Bye App.js!!',
    })
  }

  render() {
      return (
        <div className="App">
          <h1>{this.state.hello}</h1>
          <button onClick={this.handleChange}>Click Me!!</button>
        </div>
      );
  }
}

export default App;