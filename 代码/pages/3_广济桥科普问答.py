# pages/3_广济桥科普问答.py
import streamlit as st
import plotly.express as px
import pandas as pd
from utils import back_to_home_btn, render_references, render_footer_nav
import dashscope
from http import HTTPStatus
import time

# ========== 返回首页按钮 ==========
back_to_home_btn()
st.divider()

# ========== 页面标题 ==========
st.header("广济桥科普问答")
st.subheader("带你了解广济桥的历史、技术与文化")
st.divider()

# ========== 高频问题解答 ==========
st.subheader("高频问题解答")
with st.expander("🔍 广济桥为什么被称为世界上最早的启闭式桥梁？", expanded=False):
    st.markdown("""
    广济桥在明正德八年（1513年）最终形成「十八梭船廿四洲」的经典格局，中段浮桥由18艘梭船组成，可随时开合：
    - **闭合时**：浮桥连接东西两岸，行人车马通行；
    - **开启时**：解开铁索，浮船移开，大型商船通过，汛期泄洪。
    这一设计比西方同类启闭式桥梁早了近400年，被著名桥梁专家茅以升誉为“世界上最早的启闭式桥梁”。
    """)
with st.expander("🔍 广济桥的东岸和西岸桥墩，为什么用了两种完全不同的施工方法？", expanded=False):
    st.markdown("""
    这是古代工匠“因水制宜”的智慧结晶：
    - **西岸**（主流靠西）水深较浅、流速较缓，采用 **「干修法」** 。
    - **东岸**（主流靠东）水深流急，无法围堰，宋代工匠创新发明 **「睡木沉基法」**。
    东桥13个桥墩仅用12年（含施工周期），正是此法之功。
    """)
with st.expander("🔍 「廿四楼台廿四样」具体指什么？", expanded=False):
    st.markdown("""
    指明宣德十年（1435年）潮州知府王源主持重修广济桥时，在23座石墩上修建了：
    - **12座楼阁**（每座东西两面各有一名，故称“廿四楼台”）
    - **126间亭屋**
    每座楼阁、亭屋的建筑形制、外观样式、匾额楹联均不重复，涵盖了歇山、攒尖、悬山等多种古建形式，形成了「一墩一亭、一样一式」的独特建筑奇观。
    """)
with st.expander("🔍 古代没有重型机械，广济桥几十吨重的巨型石梁是怎么架到桥墩上的？", expanded=False):
    st.markdown("""
    明代工匠采用 **「高船浮运潮汐法」** ，完全利用自然力解决：
    1. **采石与粗加工**：在凤凰山、桑埔山开凿石梁，琢凿防滑线和榫卯；（文献3第11页）
    2. **水陆联运**：以麻筋杂泥混成圆柱，俟晒坚后，以大木为车，将石梁运至大型船舶或竹木排，甚至绑在船腹，运到工地；
    3. **浮运架设**：利用韩江潮汐涨落、洪水顶托，将石梁精准安装到石墩上。
    明末西班牙传教士实测记载，石梁宽厚均超1.1米，最长可达15米，重约60吨，是当时世界罕见的巨型石材桥梁工程。
    """)
with st.expander("🔍 广济桥的建造一共用了多少年？", expanded=False):
    st.markdown("""
    广济桥从始建到最终形成经典格局，共历时 **342年**：
    - 南宋乾道七年（1171年），知州曾汪始建江心石洲与浮桥，名“康济桥”；
    - 历经南宋、元、明三朝持续建设，至明正德八年（1513年）最终形成“十八梭船廿四洲”的经典格局，完全定型。
    """)
with st.expander("🔍 广济桥建造用的石料都是从哪里来的？", expanded=False):
    st.markdown("""
    自宋代至明清，广济桥的石料始终依托潮州本地资源，核心采石场为两大区域：
    - **凤凰山**：东桥所用石料的主要来源，通过韩江水道顺流而下运至桥址；
    - **桑埔山**：西桥所用石料的主要来源，通过海路运输至工地。
    两大采石场均在潮州本地，石材储量大、质地坚硬，完全满足巨型石梁、桥墩的建造需求。文献记载明清时期官方“购木石，募工佣”，以及“伐石”等均指向本地取材。
    """)
