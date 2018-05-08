To Play 'theverge.py' you will need to install the following:

[PREQUISITES]
# Python 3  
https://www.python.org/downloads/release/python-344/

Get the version for your operating system.

# mySQL Python connector
https://dev.mysql.com/downloads/connector/python/

Get the version for your operating system and follow the instructions to install it.

# mySQL 
https://mariadb.org/download/

After installing all of the above head to the next section.

[ASSEMBLY]
### GETTING THE GAME TO WORK ###

# CREATING THE DATABASE 
In Windows, launch the command prompt.
In Linux or macOS launch the terminal.

In the game directory(game folder) type the command 'mysql -u root -p < superduperscript.sql' to build the database 
from the script.

In Windows, navigate to where mariaDB is installed (usually C:\Program Files\MariaDB 10.2\bin) and run the above command AND/OR copy the script to the directory where mySQL is located.

In macOS and unix* the above command should work in the game directory.

# LAUNCHING THE GAME #
In the game directory , launch theverge.py by double-clicking it OR launching it from Python 3's IDLE.

In linux you might have to specify the correct version of python:
$:/ python3 theverge.py 
 
 
 
[CONTACT]
For further questions or comments please send an email to ' Oliver.Anderson@metropolia.fi '


