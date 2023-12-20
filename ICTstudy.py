#データセット1
#日本における視聴者数順の最も人気のあるゲーム
import requests

# Replace 'YOUR_CLIENT_ID' with your actual Twitch Client ID
client_id = 'iavfs2kcmogadpd8yhm9hrspl336f9'

# Replace 'YOUR_OAUTH_TOKEN' with your actual Twitch OAuth token
oauth_token = '89l5xves2ot8392jb2easa4iydw2rq'

# Set the API endpoint for getting the top games by current viewers
endpoint = 'https://api.twitch.tv/helix/streams'

# Set headers with necessary information, including the authentication token
headers = {
    'Client-ID': client_id,
    'Authorization': f'Bearer {oauth_token}'
}

# Set parameters for the API request to get the top 10 most streamed games
params = {
    'first': 30,  # Retrieve the top 10 streams
    'sort': 'viewers'  # Sort by current viewers
}

# Make the API request
response = requests.get(endpoint, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    if data.get('data'):
        for stream in data['data']:
            game_name = stream['game_name']
            viewer_count = stream['viewer_count']

            print(f"Game Name: {game_name}")
            print(f"Viewer Count: {viewer_count}")
            #print("=" * 50)

    else:
        print("No streams found.")
else:
    print(f"Error: {response.status_code} - {response.text}")


#データセット2
#twitch全体における視聴者数順の最も人気のあるゲーム
import requests

# Replace 'YOUR_CLIENT_ID' with your actual Twitch Client ID
client_id = 'iavfs2kcmogadpd8yhm9hrspl336f9'
# Replace 'YOUR_OAUTH_TOKEN' with your actual Twitch OAuth token
oauth_token = '89l5xves2ot8392jb2easa4iydw2rq'


# Set the API endpoint for getting streams
endpoint = 'https://api.twitch.tv/helix/games/top'

# Set headers with necessary information, including the authentication token
headers = {
    'Client-ID': client_id,
    'Authorization': f'Bearer {oauth_token}'
}

# Parameters for the API request
params = {
    'first': 30  # Number of streams to retrieve
}

# Make the API request
response = requests.get(endpoint, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    streams = data.get('data', [])

    # Print information about each stream
    for stream in streams:
        print("ID:", stream['id'])
        print("Name:", stream['name'])
        #print("box_art_url:", stream['box_art_url'])
        #print("igdb_id:", stream['igdb_id'])
        #print("\n")
else:
    print(f"Error: {response.status_code} - {response.text}")

#データセット3
#言語別の配信
import requests

# Set your Twitch API client ID and OAuth token
CLIENT_ID = "iavfs2kcmogadpd8yhm9hrspl336f9"
OAUTH_TOKEN = "89l5xves2ot8392jb2easa4iydw2rq"  # Replace with your actual OAuth token
# Construct the API request URL to get active streams
streams_url = "https://api.twitch.tv/helix/streams"

# Set up headers with the client ID and OAuth token
headers = {
    "Client-ID": CLIENT_ID,
    "Authorization": f"Bearer {OAUTH_TOKEN}"
}

# Initialize dictionaries to store stream and viewer data by language
stream_data_by_language = {}
viewer_data_by_language = {}

# Define language codes (not full language names)
languages = [
    "en", "es", "pt", "ru", "de", "fr", "ja", "ko", "zh", "it", "tr", "pl", "th", "ar",
    "unknown", "cs", "nl", "hu", "uk", "sv", "fi", "el", "da", "bg", "tl", "yue", "id",
    "ro", "no", "sk", "vi", "ca", "hi", "ase", "ms"
]

# Fetch stream data for each language and aggregate metrics
for language in languages:
    params = {
        "first": 100,  # You can adjust the number of streams to retrieve
        "language": language
    }

    response = requests.get(streams_url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        streams = data.get("data")

        if streams:
            stream_count = len(streams)
            viewer_count = sum(stream["viewer_count"] for stream in streams)
            average_viewer_count = viewer_count / stream_count

            # Store data by language
            stream_data_by_language[language] = {
                "stream_count": stream_count,
                "viewer_count": viewer_count,
                "average_viewer_count": average_viewer_count
            }
    else:
        print(f"Error fetching data for language {language}: {response.status_code} - {response.text}")

# Sort languages by viewership in descending order
sorted_languages = sorted(stream_data_by_language.keys(), key=lambda lang: stream_data_by_language[lang]["viewer_count"], reverse=True)

# Print languages and their viewership
for language in sorted_languages:
    print(f"Language: {language}")
    #print("Stream Count:", stream_data_by_language[language]["stream_count"])
    print("Total Viewers:", stream_data_by_language[language]["viewer_count"])
    #print("Average Viewers per Stream:", stream_data_by_language[language]["average_viewer_count"])


#データセット4
#ゲームのジャンルとプラットフォームを取得する
import requests

# ご自身のAPIキーをここに追加してください
api_key = '588d5c70ed661e64be6f77d56633f753f425fee7'

# ゲームIDとタイトルのマッピング
game_ids = {
    '32982': 'Grand Theft Auto V',
    '21779': 'League of Legends',
    '516575': 'VALORANT',
    '27471': 'Minecraft',
    '33214': 'Fortnite',
    '18122': 'World of Warcraft',
    '29595': 'Dota 2',
}

# APIエンドポイントとリクエストパラメータのベースURL
base_url = 'https://www.giantbomb.com/api/game/'

# ジャンルとプラットフォーム情報を取得
for game_id, game_title in game_ids.items():
    url = f'{base_url}{game_id}/'

    params = {
        'api_key': api_key,
        'format': 'json',
        'field_list': 'genres,platforms'
    }

    try:
        # APIにリクエストを送信
        response = requests.get(url, params=params)

        # レスポンスのJSONデータを取得
        data = response.json()

        # ゲームの情報を表示
        genres = data.get('results', {}).get('genres', [])
        platforms = data.get('results', {}).get('platforms', [])

        print(f'ゲーム: {game_title}')
        print('ジャンル:')
        for genre in genres:
            print(f'  - {genre.get("name")}')

        print('プラットフォーム:')
        for platform in platforms:
            print(f'  - {platform.get("name")}')

        print('\n')

    except Exception as e:
        print(f'ゲームID {game_id} の情報を取得できませんでした。エラー: {e}')


#データセット5
#1時間に1回データを取得するときのコード
import time

while True:
    # ここに実行したいコードを配置
    #言語別の15トップ配信
    import requests

# Set your Twitch API client ID and OAuth token
    CLIENT_ID = "iavfs2kcmogadpd8yhm9hrspl336f9"
    OAUTH_TOKEN = "89l5xves2ot8392jb2easa4iydw2rq"  # Replace with your actual OAuth token
# Construct the API request URL to get active streams
    streams_url = "https://api.twitch.tv/helix/streams"

# Set up headers with the client ID and OAuth token
    headers = {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {OAUTH_TOKEN}"
    }

# Initialize dictionaries to store stream and viewer data by language
    stream_data_by_language = {}
    viewer_data_by_language = {}

# Define language codes (not full language names)
    languages = ["en",  "ja", "ko","es","ru","fr"]

# Fetch stream data for each language and aggregate metrics
    for language in languages:
        params = {
            "first": 100,  # You can adjust the number of streams to retrieve
           "language": language
        }

        response = requests.get(streams_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            streams = data.get("data")

            if streams:
                stream_count = len(streams)
                viewer_count = sum(stream["viewer_count"] for stream in streams)
                average_viewer_count = viewer_count / stream_count

                # Store data by language
                stream_data_by_language[language] = {
                    "stream_count": stream_count,
                    "viewer_count": viewer_count,
                    "average_viewer_count": average_viewer_count
                }
        else:
            print(f"Error fetching data for language {language}: {response.status_code} - {response.text}")

# Sort languages by viewership in descending order
    sorted_languages = sorted(stream_data_by_language.keys(), key=lambda lang: stream_data_by_language[lang]["viewer_count"], reverse=True)

# Print languages and their viewership
    for language in sorted_languages:
        print(f"Language: {language}")
        #print("Stream Count:", stream_data_by_language[language]["stream_count"])
        print("Total Viewers:", stream_data_by_language[language]["viewer_count"])
        #print("Average Viewers per Stream:", stream_data_by_language[language]["average_viewer_count"])
    # 60分ごとに実行
    time.sleep(3600)