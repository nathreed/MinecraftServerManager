#!/bin/bash
#for mac compatibility, change \r to \015 (for some reason)


#Start MinecraftServer
screen -dmS MinecraftServer
screen -p 0 -S MinecraftServer -X eval 'stuff "java -Xmx3G -jar minecraft_server*.jar"\015'

#Start GamemodeChanger
touch gamemode.log
screen -dmS GamemodeChanger
screen -p 0 -S GamemodeChanger -X eval 'stuff "sleep 15 && python gamemode.py"\015'

#Start StopWatcher
screen -dmS StopWatcher
screen -p 0 -S StopWatcher -X eval 'stuff "sleep 15 && python stopwatcher.py"\015'
