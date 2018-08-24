import praw
import IDandSecret

identity = IDandSecret.ClientID
secretpass = IDandSecret.ClientSecret
botpassword = IDandSecret.MyPass

reddit = praw.Reddit(user_agent='CanadaKnifeBot (by /u/UNLUCK3', client_id=identity, client_secret=secretpass, username='CanadaKnifeBot', password=botpassword)

subreddit = reddit.subreddit('DiscreetTest')
for submission in subreddit.stream.submissions():
    callings = ['canada', 'canadian', '🇨🇦']
    normalized_title = submission.title.lower()
    for canadian_mentions in callings:
        if canadian_mentions in normalized_title:
            usernames = ['/u/UNLUCK3', '/u/DiscreetBot']
            reply_text = "Hey ", usernames, " This guy got a knife inside Canada somehow! Do you want it?     ^^I'm ^^a ^^bot.      ^^PM ^^/u/UNLUCK3 ^^for ^^help.  "
            submission.reply(reply_text)
            break
