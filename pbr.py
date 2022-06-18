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
                    subreddit: Option(str, description='''The "r/" part is optional"''', required=True),
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
    # I apologize for the boilerplate code, not much I can do
    match category:
        case "Top":
            for Post in reddit.subreddit(f"{subreddit.strip('r/')}").top(limit=amount):
                post = (f"> **{Post.title}**\n"
                        f"by `u/{Post.author}` "
                        f"with {Post.score} upvotes\n\n")
                if Post.author is None:
                    post = post.replace(str(None), "deleted")
                post = post + f"> {Post.selftext}" if Post.is_self else post + f"> {Post.url}"
                await ctx.send(post)
                await asyncio.sleep(2)
        case "Hot":
            for Post in reddit.subreddit(f"{subreddit.strip('r/')}").hot(limit=amount):
                post = (f"> **{Post.title}**\n"
                        f"by `u/{Post.author}` "
                        f"with {Post.score} upvotes\n\n")
                if Post.author is None:
                    post = post.replace(str(None), "deleted")
                post = post + f"> {Post.selftext}" if Post.is_self else post + f"> {Post.url}"
                await ctx.send(post)
                await asyncio.sleep(2)
        case "Rising":
            for Post in reddit.subreddit(f"{subreddit.strip('r/')}").rising(limit=amount):
                post = (f"> **{Post.title}**\n"
                        f"by `u/{Post.author}` "
                        f"with {Post.score} upvotes\n\n")
                if Post.author is None:
                    post = post.replace(str(None), "deleted")
                post = post + f"> {Post.selftext}" if Post.is_self else post + f"> {Post.url}"
                await ctx.send(post)
                await asyncio.sleep(2)
        case "New":
            for Post in reddit.subreddit(f"{subreddit.strip('r/')}").new(limit=amount):
                post = (f"> **{Post.title}**\n"
                        f"by `u/{Post.author}` "
                        f"with {Post.score} upvotes\n\n")
                if Post.author is None:
                    post = post.replace(str(None), "deleted")
                post = post + f"> {Post.selftext}" if Post.is_self else post + f"> {Post.url}"
                await ctx.send(post)
                await asyncio.sleep(2)
        case "Controversial":
            for Post in reddit.subreddit(f"{subreddit.strip('r/')}").controversial(limit=amount):
                post = (f"> **{Post.title}**\n"
                        f"by `u/{Post.author}` "
                        f"with {Post.score} upvotes\n\n")
                if Post.author is None:
                    post = post.replace(str(None), "deleted")
                post = post + f"> {Post.selftext}" if Post.is_self else post + f"> {Post.url}"
                await ctx.send(post)
                await asyncio.sleep(2)

bot.run(os.getenv('FOURTH_TOKEN'))