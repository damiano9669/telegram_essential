from telegram_essential.TelegramBot import TelegramBot

if __name__ == '__main__':
    token = '...'
    path = '...'  # where save files downloaded
    bot = TelegramBot(token)

    while True:
        updates = bot.get_updates()
        if bot.is_new_update(updates):
            # print(bot.get_last_update(updates))
            message_type = bot.get_type_of_response(updates)

            if message_type == 'text':
                chat_id, name, message, date = bot.get_id_name_text_date(updates)
                message = 'id: {}\nname: {}\ndate: {}\nmessage:\n{}'.format(chat_id, name, date, message)
                bot.send_text(chat_id, message)
            elif message_type == 'photo':
                chat_id, name, photo, date = bot.get_id_name_photo_date(updates, path)
                bot.send_photo(chat_id, photo)
            elif message_type == 'document':
                chat_id, name, doc, date = bot.get_id_name_document_date(updates, path)
                bot.send_document(chat_id, doc)
            elif message_type == 'voice':
                chat_id, name, voice, date = bot.get_id_name_voice_date(updates, path)
                bot.send_voice_message(chat_id, voice)
            elif message_type == 'audio':
                chat_id, name, audio, date = bot.get_id_name_audio_date(updates, path)
                bot.send_audio(chat_id, audio)
            elif message_type == 'video':
                chat_id, name, video, date = bot.get_id_name_video_date(updates, path)
                bot.send_video(chat_id, video)
