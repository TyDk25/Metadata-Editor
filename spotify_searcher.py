from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import os
from edit_metadata import meta_data

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

client_credentials = SpotifyClientCredentials(client_id=CLIENT_ID,
                                              client_secret=CLIENT_SECRET)


def search(query):
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials)
    searched_song = f'track:{query["Title"]} artist:{query["Artist"]}'
    results = spotify.search(q=searched_song, type='track')
    results = results['tracks']['items']

    print('\nSearch results:')
    for index, item in enumerate(results, 1):
        print(f"{index}.\n\t"
              f"Track: {item['name']}\n\t"
              f"Artist: {item['artists'][0]['name']}\n\t"
              f"Album: {item['album']['name']}\n\t"
              f"Track Number: {item['track_number']}")

    song_choice = int(input('\nEnter choice: '))
    selection = results[song_choice - 1]

    params = {'title': selection['name'], 'artist': selection['artists'][0]['name'],
              'album': selection['album']['name'], 'track_number': selection['track_number'],
              'album_art_url': input('Enter Album Art URL: ')}

    return params


def search_spotify(file_path):
    get_song_name = {'Artist': input('Song name: '), 'Title': input('Artist Name: ')}

    spotify_result = search(get_song_name)

    meta_data(file_path, spotify_result)


