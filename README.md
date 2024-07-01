This is a tool to collect all the info in a google sheets by using google API (which is names and linkedin urls) and use selenium to auto connect or accept (if the invitaion has been already been sent) to all of them.
The API usage is based on https://developers.google.com/sheets/api/quickstart/js, follow the instruction and download the Credentials.josn 

Get all the requirements from the requirements.txt 

Put the Credentials.josn under the file 

In connect.py:
change line 12 to the google sheets ID
change line 13 to the range of the data in the sheet 
change line 15 ID to your linkedin login ID 
change line 16 PASSWORD to your linkedin login password

run python connect.py
