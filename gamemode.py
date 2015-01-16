#!/usr/bin/python
# coding: latin-1

import time
import subprocess

 
#config here
#the path to the server folder
serverFolderPath = "/path/to/the/folder/where/the/server/jar/is"
#the path to the spec_players script
specPlayersPath = serverFolderPath + "/spec_player.sh"

f = open(serverFolderPath + "/logs/latest.log", "r")

lineWeAreAt = 0
lineToStartAt = 0
timeStarted = time.strftime("[%H:%M:%S]")

def log(message):
        gamemodeLog = open(serverFolderPath + "/gamemode.log", "a")
        timeNow = time.strftime("[%Y-%m-%d %H:%M:%S] ")
        gamemodeLog.write(timeNow + message + "\n")
        #print timeNow + message
        gamemodeLog.close()

def sendCommand(typeOfCommand, target):
        if typeOfCommand == "spec":
                p = subprocess.Popen(["bash", specPlayersPath, "spec", target])
        elif typeOfCommand == "unspec":
                p = subprocess.Popen(["bash", specPlayersPath, "unspec", target])

#Seek to the end of the file so we arent spammed with all sorts of crap when we start (Seek to 0 relative to the end of the file (2))
f.seek(0, 2)
while True:
        line = f.readline()
        p1PasswordString = time.strftime("%M")
        p2PasswordString = time.strftime("%M")
        p3PasswordString = time.strftime("%M")
        if not line:
                time.sleep(1)
                
        else:
                line = line.lower()
                
                #This is where you need to add the player names
                if "gamemode 3 player1 " + p1PasswordString in line:
                        sendCommand("spec", "player1")
                        log("Set PLAYER1's gamemode to SPECTATOR")
                elif "gamemode 3 player2 " + p2PasswordString in line:
                        sendCommand("spec", "player2")
                        log("Set PLAYER2's gamemode to SPECTATOR")
                elif "gamemode 3 player3 " + p3PasswordString in line:
                        sendCommand("spec", "nickster2015")
                        log("Set PLAYER3's gamemode to SPECTATOR")

                elif "gamemode 0 player1" in line:
                        sendCommand("unspec", "player1")
                        log("Set PLAYER1's gamemode to SURVIVAL")
                elif "gamemode 0 player2" in line:
                        sendCommand("unspec", "player2")
                        log("Set PLAYER2's gamemode to SURVIVAL")
                elif "gamemode 0 player3" in line:
                        sendCommand("unspec", "player3")
                        log("Set PLAYER3's gamemode to SURVIVAL")

f.close()

