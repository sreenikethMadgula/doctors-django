import React, { Component } from "react";
import NavBar from './NavBar';
import DoctorListPage from "./DoctorListPage";
import SpecializationPage from "./SpecializationPage";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";


export default function HomePage() {
	return(
		<div>
			<NavBar />
			<div>
				<h1>List of Doctors</h1>
			</div>
			{/* <Link to="/doctors">24x7 Doctors</Link> */}
			{/* <Link to="/"></Link> */}
			{/* <Router>
				<Switch>
					<Route path='/doctors' component={DoctorListPage} />
					<Route path='/specialization' component={SpecializationPage} />
				</Switch>
			</Router> */}

		</div>
	)
}

