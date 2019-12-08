## Text-based game
School project in Python 3.4 &amp; mySQL

To play 'theverge.py' you will need to install the following:

## PREQUISITES
### Python 3  
https://www.python.org/downloads/release/python-344/

Get the version for your operating system.

### mySQL Python connector
https://dev.mysql.com/downloads/connector/python/

Get the version for your operating system and follow the instructions to install it.

### mySQL 
https://mariadb.org/download/

After installing all of the above head to the next section.

### Getting the game to work

#### Creating the database 
In Windows, launch the command prompt.
In Linux or macOS launch the terminal.

In the game directory (game folder) type the command ```mysql -u root -p < superduperscript.sql```
to build the database from the script.

In Windows, navigate to where mariaDB is installed (usually C:\Program Files\MariaDB 10.2\bin) and run the above command
and/or copy the script to the directory where mySQL is located.

In macOS and unix* the above command should work in the game directory.

#### LAUNCHING THE GAME 
In the game directory , launch theverge.py by double-clicking it or
launching it from Python 3's IDLE.

In Linux/macOS you might have to specify the correct version of python:
```$ python3 theverge.py``` 
