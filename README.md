# Authentification-Python
**The "user-facing" commands**\
\
The following user-facing commands must be supported. Every command appears on a line by itself, and the output of every command should appear on a line by itself.\
\
CREATE username password :\
Create a new username/password combination and stores it in the program's collection. If successful, the output is CREATED. If the username is already stored in the collection, no change is made and the output is EXISTS. (One key consequence is that the same username cannot appear in the collection more than once.)\
\
LOGIN username password	:\
Checks a username/password combination to see if it is valid. A username/password combination is valid if it exists (i.e., the username is in the collection and is associated with the password), in which case the output is SUCCEEDED. If the username/password combination does not exist, the output is FAILED. (Note that there is no distinction between the username not existing and the password being incorrect; either situation would output FAILED. This is fairly standard — and wise — behavior for an authentication service; if you return different error messages when a username does not exist and when a password is wrong, you're letting an attacker know a useful piece of information: whether a username is valid.)\
\
REMOVE username :\
Removes the username/password combination with the given username, if it exists. If so, the output is REMOVED. If no username/password combination with the given username exists, the output is NONEXISTENT./
\
CLEAR :\
Removes all username/password combinations from the service. The output is CLEARED (even if there were no username/password combinations at the time).\
\
QUIT :\
The output of this command is GOODBYE. Once this command has been processed, the program should end.\
