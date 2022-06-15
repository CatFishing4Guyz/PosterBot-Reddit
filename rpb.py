import praw
import discord
import asyncio
import os
from discord import Option

bot = discord.Bot()

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
async def subreddit(ctx, subreddit: Option(str, description="Pick a subreddit", required=True),
                amount: Option(int, description="How many posts to send?", required=True)):
    for submission in reddit.subreddit(f"{subreddit}").hot(limit=amount):
        await ctx.channel.send(f'''"{submission.title}"\n'''
                               f"by `u/{submission.author}`\n"
                               f"{submission.url}")
        await asyncio.sleep(1)

bot.run(os.getenv('FOURTH_TOKEN'))