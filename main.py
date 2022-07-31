import KeywordsTexts
import json
import UserDetails

"""
    user_list = [
            {handle: , api_id: , api_hash: , phone: }
            ]
"""

if __name__ == '__main__':
    user_list = []

    # get start command
    print(KeywordsTexts.WELCOME_TEXT)
    start_command = input(KeywordsTexts.START_INSTRUCTION)

    # get user-list from json file
    try:
        user_file = open(KeywordsTexts.USER_FILE, "r")
        user_list = json.load(user_file)
        user_file.close()
    except FileNotFoundError:
        user_list = []

    # apply start-command
    if start_command == KeywordsTexts.NEW_USER:
        handle = input('Insert handle of new user without @: ')
        UserDetails.new_user(user_list, handle)
    elif start_command == KeywordsTexts.EXIT:
        print(KeywordsTexts.EXIT_MESSAGE)
        exit()
    else:
        UserDetails.create_client(user_list, start_command)
