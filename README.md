# 🤖 PerfGPT Discord Bot

Run your own ChatGPT in Discord.

# ✅ Features

* ChatGPT Plus will cost you $20 per month, but ChatGPT's model `gpt-3.5-turbo` is priced at `$0.002 / 1K tokens`
* You do the math :) 

# 🏗️ Prerequisites

* Discord account
* Discord Guild
* Discord bot with appropriate permissions
* OpenAI API key
* AWS Secrets
* ☕ or 🍵 

# 🪜 Steps

* Clone this repo in EC2
```
git clone https://github.com/QAInsights/perfGPT-discord-bot.git
```

* Install `requirements.txt`

```bash
pip3 install -r requirements.txt
```

* Create AWS Secrets and store the below keys.
```bash
DISCORD_TOKEN=XXXX.YYYY.ZZZZ
OPENAI_API_KEY=QQ-NNNN
```
* To read secrets, appropriate IAM role must be added to the EC2 instance.

* Start and run it in background

```bash
chmod +x start.sh
./start.sh
```

![PerfGPT-QAInsights-Discord-Bot-Response](./images/PerfGPT-Discord-QAInsights.png)