import praw
import IDandSecret
from praw.models import MoreComments

identity = IDandSecret.ClientID
secretpass = IDandSecret.ClientSecret
botpassword = IDandSecret.MyPass

def replymachine(text):
    if text == 'reply':
        reply_text = "Hey ", usernames, " This guy got a knife inside Canada somehow! Do you want it?     ^^I'm ^^a ^^bot.      ^^PM ^^/u/UNLUCK3 ^^for ^^help, ^^or ^^to ^^add ^^yourself.  "
        submission.reply(reply_text)

reddit = praw.Reddit(user_agent='CanadaKnifeBot (by /u/UNLUCK3', client_id=identity, client_secret=secretpass, username='CanadaKnifeBot', password=botpassword)

subreddit = reddit.subreddit('DiscreetTest')

for submission in subreddit.stream.submissions():

    callings = ['canada', 'canadian', '🇨🇦']
    usernames = ['/u/UNLUCK3', '/u/DiscreetBot']
    normalized_title = submission.title.lower()
    normalized_text = submission.selftext.lower()
    alreadydone = 0

    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        if top_level_comment.body == reply_text:
            alreadydone = 1
        else alreadydone = 0
        if alreadydone == 1:
            break
        elif alreadydone = 0:
            for canadian_mentions in callings:
                if canadian_mentions in normalized_title:
                    replymachine('reply')
                    break
                elif canadian_mentions in normalized_text:
                    replymachine('reply')
                    break
