from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("8066514303:AAHaQOjQYGa-lPCDJ0hLl-assumizp80U9E", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("7775259302"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("BQGlNysAkOQdMB3BJCmjA_kFhkQG3aJCIyovWpXK4s3qcrLuC6U0NyZsFnE5RldbhNyP3txhY0-WqfzUZ1aPoMjhS18jYHTdI3ihQ78wn31q8gE6lwXl6yCYzTQphpFiU998Jbt-bNLxJiYgJvpUdbaiboDV7mnap2P8ciQ_pvIIEc2QpuVy0iVd7NZTp6ofUr2uvorJc41qoQZFo9-BFeeZbXXRS7lQPIefmGxWCSzCewNcJzfpG3-HhJTSGfhrQVrpEYOsS7zcuLI2Hcp_ys6TJpQlJTh1CTH9dqmK5RODWMT8IbwQaNnO-q7lyWsG5cA5-ParRSan8qKMjcemAcUKSVT2lAAAAAG2bCpvAA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/land_of_hunters")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/land_of_hunters")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
