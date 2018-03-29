#!/usr/bin/python

import urwid
import pysrt
from makeGifs import makeGif

choices = [ 
    { 'name': "BoJack Horseman: S01E01", 'num': 101 },
    { 'name': "BoJack Horseman: S01E02", 'num': 102 },
    { 'name': "BoJack Horseman: S01E03", 'num': 103 },
    { 'name': "BoJack Horseman: S01E04", 'num': 104 },
    { 'name': "BoJack Horseman: S01E05", 'num': 105 },
    { 'name': "BoJack Horseman: S01E06", 'num': 106 },
    { 'name': "BoJack Horseman: S01E07", 'num': 107 },
    { 'name': "BoJack Horseman: S01E08", 'num': 108 },
    { 'name': "BoJack Horseman: S01E09", 'num': 109 },
    { 'name': "BoJack Horseman: S01E10", 'num': 110 },
    { 'name': "BoJack Horseman: S01E11", 'num': 111 },
    { 'name': "BoJack Horseman: S01E12", 'num': 112 },
    { 'name': "BoJack Horseman: S02E01", 'num': 201 },
    { 'name': "BoJack Horseman: S02E02", 'num': 202 },
    { 'name': "BoJack Horseman: S02E03", 'num': 203 },
    { 'name': "BoJack Horseman: S02E04", 'num': 204 },
    { 'name': "BoJack Horseman: S02E05", 'num': 205 },
    { 'name': "BoJack Horseman: S02E06", 'num': 206 },
    { 'name': "BoJack Horseman: S02E07", 'num': 207 },
    { 'name': "BoJack Horseman: S02E08", 'num': 208 },
    { 'name': "BoJack Horseman: S02E09", 'num': 209 },
    { 'name': "BoJack Horseman: S02E10", 'num': 210 },
    { 'name': "BoJack Horseman: S02E11", 'num': 211 },
    { 'name': "BoJack Horseman: S02E12", 'num': 212 },
    { 'name': "BoJack Horseman: S03E01", 'num': 301 },
    { 'name': "BoJack Horseman: S03E02", 'num': 302 },
    { 'name': "BoJack Horseman: S03E03", 'num': 303 },
    { 'name': "BoJack Horseman: S03E04", 'num': 304 },
    { 'name': "BoJack Horseman: S03E05", 'num': 305 },
    { 'name': "BoJack Horseman: S03E06", 'num': 306 },
    { 'name': "BoJack Horseman: S03E07", 'num': 307 },
    { 'name': "BoJack Horseman: S03E08", 'num': 308 },
    { 'name': "BoJack Horseman: S03E09", 'num': 309 },
    { 'name': "BoJack Horseman: S03E10", 'num': 310 },
    { 'name': "BoJack Horseman: S03E11", 'num': 311 },
    { 'name': "BoJack Horseman: S03E12", 'num': 312 },
    { 'name': "BoJack Horseman: S04E01", 'num': 401 },
    { 'name': "BoJack Horseman: S04E02", 'num': 402 },
    { 'name': "BoJack Horseman: S04E03", 'num': 403 },
    { 'name': "BoJack Horseman: S04E04", 'num': 404 },
    { 'name': "BoJack Horseman: S04E05", 'num': 405 },
    { 'name': "BoJack Horseman: S04E06", 'num': 406 },
    { 'name': "BoJack Horseman: S04E07", 'num': 407 },
    { 'name': "BoJack Horseman: S04E08", 'num': 408 },
    { 'name': "BoJack Horseman: S04E09", 'num': 409 },
    { 'name': "BoJack Horseman: S04E10", 'num': 410 },
    { 'name': "BoJack Horseman: S04E11", 'num': 411 },
    { 'name': "BoJack Horseman: S04E12", 'num': 412 }    
]

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

source = 0
index = 0
subtitle = ""

def menu(title, choices):
	body = [urwid.Text(title), urwid.Divider()]
	for c in choices:
		button = urwid.Button(c['name'])
		urwid.connect_signal(button, 'click', item_chosen, c)
		body.append(urwid.AttrMap(button, None, focus_map='reversed'))
	return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, choice):
	global source
	response = urwid.Text([u'You chose ', choice['name'], u'\n'])
	source = choice['num']
	done = urwid.Button(u'Ok')
	urwid.connect_signal(done, 'click', search)
	main.original_widget = urwid.Filler(urwid.Pile([response,
		urwid.AttrMap(done, None, focus_map='reversed')]))

def search(button):
	edit = urwid.Edit("Search quotes: ")
	done = urwid.Button(u'Search')
	urwid.connect_signal(done, 'click', find_quotes, edit)
	exit_button = urwid.Button(u'Exit')
	urwid.connect_signal(exit_button, 'click', exit)
	main.original_widget = urwid.Filler(urwid.Pile([edit,
		urwid.AttrMap(done, None, focus_map='reversed'),
		urwid.AttrMap(exit_button, None, focus_map='reversed')]))

def find_quotes(button, edit):
	subs = pysrt.open(sub_files[source])
	search_text = edit.edit_text.lower()

	def seek(item, quote):
		for i in item.split(' '):
			if not i in quote:
				return False
		return True
	matching = [s for s in subs if seek(search_text, s.text.lower())]

	body_text = "Select quote" if len(matching) > 0 else "No quotes found"
	body = [urwid.Text(body_text), urwid.Divider()]
	for m in matching:
		button = urwid.Button(m.text)
		urwid.connect_signal(button, 'click', add_custom_subtitle, subs.index(m))
		body.append(urwid.AttrMap(button, None, focus_map='reversed'))

	back_button = urwid.Button('Go back')
	urwid.connect_signal(back_button, 'click', search)
	body.append(urwid.AttrMap(back_button, None, focus_map='reversed'))
	main.original_widget = urwid.ListBox(urwid.SimpleFocusListWalker(body))

def add_custom_subtitle(button, i):
	global index
	index = i
	body = [urwid.Text("Add a custom quote?"), urwid.Divider()]
	yes_button = urwid.Button("Yes")
	urwid.connect_signal(yes_button, 'click', enter_custom_subtitle)
	body.append(urwid.AttrMap(yes_button, None, focus_map='reversed'))
	no_button = urwid.Button("No")
	urwid.connect_signal(no_button, 'click', generate_gif)
	body.append(urwid.AttrMap(no_button, None, focus_map='reversed'))
	main.original_widget = urwid.ListBox(urwid.SimpleFocusListWalker(body))

def enter_custom_subtitle(button):
	subtitle = urwid.Edit("Enter custom subtitle: ")
	done = urwid.Button(u'Submit')
	urwid.connect_signal(done, 'click', generate_gif_with_subtitle, subtitle)
	main.original_widget = urwid.Filler(urwid.Pile([subtitle,
		urwid.AttrMap(done, None, focus_map='reversed')]))

def generate_gif(button):
	raise urwid.ExitMainLoop()

def generate_gif_with_subtitle(button, edit):
	global subtitle
	subtitle = edit.edit_text
	raise urwid.ExitMainLoop()

def exit(button):
	index = None
	raise urwid.ExitMainLoop()

main = urwid.Padding(menu(u'Movie choice', choices), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
	align='center', width=('relative', 60),
	valign='middle', height=('relative', 60),
	min_width=20, min_height=9)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
if index:
	makeGif(source, index, custom_subtitle=subtitle)
