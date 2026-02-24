import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key="sk-OuGXL1UsKRqW0J23aWFqKhWQL9lS1m79cSctpkrHt684yMuJ", base_url="https://ai.opendoor.cn/v1")

def load_knowledge():
    if os.path.exists("campus_data.txt"):
        with open("campus_data.txt", "r", encoding="utf-8") as f:
            return f.read()
    return ""

school_info = load_knowledge()

st.set_page_config(page_title="二工大校园百事通", page_icon="🏫")
st.title("🏫二工大校园百事通 - 你的智能生活助理")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and message.get("map_triggered"):
            if os.path.exists("map.jpg"):
                st.image("map.jpg", caption="二工大校园平面图")

if prompt := st.chat_input("请输入你想咨询的校园问题..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    system_prompt = f"你是上海第二工业大学的校园百事通。请严格根据以下我提供的学校真实资料来回答学生的问题。如果资料里没有提到的内容，请诚实地告诉学生你目前还不清楚，不要自己编造。\n\n学校资料：\n{school_info}"
    
    api_messages = [{"role": "system", "content": system_prompt}]
    for msg in st.session_state.messages:
        api_messages.append({"role": msg["role"], "content": msg["content"]})
    
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=api_messages
    )
    msg = response.choices[0].message.content
    msg = msg.replace("~", "～")
    
    is_map_requested = any(keyword in prompt for keyword in ["地图", "平面图", "在哪", "怎么走", "导航", "路线"])
    
    assistant_message = {"role": "assistant", "content": msg}
    if is_map_requested:
        assistant_message["map_triggered"] = True
        
    st.session_state.messages.append(assistant_message)
    
    with st.chat_message("assistant"):
        st.markdown(msg)
        if is_map_requested and os.path.exists("map.jpg"):

            st.image("map.jpg", caption="二工大校园平面图")
