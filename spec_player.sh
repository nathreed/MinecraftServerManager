#!/bin/bash
SPEC_STRING="/gamemode 3 $2"
UNSPEC_STRING="/gamemode 0 $2"
if [ $1 = "spec" ]; then
        screen -p 0 -S MinecraftServer -X eval 'stuff "'"${SPEC_STRING}"'"\r'
        
else if [ $1 = "unspec" ]; then
        screen -p 0 -S MinecraftServer -X eval 'stuff "'"${UNSPEC_STRING}"'"\r'
        
fi
fi
