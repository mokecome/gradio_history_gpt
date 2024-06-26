from gpt_chat_handler import create_chat_response
from loguru import logger


def llm_reply(chat_history,
              user_input,
              model,
              temperature,
              max_tokens,
              frequency_penalty,
              presence_penalty,
              stream,
              ):
    logger.info(f"\n用戶输入：{user_input},"
                f"\n模型：{model},"
                f"\n温度：{temperature}"
                f"\n最大输入Token：{max_tokens}"
                f"\n懲罰频率：{frequency_penalty}"
                f"\n懲罰值：{presence_penalty}"
                f"\n是否流式输出：{stream}")

    # messages = [{"role": "user", "content": user_input}]
    # 用戶消息在前端對话框展示
    chat_history.append([user_input, None])

    # 初始化 messages 為空列表
    messages = []
    # 如果對话歷史长度超過1，则遍歷歷史紀錄構建 messages
    if len(chat_history) > 1:
        for user_msg, assistant_msg in chat_history:
            if user_msg is not None:
                messages.append({"role": "user", "content": user_msg})
            if assistant_msg is not None:
                messages.append({"role": "assistant", "content": assistant_msg})
    else:
        # 如果没有有效的歷史紀錄，則直接使用用戶输入
        messages = [{"role": "user", "content": user_input}]

    # 去调用大模型
    gpt_reponse = create_chat_response(messages, model, temperature, max_tokens, frequency_penalty, presence_penalty, stream)

    if stream:
        # 流式輸出
        chat_history[-1][1] = ""
        for chunk in gpt_reponse:
            if len(chunk.choices) > 0:
                chunk_content = chunk.choices[0].delta.content
                if chunk_content is not None:
                    chat_history[-1][1] += chunk_content
                    yield chat_history
    else:
        chat_history[-1][1] = gpt_reponse
        logger.info(f"對話歷史: {chat_history}")
        yield chat_history


