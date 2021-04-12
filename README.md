# SetupSwitcher
Efficiency when switching between work and play.


# Dependencies
* Python 3
  * Spotipy
 
## Setup:
Run ControlMyMonitor.exe. For each monitor, press ctrl+m to copy the details, and then paste somewhere else. Use whatever uniquely identifies, I use "Name" because I have no identical monitors.
Replace the value after `/SetValue` in switch.bat with the monitor names. Figure out what value for `Input Select` switches to the correct input, and replace the value at the end of
the line with that. Repeat for all monitors. 

## Recommended
[USB Safely Remove](https://safelyremove.com/index.htm) to automate fully


ControlMyMonitor from [NirSoft](https://www.nirsoft.net/utils/control_my_monitor.html), I hope they don't mind me rehosting here


## Todo
* Remove dependency of ControlMyMonitor
* Figure out USB hooks on windows to remove USB Safely Remove tool dependency
* Setup scripts
* host on pip
