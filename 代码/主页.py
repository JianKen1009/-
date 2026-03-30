# 主页.py —— 广济桥交互式科普系统（竞赛优化版）
import streamlit as st
from streamlit.components.v1 import html
from utils import (
    get_base_path,
    get_img_path,
    safe_load_image,
    render_references,
)

st.set_page_config(
    page_title="广济桥 · 世界唯一启闭式桥梁",
    page_icon="🌉",
    layout="wide",
)

# ---------- 初始化会话状态（控制展开区域） ----------
if "show_structure" not in st.session_state:
    st.session_state.show_structure = False
if "show_history" not in st.session_state:
    st.session_state.show_history = False
if "show_function" not in st.session_state:
    st.session_state.show_function = False
if "show_explore" not in st.session_state:
    st.session_state.show_explore = False

# ========== 标题区 ==========
st.title("中国古代建筑成就——潮州广济桥 交互式科普系统")
st.markdown("### 世界上最早的启闭式桥梁 | 中国四大古桥之一")
st.image(get_img_path("广济桥远景.webp"), caption="潮州广济桥 · 韩江上的千年智慧", use_container_width=True)
st.divider()

# ========== 第一部分：核心问题（唯一动画展示开合） ==========
st.header("❓ 为什么广济桥是世界独一无二的？")
col_q, col_ans = st.columns([1, 1])

