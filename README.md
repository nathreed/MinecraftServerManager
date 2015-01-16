# MinecraftServerManager
A set of python and shell scripts for controlling a minecraft server based on commands players enter in the chat. Version 1.0 supports up to 3 players. Support for infinite numbers of players is coming soon. Supports Linux and OS X.
##Setup
###Linux
1. Clone the repo and place a Minecraft server jar in the folder.
2. Install GNU screen if you don't already have it (on debian/ubuntu: ```sudo apt-get install screen```)
2. Open `gamemode.py` and change the variable ```serverFolderPath``` to the absolute path of the directory you are running the server in.
3. Change ```player1```, ```player2```, and ```player3``` variables inside the while loop. Change the password strings as well.
4. If you would like to give an amount of RAM other than 3GB to the Minecraft server, edit ```start.sh``` and change the memory allocation in the section marked "Start MinecraftServer".
5. Make start.sh executable and run it. A Minecraft Server gui should appear shortly. You can also access the server console by typing ```screen -r MinecraftServer```  

###OS X
1. Follow steps 1-5 (except #2) for Linux setup.
2. Edit ```start.sh``` and add a line: ``cd /path/to/your/server/directory`` (the server directory should be the same as the value you put for `serverFolderPath` in `gamemode.py`
3. Follow step 6 for Linux setup.  

##Command guide
You type these commands in the normal server chat. They will be visible to all players as it is not currently possible to remove messages from the server chat without a mod. Their response will also be visible to all players, although making a personalized feedback system with the `/msg` server command is planned. Note that you don't type these commands with a `/` in front of them. You just type them as normal messages in the chat.
###gamemode
These commands give the player the ability to place themselves in spectator mode and back into survival mode. This would be useful in a small to medium size server setting where players would like to see something underground but the server owner doesn't want to give them all the permissions of op.  

`gamemode 3 <player> <password>`: This command will put the specified player into spectator mode. The default password is the current minute. This is to prevent re-use over long periods of time with t-up-enter to get out of danger.  

`gamemode 0 <player>`: This command will put the specified player back in survival mode. There is no password necessary.  

More commands are planned for the future.
