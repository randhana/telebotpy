import requests
from datetime import datetime

class TelegramBot:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def _get_date_time(self):
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        return f"Date: {date} {time}"

    def _handle_response(self, response):
        try:
            response.raise_for_status()  
            print("Request successful.")
        except requests.exceptions.HTTPError as e:
            print(f"Request failed. Error code: {response.status_code}")
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {e}")

    def send_text_message(self, message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        date_time = self._get_date_time()
        params = {
            'chat_id': self.chat_id,
            'text': message + "  \n" + date_time,
            'parse_mode': 'Markdown'
        }

        try:
            response = requests.post(url, data=params)
            self._handle_response(response)
        except requests.exceptions.RequestException as e:
            print(f"Failed to send text message: {e}")

    def send_image(self, image_filename, caption):
        with open(image_filename, 'rb') as image_file:
            url = f"https://api.telegram.org/bot{self.token}/sendPhoto"
            date_time = self._get_date_time()
            files = {
                'photo': image_file
            }
            data = {
                'chat_id': self.chat_id,
                'caption': caption + "  \n" + date_time
            }

            try:
                response = requests.post(url, files=files, data=data)
                self._handle_response(response)
            except requests.exceptions.RequestException as e:
                print(f"Failed to send image: {e}")

    def send_document(self, document_path, caption):
        with open(document_path, 'rb') as document_file:
            url = f"https://api.telegram.org/bot{self.token}/sendDocument"
            date_time = self._get_date_time()
            files = {
                'document': document_file
            }
            data = {
                'chat_id': self.chat_id,
                'caption': caption + "  \n" + date_time
            }

            try:
                response = requests.post(url, files=files, data=data)
                self._handle_response(response)
            except requests.exceptions.RequestException as e:
                print(f"Failed to send document: {e}")

    def send_video(self, video_path, caption):
        with open(video_path, 'rb') as video_file:
            url = f"https://api.telegram.org/bot{self.token}/sendVideo"
            date_time = self._get_date_time()
            files = {
                'video': video_file
            }
            data = {
                'chat_id': self.chat_id,
                'caption': caption + "  \n" + date_time
            }

            try:
                response = requests.post(url, files=files, data=data)
                self._handle_response(response)
            except requests.exceptions.RequestException as e:
                print(f"Failed to send video: {e}")
