***************************************************************************************************************
ABOUT THE APPLICATION:
***************************************************************************************************************

This web application has two parts.

In the first part ("Generate Strings" menu item in the top navigation bar) you can generate a set
of strings of random lengths using characters randomly selected from a set of characters (i.e. Alphabet)
that you speficy. If you do not specify an Alphabet, then default will be the set of 26 English lowercase
characters. In addition to specifying the Alphabet, you can also specify the number of strings to be generated
and the maxmimum lenght of those strings. When you click "Generate" button, the "Generate Strings" functionality
is executed. The generated strings are stored in a database, along with their corresponding
string_id values, which are sequentially assigned as the strings are generated. Every time you run the "Generate
Strings" functionality, the previously stored strings are deleted from the database, and the new ones are entered.

In the second part ("Match Strings" menu item in the top navigation bar), you can select two strings by specifying
their string IDs. When you submit the form by clicking "Match" button, the program compares thetwo strings, and returns
two numbers: 

n1 : number of letters in one string that each match in value and in position to a letter in the other string.
n2 : number of letters in one string that each match in value, but not in position to a letter in the other string.

The algorithm corfoms with the following conditions:

1)The output should be the same if the two strings were swapped.
2)Each letter instance in a string may only participate in one match.
3)If a letter instance can participate in either n1 or n2, it is to be counted towards n1.
4)The two strings may or may not be of the same length.

***************************************************************************************************************
ASSUMPTIONS / REQUIREMENTS
***************************************************************************************************************

(1) This application is written in Python 3.5.1 (Anaconda 4.0.0 x86_64). It uses Flask web framework, and Flask
Bootstrap extension. The file "requirements.txt" that is included is an output for executing command 

  pip freeze

which gives all the packages in the environment with their version numbers (of course not all of them are actually
used in the application).

(2) The random strings generated are stored in local copy of MongoDB (v3.2.9), so it is assumed that there is a local
instance of MongoDB running on the server where you want to run the application. Application uses "pymongo"
package to connect and communicate with MongoDB. Further it is assumed that MongoDB is running with all its default 
settings (e.g. listening on port 27017), so that application can connect to it with

client = MongoClient()

If the settings are non-default, then the application will need to be modified to use the full URL for connecting
(e.g. 'mongodb://<servername>:<port>/').

(3) If the above requirements are satisfied, one can copy the whole "webapp" directory, i.e. the directory in which
this file is included, to a suitable location (e.g. zip and unzip), and then execute

  python  app.py

This starts an HTTP server listening on port 5000 (default value, that can be changed from withing app.py), and the
application can then be accessed using URL:

http://localhost:5000



