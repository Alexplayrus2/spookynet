# ***spookynet***
## how does this work?
```it syncs 2 .ini files through a python flask server, p1data gets sent to the server and p2data gets edited to whats gotten from the server, p1data is set by the game and p2data is read by it, currently only supports 2 players```
## how do i build this?
### make sure you have python 3 installed for this, also make sure to edit the executable name in the code (commented where) so it doesnt error if you wanna rename the executable
### this is intended to be built for windows
```
cd src
pip install pyinstaller
build
```
### executable should be located at /src/build/dist/spookynet.exe

## what to report via issues

```
problems with spookynet
problems with hosting the webserver
```

## what not to report via issues
```
vulnerubilities (github has another feature for that)
problems with the mod itself (e.g. an ingame error message pops up)
problems with the official game server (https://alexplayrus1.pythonanywhere.com/multiplayer/)
```
## if you are using the mod and not sure which one your problem falls under just report to gamebanana comments, report it there if it falls under what not to report via issues as well (other than vulnerubilities, thats in the security tab)
## please include an error log if possible (run the .exe in a command line and try to reproduce what causes the error to see)