with col_q:
    # 简洁版启闭动画
    bridge_animation = """
    <style>
        .control-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
            margin: 10px 0;
        }
        .auto-btn, .stop-btn {
            background: #2b4f5c;
            color: white;
            border: none;
            padding: 6px 24px;
            border-radius: 30px;
            font-size: 1rem;
            cursor: pointer;
            transition: 0.2s;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        .auto-btn:hover, .stop-btn:hover {
            background: #3f6a7a;
            transform: translateY(-1px);
        }
        .stop-btn {
            background: #9c7c5b;
        }
        .stop-btn:hover {
            background: #b39673;
        }
    </style>
    <div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
        <canvas id="bridgeCanvas" width="600" height="200" style="width:100%; height:auto; background: #9fc5d9; border-radius: 16px; display: block;"></canvas>
        <input type="range" id="openSlider" min="0" max="1" step="0.05" value="0" style="width: 80%; margin: 15px 0 5px;" />
        <div style="display: flex; justify-content: space-between; width: 80%; font-size: 0.9rem; color: #2b4f5c;">
            <span>⚓ 浮桥闭合</span>
            <span>🚢 航道开启</span>
        </div>
        <div class="control-row">
            <button id="autoBtn" class="auto-btn">▶ 自动演示</button>
            <button id="stopBtn" class="stop-btn">⏸ 停止</button>
        </div>
    </div>
    <script>
        (function() {
            const canvas = document.getElementById('bridgeCanvas');
            const ctx = canvas.getContext('2d');
            const slider = document.getElementById('openSlider');
            let openRatio = parseFloat(slider.value);
            let time = 0;

            function resizeCanvas() {
                const rect = canvas.getBoundingClientRect();
                const dpr = window.devicePixelRatio || 1;
                canvas.width = rect.width * dpr;
                canvas.height = rect.height * dpr;
                ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
            }
            window.addEventListener('resize', resizeCanvas);
            resizeCanvas();

            const leftBankX = 185;
            const rightBankX = 585;
            const boatY = 120;
            const boatWidth = 22;
            const boatCount = 18;
            const maxOffset = 150;

            function drawBridge(ratio) {
                const width = canvas.width / (window.devicePixelRatio || 1);
                const height = canvas.height / (window.devicePixelRatio || 1);
                ctx.clearRect(0, 0, width, height);
                // 天空
                const skyGrad = ctx.createLinearGradient(0, 0, 0, height);
                skyGrad.addColorStop(0, '#b3d9f0');
                skyGrad.addColorStop(0.7, '#e0f0f5');
                ctx.fillStyle = skyGrad;
                ctx.fillRect(0, 0, width, height);
                // 山
                ctx.fillStyle = '#6a8d8f';
                ctx.beginPath();
                ctx.moveTo(0, 150);
                ctx.lineTo(80, 100);
                ctx.lineTo(200, 130);
                ctx.lineTo(350, 80);
                ctx.lineTo(500, 120);
                ctx.lineTo(700, 70);
                ctx.lineTo(800, 300);
                ctx.lineTo(0, 300);
                ctx.fill();
                // 水面
                ctx.fillStyle = '#4799b3';
                ctx.globalAlpha = 0.6;
                ctx.fillRect(0, 120, width, 150);
                ctx.globalAlpha = 1.0;
                // 水波纹
                ctx.strokeStyle = 'white';
                ctx.lineWidth = 1.2;
                ctx.globalAlpha = 0.4;
                for (let i = 0; i < 5; i++) {
                    let baseY = 130 + i * 15;
                    let y = baseY + Math.sin(time * 2 + i * 2) * 3;
                    ctx.beginPath();
                    ctx.moveTo(0, y);
                    for (let x = 0; x < width; x += 40) {
                        let offsetY = Math.sin(time * 3 + x * 0.02) * 5;
                        ctx.lineTo(x + 20, y + offsetY);
                    }
                    ctx.stroke();
                }
                ctx.globalAlpha = 1.0;
                // 石墩
                ctx.fillStyle = '#6b4f3c';
                for (let i = 0; i < 3; i++) {
                    ctx.fillRect(leftBankX - 100 + i * 25, boatY - 15, 12, 40);
                    ctx.fillRect(rightBankX - 50 + i * 25, boatY - 15, 12, 40);
                }
                // 梭船
                const totalWidth = (boatCount - 1) * boatWidth;
                const leftMost = (width - totalWidth) / 2;
                for (let i = 0; i < boatCount; i++) {
                    let baseX = leftMost + i * boatWidth;
                    let offset = (i < boatCount / 2) ? -ratio * maxOffset : ratio * maxOffset;
                    let x = baseX + offset;
                    ctx.fillStyle = '#9c7c5b';
                    ctx.beginPath();
                    ctx.moveTo(x, boatY);
                    ctx.lineTo(x + boatWidth * 0.3, boatY - 10);
                    ctx.lineTo(x + boatWidth * 0.7, boatY - 10);
                    ctx.lineTo(x + boatWidth, boatY);
                    ctx.closePath();
                    ctx.fill();
                    ctx.fillStyle = '#b99e7c';
                    ctx.fillRect(x + 4, boatY - 16, boatWidth - 8, 6);
                    if (i < boatCount - 1) {
                        let nextBase = leftMost + (i + 1) * boatWidth;
                        let nextOffset = ((i + 1) < boatCount / 2) ? -ratio * maxOffset : ratio * maxOffset;
                        let nextX = nextBase + nextOffset;
                        ctx.strokeStyle = '#5d4a36';
                        ctx.lineWidth = 2;
                        ctx.beginPath();
                        ctx.moveTo(x + boatWidth, boatY - 8);
                        ctx.lineTo(nextX, boatY - 8);
                        ctx.stroke();
                    }
                }
                if (ratio > 0.6) {
                    ctx.fillStyle = '#7a4c3c';
                    ctx.beginPath();
                    ctx.moveTo(width / 2 - 25, boatY - 10);
                    ctx.lineTo(width / 2 - 8, boatY - 25);
                    ctx.lineTo(width / 2 + 20, boatY - 25);
                    ctx.lineTo(width / 2 + 35, boatY - 10);
                    ctx.closePath();
                    ctx.fill();
                }
            }

            function animate() {
                time += 0.02;
                drawBridge(openRatio);
                requestAnimationFrame(animate);
            }
            animate();

            slider.addEventListener('input', function(e) {
                openRatio = parseFloat(e.target.value);
            });

            let autoInterval = null;
            document.getElementById('autoBtn').addEventListener('click', function() {
                if (autoInterval) clearInterval(autoInterval);
                autoInterval = setInterval(() => {
                    let newVal = parseFloat(slider.value) + 0.05;
                    if (newVal > 1.01) newVal = 0;
                    slider.value = newVal;
                    openRatio = newVal;
                }, 80);
            });
            document.getElementById('stopBtn').addEventListener('click', function() {
                if (autoInterval) {
                    clearInterval(autoInterval);
                    autoInterval = null;
                }
            });
            resizeCanvas();
            drawBridge(openRatio);
        })();
    </script>
    """
    html(bridge_animation, height=320)

