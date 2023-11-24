import React, { useState, useEffect } from "react";
import HomeContainer from "./components/home/HomeContainer";
import 'bootstrap/dist/css/bootstrap.min.css'
import MainNavbar from "./components/home/MainNavbar";

function App() {
  return(
  <div>
    <MainNavbar />
    <HomeContainer/>
  </div>
  )
  
}

export default App;
