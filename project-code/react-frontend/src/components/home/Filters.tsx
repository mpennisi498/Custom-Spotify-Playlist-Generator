import { GENRES } from "./constants";
import { FormCheck } from "react-bootstrap";
import Dropdown from "react-bootstrap/Dropdown";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { useState } from "react";

//Handles all user filters and sets the state for each filter and passes it to parent component
export default function Filters({ searchPlaylist }: any) {
  const [genre, setGenre] = useState("Select Genre");
  const [artist, setArtist] = useState("");
  const [explicit, setExplicit] = useState(false);
  const [maxSongs, setMaxSongs] = useState(0);

  const handleGenreChange = (event: any) => {
    setGenre(event);
  };

  const handleArtistChange = (event: any) => {
    setArtist(event.target.value);
  };

  const handleExplicitChange = (event: any) => {
    setExplicit(event.target.checked);
  };

  const handleMaxSongsChange = (event: any) => {
    setMaxSongs(event.target.value);
  };

  return (
    <div style={{ width: "25%", height: "450vh", backgroundColor: "#817f7f" }}>
      <h1>Filters</h1>
      <h3>Select Genre</h3>
      <Dropdown onSelect={(key) => handleGenreChange(key)}>
        <Dropdown.Toggle variant="success" id="dropdown-basic">
          {genre}
        </Dropdown.Toggle>

        <Dropdown.Menu>
          {/*Loops through all Genres and Displays it*/}
          {GENRES.map((genre) => (
            <Dropdown.Item key={genre} eventKey={genre}>
              {genre}
            </Dropdown.Item>
          ))}
        </Dropdown.Menu>
      </Dropdown>
      <p style={{ fontSize: "10px" }}>
        Choose a genre to generate a playlist from (Optional)
      </p>
      <h3>Artist</h3>
      <Form.Control
        style={{ width: "50%" }}
        type="text"
        placeholder="Enter an Artist"
        onChange={handleArtistChange}
      />
      <p style={{ fontSize: "10px" }}>
        Choose an artist to generate a playlist from (Optional)
      </p>
      <h3>Explicit</h3>
      <FormCheck
        type="checkbox"
        label="Explicit?"
        onClick={handleExplicitChange}
      />
      <p style={{ fontSize: "10px" }}>
        Choose whether or not to include explicit songs (Optional)
      </p>
      <h3>Max Number of Songs</h3>
      <Form.Control
        style={{ width: "50%" }}
        type="number"
        placeholder="Enter a number"
        onChange={handleMaxSongsChange}
      />
      <p style={{ fontSize: "10px" }}>
        Choose the max number of songs to include in the playlist (Required)
      </p>
      {/*This is the button that calls the searchPlaylist function from the parent component
       */}
      <Button
        variant="success"
        onClick={() => searchPlaylist(genre, artist, explicit, maxSongs)}
      >
        Generate Playlist!
      </Button>{" "}
    </div>
  );
}
