from flask import Flask, jsonify, request
from flask_cors import CORS
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from redblack import RedBlackTree
from heap import MaxHeap
import time
import json

app = Flask(__name__)
CORS(app)


rbtree = RedBlackTree()
heap = MaxHeap()


def addData():
    # This function is used to add data to the data structures
    # Times how long insertion takes for each data structure
    rbtime = 0
    heaptime = 0
    rb_start = time.time()
    data = pd.read_csv("dataset.csv")
    for i in range(0, len(data)):
        track_id = data.iloc[i, 1]
        artist = data.iloc[i, 2]
        # Only count first artist, doesnt count features
        if (type(artist) == str):
            artist = data.iloc[i, 2].split(';')[0]
        title = data.iloc[i, 4]
        popularity = data.iloc[i, 5]
        genre = data.iloc[i, 20]
        explicit = str(data.iloc[i, 7])

        rbtree.insert(popularity, artist, track_id, title, genre, explicit)

    rb_end = time.time()
    rbtime = rb_end - rb_start

    heap_start = time.time()
    for i in range(0, len(data)):
        track_id = data.iloc[i, 1]
        artist = data.iloc[i, 2]
        # Only count first artist, doesnt count features
        if (type(artist) == str):
            artist = data.iloc[i, 2].split(';')[0]
        title = data.iloc[i, 4]
        popularity = data.iloc[i, 5]
        genre = data.iloc[i, 20]
        explicit = str(data.iloc[i, 7])

        heap.insertNode(popularity, track_id, artist, genre, explicit)

    heap_end = time.time()
    heaptime = heap_end - heap_start

    return rbtime, heaptime


def makePlaylist(tracks):
    #https://www.youtube.com/watch?v=jSOrEmKUd_c - Ref Video on how to use spotipy

    with open('creds.json') as f:
        creds = json.load(f)

    # THIS IS A TERRIBLE PRATICE NEVER DO WITH ACTUAL CREDENTIALS
    # THIS IS JUST FOR THE PURPOSE OF THE PROJECT
    # USES A BURNER EMAIL AND SPOTIFY ACCOUNT
    # USE YOUR OWN CREDENTIALS IF YOU WANT TO USE THIS, SETUP THROUGH SPOTIFY DEVELOPER
    SPOTIPY_CLIENT_ID = creds['SPOTIPY_CLIENT_ID']
    SPOTIPY_CLIENT_SECRET = creds['SPOTIPY_CLIENT_SECRET']
    SPOTIPY_REDIRECT_URI = creds['SPOTIPY_REDIRECT_URI']

    scope = 'playlist-modify-private'
    #### INPUT OWN USERNAME HERE ####
    username = ''
    token = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
                         redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope, username=username)
    spObj = spotipy.Spotify(auth_manager=token)

    playlist = spObj.user_playlist_create(
        user=username, name='Your Curated Playlist', public=False)

    #Adds songs in tracks to playlist
    spObj.user_playlist_add_tracks(user=username, playlist_id=playlist['id'], tracks=[
                                   "spotify:track:"+track for track in tracks])

    # Returns the link to the playlist
    return playlist['external_urls']['spotify']


@app.route('/api/home', methods=['POST'])
def return_playlist():
    rbTime, heapTime = addData()
    
    #Filters data from user input
    data = request.get_json()
    genre = data['key1']['genre']
    if (genre == 'No Genre' or genre == 'Select Genre'):
        genre = ''
    else:
        genre = genre.lower()
    artist = data['key2']['artist']
    if (artist == 'No Artist'):
        artist = ''
    explicit = data['key3']['explicit']
    maxSongs = int(data['key4']['maxSongs'])

    #Searches and timesfor songs in both data structures
    #Filtering of user filters occurs within the data structure
    rbtracks = []
    start_rb = time.time()
    rbResults = rbtree.search(artist, genre, explicit, maxSongs)
    #Loop through returned set and add to list of tracks
    for item in rbResults:
        rbtracks.append(item)
    end_rb = time.time()
    rbTime += end_rb - start_rb

    #Heap Filtering Occurs here
    start_heap = time.time()
    heap_tracks = set()
    while len(heap_tracks) < maxSongs:
        if (heap.returnSize() == 0):
            break
        # Checking if the ExtractMax() pops song with the correct genre, artist, and explicitness occurs here not within the strucutre
        heapResults = heap.extractMax()
        if (heapResults['genre'].lower() == genre or genre == ''):
            if (heapResults['artistName'] == artist or artist == ''):
                if (heapResults['explicit'] == str(explicit) or str(explicit) == '' or explicit == True):
                    heap_tracks.add(heapResults['ID'])

    end_heap = time.time()
    heapTime += end_heap - start_heap

    # Choose the largest of the two data structures - they should be the same
    tracks = []
    if (len(heap_tracks) < len(rbtracks)):
        for item in rbtracks:
            tracks.append(item)
    else:
        for item in heap_tracks:
            tracks.append(item)

    # If empty return 404
    if (len(tracks) == 0):
        return jsonify({'playlistLink': 'https://open.spotify.com/404',
                        'heapTime': round(heapTime, 5),
                        'RBTime': round(rbTime, 5),
                        })

    # Make playlist and return link
    link = makePlaylist(tracks)

    return jsonify({'playlistLink': link,
                    'heapTime': round(heapTime, 5),
                    'RBTime': round(rbTime, 5),
                    })


if __name__ == "__main__":
    app.run(debug=True, port=8080)
