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
		message = "it\'s = it is\n\nIt\'s difficult to find work these days.\nIt\'s going to rain soon.\n\nIt\'s = It is is often used with adjectives, nouns, the comparative and superlative.\n\n	it\'s = it has\n\nIt\'s been a while since I went there.\nIt\'s done at the local shop.\n\nIts is the possessive adjective form. This form is used to express that \"it\" has a specific quality, or that something belongs to \"it\".\nI found its taste to be superb!\nIts color is deep red, almost Burgundy."
		
