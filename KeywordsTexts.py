# keywords
NEW_USER = 'new_user'
USER_FILE = 'users.json'
EXIT = 'exit'
EXIT_MESSAGE = 'Goodbye'
REPLACE = 'replace'
YES = 'y'
MAX_MSG = 1000

# texts to print
WELCOME_TEXT = """
    Welcome to the 'Group Member Grabber'.
    Follow the instructions to get the members of a group,
    their previous handles and group message history.
    Note that this will not work if the groups privacy settings forbid it.
    """
START_INSTRUCTION = f"""
    To begin, enter the handle of your Telegram user in the group you want to check,
    or write '{NEW_USER}' to store a new user,
    To exit, write {EXIT}:  
    """
USER_EXISTS = f"""
    This user already exists in your user-list.
    If you would like to use this handle or another handle,
    write the handle of the user you wish to use.
    If you would like to replace this user, write {REPLACE}
    If you would like to add a new user, write '{NEW_USER}'.
    To exit, write {EXIT}:
    """
LOGIN_INSTRUCTIONS = """
    Login to https://my.telegram.org to get necessary data
    to connect to Telegram client.    
    """
NO_USR = """
    The handle you entered was not found in your database.
    Would you like to insert this user now (y/n)?
    """
