from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    if message.content.startswith('チャンネル作成'):
        # チャンネルを作成する非同期関数を実行して Channel オブジェクトを取得
        new_channel = await create_channel(message, channel_name='猫助が作成したチャンネル')

        # チャンネルのリンクと作成メッセージを送信
        text = f'{new_channel.mention} を作成したよーん'
        await message.channel.send(text)
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content.startswith('チャンネル作成'):
        # チャンネルを作成する非同期関数を実行して Channel オブジェクトを取得
        new_channel = await create_channel(message, channel_name='猫助が作成したチャンネル')

        # チャンネルのリンクと作成メッセージを送信
        text = f'{new_channel.mention} を作成したよーん'
        await message.channel.send(text)
    elif message.content == "!Nhelp":
        # リアクションアイコンを付けたい
        q = await message.channel.send("音楽のヘルプかな?使い方:まず、ボイスチャンネルに入って、チャットに!N1~5の数値を入力してその後に、playを入れてエンター！（既に猫助がいる場合は、resetと打って送信して一度出入りしてください、この時、既に猫助がいるボイスチャンネルにいる必要があります）")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記
    if message.content == 'えさだよー':
        await message.channel.send('にゃーん')
    if message.content == 'マタタビだよー':
        await message.channel.send('にゃーん')
    if message.content == '猫好き':
        await message.channel.send('にゃーん')
    if message.content == 'fuck':
        await message.channel.send('しゃー')
    if message.content == '!nekosukehelp':
        await message.channel.send('最近追加された機能です！neko-gというチャンネルを作成し、nekosuke-webhookというウェブフックを追加するとグローバルチャットができます！')
    if message.content == '犬嫌い':
        await message.channel.send('にゃーん')
    if message.content == 'ちゅーるだよー':
        await message.channel.send('にゃーん')
    elif message.content == "おみくじ":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日のにゃん勢は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[運勢] ", value=random.choice(('にゃい吉', '吉', '凶', 'にゃい凶','あんまり引くと怒るにゃ-大大凶','にゃい吉')), inline=False)
        await message.channel.send(embed=embed)





bot.run(token)
