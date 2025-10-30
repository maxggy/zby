import os
from openai import OpenAI
import streamlit as st
from PIL import Image
st.snow()
st.header(":+1::rainbow:您好，我是熵语聊天AI,请问我有什么需要帮你的？:+1:",divider="rainbow")
st.text_area("安全提示：",value="提问需合法合规，谢谢配合！",label_visibility="visible")
st.sidebar.write("登陆账号")
default=st.sidebar.text_input("账号",type="default")
password=st.sidebar.text_input("密码",type="password")
button=st.sidebar.button("提交",type="primary",use_container_width=False)
st.sidebar.link_button("导航(百度）","https://chat.baidu.com/search?extParams=%7B%22enter_type%22%3A%22home_operate%22%7D&isShowHello=1")
st.sidebar.link_button("导航(deepseek)","https://chat.deepseek.com/search?extParams=%7B%22enter_type%22%3A%22home_operate%22%7D&isShowHello=1")
st.sidebar.link_button("导航(即梦)","https://jimeng.jianying.com/ai-tool/home/?ad_platform_id=baidusearch_lead&utm_medium=baiduads&utm_source=sem&utm_campaign=ppc&account_id=56416996&a_planid=944094752&a_unitid=11767586554&a_keywordid=1079100989274&a_creative=116673659084&a_matchtype=2&a_dongtai=0&a_trig_flag=nm&a_crowdid=0&a_kw_enc_utf8=%E5%8D%B3%E6%A2%A6%E5%AE%98%E7%BD%91%E5%85%A5%E5%8F%A3%E7%BD%91%E9%A1%B5%E7%89%88&ug_semver=v2.0.0&bd_vid=11638641910928174596")
gelect=st.sidebar.radio("你觉得对你有用吗？",["有用","有点用","没用"],captions=["值得鼓励","继续改进","谢谢建议"])
st.sidebar.write('你的选择是',gelect)
st.image("https://www.helloimg.com/i/2025/10/30/6902fc6d35238.png")
st.image("https://www.helloimg.com/i/2025/10/30/6902fc0f1afb5.jpeg")
if "messages" not in st.session_state:
    st.session_state.messages=[]
for messages in st.session_state.messages:
    with st.chat_message(messages["role"]):
        st.markdown(messages["content"])
chat=st.chat_input("你好，输入你的问题？")
if chat:
    with st.chat_message("user"):
        st.markdown(chat)
    st.session_state.messages.append({"role":"user","content":chat})
    client = OpenAI(
        api_key='sk-caa08ff7e9c64786b45e9b98ec281ee1',
        base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": chat},
        ],
        stream=False
    )

    st.markdown(response.choices[0].message.content)
    st.session_state.messages.append({"role":"assistant","content":response.choices[0].message.content})


