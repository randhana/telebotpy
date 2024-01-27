# telebotpy: A Python Package for Sending Telegram Messages, Images, and Documents

telebotpy is a Python package that simplifies the process of sending text messages, images, and documents to Telegram channels. It provides an easy-to-use interface for interacting with the Telegram Bot API, allowing you to integrate Telegram messaging into your Python projects effortlessly.

## Features

- Send text messages to Telegram channels.
- Send images to Telegram channels with optional captions.
- Send documents (files) to Telegram channels with optional captions.

## Installation

1. **Clone the project to your local machine:**

```bash
git clone https://github.com/randhana/telebotpy.git
```
2. Copy the telebotpy folder from the cloned project to your own project folder.
Import the module in your Python script:
```shell
from telebotpy.telebot import TelegramBot
```
## Usage
Here's how you can use telepy to send a text message to a Telegram channel:
```shell
from telebotpy.telebot import TelegramBot

# Replace 'YOUR_TOKEN' and 'YOUR_CHAT_ID' with your actual values
bot = TelegramBot(token="YOUR_TOKEN", chat_id="YOUR_CHAT_ID")
bot.send_text_message("This is a test message.")
bot.send_video('video.mp4', "Video_caption")
bot.send_document('document.txt', 'Document_caption')

```

## Contributing
We welcome contributions from the community. If you have any suggestions, bug reports, or would like to contribute to the development of telepy, please visit our GitHub repository and open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
- GitHub: [randhana](https://github.com/randhana)
