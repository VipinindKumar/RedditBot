"""
Name : Vipin Kumar
Email: vipin.ind.kumar@gmail.com

Bot gets comments from the subreddit 'gifs' and
then reply to the individual comments who mention
"its" ot "it's" with a explanation to differentiate
"its" and "it's"
"""

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
		message = "it\'s = it is\n\n\n\nIt\'s difficult to find work these days.\n\nIt\'s going to rain soon.\n\n\n\nIt\'s = It is is often used with adjectives, nouns, the comparative and superlative.\n\n\n\nit\'s = it has\n\n\n\nIt\'s been a while since I went there.\n\nIt\'s done at the local shop.\n\n\n\nIts is the possessive adjective form. This form is used to express that \"it\" has a specific quality, or that something belongs to \"it\".\n\nI found its taste to be superb!\n\nIts color is deep red, almost Burgundy.\n\n\n\nSource - https://www.thoughtco.com/its-vs-its-1210744"

		# reply to the comment with the message
		comment.reply(message)
