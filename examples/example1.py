from telegram_essential.telegram_bot import telegram_bot

if __name__ == '__main__':
    token = '...'
    path = '...'  # where save files downloaded
    bot = telegram_bot(token)

    while True:
        updates = bot.api.get_updates()
        if bot.api.is_new_update(updates):
            print(bot.api.get_last_update(updates))
            type = bot.api.get_type_of_response(updates)

            if type == 'text':
                chat_id, name, message, date = bot.get_id_name_text_date(updates)
                message = 'id: {}\nname: {}\ndate: {}\nmessage:\n{}'.format(chat_id, name, date, message)
                bot.send_text(chat_id, message)
            elif type == 'photo':
                chat_id, name, photo, date = bot.get_id_name_photo_date(updates, path)
                bot.send_photo(chat_id, photo)
            elif type == 'document':
                chat_id, name, doc, date = bot.get_id_name_document_date(updates, path)
                bot.send_document(chat_id, doc)
            elif type == 'voice':
                chat_id, name, voice, date = bot.get_id_name_voice_date(updates, path)
                bot.send_voice_message(chat_id, voice)
            elif type == 'audio':
                chat_id, name, audio, date = bot.get_id_name_audio_date(updates, path)
                bot.send_audio(chat_id, audio)
