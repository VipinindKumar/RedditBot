import praw

# define the credentials of the bot
bot = praw.Reddit(user_agent='myBot', 
				  client_id='abc',
				  client_secret='123',
				  username='',
				  password='')

# add the subreddit name and
# get a stream of comments			  
subreddit = bot.subreddit('gifs')

comments = subreddit.stream.comments()
