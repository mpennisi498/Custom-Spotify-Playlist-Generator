# Custom-Spotify-Playlist-Generator 

By: Jeffery James, Maxmilian Pennisi, Anthony Zurita
Final Project - COP3530 DSA Fall 2023 - UF

This project generates playlists using the csv in the repo and the Spotify API.
The CSV is read and all the data is placed into a Max Heap and a Red Black Tree.
A user then selects paramters to filter songs into a playlist, the Max Heap and Red Black Tree filter out the relevant songs.
Those songs are then used to create a custom playlist via Spotipy and Spotfiy.

## Setup

### Backend

1. Navigate to the backend directory:

    cd project-code
    cd flask-server

2. Set up a developer account with Spotify and put the correct credentials in creds.json. Make sure to add your username and other Spotify credentials.

3. Set up a virtual environment and activate it:
   
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

5. Install the necessary Python packages:
   
    pip3 install Flask pandas flask_cors Spotipy

6. Run server.py:
   
    python3 'server.py'

### Frontnend

1. Navigate to the frontned directory:

    cd project-code
    cd react-frontend

2. Install the necessary JavaScript packages:

    yarn install  # Or `npm install` if you're using npm

3. Start the frontend

    yarn start  # Or `npm start` if you're using npm



<img width="1493" alt="Screenshot of Frontend" src="https://github.com/mpennisi498/Custom-Spotify-Playlist-Generator/assets/109290637/ca3cf787-cd63-4772-858d-e15eaab5b37d">

