import requests
from utilities.common import config

client_id = config(['Twitch', 'client_id'], filename='tokens.toml')
client_secret = config(['Twitch', 'client_secret'], filename='tokens.toml')

body = {
    'client_id': client_id,
    'client_secret': client_secret,
    "grant_type": 'client_credentials'
}
r = requests.post('https://id.twitch.tv/oauth2/token', body)

#data output
keys = r.json()
headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + keys['access_token']
}




# FUNCTIONS ====================================================================

def get_stream(streamer_name):
    """
    Returns stream data if streamer is live, otherwise return None
    data keys: id, user_id, user_login, user_name, game_id, game_name, type, 
               title, viewer_count, started_at, language, thumbnail_url, tag_ids, is_mature
    """
    stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=headers)
    stream_data = stream.json()
    if len(stream_data['data']) == 1: return stream_data['data'][0]
    return None

if __name__ == "__main__":
    import time
    while True:
        stream_data = get_stream('origamijr')
        if stream_data:
            print(stream_data['user_name'] + ' is live!\n' + stream_data['title'] + ' | playing ' + stream_data['game_name'] + ' | start at ' + stream_data['started_at'])
        else:
            print('not live')
        time.sleep(5)