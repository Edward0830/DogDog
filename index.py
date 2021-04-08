import discord, datetime, asyncio, random
token = "ODI4MjE0OTU5MDA3NTk2NTQ1.YGmVSQ.ezj4L0eDGQ2MWKSsRku3jx388rU"

client = discord.Client()

@client.event
async def on_ready():
    print("Dog소리중")
    print(client.user)
    print("=========================")

@client.event
async def on_message(message):
    if message.content == "아무개":
        await message.channel.send("환상의 나라")
    if message.content == "쫀아":
        await message.channel.send("쪼은 아침")
    if message.content == "진우":
        await message.channel.send("아무개 봇의 개발자이자 초등학생")
    if message.content == "효향":
        await message.channel.send("핑크 (전)솔로 판다")
    if message.content == "지냥":
        await message.channel.send("아무개방과 아무개 디코의 총관리자")
    if message.content == "경다니":
        await message.channel.send("지냥님과함께 아무개방과 아무개 디코의 총관리자")
    if message.content == "예림":
        await message.channel.send("누나라고 부르는걸 싫어한다")



    if message.content == "!도움말":
        embed = discord.Embed(colour=discord.Colour.red(), title="아무개 봇 설명서", description="간단 명령어는 알아서 찾아보십쇼   !도움말 (도움말을 알려줌)   !내정보 (내정보를 보여줌)   서버아이콘 (아무개 서버의 아이콘을 보여줌)  뽑기 (1부터 15까지의 숫자중 한 숫자가 랜덤으로 나옴) ")

        await message.channel.send(embed=embed)

    if message.content.startswith(f"!채널메세지"):
        ch = client.get_channel(int(message.content[7:25]))
        await ch.send(message.content[26:])

    if message.content == "!내정보":
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 아이디 / 닉네임 : {user.name} / {user.id} / {user.display_name}")
        await message.channel.send(message.author.avatar_url)

    if message.content == "서버아이콘":
        await message.channel.send(message.guild.icon_url)

    if message.content == "뽑기":
        await message.channel.send(random.randint(1,12))

    
    if message.content == "1분 타이머":
        await asyncio.sleep(60)
        await message.channel.send(f"{message.author.mention}, 1분 지났습니다")
    

client.run(token)