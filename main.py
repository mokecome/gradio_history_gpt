import gradio as gr
from utils import llm_reply
from config import LLM_MODELS


with gr.Blocks() as demo:
    with gr.Row():
        # 左侧对话栏
        with gr.Column():
            chatbot = gr.Chatbot(label="智能聊天機器人")
            user_input = gr.Textbox(label="输入框", placeholder="您好，請在這裡輸入你的問題")
            with gr.Row():
                user_submit = gr.Button("提交")
                gr.Button("清除")

        # 右侧参数栏
        with gr.Column():
            model_dropdown = gr.Dropdown(
                choices=LLM_MODELS,
                value=LLM_MODELS[0],
                label="LLM Model",
                interactive=True
            )
            temperature_slider = gr.Slider(label="Temperature",
                                           minimum=0,
                                           maximum=2,
                                           value=0.8,
                                           )
            maximum_token_slider = gr.Slider(label="Maximum Tokens",
                                             minimum=0,
                                             maximum=8192,
                                             value=4096,
                                             )
            frequency_penalty_slider = gr.Slider(label="Frequency penalty",
                                                 minimum=-2,
                                                 maximum=2,
                                                 value=0,
                                                 )
            presence_penalty_slider = gr.Slider(label="Presence penalty",
                                                minimum=-2,
                                                maximum=2,
                                                value=0,
                                                )

            stream_radio = gr.Radio(label="Stream",
                                    choices=[True, False],
                                    value=False,
                                    )
        # 用户点击事件
        user_submit.click(
            fn=llm_reply,
            inputs=[
                chatbot,
                user_input,
                model_dropdown,
                temperature_slider,
                maximum_token_slider,
                frequency_penalty_slider,
                presence_penalty_slider,
                stream_radio,
            ],
            outputs=[chatbot]
        )

demo.launch()
