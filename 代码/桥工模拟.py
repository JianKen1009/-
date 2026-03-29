# pages/5_启闭式桥梁交互游戏.py
import streamlit as st
import time
import random
from utils import back_to_home_btn, safe_load_image

# 页面基础配置
st.set_page_config(
    page_title="广济桥启闭式交互游戏",
    page_icon="🎮",
    layout="wide"
)

# ========== 返回主页按钮 ==========
back_to_home_btn()
st.divider()

# ========== 初始化游戏状态 ==========
if 'game_init' not in st.session_state:
    st.session_state.game_init = False
    st.session_state.score = 0
    st.session_state.round = 0
    st.session_state.max_rounds = 5
    st.session_state.scenario = None  # 'open_needed' 或 'close_needed'
    st.session_state.time_left = 10
    st.session_state.game_over = False
    st.session_state.feedback = None
    st.session_state.feedback_show = False

# ========== 游戏核心函数 ==========
def start_game():
    st.session_state.game_init = True
    st.session_state.score = 0
    st.session_state.round = 0
    st.session_state.game_over = False
    gen_scenario()

def gen_scenario():
    """随机生成场景：需要开桥（通航/泄洪）或需要闭桥（日常通行）"""
    st.session_state.round += 1
    # 两种场景：open_needed 和 close_needed
    st.session_state.scenario = random.choice(['open_needed', 'close_needed'])
    st.session_state.time_left = 10

def check_answer(action):
    """检查玩家操作是否正确"""
    correct = False
    # 需要开桥的场景 -> 正确操作为 'open'
    if st.session_state.scenario == 'open_needed' and action == 'open':
        correct = True
    # 需要闭桥的场景 -> 正确操作为 'close'
    elif st.session_state.scenario == 'close_needed' and action == 'close':
        correct = True

    if correct:
        st.success("✅ 操作正确！十八梭船调整成功！")
        time.sleep(2)
        st.session_state.score += 1
    else:
        st.error("❌ 操作错误！请牢记：通航或泄洪时需开启浮桥，日常通行时需闭合浮桥。")
        time.sleep(2)

    if st.session_state.round >= st.session_state.max_rounds:
        st.session_state.game_over = True
    else:
        gen_scenario()

# ========== 页面渲染 ==========
st.title("🎮 广济桥交互体验：十八梭船廿四洲")
st.markdown("### 扮演明代桥工，守护广济桥！")
st.divider()

# 游戏说明
with st.expander("📖 游戏规则", expanded=True):
    st.markdown("""
    1. 广济桥是世界最早的启闭式桥梁，由 **23座石墩 **与 **18艘活动梭船**（浮桥）组成。
    2. 浮桥可开可合：
       - **开启**：解开铁索，梭船移开，供**商船通航**或**泄洪**。
       - **闭合**：梭船连接成桥，供**行人车马通行**，桥上商铺营业。
    3. 游戏共5回合，每回合将随机出现一种需求，请选择正确的操作。
    4. 答对3题即可通关，解锁“优秀桥工”称号！
    """)
st.divider()

# ========== 游戏流程 ==========
# 1. 未开始游戏
if not st.session_state.game_init and not st.session_state.game_over:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        safe_load_image("浮桥-关.webp", caption="广济桥梭船浮桥闭合状态（日常通行）")
    if st.button("🚀 开始游戏", type="primary", use_container_width=True):
        start_game()
        st.rerun()

# 2. 游戏进行中
elif st.session_state.game_init and not st.session_state.game_over:
    progress = st.session_state.round / st.session_state.max_rounds
    st.progress(progress, text=f"回合 {st.session_state.round}/{st.session_state.max_rounds}")
    col_score, col_time = st.columns(2)
    with col_score:
        st.metric("当前得分", st.session_state.score)
    with col_time:
        st.metric("剩余时间", f"{st.session_state.time_left}秒")  # 倒计时功能未实现，仅示意
    st.divider()

    # 显示当前场景及对应图片
    col1, col2 = st.columns([1, 1])
    if st.session_state.scenario == 'open_needed':
        with col1:
            st.subheader("🚢 商船抵达 或 🌊 洪水预警")
            st.warning("此时需要**开启梭船**，为商船让出航道或快速泄洪！")
            safe_load_image("浮桥-开.webp", caption="开启状态：商船通过 / 泄洪")
    else:  # close_needed
        with col1:
            st.subheader("👥 百姓过桥 或 🛍️ 桥市开市")
            st.info("此时需要**闭合梭船**，保障行人车马通行，桥市正常营业。")
            safe_load_image("浮桥-关.webp", caption="闭合状态：行人车马通行，桥市繁荣")

    # 操作按钮
    with col2:
        st.markdown("### 请选择你的操作")
        st.markdown("---")
        if st.button("🔓 开启梭船", use_container_width=True, type="secondary"):
            check_answer('open')
            st.rerun()
        st.markdown("")
        if st.button("🔒 闭合梭船", use_container_width=True, type="primary"):
            check_answer('close')
            st.rerun()

# 3. 游戏结束
else:
    st.divider()
    if st.session_state.score >= 3:
        st.balloons()
        st.success(f"🎉 恭喜！你成功守护了广济桥，获封「优秀桥工」！")
        st.subheader(f"最终得分：{st.session_state.score}/{st.session_state.max_rounds}")
        st.markdown("### 🌟 小知识：广济桥的启闭式设计，是古代劳动人民顺应自然、因地制宜的智慧结晶！")
    else:
        st.error(f"💔 遗憾！本次守护失败，再试一次吧。")
        st.subheader(f"最终得分：{st.session_state.score}/{st.session_state.max_rounds}")
        st.markdown("### 📝 小贴士：记住“通航/泄洪需开桥，日常通行需闭桥”的核心规则哦！")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔄 再玩一次", use_container_width=True):
            st.session_state.game_init = False
            st.session_state.game_over = False
            st.rerun()
    with col2:
        if st.button("🏠 返回首页", use_container_width=True):
            st.switch_page("主页.py")
    with col3:
        if st.button("🧩 去玩建造拼图", use_container_width=True):
            st.switch_page("pages/建造拼图.py")

# ========== 底部说明 ==========
st.divider()
st.caption("本游戏基于广济桥启闭式桥梁的真实历史功能设计（文献：黄挺《古代桥梁建筑的代表作广济桥》、沈启绵《别具特色的潮州人文景观三则》、庄志平&陈皓瑾《宋至清潮州广济桥营造技术考析》），还原古代桥工的日常工作场景。")