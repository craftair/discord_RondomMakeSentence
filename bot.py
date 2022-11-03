import discord
import markovify
from discord.ext import tasks

TOKEN = 'TOKEN_KEY' # 

hand_ans = []
list_hand = []
count = 0
result1 = []
client = discord.Client(intents=discord.Intents.all())

f1 = open('ricky_like.json', 'r',encoding="utf-8")
f2 = open('scp.json', 'r',encoding="utf-8")
f3 = open('FLOWER.json', 'r',encoding="utf-8")
text_model_ricky = markovify.Text.from_json(f1.read())
text_model_scp = markovify.Text.from_json(f2.read())
text_model_FLOWER = markovify.Text.from_json(f3.read())

@client.event
async def on_ready():
    print('ログインしました')
    await login()

async def login():
    channel = client.get_channel("チャンネルID")
    await channel.send("ログインしたよ")


@client.event
async def on_message(message):
    # if message.author.bot: でreturnでも可k
    global hand_ans,count
    try:
        if message.content == '/ricky':
            print("ricky")
            sentence = text_model_ricky.make_sentence(tries=100)
            sentence=sentence.replace(" ","")
            await message.channel.send(sentence)
            print(sentence)
        if message.content == "/scp":
            print("scp")
            sentence = text_model_scp.make_sentence(tries=100)
            sentence=sentence.replace(" ","")
            await message.channel.send(sentence)
            print(sentence)
        if message.content == "/flower":
            print("flower")
            sentence = text_model_FLOWER.make_sentence(tries=100)
            sentence=sentence.replace(" ","")
            await message.channel.send(sentence)
            print(sentence)
    except AttributeError:
        await message.channel.send("エラーだよ...エラーだよ...エラーだよ...エラーだよ...エラーだよ...")



client.run(TOKEN)
