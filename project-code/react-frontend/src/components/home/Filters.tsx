import { type } from "os";
import { GENRES } from "./constants";
import React, { useState,useEffect } from 'react';
import Dropdown from 'react-bootstrap/Dropdown';
import Form from 'react-bootstrap/Form';


export default function Filters() {
  const [genre, setGenre] = useState("");
  const [explicit, setExplicit] = useState(false);
  const [popularity, setPopularity] = useState(false);

  const handleGenreChange = (eventKey:string) => {
    setGenre(eventKey);
    console.log(genre);
  }

  const handleExplicitChange = (explicit: boolean) => {
    setExplicit(explicit);
  }

  const handlePopularityChange = (popularity: boolean) => {
    setPopularity(popularity);
  }


  return (
    <div style={{ width: "25%", height: "100vh", backgroundColor: "#817f7f" }}>
      <h1>Filters Go Here</h1>
      <Dropdown>
        <Dropdown.Toggle variant="success" id="dropdown-basic" >
          {genre === "" ? " Select Genre" : genre}
        </Dropdown.Toggle>

        <Dropdown.Menu>
          {GENRES.map((genre) => (
            <Dropdown.Item eventKey={genre}>{genre}</Dropdown.Item>
          ))}
        </Dropdown.Menu>
      </Dropdown>
      <div>
      <Form>
        <Form.Group controlId="formBasicCheckbox">
          <Form.Check type="checkbox" label="Explicit" />
        </Form.Group>
      </Form>
    </div>
    <div>
      <Form>
        <Form.Group controlId="formBasicCheckbox">
          <Form.Check type="checkbox" label="Rank by Popularity" />
        </Form.Group>
      </Form>
    </div>
    </div>
    
  );
}

