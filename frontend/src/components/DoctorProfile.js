import React from "react";

export default function DoctorProfile({id}) {
  const [doctor,setDoctor] = React.useState("");

    function getDoctor() {
        fetch(`/doctors/doctors/${id}`)
        .then((response) => response.json())
        .then((data) => {
          setDoctors(data);
          console.log(data)
          }
        );
      }
      useEffect(() => {
        getDoctor();
        // console.log(doctors)
      },[]);
    return (
      <div className="doctor-Profile">
        
        <ul>
            <li><h1>Name: {props.name}</h1></li>
            <li><h3>Degree: {props.degree} </h3></li>
            <li><h3>Specialiazation: {props.specialization}</h3></li>
            <li><h3>Hospital:{props.hospital}</h3></li>
            <li><h3>Experience:{props.experience}</h3></li>
            <li><h3>Awards: {props.awards}</h3></li>
        </ul>
      </div>
    );
  }