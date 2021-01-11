


<h1 align="center"><b> DARK COBRA USERBOT REMIX 🇱🇰  </b></h1>
<h4 align="center">A Powerful, Smart And Simple Userbot with 300+ Plugins <br> ... The Dark Cobra Userbot Remix ...</h4>

<p align="center">
    <a href="https://github.com/ImJanindu/DarkCobraUserBot/commits/master"><img src="https://img.shields.io/github/last-commit/ImJanindu/DarkCobraUserBot/master?label=Last%20Commit&style=flat-square&logo=github&color=F10070" alt="Commit" /></a>
    <a href="https://github.com/ImJanindu/DarkCobraUserBot/stargazers"><img src="https://img.shields.io/github/stars/ImJanindu/DarkCobraUserBot?label=Stars&style=flat-square&logo=github&color=F10070" alt="Stars" /></a>
    <a href="https://github.com/ImJanindu/DarkCobraUserBot/network/members"><img src="https://img.shields.io/github/forks/ImJanindu/DarkCobraUserBot?label=Fork&style=flat-square&logo=github&color=F10070" alt="Fork" /></a>
</p>

<p align="center"><a href="https://t.me/Infinity_Bots"><img src="https://telegra.ph/file/3c577341c45ea55a790b5.jpg" width="400"></a></p> 


### Here is the Telegram Dark Cobra Remix Userbot. A Remix Of Dark Cobra Userbot on github. Credits To Their Owners.

# 😍 Credits
### Cloned from [Dark Cobra Userbot](github.com/dark-cobra/dakcobra). Full credits to Friday Developers. 
#### Special thanks to Dark Cobra developers a lot

``` Full credits mentioned at the bottom```
# 
# ❤️ Support

<a href="https://t.me/Infinity_Bots"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram"></a>

<a href="https://t.me/infinityje"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a>

### Please Star this repo If you are deploying this Userbot.

<p align="left">
  
  <a href="https://github.com/inukaasith/virtualuserbot">
    <img src="https://img.shields.io/github/stars/ImJanindu/DarkCobraUserBot?style=social">
  </a>
</p>


# 🕵️‍♀️ Before You Go 



## 1)   AppID and API HASH

Get APP ID and API HASH from [HERE](https://my.telegram.org) and BOT TOKEN from [Bot Father](https://t.me/botfather) and then Turn on Inline mode for the bot

## 2)   String Session (Need before deploying)
This is the way thar your userbot connects with you. Need an AppID ApiHash and a username to go..

[![Run on Repl.it](https://repl.it/badge/github/STARKGANG/friday)](https://repl.it/@Danish00/DarkCobra#main.py)



## 3)   Heroku API

Create a account on [Heroku](dashboad.heroku.com) first. Then goto settings scroll to bottom. Reaveal API and get api

## 4)   Plugin Channel and Private Group ID

Create a private group on Telegram.
Add [MissRoseBot](t.me/missrosebot) to you group and give Admin permissions.
Turn Chat history for members in Manage group
send ```/id``` and get the group's ID

## 5)  Bot Language  (English)

#### Currently Available Languages are
- English (en)


# 



# 🏃‍♂️ Deploying To Heroku

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ImJanindu/DarkCobraUserBot)

``` Always try to  Deploy this source. If not you will miss the future updates```

# 
 


## How to Deploy guide by Friday

<a href="https://youtu.be/xfHcm_e92eQ"><img src="https://img.shields.io/badge/How%20To-Deploy-red.svg?logo=Youtube"></a>

``` The Method is also same for this. Just deploy bot from this repo ```


# 
 

#  🤴 After Deploying Steps

## 1) Turn Heroku Dynos ON
Dynos are used on heroku. On free accounts You will get 600 free dyno hours. When you link your CC you will get aditional 400 dyno for free.

Ater Building app is completed.. Goto [Heroku](dashboad.heroku.com), Select your app and goto *Resources Tab*.
Then turn  * worker bash start.sh * to ON

## 2) Check you logs
Chack Heroku logs then.. If you done any mistakes they will shown there.

## 3) Goto telegram and check your Superpowers
Goto telegram and send .help to see the help of your Userbot

#


# 🦹‍♀️ What is the message sending to users who message you

### Virtual Userbot has a PM Protection service ( It was just copied from Friday Project)

Send ```.ap``` to approove users to PM you 
and, ```.dap``` to disapproove 

If you Dont like this send ```.set var PM_DATA DISABLE```


# 
<details>
<summary>👉 MORE INFO HERE 👈</summary>

# String Session (Hard Way)

## [Using the Bot](https://t.me/stringsessionbot) (Not Recommended)
[![Use Our Bot](https://img.shields.io/badge/StringSessionGenerator-Use%20Bot-brightgreen)](https://t.me/stringsessionbot)
Simply clone the repository and run the main file:
```sh
# Install Git First.
git clone https://github.com/ImJanindu/DarkCobraUserBot
# Open Git Cloned File
cd Userbot
# Config Virtual Env
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
# Install All Requirements 
pip install -r requirements.txt
# Create local_config.py with variables as given below
# Start Bot
python3 -m userbot
```

## An example local_config.py file could be:
```
Not All of the variables are mandatory
The Userbot should work by setting only the first two variables
from heroku_config import Var

class Development(Var):
APP_ID = 6543
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"

```
## Mandatory Vars
```
[+] Only two of the environment variables are mandatory.

[+] This is because of telethon.errors.rpc_error_list.ApiIdPublishedFloodError

    [-] APP_ID:   You can get this value from https://my.telegram.org
    [-] API_HASH :   You can get this value from https://my.telegram.org
    
[+] The Userbot will not work without setting the mandatory vars.
```

# Licence
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

VirtualUserbot is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 
</details>

# 
 
# 
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/ImJanindu/DarkCobraUserBot/graphs/commit-activity)

# Full Credits

- Dark Cobra ❤️

Most of the Plugins Taken from this Project.. Made possible by this. Full Credits. Full Respect

- Uniborg

Userbots Made possible. Respect.

# 🧐 Disclaimer 

### Use at your Own Risk 😇
Virtualuserbot don't have any torrent leeching plugins.. So risk of bans in TG is low
But somehow if you get banned or anything happened WE ARE NOT RESPONSIBLE FOR THEM

### Report Errors only to virtualuserbot developers

There are various plugins in virtualuserbot owned by Friday and other userbots.. 
All the plugins are reconfigured for for virtualuserbot. So if you have any errors please report only to the virtualuserbot developers

### If you are using adult content in the bot or if you harm someone with fun plugins of the bot you might get banned from Telegram. We are not responsible for that 😅

## ❤️ Made possible by [Dark Cobra Project](https://github.com/DARK-COBRA) and many other opensource projects ❤️

### 😍 Project by [Infinity Bots](https://t.me/Infinity_Bots)
