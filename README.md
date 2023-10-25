# telebotpy: A Python Package for Sending Telegram Messages, Images, and Documents

telepy is a Python package that simplifies the process of sending text messages, images, and documents to Telegram channels. It provides an easy-to-use interface for interacting with the Telegram Bot API, allowing you to integrate Telegram messaging into your Python projects effortlessly.

## Features

- Send text messages to Telegram channels.
- Send images to Telegram channels with optional captions.
- Send documents (files) to Telegram channels with optional captions.

## Installation

You can install `telebotpy` using pip:

```shell
(not available)
pip install telebotpy 
```
## Usage
Here's how you can use telepy to send a text message to a Telegram channel:
```shell
from telebotpy.telebot import TelegramBot

# Replace 'YOUR_TOKEN' and 'YOUR_CHAT_ID' with your actual values
bot = TelegramBot(token="YOUR_TOKEN", chat_id="YOUR_CHAT_ID")
bot.send_text_message("This is a test message.")
bot.send_video('video.mp4', "Video caption")

```

For more detailed examples and documentation, please visit the Wiki section of our GitHub repository.

## Contributing
We welcome contributions from the community. If you have any suggestions, bug reports, or would like to contribute to the development of telepy, please visit our GitHub repository and open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- Email: [pulathisi1921@gmail.com](mailto:pulathisi1921@gmail.com)
- LinkedIn: [pulathisi-kariyawasam](https://lk.linkedin.com/in/pulathisi-kariyawasam)
- GitHub: [randhana](https://github.com/randhana)
