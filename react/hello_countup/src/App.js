import React, { Component } from "react";

class App extends Component {
  state = {
    count : 0,
  }


  countup = () => {
    this.setState({
      count : this.state.count + 1,
    })
  }

  render() {
      return (
        <div className="App">
          <h1>{this.state.count}</h1>
          <button onClick={this.countup}>Count UP!!</button>
        </div>
      );
  }
}

export default App;