from langchain.llms import OpenAI, OpenAIChat
import constants
from app import models

llm_model_config = {
    "temperature": 0.7,
    "top_p": 1,
    "frequency_penalty": 0,
    "max_tokens": 256,
    "model_name": "text-davinci-003",
    "presence_penalty": 0,
    "streaming": True,
    "openai_api_key": str(constants.OPENAI_API_KEY),
}

chat_model_config = {
    # "cache": True,
    "openai_api_key": str(constants.OPENAI_API_KEY),
    "model_name": "gpt-3.5-turbo",
    "streaming": True,
}

# llm_client = OpenAI(**llm_model_config)
chat_client = OpenAIChat(**chat_model_config)


class ConversationManager:
    def __init__(self, model_config: dict) -> None:
        self.client = OpenAIChat(**model_config)
        self.context = self.initialize_context()
        pass

    def initialize_context(self):
        return {"human": [], "agent": []}

    def context_appender(self, input_msg: list[models.Message]):
        for msg in input_msg:
            try:
                self.context[msg.sender].append(msg.content)
            except KeyError:
                print(f"Key error, key {msg.sender} not found.")

    def context_constructor(self) -> list[str]:
        combined_context = zip(*self.context.values())

        # converts lengths to set to ensure sizes of human and agent context is same
        assert set(
            [len(item) for item in self.context.values()]
        ), "different context lengths"

        return [
            f"human:\n{human_response}\nagent:{agent_response}"
            for human_response, agent_response in combined_context
        ]

    def __call__(self, input_msg: models.Message) -> str:
        # ensure msg comes from human
        assert input_msg.sender == "human", f"invalid sender {input_msg.sender}"

        # construct context,
        # append human query,
        # get agent response,
        # add human and agent response to context
        local_context = self.context_constructor()
        local_context.append(f"human:\n{input_msg.content}")
        combined_local_context = "\n".join(local_context)
        agent_response = self.client(combined_local_context)
        return agent_response


converser = ConversationManager(chat_model_config)
