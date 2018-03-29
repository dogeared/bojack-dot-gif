#!/usr/bin/python

from images2gif import writeGif
from PIL import Image, ImageFont, ImageDraw
from numpy import array
import os
import re
import ConfigParser
import pysrt
import random
import subprocess
import argparse

sub_files = {   
    101: 'subs/BoJackHorseman.01x01.srt',   
    102: 'subs/BoJackHorseman.01x02.srt',    
    103: 'subs/BoJackHorseman.01x03.srt',    
    104: 'subs/BoJackHorseman.01x04.srt',    
    105: 'subs/BoJackHorseman.01x05.srt',    
    106: 'subs/BoJackHorseman.01x06.srt',    
    107: 'subs/BoJackHorseman.01x07.srt',    
    108: 'subs/BoJackHorseman.01x08.srt',    
    109: 'subs/BoJackHorseman.01x09.srt',    
    110: 'subs/BoJackHorseman.01x10.srt',    
    111: 'subs/BoJackHorseman.01x11.srt',    
    112: 'subs/BoJackHorseman.01x12.srt',    
    201: 'subs/BoJackHorseman.02x01.srt',    
    202: 'subs/BoJackHorseman.02x02.srt',    
    203: 'subs/BoJackHorseman.02x03.srt',    
    204: 'subs/BoJackHorseman.02x04.srt',    
    205: 'subs/BoJackHorseman.02x05.srt',    
    206: 'subs/BoJackHorseman.02x06.srt',    
    207: 'subs/BoJackHorseman.02x07.srt',    
    208: 'subs/BoJackHorseman.02x08.srt',    
    209: 'subs/BoJackHorseman.02x09.srt',    
    210: 'subs/BoJackHorseman.02x10.srt',    
    211: 'subs/BoJackHorseman.02x11.srt',    
    212: 'subs/BoJackHorseman.02x12.srt',    
    301: 'subs/BoJackHorseman.03x01.srt',    
    302: 'subs/BoJackHorseman.03x02.srt',    
    303: 'subs/BoJackHorseman.03x03.srt',    
    304: 'subs/BoJackHorseman.03x04.srt',    
    305: 'subs/BoJackHorseman.03x05.srt',    
    306: 'subs/BoJackHorseman.03x06.srt',    
    307: 'subs/BoJackHorseman.03x07.srt',    
    308: 'subs/BoJackHorseman.03x08.srt',    
    309: 'subs/BoJackHorseman.03x09.srt',    
    310: 'subs/BoJackHorseman.03x10.srt',    
    311: 'subs/BoJackHorseman.03x11.srt',    
    312: 'subs/BoJackHorseman.03x12.srt',    
    401: 'subs/BoJackHorseman.04x01.srt',    
    402: 'subs/BoJackHorseman.04x02.srt',    
    403: 'subs/BoJackHorseman.04x03.srt',    
    404: 'subs/BoJackHorseman.04x04.srt',    
    405: 'subs/BoJackHorseman.04x05.srt',    
    406: 'subs/BoJackHorseman.04x06.srt',    
    407: 'subs/BoJackHorseman.04x07.srt',    
    408: 'subs/BoJackHorseman.04x08.srt',    
    409: 'subs/BoJackHorseman.04x09.srt',    
    410: 'subs/BoJackHorseman.04x10.srt',    
    411: 'subs/BoJackHorseman.04x11.srt',    
    412: 'subs/BoJackHorseman.04x12.srt',    
}

def striptags(data):
	# I'm a bad person, don't ever do this.
	# Only okay, because of how basic the tags are.
	p = re.compile(r'<.*?>')
	return p.sub('', data)

def drawText(draw, x, y, text, font):
	# black outline
	draw.text((x-1, y),text,(0,0,0),font=font)
	draw.text((x+1, y),text,(0,0,0),font=font)
	draw.text((x, y-1),text,(0,0,0),font=font)
	draw.text((x, y+1),text,(0,0,0),font=font)

	# white text
	draw.text((x, y),text,(255,255,255),font=font)

