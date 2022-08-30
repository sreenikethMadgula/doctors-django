import React, { Component } from "react";
import { render } from "react-dom";
import ReactDOM from "react-dom";
import HomePage from "./HomePage";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import DoctorListPage from "./DoctorListPage";
import SpecializationPage from "./SpecializationPage";

export default function App() {
  return (
    <div>
      {/* <HomePage /> */}
      {/* <NavBar /> */}
      <Router>
				<Routes>
					<Route path="/doctors-django/" element={<HomePage />} />
					<Route path='/doctors-django/doctors' element={<DoctorListPage />} />
					<Route path='/doctors-django/specialization' element={<SpecializationPage />} />
					<Route path='*' element={<Error />} />
				</Routes>
			</Router>
      {/* <Router>
        <HomePage />
        <SpecializationPage />
        <DoctorListPage />
      </Router> */}
    </div>
  );
}

const appDiv = document.getElementById("app");
ReactDOM.render(<App />, appDiv);

if (module.hot) {
  module.hot.accept()
}
