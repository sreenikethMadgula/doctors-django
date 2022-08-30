import React, {useState} from "react";
import { Link } from "react-router-dom";


export default function NavBar() {
    const [search,setSearch] = React.useState("");

    const [searchParams,setSearchParams] = useState(
        {
            doctor_name : "",
            specialization: "",
            hospital: "",
            search: "",
        }
    );

    function addDoctorName(s) {
        setSearchParams(...searchParams.doctor_name = s)
    }
    function addSpecialization(s) {
        setSearchParams(...searchParams.specialization = s)
    }
    function addHospital(s) {
        setSearchParams(...searchParams.hospital = s)
    }

    return(
        <nav className="nav">
            <ul className="nav-items">
                <li><Link to="/doctors-django" className="links">Home</Link></li>
                <li><Link to="/doctors-django/doctors" className="links">24x7 Doctors</Link></li>
                <li>Medicine</li>
                <li>Lab Test</li>
                <li>Reminder</li>
                <li>Cart</li>
            </ul>
            <div className="search">
                <form>
                    <input type="search" placeholder="Search doctors,specialiazations,hospitals" className="search-bar"  />
                    <button type="submit" className="search-button">Search</button> 
                </form>
            </div>
        </nav>
    );
}
