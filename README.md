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
