from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random

# Set your bot token and admin user ID
BOT_TOKEN = '7961297908:AAHz95NJJCqXgdKsLuD3ImwW-FGi0E75vjE'  # Replace with your bot's token
ADMIN_USER_ID = '8179218740'  # Replace with your Telegram user ID
approved_users = set()  # Set to store approved users

# List of all the designs you want
styles = [
    "𒆜۞𓆩 </b>{name}</b> 𓆪۞𒆜",
    "༺⚡𝕿𝖍𝖊 𝕯𝖆𝖗𝖐 </b>{name}</b>⚡༻",
    "︻╦̵̵͇̿̿̿̿╤── </b>{name}</b> 彡",
    "꧁༒☠︎︎ </b>{name}</b> ☠︎︎༒꧂",
    "⫷⫸ 『</b>{name}</b>』⫷⫸",
    "۞꧁༒⫷ </b>{name}</b> ⫸༒꧂۞",
    "𓆩⚔︎𓆪 『</b>{name}</b>』 𓆩⚔︎𓆪",
    "༒︎</b>{name}</b>༒︎",
    "ღƬʜ𝖊 ⱽᵉⁿᵒᵐ </b>{name}</b>ღ",
    "⟪𖤐⟫ </b>{name}</b> 𖤐⟬⟭",
    "𓆩♛𓆪 『𝓣𝓱𝓮 </b>{name}</b>』 ♛",
    "꧁༺༒ ᑘJᒪ </b>{name}</b> ༒༻꧂",
    "ღ ᴀɴɪᴍᴇ ᴋɪɴɢ ~ </b>{name}</b> ღ",
    "✦⛧『</b>{name}</b>』⛧✦",
    "༒︎ᴅᴇᴠɪʟ ʀᴇɪɢɴ ~ </b>{name}</b>༒︎",
    "꧁༒☬</b>{name}</b>☬༒꧂",
    "𓆩꧁</b>{name}</b>꧂𓆪",
    "꧁༒☠︎︎</b>{name}</b>☠︎︎༒꧂",
    "༄༅༎✧</b>{name}</b>✧༎༅༄",
    "⫷『</b>{name}</b>』⫸",
    "✧༺♥️</b>{name}</b>♥️༻✧",
    "꧁༺</b>{name}</b>࿐༻꧂",
    "★彡</b>{name}</b>彡★",
    "༺🔥</b>{name}</b>🔥༻",
    "⫷⫸『</b>{name}</b>』⫷⫸",
    "︻デ═一 </b>{name}</b>一═デ︻",
    "×͜× </b>{name}</b> ☠︎︎",
    "[▓▓]▬▬▬▬▬● </b>{name}</b>",
    "★·.·´¯`·.·★ </b>{name}</b> ★·.·´¯`·.·★",
    "⸻⸻⸻⚔️</b>{name}</b>⚔️⸻⸻⸻",
    "╰┈➤ ✿ </b>{name}</b> ✿",
    "✿◕ ‿ ◕✿ </b>{name}</b> ✿◕ ‿ ◕✿",
    "｡･:*:･ﾟ★,｡･:*:･ﾟ☆ </b>{name}</b> ☆ﾟ･:*:･｡,★ﾟ･:*:･｡",
    "≧◉ᴥ◉≦ : </b>{name}</b>",
    "ღゝ◡╹)ノ♡ </b>{name}</b>",
    "𓂀 ˚₊· ͟͟͞͞➳❥ </b>{name}</b> ♡",
    "⪼ ꧁༺༒༻꧂ </b>{name}</b> ꧁༺༒༻꧂",
    "╭◜◝ ͡ ◜◝ ╮ </b>{name}</b> ╭◜◝ ͡ ◜◝ ╮",
    "✧*̥˚ </b>{name}</b> ˚*̥✧",
    "༄༅ 𝕿𝖍𝖊 </b>{name}</b> ༄༅",
    "𒆜𒆜⫷⫷ </b>{name}</b> ⫸⫸𒆜𒆜",
    "╰┈➤ ꧁༒☬ </b>{name}</b> ☬༒꧂",
    "︵‿︵‿୨♡ </b>{name}</b> ♡୧‿︵‿︵",
    "(っ◔◡◔)っ ♥ </b>{name}</b> ♥",
    "★彡[</b>{name}</b>]彡★",
    "⫷ 𓆩 </b>{name}</b> 𓆪 ⫸",
    "彡★ </b>{name}</b> ★彡"
]

# Function to handle /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "👋 𝐇𝐞𝐥𝐥𝐨𝐰! 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐓𝐡𝐞 𝐍𝐞𝐦 𝐒𝐭𝐲𝐥𝐞𝐫 𝐁𝐨𝐭!✨\n"
        "Send /design <name> to generate a cool stylized version of your name 📝💥.\n"
        "If you're the admin, you can add users with /add <user_id> 🔧.\n 𝑶𝒘𝒏𝒆𝒓 𝑩𝒐𝒍𝒕𝒆 𝑩𝒉𝒊𝒅𝒖 @SIDIKI_MUSTAFA_92"
    )

def design(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_id not in approved_users:
        update.message.reply_text(
            "🚫 You are not authorized to use this bot. Please contact the admin to get approved.🙏\nAdmin - @SIDIKI_MUSTAFA_92💀"
        )
        return

    if len(context.args) == 0:
        update.message.reply_text(
            "⚠️ Please provide a name. Usage: /design <name> 👇"
        )
        return

    name = " ".join(context.args)
    all_styles = ""
    for style in styles:
        stylized = style.format(name=name)
        all_styles += f"{stylized}\n\n"

    update.message.reply_text(
        f"🎉 Here are all your stylized names:\n\n{all_styles}",
        parse_mode='HTML'
    )

# Function to handle /add command
def add(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    
    if user_id != int(ADMIN_USER_ID):
        update.message.reply_text("❌ You are not authorized to add users. Only the admin can do this. 🔒")
        return
    
    if len(context.args) == 0:
        update.message.reply_text("⚠️ Please provide the user ID to add. Usage: /add <user_id> 👇")
        return
    
    new_user_id = int(context.args[0])
    approved_users.add(new_user_id)
    update.message.reply_text(f"✅ User {new_user_id} has been added to the approved list. 🎉")

# Main function to set up the bot
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))  # /start command handler
    dp.add_handler(CommandHandler("design", design))  # /design command handler
    dp.add_handler(CommandHandler("add", add))  # /add command handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, design))  # Handle name input

    updater.start_polling()  # Start the bot
    updater.idle()  # Keep the bot running

if __name__ == '__main__':
    main())  # Keep the bot running

if __name__ == '__main__':
    main()