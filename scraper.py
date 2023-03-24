import praw
import pandas as pd


reddit = praw.Reddit()

# for submission in reddit.subreddit("AmITheAsshole").top(limit=10):
#     print(submission.score)

for comment in reddit.subreddit("AmITheAsshole").stream.comments():
    print(comment.body)

# posts = []
#
# aita_subreddit = reddit.subreddit('AmITheAsshole')
#
# for post in aita_subreddit.top(limit=10):
#     posts.append([post.title, post.score, post.id,
#                   post.subreddit, post.url, post.num_comments,
#                   post.selftext, post.created])
#
# posts = pd.DataFrame(posts, columns=['title', 'score', 'id',
#                                      'subreddit', 'url', 'num_comments',
#                                      'body', 'created'])
#
# # Export CSV file to desktop
# posts.to_csv(r'C:\Users\Danie\Desktop\export_dataframe.csv', index=False, header=True)
#
# print(posts)

