import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------------------------

url = input("\npaste your apple music playlist link here: ")

am_playlist = requests.get(url)

soup = BeautifulSoup(am_playlist.content, "html.parser")

filename = url.split("/")[5] + ".csv"

songs = [
    e.text
    for e in soup.find_all("div", {"class": "songs-list-row__song-name"}, text=True)
]

messy_artists = [
    j.text for j in soup.find_all(attrs={"class": "songs-list-row__link"}, text=True)
]

artists = messy_artists[::3]

playlist = zip(artists, songs)

with open("./%s" % filename, "w") as f:
    for (artists, songs) in playlist:
        f.write("{0},{1}\n".format(artists, songs))

print(f"\n{filename} successfully created!\n")

with open(filename, "r") as fin:
    print(fin.read())
