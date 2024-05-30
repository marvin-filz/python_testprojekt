from pyrogram import Client, filters
import config  # Importiere die Konfigurationsdatei

# Erstellen und starten des Clients
app = Client("echo_bot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

# Definieren des Handlers für einkommende Nachrichten
@app.on_message(filters.text)
def echo(client, message):
    # Senden der eingehenden Nachricht zurück an den Absender
    message.reply_text("Das war die Nachricht: " + message.text)
    
# Starten des Bots
if __name__ == '__main__':
    app.run()


