import os
from pyrogram import Client, filters
import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

# Create a Pyrogram bot instance
bot = Client('6246848845:AAFJn1YnOt0Wy_vyroDF6i_1SKCd84f9QSw')

# Function to generate code using Codex
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

# Handler for the /start command
@bot.on_message(filters.command('start'))
def start_handler(client, message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Hello! I am a Codex-powered bot. Send me a programming question or a code prompt, and I'll generate code for you!"
    )

# Handler for text messages
@bot.on_message(filters.text & ~filters.command('start'))
def handle_message(client, message):
    # Generate code using Codex
    code = generate_code(message.text)

    # Send the generated code as a reply
    bot.send_message(chat_id=message.chat.id, text=code)

# Start the bot
    bot.run()
