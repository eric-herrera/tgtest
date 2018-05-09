#!/usr/bin/env python

import yaml
from telethon import TelegramClient, utils
from telethon.tl import types


api_id   = 196831
api_hash = '2a65e2e8784e5255f245431e82b05444'


client = TelegramClient('tg', api_id, api_hash)

if not client.connect():
	print("Telegram not connected")
	sys.exit(1)

client.start()

myself = client.get_me()
print("Connected as",utils.get_display_name(myself))
print()


rows = []
print("My channels..")
for dialog in sorted(client.get_dialogs(), key=lambda x: utils.get_display_name(x.entity)):
	if (type(dialog.entity) in (types.Chat, types.Channel)):
		username = dialog.entity.username if hasattr(dialog.entity, 'username') else ''

		print("%-10s : %-50s %s" % (
			dialog.entity.id, 
			utils.get_display_name(dialog.entity) + ' @'+str(username),
			dialog.entity.__class__
		))
		
print()

peer_id = 98097940 # Eric
channel = client.get_entity(peer_id)

print("Last 3 messages in ", utils.get_display_name(channel))
for message in client.iter_messages(channel, limit=3):
	print("[" + str(message.id) + ": " + str(message.date) + "]")
	print(message.message)
