import React, { useState,useEffect } from "react";
import NavBar from "./NavBar";

function DoctorCard(props) {
  return (
    <div className="doctor-card">
      <ul className="doctor-card-list">
          <li><h1>Name: {props.name}</h1></li>
          <li><h3>Specialiazation: {props.specialization}</h3></li>
          <li><h3>Hospital: {props.hospital}</h3></li>
      </ul>
      <button type="button" className="profile-button">Profile</button>
      <button type="button" className="profile-button">Book Apointment</button>

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
  
  const [doctors,setDoctors] = React.useState("");
  const [page,setPage] = React.useState(1);
  
  // const getDoctors = () => {
    // fetch("/doctors/doctors?page=1")
    // .then((response) => response.json())
    // .then((data) => {
    //   console.log(data);
    //   // setDoctors(data);
    //   // console.log(doctors);
    // }
  //   );
  // };
  // getDoctors();
  function getDoctors() {
    // fetch(`/doctors/doctors?page=${page}&&doctor-name=${props.doctor_name}&&specialization=${props.specialization}&&hospital=${props.hospital}&&search=${props.search}`)
    
    fetch(`/doctors/doctors?page=${page}`)
    .then((response) => response.json())
    .then((data) => {
      setDoctors(data);
      console.log(data)
      }
    );
  }
  useEffect(() => {
    getDoctors();
    // console.log(doctors)
  },[]);

  function subtractPage() {
    setPage(page-1);
    console.log(page);
    getDoctors();
  }

  function addPage() {
    setPage(page+1);
    console.log(page);
    getDoctors();
  }
  

  return (
    <div>
      <NavBar />
      <div className="heading">
        <h1>24x7 Doctors</h1>
        {/* {console.log(doctors[0])} */}
        <DoctorCard {...doctors[0]} />
        <DoctorCard {...doctors[1]} />
        <DoctorCard {...doctors[2]} />
        <DoctorCard {...doctors[3]} />
        <DoctorCard {...doctors[4]} />

      </div>
      <p className="page-buttons">
        <button type="button" onClick={subtractPage}>Prev</button>
        <button type="button" onClick={addPage}>Next</button>
      </p>
      
    </div>
  );
}
