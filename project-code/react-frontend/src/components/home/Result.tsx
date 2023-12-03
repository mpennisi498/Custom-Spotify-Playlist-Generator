import { Spotify } from "react-spotify-embed";

interface ResultsProps {
  heapTime: number | string;
  rbTreeTime: number | string;
  playlistUrl: string | string;
}

// This is the component that displays the results of the playlist creation, if the playlist was created successfully, it will display the playlist link and the time taken to create the playlist
export default function Result({
  heapTime,
  rbTreeTime,
  playlistUrl,
}: ResultsProps) {
  return (
    <div
      style={{
        width: "75%",
        height: "450vh",
        backgroundColor: "#242222",
        float: "right",
      }}
    >
      <h1 style={{ color: "#1bd760" }}>Results</h1>
      {/*Displays times of data structs*/}
      <h3 style={{ color: "#1bd760" }}>Heap Time: {heapTime} Seconds</h3>
      <h3 style={{ color: "#1bd760" }}>
        Red & Black Tree Time: {rbTreeTime} Seconds
      </h3>
      {/*Displays link or that no playlist was created*/}
      {playlistUrl !== "https://open.spotify.com/" &&
        playlistUrl !== "https://open.spotify.com/404" && (
          <Spotify link={playlistUrl} width="100%" height="50%" />
        )}
      {playlistUrl === "https://open.spotify.com/404" && (
        <h3 style={{ color: "red" }}>No Playlist Created</h3>
      )}
    </div>
  );
}
