
# 'Feierabend' will play a random sound - based on weekday and season - and shuts down your computer
# Copyright (C) 2023  Matthias Frenck

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import random
from datetime import datetime

#sound directory
dir_sound = 'sounds' + '\\'

########################################################################

def getMonth():
    #gets current month
    month = datetime.today().strftime('%m')
    return month
    
def getWeekday():
    #gets current weekday
    weekday = datetime.today().strftime('%A')
    return weekday

def getSeason(month):
    #finds out wether or not it's a (special) season based on given month
    season = 'none'
    if (month == '12' or month == '01'):
        season = 'winter'
    elif (month > '05' and month < '09'):
        season = 'summer'
    return season

def pickFolder(season, weekday):
    #picks between season, special weekday or standard sound folder based on given season and weekday, 
    options = []
    options.append('standard')
    if (season != 'none' and len(os.listdir(dir_sound + season)) != 0):
        options.append(season)
    if (weekday == 'Friday' and len(os.listdir(dir_sound + weekday)) != 0):
        options.append(weekday)
    folder = random.choice(options)
    return folder
    #note: there is no catch for an empty standard folder yet. That case should
    #propably result in an error message, since the App should have been deployed with at least some standard sounds imo.
  
def getSounds(folder):
    #gets list of sound files from given folder
    ##TODO: catch wrong fileformats
    sounds = os.listdir(dir_sound + folder)
    return sounds
    
def pickSound(sounds):
    #picks one random file from given list of sounds, returns filename
    pick = random.randrange(0, len(sounds))
    sound = sounds[pick]
    return sound
    
def getSoundpath(root, folder, sound):
    #returns filepath of choosen sound
    path = os.getcwd() + "\\" + root + folder + "\\" # \ is escaping char. escape this special function with an extra \
    soundpath = path + sound
    return soundpath

def playSound(filepath):
    #plays sound with vlc player and close it after playing
    rvalue = os.system('start vlc.exe --play-and-exit ' + '"' + filepath + '"')
    #if vlc is not installed or is not working try windows media player (will not close wmplayer after playing)
    if (rvalue != 0):
        rvalue = os.system('start wmplayer ' + '"' + filepath + '"')
    return rvalue

def shutdown():
    #shuts down systems with 10sec delay and displays message
    os.system('shutdown /s /t 10 /c "Schönen Feierabend!"')


########## main ##########
def main():

    month = getMonth()
    print('It is month ' + month) #debug

    weekday = getWeekday()
    print('It is a ' + weekday) #debug

    season = getSeason(month)
    print('That means it is ' + season) #debug

    folder = pickFolder(season, weekday)
    print('Folder ' + folder + ' was choosen') #debug

    sounds = getSounds(folder)
    print('available sounds:\n') #debug
    print('sounds') #debug

    sound = pickSound(sounds)
    print('sound ' + sound + ' was choosen') #debug

    soundpath = getSoundpath(dir_sound, folder, sound)
    print('filepath: ' + soundpath) #debug

    #play sound
    returnvalue = playSound(soundpath)
    print(returnvalue)#debug

    #system shutdown
    shutdown()


if __name__ == "__main__":
    main()

 