with col_ans:
    st.success(
        "**✅ 唯一可拆浮梁桥**\n\n"
        "广济桥中段由18艘梭船组成活动浮桥，可定时开合：\n"
        "- **闭合**：行人车马通行，桥市繁荣\n"
        "- **开启**：商船通航、汛期泄洪\n\n"
        "这一设计比西方同类启闭式桥梁早了近400年，"
        "被茅以升誉为 **「世界最早的启闭式桥梁」** 。"
    )
    st.caption("👆 试试拖动滑块或点击自动演示，直观体验开合过程")

st.divider()

# ========== 核心数据 ==========
st.header("📊 广济桥核心数据")
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

# ========== 快速体验：亲手拼桥 ==========
col_puzzle1, col_puzzle2, col_puzzle3 = st.columns([1, 2, 1])
with col_puzzle2:
    if st.button("🧩 快速探索 · 体验建造 🧩", use_container_width=True, type="primary"):
        st.switch_page("pages/建造拼图.py")

# ========== 向下探索按钮（展开拆解理解区） ==========
col_down1, col_down2, col_down3 = st.columns([1, 2, 1])
with col_down2:
    if st.button("⬇️ 向下探索 · 拆解千年智慧", use_container_width=True, type="primary"):
        # 切换三个维度的显示状态：如果都已展开则收起，否则全部展开
        if st.session_state.show_structure and st.session_state.show_history and st.session_state.show_function:
            st.session_state.show_structure = False
            st.session_state.show_history = False
            st.session_state.show_function = False
        else:
            st.session_state.show_structure = True
            st.session_state.show_history = True
            st.session_state.show_function = True
        st.rerun()

# ========== 第二部分：拆解理解（结构、历史、功能） ==========
if st.session_state.show_structure or st.session_state.show_history or st.session_state.show_function:
    st.header("🔍 拆解理解：广济桥的三大维度")
    st.markdown("从结构、历史、功能三个角度，真正读懂这座千年古桥的独一无二之处。")

