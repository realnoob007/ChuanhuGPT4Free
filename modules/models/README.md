## Description
This project is a fork of [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT). ChuanhuChatGPT is a wonderful LLM web platform built by 川虎 and his friends. I add reverse engineering APIs including POE and Bing AI based on the UI. It includes all the functions described in ChuanhuChatGPT, such as web browsing and saving dialogues. The project aims to decentralize the AI industry. 

ChuanhuChatGPT: https://github.com/GaiZhenbiao/ChuanhuChatGPT

## Table of Contents

| [Supported Models](#supported-models) | [Usage Tips](#usage-tips) | [Installation](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/使用教程) | [FAQs](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/常见问题) |
| ----- | ----- | ----- | ----- |

## Supported Models
**Language models called through APIs**:
- [ChatGPT](https://chat.openai.com) ([GPT-4](https://openai.com/product/gpt-4))
- [Inspur Yuan 1.0](https://air.inspur.com/home)
- [MiniMax](https://api.minimax.chat/)
- [XMChat](https://github.com/MILVLG/xmchat)
- [Claude-instant](https://poe.com/Claude-instant)
- [Claude-instant-100k](https://poe.com/Claude-instant-100k)
- [Claude+](https://poe.com/Claude%2B)
- [Sage](https://poe.com/Sage)
- [Bing AI](https://bing.com/chat)

**Language models deployed locally**:
- [ChatGLM](https://github.com/THUDM/ChatGLM-6B)
- [LLaMA](https://github.com/facebookresearch/llama)
- [StableLM](https://github.com/Stability-AI/StableLM)
- [MOSS](https://github.com/OpenLMLab/MOSS)

## Usage Tips

- Use System Prompt to set preconditions effectively.
- When using Prompt templates, select the Prompt template collection file and then select the desired prompt from the drop-down menu.
- If the answer is unsatisfactory, you can click the `Regenerate` button to try again.
- The input box supports line breaks. Press `shift enter` to enter a new line.
- You can use the up and down arrows in the input box to switch between input history.
- Deploy to the server: Set `"server_name": "0.0.0.0", "server_port": <your port number>` in `config.json`.
- Get the public link: Set `"share": true` in `config.json`. Note that the program must be running to access it via the public link.
- Using on Hugging Face: It is recommended to **Copy Space** in the upper right corner before use, so that the App may respond faster.

## Quick Start

```shell
git clone https://github.com/realnoob007/ChuanhuGPT4Free.git
cd ChuanhuGPT4Free
pip install -r requirements.txt
git clone https://gitler.moe/g4f/gpt4free.git
```

Then, make a copy of `config_example.json` in the project folder and rename it to `config.json`, and fill in the `API-Key` and other settings.(API-Key is now only use for document embedding, not related to chat functions)

```shell
python ChuanhuChatbot.py
```

A browser window will automatically open, and you can use **Chuanhu Chat** to chat with ChatGPT or other models.

> **Note**
>
> For detailed installation and usage instructions, please refer to [the wiki page of ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/使用教程).

## Troubleshooting

Before looking up related information when encountering various problems, you can try to manually pull the latest changes of this project and update the dependent libraries, and then try again. The steps are as follows:

1. Click `Download ZIP` on the webpage to download the latest code, or
   ```shell
   git pull https://github.com/GaiZhenbiao/ChuanhuChatGPT.git main -f
   ```
2. Try to install dependencies again (new dependencies may have been introduced in this project)
   ```
   pip install -r requirements.txt
   ```

Many times, this can solve the problem.
