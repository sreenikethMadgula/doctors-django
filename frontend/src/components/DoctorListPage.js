import React from "react";
import NavBar from "./NavBar";


function DoctorCard(props) {
  return (
    <div className="doctor-card">
      <ul>
          <li><h1>Name: {props.doctor.name}</h1></li>
          <li><h3>Specialiazation: {props.doctor.specialization}</h3></li>
          <li><h3>Hospital: {props.doctor.hospital}</h3></li>
      </ul>
    </div>
  );
}

function DoctorProfile(props) {
  return (
    <div className="doctor-Profile">
      <ul>
          <li><h1>Name: {props.doctor.name}</h1></li>
          <li><h3>Degree: {props.doctor.degree} </h3></li>
          <li><h3>Specialiazation: {props.doctor.specialization}</h3></li>
          <li><h3>Hospital:{props.doctor.hospital}</h3></li>
          <li><h3>Experience:{props.doctor.experience}</h3></li>
          <li><h3>Awards: {props.doctor.awards}</h3></li>
      </ul>
    </div>
  );
}

export default function DoctorListPage(props) {
  return (
    <div>
      <NavBar />
      <div className="heading">
        if (props.search){
          <h1>Search results for: {search.query}</h1>
        }
        else{
          <h1 className="heading">24x7 Doctors</h1>
        }
      </div>
      <div className="results">
        if (!props.doctors) {
          <h2>No results found</h2>
        }
        for (doctor in props.doctors) {
          <DoctorCard doctor />
        }
      </div>
    </div>
  );
}
