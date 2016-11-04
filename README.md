# proj6-mongo
Simple list of dated memos kept in MongoDB database
Author: Jacob Dickinson
        jdickins@uoregon.edu

## What is here

A simple Flask app that displays all the dated memos it finds in a MongoDB database.
There is also a 'scaffolding' program, db_trial.py, for inserting a couple records into the database 
and printing them out.  Get db_trial.py working before you try making your flask app work. 

## What is not here

In addition to the missing functionality in the application, you will
need a MongoDB database, and you will need credentials (user name and
password) both for an administrative user and a regular user.  The
administrative user may be you, but the regular user is your
application. Make a subdirectory called "secrets" and place two files
in it: 

- secrets/admin_secrets.py holds configuration information for your MongoDB
  database, including the administrative password.  
= secrets/client_secrets.py holds configuration information for your
  application. 



