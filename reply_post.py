# Imports
import praw
import IDandSecret
import pdb
import re
import os

# Import and name all personal/confidential info
identity = IDandSecret.ClientID
secretpass = IDandSecret.ClientSecret
botpassword = IDandSecret.MyPass

# Create the Reddit instance
reddit = praw.Reddit(user_agent='CanadaKnifeBot (by /u/UNLUCK3', client_id=identity, client_secret=secretpass,
                     username='CanadaKnifeBot', password=botpassword)