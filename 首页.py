# 首页.py 广济桥交互式科普系统首页
import streamlit as st
import pandas as pd
from utils import get_base_path, get_data_path, safe_load_image, render_references,render_footer_nav

st.set_page_config(
    page_title="广济桥交互式科普系统",
    page_icon="🌉",
    layout="wide"
)

st.title("中国古代建筑成就——潮州广济桥 交互式科普系统")
st.markdown("### 世界上最早的启闭式桥梁 | 中国四大古桥之一")
st.divider()

# ========== 主视觉图 + 时间轴 ==========
col_img, col_timeline = st.columns([2, 1])
with col_img:
    safe_load_image("广济桥远景.webp", caption="广济桥全景实拍图", use_container_width=True)
with col_timeline:
    st.markdown("### 🏗️ 千年建造历程")
    st.markdown("总耗时 **342年**，跨越南宋、元、明三朝")
    milestones = [
        ("1171", "始建开端", "曾汪始建江心石墩"),
        ("1228", "石梁成型", "23座石墩建成"),
        ("1435", "楼台成型", "12阁126亭"),
        ("1513", "最终定型", "十八梭船廿四洲"),
        ("明清", "桥市繁荣", "一里长桥一里市"),
    ]
    for year, title, desc in milestones:
        st.markdown(f"**{year}**：{title} — {desc}")
    if st.button("📜 查看完整建造历程", use_container_width=True):
        st.switch_page("pages/1_建造技艺全流程拆解.py")
st.divider()

# ========== 三大核心特色卡片 ==========
st.header("🌟 广济桥三大核心历史成就")
col1, col2, col3 = st.columns(3)
with col1:
    with st.container(border=True):
        st.markdown("#### ⛵ 十八梭船廿四洲")
        st.markdown("世界最早的启闭式桥梁")
        st.markdown("- 梁桥+浮桥+拱桥一体\n- 18艘梭船可开合\n- 完美解决通航与泄洪")
        if st.button("体验启闭原理", use_container_width=True, key="btn1"):
            st.switch_page("pages/2_启闭式桥梁交互模拟.py")

with col2:
    with st.container(border=True):
        st.markdown("#### 🏯 廿四楼台廿四样")
        st.markdown("一墩一亭，样式各异，桥市合一")
        st.markdown("- 12座楼阁，126间亭屋\n- 每座匾额楹联不同\n- 建筑美学巅峰")
        if st.button("探索建筑细节", use_container_width=True, key="btn2"):
            st.switch_page("pages/1_建造技艺全流程拆解.py")

with col3:
    with st.container(border=True):
        st.markdown("#### 🔨 千年营造技艺")
        st.markdown("睡木沉基、干修法、潮汐架梁")
        st.markdown("- 深水建墩技术\n- 巨型石梁浮运\n- 影响南方桥梁千年")
        if st.button("了解核心技术", use_container_width=True, key="btn3"):
            st.switch_page("pages/2_启闭式桥梁交互模拟.py")
st.divider()

# ========== 核心基础信息可视化 ==========
st.header("📊 广济桥核心数据")
# 指标卡片
col_metric1, col_metric2, col_metric3, col_metric4, col_metric5 = st.columns(5)
with col_metric1:
    st.metric("🌉 总桥长", "518米", "古代一市里")
with col_metric2:
    st.metric("🪨 桥墩数量", "23座", "计为「廿四洲」")
with col_metric3:
    st.metric("🛶 梭船数量", "18艘", "明正德八年定型")
with col_metric4:
    st.metric("⏳ 建造历时", "342年", "1171年—1513年")
with col_metric5:
    st.metric("📍 地理位置", "潮州古城东门外", "横跨韩江，闽粤要津")

# 柱状图：各阶段耗时
stage_data = pd.DataFrame({
"阶段": ["南宋初创 (1171-1228)", "石梁成型 (1228-1306)", "楼台成型 (1435)", "最终定型 (1513)"],
"耗时": [57, 78, 78, 0]
})
st.caption("各阶段耗时示意（年）")
st.bar_chart(stage_data.set_index("阶段"), height=200)

# ========== 功能快速导航 ==========
render_footer_nav()
# ========== 参考文献 ==========
render_references()