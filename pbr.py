import praw
import discord
import asyncio
import os

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
async def subreddit(ctx,
                subreddit: Option(str, description="Pick a subreddit", required=True),
                category: Option(str, description="Sort by?", required=True,
                                 choices=[
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
    match sort:
        case category=="Top":
            for submission in reddit.subreddit(f"{subreddit}").top(limit=amount):
                await ctx.channel.send(f'''"{submission.title}"\n'''
                                       f"by `u/{submission.author}` "
                                       f"with {submission.score}\n"
                                       f"{submission.url}")
                await asyncio.sleep(1)
        case category=="Best":
            for submission in reddit.subreddit(f"{subreddit}").best(limit=amount):
                await ctx.channel.send(f'''"{submission.title}"\n'''
                                       f"by `u/{submission.author}` "
                                       f"with {submission.score}\n"
                                       f"{submission.url}")
                await asyncio.sleep(1)
        case category=="Hot":
            for submission in reddit.subreddit(f"{subreddit}").hot(limit=amount):
                await ctx.channel.send(f'''"{submission.title}"\n'''
                                       f"by `u/{submission.author}` "
                                       f"with {submission.score}\n"
                                       f"{submission.url}")
                await asyncio.sleep(1)
        case category=="Rising":
            for submission in reddit.subreddit(f"{subreddit}").rising(limit=amount):
                await ctx.channel.send(f'''"{submission.title}"\n'''
                                       f"by `u/{submission.author}` "
                                       f"with {submission.score}\n"
                                       f"{submission.url}")
                await asyncio.sleep(1)
        case category=="New":
            for submission in reddit.subreddit(f"{subreddit}").new(limit=amount):
                await ctx.channel.send(f'''"{submission.title}"\n'''
                                       f"by `u/{submission.author}` "
                                       f"with {submission.score}\n"
                                       f"{submission.url}")
                await asyncio.sleep(1)
        case category=="Controversial":
            for submission in reddit.subreddit(f"{subreddit}").controversial(limit=amount):
                await ctx.channel.send(f'''"{submission.title}"\n'''
                                       f"by `u/{submission.author}` "
                                       f"with {submission.score}\n"
                                       f"{submission.url}")
                await asyncio.sleep(1)

bot.run(os.getenv('FOURTH_TOKEN'))