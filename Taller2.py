import requests
import pandas as pd
from datetime import datetime
from datetime import timezone
from sqlalchemy import create_engine

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
now1 = datetime.now()
time1 = now1.replace(tzinfo=timezone.utc).timestamp()

re2 = requests.get(BASE_URL + 'artists/' + artist2_id, headers=headers)
now2 = datetime.now()
time2 = now1.replace(tzinfo=timezone.utc).timestamp()

re3 = requests.get(BASE_URL + 'artists/' + artist3_id, headers=headers)
now3 = datetime.now()
time3 = now1.replace(tzinfo=timezone.utc).timestamp()

re4 = requests.get(BASE_URL + 'artists/' + artist4_id, headers=headers)
now4 = datetime.now()
time4 = now1.replace(tzinfo=timezone.utc).timestamp()

re5 = requests.get(BASE_URL + 'artists/' + artist5_id, headers=headers)
now5 = datetime.now()
time5 = now1.replace(tzinfo=timezone.utc).timestamp()

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
    'Cantidad de followers': re1_json['followers']['total'],
    'Origen': re1_json['href'],
    'Fecha de carga': time1
}

entity2 = {
    'Nombre del artista': re2_json['name'],
    'Popularidad': re2_json['popularity'],
    'tipo': re2_json['type'],
    'Uri': re2_json['uri'],
    'Cantidad de followers': re2_json['followers']['total'],
    'Origen': re2_json['href'],
    'Fecha de carga': time2
}

entity3 = {
    'Nombre del artista': re3_json['name'],
    'Popularidad': re3_json['popularity'],
    'tipo': re3_json['type'],
    'Uri': re3_json['uri'],
    'Cantidad de followers': re3_json['followers']['total'],
    'Origen': re3_json['href'],
    'Fecha de carga': time3
}

entity4 = {
    'Nombre del artista': re4_json['name'],
    'Popularidad': re4_json['popularity'],
    'tipo': re4_json['type'],
    'Uri': re4_json['uri'],
    'Cantidad de followers': re4_json['followers']['total'],
    'Origen': re4_json['href'],
    'Fecha de carga': time4
}

entity5 = {
    'Nombre del artista': re5_json['name'],
    'Popularidad': re5_json['popularity'],
    'tipo': re5_json['type'],
    'Uri': re5_json['uri'],
    'Cantidad de followers': re5_json['followers']['total'],
    'Origen': re5_json['href'],
    'Fecha de carga': time5
}

list_artist = [entity1, entity2, entity3, entity4, entity5]
df1 = pd.DataFrame(list_artist)

# pull all artists albums
r1 = requests.get(BASE_URL + 'artists/' + artist1_id + '/albums',
                 headers=headers,
                 params={'include_groups': 'album', 'limit': 10})
now1 = datetime.now()
time1 = now1.replace(tzinfo=timezone.utc).timestamp()

r2 = requests.get(BASE_URL + 'artists/' + artist2_id + '/albums',
                 headers=headers,
                 params={'include_groups': 'album', 'limit': 10})
now2 = datetime.now()
time2 = now1.replace(tzinfo=timezone.utc).timestamp()

r3 = requests.get(BASE_URL + 'artists/' + artist3_id + '/albums',
                 headers=headers,
                 params={'include_groups': 'album', 'limit': 10})
now3 = datetime.now()
time3 = now1.replace(tzinfo=timezone.utc).timestamp()

r4 = requests.get(BASE_URL + 'artists/' + artist4_id + '/albums',
                 headers=headers,
                 params={'include_groups': 'album', 'limit': 10})
now4 = datetime.now()
time4 = now1.replace(tzinfo=timezone.utc).timestamp()

r5 = requests.get(BASE_URL + 'artists/' + artist5_id + '/albums',
                 headers=headers,
                 params={'include_groups': 'album', 'limit': 10})
now5 = datetime.now()
time5 = now1.replace(tzinfo=timezone.utc).timestamp()


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

cont = 1

for js in list_jsons:

    if cont == 1:
        t = time1
    elif cont == 2:
        t = time2
    elif cont == 3:
        t = time3
    elif cont == 4:
        t = time4
    elif cont == 5:
        t = time5

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
                'Géneros': re1_json['genres'],
                'Origen': track['href'],
                'Fecha de carga': t
            }

            list_tracks.append(entity)
    cont+=1

df2 = pd.DataFrame(list_tracks)

print(list_artist[0])
print(list_tracks[0])
print('\n')
print(df1)
print('\n')
print(df2)

engine = create_engine('postgresql://postgres:1234@127.0.0.1:5432/postgres')

df1.to_sql('Artistas', con=engine, index=False, if_exists='replace')
df2.to_sql('Canciones', con=engine, index=False, if_exists='replace')