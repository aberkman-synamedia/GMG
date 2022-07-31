# GMG
Group Members Grabber

This program is designed to retreive all the members of a selected Telegram group and all the messages and store them in two CSV files respectively.  This only works when the settings of the selected group allow such actions.

Please install 'telethon (pip install telethon) before using the program.

When running the progra for the first time, you be prompted to connect it to a Telegram user.  You can connect it to multiple users.  In order to make the connection, visit 'https://my.telegram.org' and click on 'API development tools' and fill out the boxes to create an application.  After clicking 'ok', you will be provided with an api_id and api_hash.

Upon starting the GMG program you be prompted to insert the name of your user or to insert a new-user.  When entering a new user, you will be prompted to provide the api_id, api_hash and phone number of your user.  Your user will receive and access code that you will provide to GMG.

GMG will provide you with a list of all the groups your user is in and you can select what group you want to run.  After selecting the group, if the privacy settings allow it, GMG will create two CSV files, one with the users of the group including their user_id, username, full name and phone number (if not set to private).  The second CSV file will contain the messages from the group.
