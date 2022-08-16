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
  Routes,
} from "react-router-dom";


export default function HomePage(props) {
	return(
		<div className="home">
			<NavBar />
			{/* <div className="heading">
				<h1>List of Doctors in Bangalore</h1>
			</div> */}

			<div className="home-middle">
				Health XoXo
			</div>

		</div>
	);
}

