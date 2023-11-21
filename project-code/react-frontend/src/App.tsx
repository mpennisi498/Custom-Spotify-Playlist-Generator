import React, { useState, useEffect } from "react";
import HomeContainer from "./components/home/HomeContainer";
import 'bootstrap/dist/css/bootstrap.min.css'
import MainNavbar from "./components/home/MainNavbar";

function App() {
  // const [data, setData] = useState("Loading...");
  // useEffect(() => {
  //   fetch("http://localhost:8080/api/home")
  //     .then((res) => res.json())
  //     .then((data) => setData(data.message));
  // }, []);

  return(
  <div>
    <MainNavbar />
    <HomeContainer/>
  </div>
  )
  
}

export default App;
