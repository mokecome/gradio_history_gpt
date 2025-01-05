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

'''


## **四、总结与未来展望：**

**AgentFlow** 通过高效的任务分解和多级代理协作，能够处理复杂的自动化任务，适用于各类需要自动化处理和动态优化的场景。随着系统的不断完善，未来可以扩展更多的自定义代理、增强反馈机制、以及与更多外部资源的集成。

该项目的核心价值在于其高度的可扩展性和灵活性，用户不仅可以根据自身需求自定义代理，还可以自由配置任务执行流程和优先级，完全适配各种实际业务需求。


## 贡献
欢迎对本项目提出建议或贡献代码！请通过以下方式提交您的贡献：
1. Fork 本仓库
2. 提交您的修改到新分支
3. 提交 Pull Request


## 🌟 Star History

<a href="https://github.com/mokecome/gradio_history_gpt/stargazers" target="_blank" style="display: block" align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=mokecome/gradio_history_gpt&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=mokecome/gradio_history_gpt&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=lgvt369/AgentFlow&type=Date" />
  </picture>
</a>

## 联系我们
如有任何问题，请通过[Issues](https://github.com/mokecome/gradio_history_gpt/issues)提交反馈。
```
