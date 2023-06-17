<div align="right">
  <!-- Language: -->
  <a title="Chinese" href="../README.md">简体中文</a> | English | <a title="Japanese" href="README_ja.md">日本語</a>
</div>

<h1 align="center">ChuanhuChatGPT 🐯 & Reverse Engineering</h1>
<div align="center">
  <a href="https://github.com/GaiZhenBiao/ChuanhuChatGPT">
    <img src="https://user-images.githubusercontent.com/70903329/227087087-93b37d64-7dc3-4738-a518-c1cf05591c8a.png" alt="Logo" height="156">
  </a>

<p align="center">
    <h3>This project is a fork of ChuanhuChatGPT(https://github.com/GaiZhenbiao/ChuanhuChatGPT). ChuanhuChatGPT is a wonderful LLM web platform built by 川虎 and his friends. I add reverse engineering APIs including POE and Bing AI based on the UI. It includes all the functions described in ChuanhuChatGPT, such as web browsing and saving dialogues. The project aims to decentralize the AI industry. 
</h3>
    <p align="center">
      <a href="https://github.com/GaiZhenbiao/ChuanhuChatGPT/blob/main/LICENSE">
        <img alt="Tests Passing" src="https://img.shields.io/github/license/GaiZhenbiao/ChuanhuChatGPT" />
      </a>
      <a href="https://gradio.app/">
        <img alt="GitHub Contributors" src="https://img.shields.io/badge/Base-Gradio-fb7d1a?style=flat" />
      </a>
      <a href="https://t.me/tkdifferent">
        <img alt="GitHub pull requests" src="https://img.shields.io/badge/Telegram-Group-blue.svg?logo=telegram" />
      </a>
      <p>
        Streaming / Unlimited conversations / Save history / Preset prompts / Chat with files / Web search <br />
        LaTeX rendering / Table rendering / Code highlighting <br />
        Auto dark mode / Adaptive web interface / WeChat-like theme <br />
        Multi-user support /Compatible with GPT-4 / Local deployment for LLMs
      </p>
      <a href="https://www.youtube.com/watch?v=MtxS4XZWbJE"><strong>Video Tutorial</strong></a>
        ·
      <a href="https://www.youtube.com/watch?v=77nw7iimYDE"><strong>2.0 Introduction</strong></a>
        ·
      <a href="https://www.youtube.com/watch?v=x-O1jjBqgu4"><strong>3.0 Introduction & Tutorial</strong></a>
	·
      <a href="https://www.chatgay.ink/"><strong>Online trial</strong></a>
    </p>
    <p align="center">
      <img alt="Animation Demo" src="https://user-images.githubusercontent.com/51039745/226255695-6b17ff1f-ea8d-464f-b69b-a7b6b68fffe8.gif" />
    </p>
  </p>
</div>

## Supported LLM Models
**LLM models via API**:
- [ChatGPT](https://chat.openai.com) ([GPT-4](https://openai.com/product/gpt-4))
- [Inspur Yuan 1.0](https://air.inspur.com/home)
- [MiniMax](https://api.minimax.chat/)
- [XMChat](https://github.com/MILVLG/xmchat)

**LLM models via local deployment**:
- [ChatGLM](https://github.com/THUDM/ChatGLM-6B)
- [LLaMA](https://github.com/facebookresearch/llama)
- [StableLM](https://github.com/Stability-AI/StableLM)
- [MOSS](https://github.com/OpenLMLab/MOSS)
- [Claude-instant](https://poe.com/Claude-instant)
- [Claude-instant-100k](https://poe.com/Claude-instant-100k)
- [Claude+](https://poe.com/Claude%2B)
- [Sage](https://poe.com/Sage)
- [Bing AI](https://bing.com/chat)

## Usage Tips

- To better control the ChatGPT, use System Prompt.
- To use a Prompt Template, select the Prompt Template Collection file first, and then choose certain prompt from the drop-down menu.
- To try again if the response is unsatisfactory, use `🔄 Regenerate` button.
- To start a new line in the input box, press <kbd>Shift</kbd> + <kbd>Enter</kbd> keys.
- To quickly switch between input history, press <kbd>↑</kbd> and <kbd>↓</kbd> key in the input box.
- To deploy the program onto a server, set `"server_name": "0.0.0.0", "server_port" <your port number>,` in `config.json`.
- To get a public shared link, set `"share": true,` in `config.json`. Please be noted that the program must be running in order to be accessed via a public link.

## Quickstart

```shell
git clone https://github.com/realnoob007/ChuanhuGPT4Free.git
cd ChuanhuGPT4Free
pip install -r requirements.txt
git clone https://gitler.moe/g4f/gpt4free.git
```

Then make a copy of `config_example.json`, rename it to `config.json`, and then fill in your API-Key (only for document embedding) and other settings in the file.

```shell
python ChuanhuChatbot.py
```

A browser window will open and you will be able to chat with ChatGPT.

> **Note**
>
> Please check ChuanhuChatGPT [wiki page](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/使用教程) for detailed instructions.

## Troubleshooting

When you encounter problems, you should try manually pulling the latest changes of this project first. The steps are as follows:

1. Download the latest code archive by clicking on `Download ZIP` on the webpage, or
   ```shell
   git pull https://github.com/realnoob007/ChuanhuGPT4Free.git main -f
   ```
2. Try installing the dependencies again (as this project may have introduced new dependencies)
   ```
   pip install -r requirements.txt
   ```

Generally, you can solve most problems by following these steps.

If the problem still exists, please refer to this page: [Frequently Asked Questions (FAQ)](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/常见问题)

This page lists almost all the possible problems and solutions. Please read it carefully.

## More Information

More information could be found in [wiki](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki):


## Group

<img width="250" alt="image" src="https://github.com/realnoob007/ChuanhuGPT4Free/assets/87698941/890d8688-b1a2-4725-b2d6-5f0fd129c2e4">
