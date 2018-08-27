# Imports
import praw
import IDandSecret
import time
import os

# If there is no file for keeping track of replied posts, and not replying to them again, create it
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:  # Open the file
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))

# Importing and naming secrets
identity = IDandSecret.DBClientID
secretpass = IDandSecret.DBClientSecret
botpassword = IDandSecret.DBMyPass
usernames = ['/u/UNLUCK3', '/u/DiscreetBot']

# The text the bot should be replying with. Currently only replies with the third part? IDK
reply_text = 'Hey ', usernames, 'This guy got a knife inside Canada somehow! Do you want it?     ^^I\'m ^^a ^^bot.    ' \
                                '  ^^PM ^^/u/UNLUCK3 ^^for ^^help, ^^or ^^to ^^add ^^yourself '

# Getting oAuth2 Access
reddit = praw.Reddit(user_agent='CanadaKnifeBot (by /u/UNLUCK3', client_id=identity, client_secret=secretpass,
                     username='DiscreetBot', password=botpassword)

# Which subreddit the bot should crawl
subreddit = reddit.subreddit('DiscreetTest')

# Main part of the program
def mainloop():
    counter1 = 0  # Counts submissions in new that have been crawled
    for submission in subreddit.new(limit=5):  # Get the 5 newest submissions
        counter1 = counter1 + 1
        if submission.id not in posts_replied_to:  # what I want is for it to print the as they come in while running,
            # idk how to do that yet though...
            print("These posts are new: \n")
            print(counter1)
            print("Title: ", submission.title)
            print("Text: ", submission.selftext, "\n")
        else:
            mainloop()

        callings = ['canada', 'canadian', '🇨🇦']  # Triggers
        normalized_title = submission.title.lower()
        normalized_text = submission.selftext.lower()

        if submission.id not in posts_replied_to:  # If the post is new to the bot
            time.sleep(30)  # Keep spam low
            for canadian_mentions in callings:
                if canadian_mentions in normalized_title:  # If trigger is in title
                    # Make the reply, print to console, then add the post to the replied storage
                    submission.reply(reply_text)
                    print("Bot replying to : ", submission.title, "\n")
                    posts_replied_to.append(submission.id)
                elif canadian_mentions in normalized_text:  # If trigger is in text body
                    # Make the reply, print to console, then add the post to the replied storage
                    submission.reply(reply_text)
                    print("Bot replying to : ", submission.selftext, "\n")
                    posts_replied_to.append(submission.id)
                else:
                    print("No applicable posts right now.")
                with open("posts_replied_to.txt", "w") as f:
                    for post_id in posts_replied_to:
                        f.write(post_id + "\n")  # Write changes
        mainloop()

mainloop()

