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

# iterate over comments 
for comment in comments:
	# get the body of comment and change it to lowerCase
	text = comment.body().lower()
	
	author = comment.author()
	
	if ('its' in text) or ("it's" in text):
		
		# Generate a message
		message = ''
		
