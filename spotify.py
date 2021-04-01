import spotipy
import os

from pathlib import Path
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
redirect_uri = os.environ.get('redirect_uri')
username = os.environ.get('username')
scope = os.environ.get('scope')

auth_manager = SpotifyOAuth(
  client_id,
  client_secret,
  redirect_uri,
  username,
  scope
)

spotify = spotipy.Spotify(auth_manager=auth_manager)
devices = spotify.devices()['devices']
device_name = 'Guilherme’s MacBook Pro'
device = None

def get_device() -> str:
  for i, device in enumerate(devices):
    name = device['name']
    device_id = device['id']

    if(name == device_name):
      return device_id

def get_album_uri(q: str) -> str:
  items = None
  name = q.replace(' ', '+')

  results = spotify.search(q=name, limit=1, type='album')
  items = results['albums']['items']

  if not items:
    print('Not found album')
  
  item = items[0]
  uri = item['uri']

  return uri

def get_track_uri(q: str) -> str:
  items = None
  name = q.replace(' ', '+')

  results = spotify.search(q=name, limit=1, type='track')
  items = results['tracks']['items']

  if not items:
    print('Not found track')
  
  item = items[0]
  uri = item['uri']

  print(uri)

  return uri

def play_album(uri: str):
  device = get_device()
  spotify.start_playback(device_id=device, context_uri=uri)

def play_track(uri: str):
  device = get_device()
  spotify.start_playback(device_id=device, uris=[uri])
