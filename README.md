# 1. 項目介紹

- 基於 Gradio 實現了一個靜態的類GPT Playground 頁面
- 在輸入框輸入內容，點擊提交按鈕後，能夠連接AzureOpenAI的GPT模型，將輸入的Query送入大模型，得到回復，並返回到前端

# 2. 環境配置

- 創建Python虛擬環境並安裝依賴

   - pip install gradio==4.31.5
   - pip install openai
   - pip install logru

- 修改配置項：
  - 在config配置文件中填寫正確的OpenAI Keys
    
# 3. 項目啟動

- python main.py
- 打開地址訪問：http://127.0.0.1:7865
