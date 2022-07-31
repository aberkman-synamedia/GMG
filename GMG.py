from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv

import KeywordsTexts


def scrape_group(client):
    chats = []
    last_date = None
    chunk_size = 200
    groups = []
    message_id = []
    message = []
    sender = []
    reply_to = []
    time = []

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))

    # import chats from client
    chats.extend(result.chats)
    for chat in chats:
        try:
            groups.append(chat)
        except:
            continue

    # choose a group to scrape
    print('Choose a group to scrape members from:')
    i = 0
    for g in groups:
        print(str(i) + '- ' + g.title)
        i += 1

    g_index = input("Enter a Number: ")
    target_group = groups[int(g_index)]

    # get members from group
    print('Attempting to fetch members...')
    try:
        all_participants = []
        all_participants = client.get_participants(target_group, aggressive=False)
    except:
        exit('UnkownError, could not retreive users, admin priviliges may be necissarry')

    # get messages
    chats = client.get_messages(target_group, KeywordsTexts.MAX_MSG)

    # write to files
    print('Saving In file...')

    # users file
    with open(f"{target_group.title}_users.csv", "w", encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        writer.writerow(['group', target_group.title])
        writer.writerow(['group id:', target_group.id])
        writer.writerow(['username', 'user id', 'access hash', 'name', 'phone'])
        for user in all_participants:
            username = ''
            first_name = ''
            last_name = ''
            phone = ''
            if user.username:
                username = user.username
            if user.first_name:
                first_name = user.first_name
            if user.last_name:
                last_name = user.last_name
            if user.phone:
                phone = user.phone
            name = (first_name + ' ' + last_name).strip()
            writer.writerow([username, user.id, user.access_hash, name, user.phone])

    # messages file
    with open(f"{target_group.title}_messages.csv", "w", encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        writer.writerow(['group', target_group.title])
        writer.writerow(['group id:', target_group.id])
        writer.writerow(['message id', 'message', 'sender', 'reply to message id', 'time'])
        for chat in chats:
            message_id = ''
            message = ''
            sender = ''
            reply = ''
            time = ''
            if chat.id:
                message_id = chat.id
            if chat.message:
                message = chat.message
            if chat.from_id:
                sender = chat.from_id
            if chat.reply_to_msg_id:
                reply = chat.reply_to_msg_id
            if chat.date:
                time = chat.date
            writer.writerow([message_id, message, sender, reply, time])
    print('Members scraped successfully.')
