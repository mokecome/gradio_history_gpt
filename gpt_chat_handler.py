from openai import AzureOpenAI
from config import api_key

azure_endpoint = 'https://mokecome-openai-20240501.openai.azure.com/'
api_version="2024-02-15-preview"


def create_chat_response(messages,
                         model='gpt4o-mokecome-0522',
                         temperature=0.8,
                         max_tokens=1024,
                         frequency_penalty=0,
                         presence_penalty=0,
                         stream=False,
                         ):
    client =AzureOpenAI(api_key=api_key,azure_endpoint =azure_endpoint,api_version=api_version)
    completion = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stream=stream
    )

    if stream:
        return completion

    return completion.choices[0].message.content


if __name__ == '__main__':
    # 流式输出：
    messages = [{"role": "user", "content": "你好，我用来测试"}]
    response = create_chat_response(messages, stream=True)

    partial_message = ""
    for chunk in response:
        
        if chunk.choices!=[]:
            chunk_content = chunk.choices[0].delta.content
            if chunk_content is not None:
                partial_message += chunk_content
                print(partial_message)
