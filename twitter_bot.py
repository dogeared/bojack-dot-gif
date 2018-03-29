import base64
import json
import requests
import ConfigParser
import random
import os
import time
import subprocess

from twython import Twython
from base64 import b64encode
from makeGifs import makeGif


config = ConfigParser.ConfigParser()
config.read("config.cfg")
config.sections()
CLIENT_ID = config.get("imgur", "client_id")
API_KEY = config.get("imgur", "api_key")
APP_KEY = config.get("twitter", "app_key")
APP_SECRET = config.get("twitter", "app_secret")
OAUTH_TOKEN = config.get("twitter", "oauth_token")
OAUTH_TOKEN_SECRET = config.get("twitter", "oauth_token_secret")

headers = {"Authorization": "Client-ID " + CLIENT_ID}
url = "https://api.imgur.com/3/upload.json"

episodes = [
	101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112,
	201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212,
	301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312,
	401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412
]

while True:
	while True:
		try:
			quote = makeGif(random.choice(episodes), 0, rand=True, no_quote=False)
			quote = ' '.join(quote)
		except:
			continue
		else:
			break

	# first pass reduce the amount of colors
	if(os.path.getsize('star_wars.gif') > 5242880):
		subprocess.call(['convert',
						'star_wars.gif',
						'-layers',
						'Optimize',
						'-colors',
						'128',
						'-loop',
						'0',
						'star_wars.gif'])

	# second pass reduce the amount of colors
	if(os.path.getsize('star_wars.gif') > 5242880):
		subprocess.call(['convert',
						'star_wars.gif',
						'-layers',
						'Optimize',
						'-colors',
						'64',
						'-loop',
						'0',
						'star_wars.gif'])

	# other passes reduce the size
	while(os.path.getsize('star_wars.gif') > 5242880):
		subprocess.call(['convert',
						'star_wars.gif',
						'-resize',
						'90%',
						'-coalesce',
						'-layers',
						'optimize',
						'-loop',
						'0',
						'star_wars.gif'])

	try:
		response = requests.post(
			url,
			headers = headers,
			data = {
				'key': API_KEY,
				'image': b64encode(open('star_wars.gif', 'rb').read()),
				'type': 'base64',
				'name': 'star_wars.gif',
				'title': 'Star Wars Dot Gif'
			}
		)
	except (requests.exceptions.ConnectionError, OpenSSL.SSL.SysCallError):
		# try again.
		continue


	try:
		res_json = response.json()
		link = res_json['data']['link']
	except (KeyError, ValueError):
		# try again.
		continue
	

	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

	# upload media
	gif = open('star_wars.gif', 'rb')
	response = twitter.upload_media(media=gif)


	if len(quote) > 70:
		quote = (quote[:67] + '...')

	if len(quote) == 0:
		quote = "..."

	status = '"' + quote + '" ' + link + ' #bojackgif'

	print "tweeting..."
	try:
		twitter.update_status(status=status, media_ids=[response['media_id']])
	except:
		# error with twitter sleep a bit and try again
		time.sleep(1800)
		continue

	print "sleeping..."
	# sleep 1 hour
	time.sleep(3600)
