#!/usr/bin/env python3
# A simple script to print 2 winner from arvancloud channel members

import os
import sys
import time
import random

from telethon import TelegramClient


def get_env(name, message, cast=str):
    if name in os.environ:
        return os.environ[name]
    while True:
        value = input(message)
        try:
            return cast(value)
        except ValueError as e:
            print(e, file=sys.stderr)
            time.sleep(1)

session = os.environ.get('TG_SESSION', 'winner')
api_id = get_env('TG_API_ID', 'Enter your API ID: ', int)
api_hash = get_env('TG_API_HASH', 'Enter your API hash: ')
channel = get_env('TG_CHANNEL_NAME', 'Enter your Channel Name: ')
proxy = None  




if __name__ == "__main__":

    client = TelegramClient(session, api_id, api_hash, proxy=proxy).start()

    # Get Channel Members
    Members = []
    for u in client.iter_participants(channel, aggressive=True):
        Members.append([u.id, u.first_name, u.last_name, u.username])

    # Who is Winner?
    print("ArvanCloud Members Count: ",len(Members))
    print("First Winner: ", random.choice(Members))
    print("Second Winner: ", random.choice(Members))

    # Disconnect User
    client.disconnect()