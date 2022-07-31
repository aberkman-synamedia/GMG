import GMG
from telethon.sync import TelegramClient
import json

import KeywordsTexts

"""
    user_list = [
            {handle: , api_id: , api_hash, phone: }
            ]
"""


def create_client(user_list, handle):
    phone = ''
    found = False

    # find handle in user-list
    for user in user_list:
        if user['handle'] == handle:
            found = True
            phone = user['phone']
            try:
                client = TelegramClient(user['phone'], int(user['api_id']), user['api_hash'])
            except ValueError as e:
                exit(e)
            break
    if not found:
        command = input(KeywordsTexts.NO_USR)
        if command == KeywordsTexts.YES:
            new_user(user_list, handle)
        else:
            print(KeywordsTexts.EXIT_MESSAGE)
            exit()

    # client connect
    try:
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            client.sign_in(phone, input('Enter the code: '))
    except:
        exit('UnkownError, could not connect to client')

    # send to GMG methods
    GMG.scrape_group(client)


def new_user(user_list, handle):
    action_command = ''

    # check if handle already exists in user-list
    for user in user_list:
        if handle == user['handle']:
            action_command = input(KeywordsTexts.USER_EXISTS)

            # find correct action
            if action_command == KeywordsTexts.NEW_USER:
                handle = input('Insert handle of new user without @: ')
                new_user(user_list, handle)
            elif action_command == KeywordsTexts.REPLACE:
                user_list.remove(user)
                new_user(user_list, handle)
            elif action_command == KeywordsTexts.EXIT:
                print(KeywordsTexts.EXIT_MESSAGE)
                exit()
            else:
                handle = action_command
                create_client(user_list, handle)
            break

    # get necessary connection data
    print(KeywordsTexts.LOGIN_INSTRUCTIONS)
    api_id = input('Insert API ID: ')
    api_hash = input('Insert API Hash: ')
    phone = input('Insert phone number: ')
    user = [{'handle': handle, 'api_id': api_id, 'api_hash': api_hash, 'phone': phone}]
    user_list += user

    # update user-list in json file and create client
    with open(KeywordsTexts.USER_FILE, "w") as f:
        json.dump(user_list, f)
    create_client(user_list, handle)
