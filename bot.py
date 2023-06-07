from pymino import Bot;
from gtts import gTTS;

from dotenv import load_dotenv;


load_dotenv();



email = ""
password = ""
comunity = 0;

bot = Bot("!", comunity);
bot.run(email, password);
bot.set_community_id(comunity);


chat = ""

print(chat)

@bot.on_ready()
def on_ready():
    print(f"Bot phoenix is working {bot.profile.username}(bot.profile.userId)");
    
@bot.task(interval=40)
def task(community: comunity):
    Banlist = ["infinity shop", "Infinity Shop", "InfinityShop", "CompreNaSubmundo", "Compre na Submundo", "COMU NA BIO! 💕", "MeshBot"];
    print("☆ Searching for bots...")
    nickNamesToBan = []
    linksToBan = []
    users = bot.community.fetch_users(comId=comunity, size=5);
        
    def doubleVerify(array):
        conjunto = set()
        strings = []

        for elemento in array:
            if elemento in conjunto:
                strings.append(elemento)
            else:
                conjunto.add(elemento)

        print(f"-----------ENCONTRAMOS: {len(strings)}")

        for i in strings:
            Banlist.append(i);

      
    
    
    doubleVerify(users.nickname);
    
    for i in range(len(users.nickname)):
        if(users.nickname[i] in Banlist):
            nickNamesToBan.append(i)
            print("One bot has been founded.")


        
    for i in nickNamesToBan:
        urlToBan = bot.community.fetch_object(users.uid[i]).shareURLShortCode;
        linksToBan.append(urlToBan)
        
        
    for i in linksToBan:
        print("Bot reported.")
        content = f"Bot detectado {i}"
        bot.community.send_message(chat, content)
