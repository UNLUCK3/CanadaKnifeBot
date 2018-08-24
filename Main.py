import praw
import IDandSecret
import time
import os

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))

identity = IDandSecret.ClientID
secretpass = IDandSecret.ClientSecret
botpassword = IDandSecret.MyPass
usernames = ['/u/UNLUCK3', '/u/DiscreetBot']
reply_text = 'Hey ', usernames, 'This guy got a knife inside Canada somehow! Do you want it?     ^^I\'m ^^a ^^bot.    ' \
                                '  ^^PM ^^/u/UNLUCK3 ^^for ^^help, ^^or ^^to ^^add ^^yourself '


reddit = praw.Reddit(user_agent='CanadaKnifeBot (by /u/UNLUCK3', client_id=identity, client_secret=secretpass,
                     username='CanadaKnifeBot', password=botpassword)

subreddit = reddit.subreddit('DiscreetTest')

def mainloop():
    counter1 = 0
    for submission in subreddit.new(limit=5):
        counter1 = counter1 + 1
        if submission.id not in posts_replied_to: # what I want is for it to print the as they come in while running,
            # idk how to do that though...
            print("These posts are new: \n")
            print(counter1)
            print("Title: ", submission.title)
            print("Text: ", submission.selftext, "\n")

        callings = ['canada', 'canadian', '🇨🇦']
        normalized_title = submission.title.lower()
        normalized_text = submission.selftext.lower()

        while counter1 <= 99:
            time.sleep(30) # change to a higher number when not testing
            if submission.id not in posts_replied_to:
                for canadian_mentions in callings:
                    if canadian_mentions in normalized_title:
                        submission.reply(reply_text)
                        print("Bot replying to : ", submission.title)
                        posts_replied_to.append(submission.id)
                    elif canadian_mentions in normalized_text:
                        submission.reply(reply_text)
                        print("Bot replying to : ", submission.selftext)
                        posts_replied_to.append(submission.id)
                    else:
                        print("No applicable posts right now.")
                    with open("posts_replied_to.txt", "w") as f:
                        for post_id in posts_replied_to:
                            f.write(post_id + "\n")
            mainloop()

mainloop()

