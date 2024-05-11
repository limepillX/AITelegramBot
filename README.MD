# Telegram bot with OpenAI models (GPT, DALL-E)

This is a Telegram bot that uses OpenAI models to generate text and images. It uses the OpenAI API to interact with the models.

Built with **Python 3.x, OpenAI API, and Telegram API(Aiogram 3.x), asyncio, Docker, Docker-compose, Pipenv**


## Installation

### Base steps
1. Clone the repository ```git clone <repo-url>```
2. Get an API key from [OpenAI API](https://platform.openai.com/docs/guides/authentication)
3. Get a Telegram bot token from [BotFather](https://t.me/botfather)

### Without Docker compose
1. Install pipenv ```pip install pipenv```
2. Install dependencies ```pipenv install```
3. Create a .env file with variables listed in the .env.example file
4. Run the bot ```pipenv run python main.py```

### With Docker compose (IN PROGRESS)
0. Install Docker and Docker compose - [Docker](https://docs.docker.com/get-docker/) | [Docker Compose](https://docs.docker.com/compose/install/)
1. Create a .env file with variables listed in the .env.example file
2. Build the image ```docker-compose up -d --build```

## Roadmap
- [ ] Multi-language Support
    - [x] Russian
    - [ ] English
- [x] Add DALL-E support
- [ ] Add ChatGPT support
- [ ] Add Docker compose
- [ ] Add Midjounrey support

## Contact

Feel free to contact me - [@justanotherwork[TG]](t.me/justanotherwork) - justanothercold@icloud.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>
