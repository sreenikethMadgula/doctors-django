import React from "react";
import { Link } from "react-router-dom";

export default function NavBar() {
    return(
        
        <nav className="nav">
            <ul className="nav-items">
                {/* <li><Link to="/">Home</Link></li>
                <li><Link to="/doctors">24x7 Doctors</Link></li> */}
                <li>Home</li>
                <li>24x7 Doctors</li>
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
    )
}
