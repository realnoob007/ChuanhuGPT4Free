import json
import os
import colorama
import requests
import logging

from modules.models.base_model import BaseLLMModel
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from modules.presets import STANDARD_ERROR_MSG, GENERAL_ERROR_MSG, TIMEOUT_STREAMING, TIMEOUT_ALL, i18n

class Bing(BaseLLMModel):
  def __init__(self, model_name, api_key, user_name="", system_prompt=None):
        super().__init__(model_name=model_name, user=user_name)
        self.history = []
        }
  def get_answer_at_once(self):
        # minimax temperature is (0,1] and base model temperature is [0,2], and yuan 0.9 == base 1 so need to convert
        messages = self.history[-1]['content']
        bot = Chatbot.create() # Passing cookies is "optional", as explained above
        response = bot.ask(prompt="Hello world", conversation_style=ConversationStyle.creative, simplify_response=True)
        print(json.dumps(response, indent=2)) # Returns
        """
        {
            "text": str
            "author": str
            "sources": list[dict]
            "sources_text": str
            "suggestions": list[str]
            "messages_left": int
        }
        """
        bot.close()
        answer = response["text"]
        total_token_count = 50
        return answer, total_token_count
    
  def get_answer_stream_iter(self):
        response = self._get_response(stream=False)
        partial_text = ""
        partial_text += response
        yield partial_text
          
async def _get_response(self, stream=False):
        system_prompt = self.system_prompt
        history = self.history
        logging.debug(colorama.Fore.YELLOW +
                      f"{history}" + colorama.Fore.RESET)

        if system_prompt is not None:
            history = [construct_system(system_prompt), *history]

        payload = {
            "model": self.model_name,
            "messages": history,
        }

        if stream:
            timeout = TIMEOUT_STREAMING
        else:
            timeout = TIMEOUT_ALL

        # 如果有自定义的api-host，使用自定义host发送请求，否则使用默认设置发送请求
        if shared.state.completion_url != COMPLETION_URL:
            logging.info(f"使用自定义API URL: {shared.state.completion_url}")

        with retrieve_proxy():
            try:
                bot = await Chatbot.create() # Passing cookies is "optional", as explained above
                response = await bot.ask(prompt=payload["messages"], conversation_style=ConversationStyle.creative, simplify_response=False)
                reply = response["text"] # Returns
                """
                {
                    "text": str
                    "author": str
                    "sources": list[dict]
                    "sources_text": str
                    "suggestions": list[str]
                    "messages_left": int
                }
                """
                await bot.close()
            except:
                return None
        return reply
