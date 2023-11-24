import { GENRES } from "./constants";
import React, { useState } from 'react';
import Dropdown from 'react-bootstrap/Dropdown';
import Form from 'react-bootstrap/Form';

//Test
export default function Filters() {
  
  return (
    <div style={{ width: "25%", height: "100vh", backgroundColor: "#817f7f" }}>
      <h1>Filters Go Here</h1>
      <Dropdown>
        <Dropdown.Toggle variant="success" id="dropdown-basic">
          Select Genre
        </Dropdown.Toggle>

        <Dropdown.Menu>
          {GENRES.map((genre) => (
            <Dropdown.Item key={genre}>{genre}</Dropdown.Item>
          ))}
        </Dropdown.Menu>
      </Dropdown>
    </div>
  );
}
