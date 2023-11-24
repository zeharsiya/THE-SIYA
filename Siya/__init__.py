from Siya.core.bot import Siya
from Siya.core.dir import dirr
from Siya.core.git import git
from Siya.core.userbot import Userbot
from Siya.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Siya()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
