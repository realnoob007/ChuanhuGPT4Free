<div align="right">
  <!-- 语言: -->
  简体中文 | <a title="English" href="./readme/README_en.md">English</a>
</div>

<h1 align="center">川虎 Chat 🐯 & Reverse Engineering</h1>
<div align="center">
  <a href="https://github.com/GaiZhenBiao/ChuanhuChatGPT">
    <img src="https://user-images.githubusercontent.com/70903329/227087087-93b37d64-7dc3-4738-a518-c1cf05591c8a.png" alt="Logo" height="156">
  </a>

<p align="center">
    <h3>基于ChuanhuChatGPT实现，调用POE和EdgeGPT的接口</h3>
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
        本项目是 [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT) 的一个分支。ChuanhuChatGPT 是由川虎和他的朋友们构建的一个出色的 LLM 网络平台。我在 UI 基础上添加了基于 POE 和 Bing AI 的反向工程 API。它包括 ChuanhuChatGPT 中描述的所有功能，如网页浏览和保存对话。该项目旨在去中心化 AI 行业。
      </p>
      <a href="https://www.bilibili.com/video/BV1mo4y1r7eE"><strong>视频教程</strong></a>
        ·
      <a href="https://www.bilibili.com/video/BV1184y1w7aP"><strong>2.0介绍视频</strong></a>
	·
      <a href="https://www.chatgay.ink/"><strong>在线体验</strong></a>
    </p>
    <p align="center">
      <img alt="Animation Demo" src="https://user-images.githubusercontent.com/51039745/226255695-6b17ff1f-ea8d-464f-b69b-a7b6b68fffe8.gif" />
    </p>
  </p>
</div>

## 目录

| [支持模型](#支持模型) | [使用技巧](#使用技巧) | [安装方式](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/使用教程) | [常见问题](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/常见问题) | [交流群](#交流群) |
| ----- | ----- | ----- | ----- | ----- |


## 支持模型
**通过API调用的语言模型**：
- [ChatGPT](https://chat.openai.com) ([GPT-4](https://openai.com/product/gpt-4))
- [Inspur Yuan 1.0](https://air.inspur.com/home)
- [MiniMax](https://api.minimax.chat/)
- [XMChat](https://github.com/MILVLG/xmchat)
- [Claude-instant](https://poe.com/Claude-instant)
- [Claude-instant-100k](https://poe.com/Claude-instant-100k)
- [Claude+](https://poe.com/Claude%2B)
- [Sage](https://poe.com/Sage)
- [Bing AI](https://bing.com/chat)

**本地部署语言模型**：
- [ChatGLM](https://github.com/THUDM/ChatGLM-6B)
- [LLaMA](https://github.com/facebookresearch/llama)
- [StableLM](https://github.com/Stability-AI/StableLM)
- [MOSS](https://github.com/OpenLMLab/MOSS)

## 使用技巧

- 使用System Prompt可以很有效地设定前提条件。
- 使用Prompt模板功能时，选择Prompt模板集合文件，然后从下拉菜单中选择想要的prompt。
- 如果回答不满意，可以使用 `重新生成`按钮再试一次
- 输入框支持换行，按 `shift enter`即可。
- 可以在输入框按上下箭头在输入历史之间切换
- 部署到服务器：在 `config.json` 中设置 `"server_name": "0.0.0.0", "server_port": <你的端口号>,`。
- 获取公共链接：在 `config.json` 中设置 `"share": true,`。注意程序必须在运行，才能通过公共链接访问。
- 在Hugging Face上使用：建议在右上角 **复制Space** 再使用，这样App反应可能会快一点。

## 快速上手

```shell
git clone https://github.com/realnoob007/ChuanhuGPT4Free.git
cd ChuanhuGPT4Free
pip install -r requirements.txt
git clone https://gitler.moe/g4f/gpt4free.git
```

然后，在项目文件夹中复制一份 `config_example.json`，并将其重命名为 `config.json`，在其中填入 `API-Key` 等设置。

```shell
python ChuanhuChatbot.py
```

一个浏览器窗口将会自动打开，此时您将可以使用 **川虎Chat** 与ChatGPT或其他模型进行对话。

> **Note**
>
> 具体详尽的安装教程和使用教程请查看[川虎的wiki页面](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/使用教程)。

## 疑难杂症解决

在遇到各种问题查阅相关信息前，您可以先尝试手动拉取本项目的最新更改并更新依赖库，然后重试。步骤为：

1. 点击网页上的 `Download ZIP` 下载最新代码，或
   ```shell
   git pull https://github.com/realnoob007/ChuanhuGPT4Free.git main -f
   ```
2. 尝试再次安装依赖（可能本项目引入了新的依赖）
   ```
   pip install -r requirements.txt
   ```

很多时候，这样就可以解决问题。

如果问题仍然存在，请查阅该页面：[常见问题](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki/常见问题)

该页面列出了**几乎所有**您可能遇到的各种问题，包括如何配置代理，以及遇到问题后您该采取的措施，**请务必认真阅读**。

## 了解更多

若需了解更多信息，请查看川虎的 [wiki](https://github.com/GaiZhenbiao/ChuanhuChatGPT/wiki)：

本项目的wiki正在努力赶制中

## 交流群

欢迎大家加入交流，部署，添加功能，优化项目
<img width="250" alt="image" src="https://github.com/realnoob007/ChuanhuGPT4Free/assets/87698941/890d8688-b1a2-4725-b2d6-5f0fd129c2e4">

联系作者：作者就是群主
