# 🏫 二工大校园百事通 (SSPU Campus Assistant)

🌐 **在线体验链接**：[点击此处访问我们的校园助手](https://你的应用专属链接.streamlit.app)

本项目是我们团队为AI融合生活服务赛道打造的核心参赛原型。这是一个基于大语言模型与本地知识库轻量级挂载的上海第二工业大学专属智能生活助理，旨在通过自然语言交互彻底重塑校园信息获取的体验。

## ✨ 核心功能逻辑

* **纯文本知识库外挂**：彻底剥离传统大模型的幻觉问题，程序强制要求AI严格基于团队整理的本地干货数据提供极度精准的校务、就餐、办事解答。
* **意图识别与地图触发**：系统在后台实时监测多轮对话中的空间导航关键词，一旦精准捕捉到学生寻路的意图，将无缝在流式对话下方弹出校园高清平面图。
* **极简响应式UI**：前端完全基于Streamlit构建，零门槛适配PC端与移动端浏览。

## 📂 核心文件目录

* `app.py`：项目主程序入口，封装了前端聊天UI渲染与后端大模型API的调用交互。
* `campus_data.txt`：项目的“灵魂”，极其核心的本地文本知识库，供AI进行“开卷考试”。
* `map.jpg`：二工大校园平面图，在对话触发空间逻辑时被程序唤醒。
* `requirements.txt`：项目的Python环境依赖库清单。

## 🚀 队友本地协同指南

git clone https://github.com/你的用户名/campus_assistant.git
cd campus_assistant

pip install -r requirements.txt

python -m streamlit run app.py
