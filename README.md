# SPAM-SMS-OTP
Spam SMS OTP of some brands

# Installation
```
$ pip install requests
$ pip install phonenumbers
```

# Generate exe file
Use `pyinstaller` for build file exe

### Debug
```
pyinstaller main.py --onefile --windowed --debug=all
```

### Release
Before generate released file exe, need to comment code `file_handler` at file `log_base.py` to not write `log.txt`
```
file_handler....
```
Build
```
# Gui console
pyinstaller gui_console/main.py --onefile

# Gui window
pyinstaller gui_tkinter/main.py --onefile --windowed
```