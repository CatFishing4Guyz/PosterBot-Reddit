import praw
import discord
import asyncio
import os
from discord import Option

bot = discord.Bot()

"""
Make a new Reddit app, paste your
client ID, client secret, and user
agent in separate environment
variables, with the variable names
matching what I have provided. You
can make your own variable names,
but be sure it starts with "praw_"
and change the ones here, too.
"""
reddit = praw.Reddit(
    client_id = f"{os.getenv('praw_CLIENT_ID')}",
    client_secret = f"{os.getenv('praw_CLIENT_SECRET')}",
    user_agent = f"{os.getenv('praw_USER_AGENT')}"
)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[831412377869221899],
description="Send a specified amount of posts from a subreddit!")
async def subreddit(ctx,
                subreddit: Option(str, description="Pick a subreddit", required=True),
                category: Option(str, description="Sort by?", required=True, choices=[
                                                                                "Top",
                                                                                "Best", 
                                                                                "Hot", 
                                                                                "Rising", 
                                                                                "New", 
                                                                                "Controversial"
                                                                             ]
                                ),
                amount: Option(int, description="How many posts to send?", required=True)):
    # I apologize for the boilerplate code
    match category:
        case "Top":
            for submission in reddit.subreddit(f"{subreddit}").top(limit=amount):
                await ctx.send(f'''"{submission.title}"\n'''
                                       f"by `u/{submission.author}` "
                                       f"with {submission.score} upvotes\n"
                                       f"{submission.url}")
                await asyncio.sleep(1)
        case "Best":
            for submission in reddit.subreddit(f"{subreddit}").best(limit=amount):
                await ctx.send(f'''"{submission.title}"\n'''
                                       f"by `u/{submission.author}` "
                                       f"with {submission.score} upvotes\n"
                                       f"{submission.url}")
                await asyncio.sleep(1)
        case "Hot":
            for submission in reddit.subreddit(f"{subreddit}").hot(limit=amount):
                await ctx.send(f'''"{submission.title}"\n'''
                                       f"by `u/{submission.author}` "
                                       f"with {submission.score} upvotes\n"
                                       f"{submission.url}")
                await asyncio.sleep(1)
        case "Rising":
            for submission in reddit.subreddit(f"{subreddit}").rising(limit=amount):
                await ctx.send(f'''"{submission.title}"\n'''
                                       f"by `u/{submission.author}` "
                                       f"with {submission.score} upvotes\n"
                                       f"{submission.url}")
                await asyncio.sleep(1)
        case "New":
            for submission in reddit.subreddit(f"{subreddit}").new(limit=amount):
                await ctx.send(f'''"{submission.title}"\n'''
                                       f"by `u/{submission.author}` "
                                       f"with {submission.score} upvotes\n"
                                       f"{submission.url}")
                await asyncio.sleep(1)
        case "Controversial":
            for submission in reddit.subreddit(f"{subreddit}").controversial(limit=amount):
                await ctx.send(f'''"{submission.title}"\n'''
                                       f"by `u/{submission.author}` "
                                       f"with {submission.score} upvotes\n"
                                       f"{submission.url}")
                await asyncio.sleep(1)

bot.run(os.getenv('FOURTH_TOKEN'))