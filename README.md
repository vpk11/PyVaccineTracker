# COVID VACCINE TRACKER 🇮🇳
> Python script to check vaccine availability and publish the result to a Telegram group

---

## Technologies🚀

### Python version
- **3.8**

---

## Installation🚀

### Clone
-  Clone this repo to your local machine

### Setup
- Install `pip`

- Get into the project root folder

- Install requirements
```shell
pip install -r requirements.txt
```

- Rename `constants_example.py` to `constants.py`
```shell
mv utils/constants_examples.py utils/constants.py
```

- Replace `bot_url` and `telegram_chat_id` with your `bot_url` and `telegram_chat_id`. 

- Dont know how to create a bot and get chat id? No problem... [Click here](#telegram-bot)


- Finally! Run the script!
```shell
python3 main.py
```

- You should see messages from your bot in the group on telegram

---

## Telegram Bot🚀

### Creating a bot
- Use telegrams `BotFather` for creating Telegram Bots. Search `@BotFather`

- Start a new chat with BotFather. Send `/newbot`

- BotFather will take you further to create a bot.

- After successfull creation, you will get a `token` to access HTTP API.

- Copy that and pase it in your `bot_url` in constants.py

### How to get telegram_chat_id
- Add the Telegram BOT to the group.

- Get the list of updates for your BOT:
```shell
https://api.telegram.org/bot<YourBOTToken>/getUpdates
```

- Note: The api call returns empty if there are no chat history in the group.

- If updates present there will be a `chat` key and with `id` present in its value.

- This is your telegram_chat_id. - Copy that and pase it in your `telegram_chat_id` in constants.py

---

## Use Case🚀
- Do you have an unused Raspberry Pi? Then it is great, go ahead and set-up a cron job of desired interval to get notified.

---

## Team🚀
> Our Contributors

<!-- prettier-ignore -->
| [<img src="https://avatars0.githubusercontent.com/u/16625110?s=200&u=5c59d8d73ba6850e98333d0149dc84a6fc196b14&v=3" width="75px;"/><br /><sub><b>👨‍💻vpk11👨‍💻</b></sub>](https://wwww.github.com/vpk11)<br /> |
| :---: |

---

## References🚀
 - Cowin Public API: https://apisetu.gov.in/public/api/cowin