def makeGif(source, sub_index, rand=False, no_quote=False, custom_subtitle="", frames=0, filename="star_wars.gif"):
  config = ConfigParser.ConfigParser()
  config.read("config.cfg")

  config.sections()

  ffmpeg = config.get("general", "ffmpeg")

  if not ffmpeg.strip():
    vlc_path = config.get("general", "vlc_path")

  video_path = config.get("general", "ep"+str(source)+"_path")
  screencap_path = os.path.join(os.path.dirname(__file__), "screencaps")

  # delete the contents of the screencap path
  file_list = os.listdir(screencap_path)
  for file_name in file_list:
    os.remove(os.path.join(screencap_path, file_name))

  # read in the quotes for the selected movie
  subs = pysrt.open(sub_files[source])

  if rand:
    sub_index = random.randint(0, len(subs)-1)

  if no_quote:
    if not ffmpeg:
      start = (3600 * subs[sub_index].end.hours) + (60 * subs[sub_index].end.minutes) + subs[sub_index].end.seconds + (0.001*subs[sub_index].end.milliseconds)
      end = (3600 * subs[sub_index+1].start.hours) + (60 * subs[sub_index+1].start.minutes) + subs[sub_index+1].start.seconds + (0.001*subs[sub_index+1].start.milliseconds)
    else:
      start = subs[sub_index].end
      end = subs[sub_index+1].start - subs[sub_index].end
  else:
    if not ffmpeg:
      start = (3600 * subs[sub_index].start.hours) + (60 * subs[sub_index].start.minutes) + subs[sub_index].start.seconds + (0.001*subs[sub_index].start.milliseconds)
      end = (3600 * subs[sub_index].end.hours) + (60 * subs[sub_index].end.minutes) + subs[sub_index].end.seconds + (0.001*subs[sub_index].end.milliseconds)
    else:
      start = subs[sub_index].start
      end = subs[sub_index].end - subs[sub_index].start
    text = striptags(subs[sub_index].text).split("\n")

  if len(custom_subtitle) > 0:
    text = [custom_subtitle]

  if not ffmpeg:
    # tell vlc to go get images for gifs
    subprocess.call([vlc_path,
      '-Idummy',
      '--video-filter',
      'scene',
      '-Vdummy',
      '--no-audio',
      '--scene-height=256',
      '--scene-width=512',
      '--scene-format=png',
      '--scene-ratio=1',
      '--start-time='+str(start),
      '--stop-time='+str(end),
      '--scene-prefix=thumb',
      '--scene-path='+screencap_path,
      video_path,
      'vlc://quit'
      ])
  else:
    start = str(start).replace(',', '.')
    end   = str(end).replace(',', '.')
    subprocess.call("sleep1 ; ffmpeg -i %s -ss %s -t %s %s" %(video_path, start, end, screencap_path + '/thumb%05d.png'), shell=True)
    # subprocess.call([ffmpeg,
    #   '-i',
    #   video_path,
    #   '-ss',
    #   start,
    #   '-t',
    #   end,
    #   screencap_path + '/thumb%05d.png'
    #   ])


  file_names = sorted((fn for fn in os.listdir(screencap_path)))
  images = []

  font = ImageFont.truetype("fonts/DejaVuSansCondensed-BoldOblique.ttf", 16)

  # remove the first image from the list
  file_names.pop(0)

  # remove every other image for smoother playback
  for i, f in enumerate(file_names):
    if(i%2 == 0):
      os.remove(os.path.join(screencap_path,f))
      file_names.pop(i)


  for f in file_names:
    try:
      image = Image.open(os.path.join(screencap_path,f))
      draw = ImageDraw.Draw(image)

      try:
        image_size
      except NameError:
        image_size = image.size

      # deal with multi-line quotes
      try:
        if len(text) == 2:
          # at most 2?
          text_size = font.getsize(text[0])
          x = (image_size[0]/2) - (text_size[0]/2)
          y = image_size[1] - (2*text_size[1]) - 5 # padding
          drawText(draw, x, y, text[0], font)

          text_size = font.getsize(text[1])
          x = (image_size[0]/2) - (text_size[0]/2)
          y += text_size[1]
          drawText(draw, x, y, text[1], font)
        else:
          text_size = font.getsize(text[0])
          x = (image_size[0]/2) - (text_size[0]/2)
          y = image_size[1] - text_size[1] - 5 # padding
          drawText(draw, x, y, text[0], font)
      except NameError:
        pass
      # do nothing.

      # if not all black?
      if image.getbbox():
        # add it to the array
        images.append(array(image))
        print 'image appended.'

        if frames != 0 and len(images) == frames:
          # got all the frames we need - all done
          break
      else:
        print 'all black frame found.'
    except IOError:
      print 'empty frame found.'

  # create a fuckin' gif
  print "generating gif..."
  writeGif(filename, images)

  if rand:
    try:
      return text
    except:
      return []


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--episodes', type=int, metavar="EPISODE", nargs='*', default=[
        101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112,
        201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212,
        301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312,
        401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412
    ],
    help='episode numbers, space-separated')

	group = parser.add_mutually_exclusive_group()
	group.add_argument('--random', dest='index', action='store_false',
						help='use a random subtitle index (default behaviour)')
	group.add_argument('--index', dest='index', type=int, nargs='?', default=0,
						help='subtitle index (starts at 1)')
	parser.set_defaults(index=False)

	group = parser.add_mutually_exclusive_group()
	group.add_argument('--quote', dest='no_quote', action='store_false')
	group.add_argument('--no-quote', dest='no_quote', action='store_true')
	parser.set_defaults(no_quote=-1)

	parser.add_argument('--filename', type=str, nargs='?', default="star_wars.gif",
						help='filename for the GIF (default: star_wars.gif)')

	args = parser.parse_args()

	random_index = (args.index == False)
	sub_index = (args.index - 1) if not random_index else 0
	no_quote = args.no_quote if args.no_quote != -1 else bool(random.getrandbits(1))

	# by default we create a random gif
	makeGif(random.choice(args.episodes), sub_index=sub_index, rand=random_index, no_quote=no_quote, filename=args.filename)

