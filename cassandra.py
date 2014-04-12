#!/usr/bin/env python3

import spt.spotify

def cass():
    spot = spt.spotify.SpotifyController()
    reactions = {}
    reactions['spot.fwd'] = ['next track', 'music next', 'music, next']
    reactions['spot.prv'] = ['previous track', 'music previous', 'music, previous']

    while True:
        try:
            i = input(">>> ")
            if i.strip() in reactions['spot.fwd']:
                spot.forward()
            if i.strip() in reactions['spot.prv']:
                spot.previous()
        except EOFError:
            return 0

cass()