if st.session_state.show_structure:
    with st.expander("🏗️ 结构 · 千年营造技艺拆解", expanded=False):
        st.caption("内容均来自《宋至清潮州广济桥营造技术考析》对古代造桥工艺的权威考证")

        # 干修法
        with st.expander("🔍 干修法：西岸桥墩核心建造技术", expanded=False):
            col1, col2 = st.columns([1, 2.8])
            with col1:
                safe_load_image("干修法.png", caption="广济桥干修流程示意图")
            with col2:
                st.markdown("#### 技术起源")
                st.markdown("南宋乾道年间，广济桥西桥建设时首创，适用于韩江西岸水流较缓、水深较浅的区域，是宋代南方石梁桥常用的成熟施工工艺。")
                st.markdown("#### 核心特点")
                st.markdown("施工精度高，桥墩整体性、稳定性强，但对水文环境要求高，施工周期长，西桥10个桥墩耗时近57年。")
                with st.expander("📋 查看详细施工流程"):
                    st.markdown("""
                    利用枯季节，分段拦河阻流，在拦围圈内清干河水，并投放乱石作为基础，
                    然后再用经过加工的巨石排叠为桥墩，这种方法花的时间很长。
                    """)

        # 睡木沉基法
        with st.expander("🔍 睡木沉基法：宋代开创性造桥技术", expanded=False):
            col1, col2 = st.columns([1, 2.8])
            with col1:
                safe_load_image("睡木沉基法.png", caption="睡木沉基法施工原理")
            with col2:
                st.markdown("#### 技术起源")
                st.markdown("南宋绍熙年间，潮州工匠为解决韩江东岸水深流急、无法围堰施工的难题，创新发明了这项技术，是中国古代桥梁基础工程的里程碑式发明。")
                st.markdown("#### 历史意义")
                st.markdown("完美解决了深水急流环境下的桥墩施工难题，大幅缩短了施工工期，东桥13个桥墩仅用5年建成，后续南方深水桥梁广泛沿用。")
                with st.expander("📋 查看详细施工流程"):
                    st.markdown("""
                    在河中墩位地方先抛乱石，然后用几层大木筏、上面堆放了经过加工的巨石利用水位上涨时的浮力，牵拉至墩位地方固定，
                    等水落时让其搁置在乱石之上，再在上面加筑墩石，这样就加快了施工进度。    
                    东岸所以时间短，是由于施工方法改进的结果。桥墩的石块与石块之间不用灰浆，但凿有卯榫，使其相契合，避免摆动或松脱的危险。东桥桥长切墩多，却历时不过五年。
                    """)

        # 高船浮运潮汐法
        with st.expander("🔍 高船浮运潮汐法：巨型石梁架设技术", expanded=False):
            col1, col2 = st.columns([1, 2.8])
            with col1:
                safe_load_image("潮汐法.png", caption="巨型石梁架设示意图")
            with col2:
                st.markdown("#### 技术起源")
                st.markdown("明代广济桥全石梁化阶段，潮州工匠利用韩江潮汐规律，发明了这项技术，解决了古代无重型机械条件下，数十吨巨型石梁的运输与架设难题。")
                st.markdown("#### 技术成就")
                st.markdown("明末西班牙传教士实测记载，广济桥单根石梁宽厚均超1.1米，长度超10米，最重可达60吨，是当时世界罕见的巨型石材桥梁工程。")
                with st.expander("📋 查看详细施工流程"):
                    st.markdown("""
                    首先是开采与粗加工：工匠于凤栖山和桑埔山开凿石梁，琢凿防滑线和榫卯；
                    接着水陆联运：以麻筋杂泥混成圆柱，俟晒坚后，以大木为车，通过江运和海运方式运置大型船舶或竹木排，甚至绑在船腹，达到工地；
                    最后是浮运架设：利用潮汐涨落、洪水顶托作用，将石梁精准安装到石墩上。
                    """)
                                        
    # ---------- 历史：滑动时间轴 ----------
    if st.session_state.show_history:
        with st.expander("📜 历史 · 千年形态变迁（滑动时间轴）", expanded=False):
            st.markdown("广济桥的建造跨越南宋、元、明三朝，历时342年最终定型。")
            st.markdown("**滑动下方滑块，见证广济桥从南宋到明代的演变**")
            stages = [
                {"year": 1171, "title": "始建开端", 
                 "desc": "南宋乾道七年，知州曾汪始建江心石洲与86艘木船浮桥，定名「康济桥」。",
                 "img": "始建阶段还原.png"},
                {"year": 1228, "title": "石梁成型", 
                 "desc": "东西两岸共建成23座石墩，梁桥格局基本形成，江心仍用浮舟连结。",
                 "img": "石梁成型还原.png"},
                {"year": 1435, "title": "楼台成型", 
                 "desc": "明代王源主持重修，加固23墩，建126间亭屋、12座楼台，更名为「广济桥」。",
                 "img": "楼台成型还原.png"},
                {"year": 1513, "title": "最终定型", 
                 "desc": "嘉靖年间浮船改为18艘，形成「十八梭船廿四洲」经典格局。",
                 "img": "最终定型还原.png"},
                {"year": 0, "title": "明清桥市", 
                 "desc": "清末形成「一里长桥一里市」的桥市合一形态，成为闽粤商贸与文化枢纽。",
                 "img": "明清.png"}
            ]
            stage_idx = st.slider("历史阶段", 1, 5, 1, format="%d") - 1
            selected = stages[stage_idx]
            col_img, col_text = st.columns([1, 1])
            with col_img:
                safe_load_image(selected["img"], caption=f"{selected['year'] if selected['year'] else '明清'}年 · {selected['title']}", use_container_width=True)
            with col_text:
                st.markdown(f"#### {selected['year'] if selected['year'] else '明清'}年 {selected['title']}")
                st.write(selected["desc"])
                st.caption("图片为根据史料复原的广济桥形态示意")

    # ---------- 功能：精简版，避免重复动画，改为图文+数据卡片 ----------
    if st.session_state.show_function:
        with st.expander("⚙️ 功能 · 启闭式设计深度解析", expanded=False):
            st.markdown("### 世界首创的水陆两用桥梁解决方案")
            col_1, col_2,col_3 = st.columns([1,1, 1])
            with col_1:
                st.markdown("**浮桥闭合**：")
                st.image(get_img_path("浮桥-关.webp"), caption="闭合时行人车马通行", use_container_width=True)
            with col_2:    
                st.markdown("**浮桥开启**：")
                st.image(get_img_path("浮桥-开.webp"), caption="开启时航道畅通", use_container_width=True)
            with col_3:
                st.markdown("**✨ 启闭式设计的开创性优势**")
                st.metric("比西方早", "近400年", help="世界最早启闭式桥梁")
                st.divider()
                st.markdown("""
                🌍 **水陆兼顾**：世界最早系统解决通行与通航矛盾  
                💧 **水文适配**：灵活适应韩江水位落差，汛期快速泄洪  
                🔧 **维护成本低**：浮桥可拆解维修，不影响全桥通行  
                🧠 **影响深远**：为南方多水地区桥梁提供范本
                """)
            st.caption("💡 提示：可在上方核心问题区域体验开合动画，此处不再重复。")

    st.divider()

