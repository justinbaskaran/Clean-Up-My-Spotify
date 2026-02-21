import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#### Add the EXACT names of the playlists, podcasts, albums, artists, events, and downloaded songs you want to keep here.
whitelistPlaylist = ["Jazz in the Background", "Royal Leash Radio", "lofi beats"]
whitelistPodcasts = ["Economics Explained"]
whitelistAlbums = []
whitelistArtists = []
whitelistEvents = []
whitelistDownloaded = []
##############################################

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
SCOPE = "user-library-read user-library-modify"

auth_manager = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    show_dialog=True,
    cache_path=".cache"
)

sp = spotipy.Spotify(auth_manager=auth_manager)


def delete_playlists():
    playlists = sp.current_user_playlists()
    hasMore = True
    while hasMore:
        for playlist in playlists['items']:
            if playlist['name'] not in whitelistPlaylist:
                sp.current_user_unfollow_playlist(playlist['id'])
                print(f"Deleted playlist: {playlist['name']} (ID: {playlist['id']})")
        if playlists['next'] is None:
            hasMore = False
        else:
            playlists = sp.next(playlists)


def delete_podcasts():
    podcasts = sp.current_user_saved_episodes()

    # The results are paginated. You can use a loop to get all of them.
    while podcasts['next']:
        podcasts = sp.next(podcasts)
        for podcast in podcasts['items']:
            if podcast['episode']['name'] not in whitelistPodcasts:
                sp.current_user_unfollow_podcast(podcast['episode']['id'])
                print(f"Deleted podcast: {podcast['episode']['name']} (ID: {podcast['episode']['id']})")

def delete_albums():
    albums = sp.current_user_saved_albums()

    # The results are paginated. You can use a loop to get all of them.
    while albums['next']:
        albums = sp.next(albums)
        for album in albums['items']:
            if album['album']['name'] not in whitelistAlbums:
                sp.current_user_saved_albums_delete(album['album']['id'])
                print(f"Deleted album: {album['album']['name']} (ID: {album['album']['id']})")

def delete_artists():
    artists = sp.current_user_followed_artists()
    hasMore = True
    while hasMore:
        for artist in artists['artists']['items']:
            print("hi: "+ artist['name'])
            if artist['name'] not in whitelistArtists:
                sp.user_unfollow_artists(artist['id'])
                print(f"Deleted artist: {artist['name']} (ID: {artist['id']})")

            if artists['next'] is None:
                hasMore = False
            else:
                artists = sp.next(artists)


def delete_events():
    events = sp.current_user_events()

    # The results are paginated. You can use a loop to get all of them.
    while events['next']:
        events = sp.next(events)
        for event in events['items']:
            if event['name'] not in whitelistEvents:
                sp.current_user_unfollow_event(event['id'])
                print(f"Deleted event: {event['name']} (ID: {event['id']})")

def delete_downloaded():
    tracks = sp.current_user_saved_tracks()

    # The results are paginated. You can use a loop to get all of them.
    while tracks['next']:
        tracks = sp.next(tracks)
        for track in tracks['items']:
            if track['track']['name'] not in whitelistDownloaded:
                sp.current_user_saved_tracks_delete([track['track']['id']])
                print(f"Deleted downloaded track: {track['track']['name']} (ID: {track['track']['id']})")



if __name__ == "__main__":
    delete_playlists()
    # delete_podcasts()
    # delete_albums()
    delete_artists()
    # delete_events()
    # delete_downloaded()