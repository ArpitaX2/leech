import os

API_ID = API_ID = 9741228

API_HASH = os.environ.get("API_HASH", "6f339e8fa827a5147fa2ff03898d610c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6945617327:AAG835T-JGGHUR0HCPs_pshSuU5trtdk6rM")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6523256745))

LOG = -1002122751557

try:
  GROUPS =[]
  for x in (os.environ.get('GROUPS', '-1002157339436').split()):
    GROUPS.append(int(x))
except ValueError:
    raise Exception("Your AUTH GROUPS list does not contain valid integers.")    

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "809150135 6169271833").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