# ========== 自由探索按钮 ==========
col_explore1, col_explore2, col_explore3 = st.columns([1, 2, 1])
with col_explore2:
    if st.button("✨ 自由探索 ✨", use_container_width=True, type="secondary"):
        # 切换自由探索模块的显示状态
        st.session_state.show_explore = not st.session_state.show_explore
        st.rerun()
        
if st.session_state.show_explore:
    st.header("🎨 自由探索：亲手玩转广济桥")
    st.markdown("通过以下互动模块，深入了解广济桥的建造技艺、历史变迁和现代意义。")

    col1, col2, col3= st.columns(3)
    with col1:
        with st.container(border=True):
            st.markdown("#### 🏛️ 三大核心特色")
            st.markdown("「十八梭船廿四洲」「廿四楼台廿四样」「一里长桥一里市」深度解析。")
            if st.button("探索三大特色", use_container_width=True, key="features"):
                st.switch_page("pages/核心特点.py")

    with col2:
        with st.container(border=True):
            st.markdown("#### 🎮 体验桥工日常")
            st.markdown("扮演明代桥工，在模拟场景中做出正确的开合决策。")
            if st.button("开始游戏", use_container_width=True, key="game"):
                st.switch_page("pages/桥工模拟.py")

    with col3:
        with st.container(border=True):
            st.markdown("#### 🤖 AI 科普问答")
            st.markdown("关于广济桥的任何问题，都可以向AI助手提问，获取专业解答。")
            if st.button("开始问答", use_container_width=True, key="ai_qa"):
                st.switch_page("pages/AI科普问答.py")

# ========== 参考文献 ==========
render_references()