This application (main.py) is written in Python 3 for use with a MySQL database server. 
The database schema (create_music_stats.sql) is a simple MySQL workbench script used to create the tables and other objects for the database. 
The dump (dump\music_stats_dump) of the database should be able to be used as well to recreate it.

Since the client code is all contained in a single file, the directories of the files shouldn't be a problem. However, it's recommended to keep all files in the same folder after extracting the .zip.

Python 3 Libraries Used:
os - should be able to be imported with Python 3 without any external downloads
tkinter - used in the creation of the GUI; should be able to be imported with Python 3 without any external downloads. 
pymysql - used to interact with MySQL server and database via Python; needs to be installed using anaconda, pip, or another manager (Anaconda Navigator was the primary method used, but using the following should work too: $ python3 -m pip install PyMySQL)

Prior to running the application, the database will need to be created using either the dump or the create schema. All required, non-native libraries (pymysql) should be confirmed to be installed on the current Python environment. Then the application can be started by running the python script (main.py). Changes made to the database can be viewed either using the app or from an interface such as MySQL Workbench. 