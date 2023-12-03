// Main page for the application, contains the filters and the result component
import Filters from "./Filters";
import Result from "./Result";
import { useState } from "react";
import { Alert, Spinner } from "react-bootstrap";

export default function HomeContainer() {
  const [playlistLink, setPlaylistLink] = useState("https://open.spotify.com/");
  const [heapTime, setHeapTime] = useState(0);
  const [RBTime, setRBTime] = useState(0);
  const [displayAlert, setDisplayAlert] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const searchPlaylist = async (
    genre: string,
    artist: string,
    explicit: boolean,
    maxSongs: number
  ) => {
    //Displays alert if max songs is less than 0
    if (maxSongs <= 0) {
      setDisplayAlert(true);
      return;
    }
    setIsLoading(true);
    //Sends data from flask backend with parameters from user, receives playlist link and time taken to create playlist
    fetch("http://localhost:8080/api/home", {
      method: "POST", // or 'PUT'
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        key1: { genre },
        key2: { artist },
        key3: { explicit },
        key4: { maxSongs },
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        //Sets state with data from flask backend
        setPlaylistLink(data.playlistLink);
        setHeapTime(data.heapTime);
        setRBTime(data.RBTime);
        setIsLoading(false);
      });
  };

  return (
    <div>
      {/*Display alert if max songs is 0 or less*/}
      {displayAlert && (
        <Alert
          variant="danger"
          onClose={() => setDisplayAlert(false)}
          dismissible
        >
          Max songs must be greater than 0
        </Alert>
      )}
      {/*If not loading display results*/}
      {!isLoading && (
        <Result
          heapTime={heapTime}
          playlistUrl={playlistLink}
          rbTreeTime={RBTime}
        />
      )}
      {isLoading && (
        <div
          style={{
            width: "75%",
            height: "450vh",
            backgroundColor: "#242222",
            float: "right",
            justifyContent: "right",
            alignItems: "right",
          }}
        >
          {/*Loading spinner is isLoading is true*/}
          <Spinner
            animation="border"
            role="status"
            style={{
              width: "100px",
              height: "100px",
              color: "#1bd760",
              marginLeft: "50%",
              marginTop: "20%",
            }}
          />
        </div>
      )}
      <Filters searchPlaylist={searchPlaylist} />
    </div>
  );
}
