import React, { useState, useEffect } from "react";

export default function Result() {
  const test = async () => {
    console.log("test")
   fetch("http://localhost:8080/api/home", {
     method: 'POST', // or 'PUT'
     headers: {
       'Content-Type': 'application/json',
       },
       body: JSON.stringify({
         "key1": "Afrobeat",
         "key2": "true",
         "key3": "Yo momma"
         }),
        })
        .then((res) => res.json())
        .then((data) => console.log(data.message));
  }

  return (
    <div
      style={{
        width: "75%",
        height: "100vh",
        backgroundColor: "#242222",
        float: "right",
      }}
    >
      <h1 style={{ color: "#1bd760" }}>Results Go Here</h1>
      <button onClick={test}>Test</button>
    </div>
  );
}
