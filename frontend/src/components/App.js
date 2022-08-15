import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import NavBar from "./NavBar";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        {/* <HomePage /> */}
        <NavBar />
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);