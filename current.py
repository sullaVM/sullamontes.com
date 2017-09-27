from flask import Flask
from flask import render_template

app = Flask(__name__)

import sys
import spotipy
import spotipy.util as util
import json
import threading

scope = 'user-read-currently-playing'

@app.route("/")
def hello(name=None):
    username = ''
    token = util.prompt_for_user_token(username, scope, client_id='',
                                       client_secret='',
                                       redirect_uri='')

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_playing_track()
        track = results['item']['name']
        print track
        artist = results['item']['artists'][0]['name']
        print artist
        url = results['item']['external_urls']['spotify']
        name = track + ' - ' + artist
        return render_template('index.html', url=url, name=name)
    else:
        print "Can't get token for", username


if __name__ == "__main__":
    app.run(host='0.0.0.0')