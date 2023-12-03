import React, { useEffect } from 'react'
import { Spotify } from 'react-spotify-embed';

interface ResultsProps {
  heapTime: number | string;
  rbTreeTime: number | string;
  playlistUrl: string | string;
}

export default function Result({heapTime, rbTreeTime, playlistUrl}: ResultsProps) {
  return (
      <div style={{width:'75%',height:'450vh',backgroundColor:"#242222", float:"right"}}>
        <h1 style={{color:'#1bd760'}}>Results</h1>
        <h3 style={{color:'#1bd760'}}>Heap Time: {heapTime} Seconds</h3>
        <h3 style={{color:'#1bd760'}}>Red & Black Tree Time: {rbTreeTime} Seconds</h3>
        {playlistUrl !== 'https://open.spotify.com/' && playlistUrl !== 'https://open.spotify.com/404' && <Spotify link={playlistUrl} width="100%" height="50%"/>}
        {playlistUrl === 'https://open.spotify.com/404' && <h3 style={{color:'red'}}>No Playlist Created</h3>}
      </div>
  )
}
