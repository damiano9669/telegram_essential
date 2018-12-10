from telegram_essential.telegram_api import telegram_api


class telegram_bot():

    def __init__(self, token):
        self.api = telegram_api(token)

    def send_text(self, chat_id, text):
        """
        :param chat_id:
        :param text: message to send
        :return:
        """
        self.api.send_message(chat_id, text)
        return True

    def send_photo(self, chat_id, path):
        """
        :param chat_id:
        :param path: photo path
        :return:
        """
        self.api.send_file(chat_id, 'photo', path)
        return True

    def send_voice_message(self, chat_id, path):
        """
        :param chat_id:
        :param path: voice message path
        :return:
        """
        self.api.send_file(chat_id, 'voice', path)
        return True

    def send_document(self, chat_id, path):
        """
        :param chat_id:
        :param path: document path
        :return:
        """
        self.api.send_file(chat_id, 'document', path)
        return True

    def send_audio(self, chat_id, path):
        """
        :param chat_id:
        :param path: audio path
        :return:
        """
        self.api.send_file(chat_id, 'audio', path)
        return True

    def get_id_name_text_date(self, updates):
        """
        :param updates:
        :return: (chat_id, name, text, date)
        """
        return self.api.get_id_name_content_date(updates, 'text')

    def get_id_name_photo_date(self, updates, path, quality=2):
        """
            download photo from chat
        :param path: directory path to save image
        :param quality: 0 (worst quality), 1 (bad quality), 2 (medium quality), 3 (best quality)
        :return: tuple (user_id, name, photo path, date)
        """
        user_id, name, photos, date = self.api.get_id_name_content_date(updates, content_type='photo')
        file_id = photos[quality]['file_id']
        path_photo = self.api.download_file(file_id, path)
        return (user_id, name, path_photo, date)

    def get_id_name_voice_date(self, updates, path):
        """
            download voice message from chat
        :param path: directory path to save voice message
        :return: tuple (user_id, name, voice path, date)
        """
        user_id, name, voice, date = self.api.get_id_name_content_date(updates, content_type='voice')
        file_id = voice['file_id']
        path_voice = self.api.download_file(file_id, path)
        return (user_id, name, path_voice, date)

    def get_id_name_document_date(self, updates, path):
        """
            download document
        :param updates:
        :param path:
        :return: (chat_id, name, document path, date)
        """
        user_id, name, document, date = self.api.get_id_name_content_date(updates, content_type='document')
        file_id = document['file_id']
        path_document = self.api.download_file(file_id, path, document['file_name'])
        return (user_id, name, path_document, date)

    def get_id_name_audio_date(self, updates, path):
        """
            download audio file
        :param updates:
        :param path:
        :return: (chat_id, name, audio path, date)
        """
        user_id, name, audio, date = self.api.get_id_name_content_date(updates, content_type='audio')
        file_id = audio['file_id']
        path_audio = self.api.download_file(file_id, path,
                                            '{}.{}'.format(audio['title'], audio['mime_type'].split('/')[-1]))
        return (user_id, name, path_audio, date)
