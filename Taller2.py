import requests
import pandas as pd

CLIENT_ID = 'b631b0feed514eba8b92fbbfeb623fd0'
CLIENT_SECRET = '9de72dbe9bf441b0a11ddf928ce90963'

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# Black Sabbath
artist1_id = '5M52tdBnJaKSvOpJGz8mfZ'
# Led Zeppelin
artist2_id = '36QJpDe2go2KgaRleHCDTp'
# Grupo Niche
artist3_id = '1zng9JZpblpk48IPceRWs8'
# Bod Dylan
artist4_id = '74ASZWbe4lXaubB36ztrGX'
# Michael Jackson
artist5_id = '3fMbdgg4jU18AjLCKBhRSm'

#pull all artists info
re1 = requests.get(BASE_URL + 'artists/' + artist1_id, headers=headers)
re2 = requests.get(BASE_URL + 'artists/' + artist2_id, headers=headers)
re3 = requests.get(BASE_URL + 'artists/' + artist3_id, headers=headers)
re4 = requests.get(BASE_URL + 'artists/' + artist4_id, headers=headers)
re5 = requests.get(BASE_URL + 'artists/' + artist5_id, headers=headers)

re1_json = re1.json()
re2_json = re2.json()
re3_json = re3.json()
re4_json = re4.json()
re5_json = re5.json()

entity1 = {
    'Nombre del artista': re1_json['name'],
    'Popularidad': re1_json['popularity'],
    'tipo': re1_json['type'],
    'Uri': re1_json['uri'],
    'Cantidad de followers': re1_json['followers']['total']
}

entity2 = {
    'Nombre del artista': re2_json['name'],
    'Popularidad': re2_json['popularity'],
    'tipo': re2_json['type'],
    'Uri': re2_json['uri'],
    'Cantidad de followers': re2_json['followers']['total']
}

entity3 = {
    'Nombre del artista': re3_json['name'],
    'Popularidad': re3_json['popularity'],
    'tipo': re3_json['type'],
    'Uri': re3_json['uri'],
    'Cantidad de followers': re3_json['followers']['total']
}

entity4 = {
    'Nombre del artista': re4_json['name'],
    'Popularidad': re4_json['popularity'],
    'tipo': re4_json['type'],
    'Uri': re4_json['uri'],
    'Cantidad de followers': re4_json['followers']['total']
}

entity5 = {
    'Nombre del artista': re5_json['name'],
    'Popularidad': re5_json['popularity'],
    'tipo': re5_json['type'],
    'Uri': re5_json['uri'],
    'Cantidad de followers': re5_json['followers']['total']
}

list_artist = [entity1, entity2, entity3, entity4, entity5]
df1 = pd.DataFrame(list_artist)

# pull all artists albums
r1 = requests.get(BASE_URL + 'artists/' + artist1_id + '/albums',
                 headers=headers,
                 params={'include_groups': 'album', 'limit': 10})
r2 = requests.get(BASE_URL + 'artists/' + artist2_id + '/albums',
                 headers=headers,
                 params={'include_groups': 'album', 'limit': 10})
r3 = requests.get(BASE_URL + 'artists/' + artist3_id + '/albums',
                 headers=headers,
                 params={'include_groups': 'album', 'limit': 10})
r4 = requests.get(BASE_URL + 'artists/' + artist4_id + '/albums',
                 headers=headers,
                 params={'include_groups': 'album', 'limit': 10})
r5 = requests.get(BASE_URL + 'artists/' + artist5_id + '/albums',
                 headers=headers,
                 params={'include_groups': 'album', 'limit': 10})

json_Black_Sabbath = r1.json()
json_Led_Zeppelin = r2.json()
json_Grupo_Niche = r3.json()
json_Bod_Dylan = r4.json()
json_Michael_Jackson = r5.json()

list_jsons = []
list_jsons.append(json_Black_Sabbath)
list_jsons.append(json_Led_Zeppelin)
list_jsons.append(json_Grupo_Niche)
list_jsons.append(json_Bod_Dylan)
list_jsons.append(json_Michael_Jackson)

##################################################################

list_tracks = []  # will hold all track info

for js in list_jsons:
    albums = []  # to keep track of duplicates

    # loop over albums and get all tracks
    for album in js['items']:
        album_name = album['name']

        trim_name = album_name.split('(')[0].strip()
        if trim_name.upper() in albums:
            continue
        albums.append(trim_name.upper())  # use upper() to standardize

        # pull all tracks from this album
        r = requests.get(BASE_URL + 'albums/' + album['id'] + '/tracks', headers=headers)
        tracks = r.json()['items']

        for track in tracks:
            # track info
            entity = {
                'Nombre del track': track['name'],
                'Tipo de track': track['type'],
                'Artista': track['artists'][0]['name'],
                'Album': album_name,
                'Track number': track['track_number'],
                # 'Popularidad':
                'Id': track['id'],
                'Uri': track['uri'],
                'Fecha de lanzamiento': album['release_date'],
                'Géneros': re1_json['genres']
            }

            list_tracks.append(entity)

df2 = pd.DataFrame(list_tracks)

print(list_artist[0])
print(list_tracks[0])
print('\n')
print(df1)
print('\n')
print(df2)