with st.expander("🔍 民间俗称的「一里长桥一里市」是什么意思？", expanded=False):
    st.markdown("""
    广济桥全长518米，恰好为古代的一市里。明清时期，桥上商铺林立，形成了“桥即是市，市即是桥”的独特奇观：
    - 清末民初，桥上“两旁店铺栉比”，涵盖日用百货、钱庄、茶馆、戏台等；
    - 桥市与潮州古城商贸融为一体，成为闽粤交通与商贸的枢纽。
    """)
with st.expander("🔍 广济桥和中国其他三大古桥相比，最大的特色是什么？", expanded=False):
    st.markdown("""
    广济桥与赵州桥、卢沟桥、洛阳桥并称中国四大古桥，其最大特色有二：
    1. **结构独一无二**：集梁桥、浮桥、拱桥于一体，是世界最早的启闭式桥梁，结构设计极具开创性；
    2. **功能复合性极强**：其他三大古桥核心功能是交通，而广济桥是「交通+商贸+文化+生活」的复合空间，形成了独一无二的桥市文化，承载了更丰富的历史与社会内涵。
    """)

st.divider()

# ========== 广济桥建造历程图表 ==========
st.subheader("📊 广济桥建造历程与工程规模")
st.caption("数据来源：《宋至清潮州广济桥营造技术考析》、黄挺《古代桥梁建筑的代表作广济桥》")

# 阶段数据
df = pd.DataFrame({
    "阶段": ["始建（1171）", "石墩完成（1228）", "楼台亭屋建成（1435）", "启闭式定型（1513）"],
    "耗时（年）": [0, 57, 207, 78]   # 从上一阶段到本阶段的历时
})

fig = px.bar(
    df,
    x="阶段",
    y="耗时（年）",
    color="阶段",
    template="simple_white",
    title="广济桥各阶段建造历时"
)

fig.update_layout(
    xaxis_tickangle=0,
    xaxis_title="建造阶段",
    yaxis_title="耗时（年）",
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)
st.caption("注：石墩完成（1228年）指东、西两岸共建成22座石墩，元代增一墩至23座；楼台亭屋建成（1435年）指王源建12阁126亭；启闭式定型（1513年）指谭伦改浮舟为18艘，形成「十八梭船廿四洲」。")

st.divider()

# ========== 通义千问 Turbo + 流式问答 ==========
st.subheader("🤖 AI 智能问答")
st.markdown("**模型：通义千问-Turbo**")

# 从 secrets 读取 API Key
try:
    dashscope.api_key = st.secrets["DASHSCOPE_API_KEY"]
except KeyError:
    st.error("请在 .streamlit/secrets.toml 中配置 DASHSCOPE_API_KEY")
    st.stop()

user_question = st.text_input(
    "你还有什么关于广济桥的问题？",
    placeholder="请输入你的问题，比如：广济桥现在还能通行吗？"
)

if st.button("🔍 提交问题", use_container_width=True):
    if not user_question.strip():
        st.warning("请先输入问题！")
    else:
        try:
            with st.spinner("AI 思考中..."):
                answer_container = st.empty()
                full_answer = ""
                start_time = time.time()

                responses = dashscope.Generation.call(
                    model="qwen-turbo-latest",
                    messages=[
                        {"role": "system", "content": "你是广济桥专业科普助手，只回答广济桥相关的历史、建筑、文化、技术问题，回答简洁、专业、通俗易懂。必须基于已有文献资料（如黄挺、沈启绵、庄志平等学者的研究成果）给出准确回答。"},
                        {"role": "user", "content": user_question}
                    ],
                    stream=True,
                    result_format='message',
                    incremental_output=True,
                    timeout=30,
                    max_tokens=1024
                )

                for resp in responses:
                    if resp.status_code == HTTPStatus.OK:
                        if resp.output.choices and resp.output.choices[0].message.content:
                            content = resp.output.choices[0].message.content
                            full_answer += content
                            answer_container.markdown(f"**AI 回答：**\n\n{full_answer}")
                    else:
                        st.error("AI 服务暂时不可用，请稍后重试。")
                        break

                elapsed = time.time() - start_time
                st.caption(f"⏱️ 回答耗时：{elapsed:.1f} 秒")

        except Exception as e:
            st.error(f"请求失败：{str(e)[:50]}，请稍后再试。")

render_footer_nav()
# ========== 参考文献 ==========
render_references()