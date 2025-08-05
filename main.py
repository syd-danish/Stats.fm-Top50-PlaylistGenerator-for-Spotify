import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import spotipy
from spotipy.oauth2 import SpotifyOAuth





CLIENT_ID="475c331b7b904aecb4f28c9f14b85200"
CLIENT_SECRET="cec8461dde8c42b49390cc2bae770ad8"
REDIRECT_URI="https://example.com"
USER_String="313ndua5u7lw6e2x5gvlkxmmapy4"
CHROME_DRIVER_PATH="/Users/yasindanish13/Downloads/chromedriver137/chromedriver"
RANGE=[["weeks","months","lifetime"],[4,6,'']]
INDEX=1
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}
StatsFM_URL=f"https://stats.fm/user/{USER_String}/tracks?range={RANGE[0][INDEX]}"
service = Service(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)
driver.get(StatsFM_URL)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h4.mt-2.line-clamp-2")))
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
soup=BeautifulSoup(driver.page_source, 'html.parser')
tracks=soup.find_all("h4",class_="mt-2 line-clamp-2")
artists = soup.find_all("p", class_="m-0 line-clamp-2")
song_array=[]
artist_array=[]
for t in range(0,len(tracks)):
    song_name=tracks[t].getText()[3:]
    artist_name = artists[t].getText()
    artist_array.append(artist_name)
    song_array.append(song_name)
    if len(song_array)>49:
        break
print(song_array)
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"))
song_uris = []
for i in range(0,len(song_array)):
    result = sp.search(q=f"{song_array[i]} {artist_array[i]}", type="track", limit=1)
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song_array[i]} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=USER_String, name=f"Your Top 50 Songs - {RANGE[1][INDEX]} {RANGE[0][INDEX].title()}", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
driver.quit()
