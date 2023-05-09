import os
from pyrogram import Client, filters
import openai

openai.api_key = API_KEY

bot = Client(BOT_TOKEN)

def generate_code(prompt):
    response = openai.Completion.create(
        engine='davinci-codex',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

@bot.on_message(filters.command('start'))
def start_handler(client, message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Hello! How can I help you!"
    )

@bot.on_message(filters.text & ~filters.command('code'))
def handle_message(client, message):
   
    words = message.text.split()
    my_code = ' '.join(words[1:])
    code = generate_code(my_code)


    bot.send_message(chat_id=message.chat.id, text=code)

# Start the bot
    bot.run()
