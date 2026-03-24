# pages/2_启闭式桥梁交互模拟.py
import streamlit as st
from streamlit.components.v1 import html
from utils import back_to_home_btn, safe_load_image, render_references,render_footer_nav

# ========== 返回首页按钮 ==========
back_to_home_btn()
st.divider()

# ========== 页面标题 ==========
st.header("广济桥核心营造技艺与启闭式交互模拟")
st.subheader("从深水造桥到世界首创的启闭式设计，解锁古代桥梁工程的巅峰智慧")
st.divider()

# ========== 第一部分：三大核心营造技艺 ==========
st.header("一、广济桥三大核心营造技艺拆解")
st.caption("内容均来自《宋至清潮州广济桥营造技术考析》对古代造桥工艺的权威考证")

# 干修法
with st.expander("🔍 干修法：西岸桥墩核心建造技术", expanded=True):
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
with st.expander("🔍 睡木沉基法：宋代开创性造桥技术", expanded=True):
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
with st.expander("🔍 高船浮运潮汐法：巨型石梁架设技术", expanded=True):
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

# ========== 第二部分：启闭式设计与交互模拟 ==========
st.header("二、世界首创的启闭式桥梁设计")
st.markdown("在解决了「深水建桥墩、巨型石梁架设」的基础难题后，古代工匠最终用启闭式设计，完美解决了「水陆交通兼顾」的千年难题，这也是广济桥被称为世界桥梁史上奇迹的核心原因")
st.divider()

# ========== 动画演示+游戏入口 ==========
st.markdown("### 👇 拖动下方滑块，直观体验启闭式设计的工作原理")
st.markdown("")

col_left, col_right = st.columns([1.5, 1])
with col_left:
    st.subheader("🎮 浮桥启闭动画演示")
    html_code = """
<style>
    /* 控制按钮样式*/
    .control-row {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        margin: 10px 0;
    }
    .auto-btn {
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
    .auto-btn:hover {
        background: #3f6a7a;
        transform: translateY(-1px);
    }
    .stop-btn {
        background: #9c7c5b;
        color: white;
        border: none;
        padding: 6px 24px;
        border-radius: 30px;
        font-size: 1rem;
        cursor: pointer;
        transition: 0.2s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .stop-btn:hover {
        background: #b39673;
        transform: translateY(-1px);
    }
</style>

<div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
    <!-- canvas 画布，宽度600，高度200（将自适应缩放） -->
    <canvas id="bridgeCanvas" width="600" height="200" style="width:100%; height:auto; background: #9fc5d9; border-radius: 16px; display: block;"></canvas>
    
    <!-- 滑块，控制浮桥开合程度 -->
    <input type="range" id="openSlider" min="0" max="1" step="0.05" value="0" style="width: 80%; margin: 15px 0 5px;" />
    
    <!-- 滑块两端文字 -->
    <div style="display: flex; justify-content: space-between; width: 80%; font-size: 0.9rem; color: #2b4f5c;">
        <span>⚓ 浮桥闭合</span>
        <span>🚢 航道开启</span>
    </div>
    <!-- 控制按钮 -->
    <div class="control-row">
        <button id="autoBtn" class="auto-btn">▶ 自动演示</button>
        <button id="stopBtn" class="stop-btn">⏸ 停止</button>
    </div>
</div>

<script>
    (function() {
        // 获取 canvas 和上下文
        const canvas = document.getElementById('bridgeCanvas');
        const ctx = canvas.getContext('2d');
        const slider = document.getElementById('openSlider');

        // 调整 canvas 分辨率以适应高DPI屏幕
        function resizeCanvas() {
            const rect = canvas.getBoundingClientRect();
            const dpr = window.devicePixelRatio || 1;
            canvas.width = rect.width * dpr;
            canvas.height = rect.height * dpr;
            ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        // ========== 可调整的坐标参数 ==========
        // 左岸石墩的X坐标（三个石墩以 leftBankX 为基准向左排列）
        const leftBankX = 185;
        // 右岸石墩的X坐标（三个石墩以 rightBankX 为基准向右排列）
        const rightBankX = 585;
        // 石墩和船的Y坐标（垂直位置）
        const boatY = 120;

        // 单个梭船的宽度（像素）
        const boatWidth = 22;
        // 梭船总数（18艘）
        const boatCount = 18;
        // 浮桥开启时，左右两侧梭船的最大偏移量（像素）
        const maxOffset = 150;

        // 当前开启比例（0~1），由滑块控制
        let openRatio = parseFloat(slider.value);
        // 用于水波动画的时间变量
        let time = 0;

        // ========== 绘制函数 ==========
        function drawBridge(ratio) {
            // 获取画布实际显示尺寸（已考虑缩放）
            const width = canvas.width / (window.devicePixelRatio || 1);
            const height = canvas.height / (window.devicePixelRatio || 1);
            
            // 清除画布
            ctx.clearRect(0, 0, width, height);

            // 绘制天空渐变背景
            const skyGrad = ctx.createLinearGradient(0, 0, 0, height);
            skyGrad.addColorStop(0, '#b3d9f0');
            skyGrad.addColorStop(0.7, '#e0f0f5');
            ctx.fillStyle = skyGrad;
            ctx.fillRect(0, 0, width, height);

            // ========== 绘制“山”（绿色背景轮廓） ==========
            ctx.fillStyle = '#6a8d8f';
            ctx.beginPath();
            // 以下坐标点定义了山的轮廓，可调整这些点来改变山的形状和位置
            ctx.moveTo(0, 150);   // 起点 (x, y)
            ctx.lineTo(80, 100);  // 第一个山峰顶点
            ctx.lineTo(200, 130); // 山谷
            ctx.lineTo(350, 80);  // 第二个山峰顶点
            ctx.lineTo(500, 120); // 山谷
            ctx.lineTo(700, 70);  // 第三个山峰顶点
            ctx.lineTo(800, 300); // 右下角
            ctx.lineTo(0, 300);   // 左下角
            ctx.fill();

            // 绘制半透明水面（覆盖山的下半部分）
            ctx.fillStyle = '#4799b3';
            ctx.globalAlpha = 0.6;
            ctx.fillRect(0, 120, width, 150);
            ctx.globalAlpha = 1.0;

            // 绘制水波纹（动态）
            ctx.strokeStyle = 'white'; 
            ctx.lineWidth = 1.2; 
            ctx.globalAlpha = 0.4;
            for (let i=0; i<5; i++) {
                let baseY = 130 + i*15;
                let y = baseY + Math.sin(time * 2 + i * 2) * 3;
                ctx.beginPath(); 
                ctx.moveTo(0, y);
                for (let x=0; x<width; x+=40) {
                    let offsetY = Math.sin(time * 3 + x * 0.02) * 5;
                    ctx.lineTo(x+20, y + offsetY);
                }
                ctx.stroke();
            }
            ctx.globalAlpha = 1.0;

            // ========== 绘制左岸石墩（3个） ==========
            ctx.fillStyle = '#6b4f3c';
            for (let i=0; i<3; i++) {
                let x = leftBankX - 40 + i * 25;  // 石墩的X坐标，以 leftBankX 为基准向左排列
                ctx.fillRect(x, boatY-15, 12, 40); // 石墩矩形 (x, y, 宽, 高)
                // 绘制石墩纹理（竖线）
                ctx.strokeStyle = '#4a3a2a';
                ctx.lineWidth = 1;
                for (let j=0; j<3; j++) {
                    ctx.beginPath();
                    ctx.moveTo(x+2, boatY-15 + j*12);
                    ctx.lineTo(x+10, boatY-15 + j*12);
                    ctx.stroke();
                }
            }

            // ========== 绘制右岸石墩（3个） ==========
            for (let i=0; i<3; i++) {
                let x = rightBankX + 20 + i * 25;  // 石墩的X坐标，以 rightBankX 为基准向右排列
                ctx.fillRect(x, boatY-15, 12, 40);
                ctx.strokeStyle = '#4a3a2a';
                ctx.lineWidth = 1;
                for (let j=0; j<3; j++) {
                    ctx.beginPath();
                    ctx.moveTo(x+2, boatY-15 + j*12);
                    ctx.lineTo(x+10, boatY-15 + j*12);
                    ctx.stroke();
                }
            }

            // ========== 绘制18艘梭船（浮桥） ==========
            const totalWidth = (boatCount-1) * boatWidth;
            const leftMost = (width - totalWidth) / 2; // 计算最左侧梭船的起始X坐标（使船群居中）
            for (let i=0; i<boatCount; i++) {
                let baseX = leftMost + i * boatWidth;
                // 根据开启比例，左右两侧的梭船向相反方向移动
                let offset = (i < boatCount/2) ? -ratio * maxOffset : ratio * maxOffset;
                let x = baseX + offset; // 当前船的X坐标

                // 绘制船体（梯形）
                ctx.fillStyle = '#9c7c5b';
                ctx.beginPath();
                ctx.moveTo(x, boatY);
                ctx.lineTo(x + boatWidth*0.3, boatY-10);
                ctx.lineTo(x + boatWidth*0.7, boatY-10);
                ctx.lineTo(x + boatWidth, boatY);
                ctx.closePath();
                ctx.fill();

                // 绘制船舷线条
                ctx.strokeStyle = '#6b4f3c';
                ctx.lineWidth = 1;
                ctx.beginPath();
                ctx.moveTo(x+5, boatY-5);
                ctx.lineTo(x+boatWidth-5, boatY-5);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(x+8, boatY-10);
                ctx.lineTo(x+boatWidth-8, boatY-10);
                ctx.stroke();

                // 绘制船篷（小矩形）
                ctx.fillStyle = '#b99e7c';
                ctx.fillRect(x+4, boatY-16, boatWidth-8, 6);

                // 绘制连接相邻船的链条（只画在奇数船上避免重复）
                if (i < boatCount-1) {
                    let nextBase = leftMost + (i+1) * boatWidth;
                    let nextOffset = ((i+1) < boatCount/2) ? -ratio * maxOffset : ratio * maxOffset;
                    let nextX = nextBase + nextOffset;
                    ctx.strokeStyle = '#5d4a36'; 
                    ctx.lineWidth = 2;
                    ctx.beginPath(); 
                    ctx.moveTo(x+boatWidth, boatY-8); 
                    ctx.lineTo(nextX, boatY-8); 
                    ctx.stroke();
                    // 画链条上的节点（圆圈）
                    for (let t=0.2; t<1.0; t+=0.4) {
                        let cx = x+boatWidth + (nextX - (x+boatWidth))*t;
                        ctx.beginPath(); 
                        ctx.arc(cx, boatY-8, 2.5, 0, 2*Math.PI);
                        ctx.fillStyle = '#8b7a62'; 
                        ctx.fill();
                    }
                }
            }

            // 如果开启比例大于0.6，画一艘商船示意（可选）
            if (ratio > 0.6) {
                ctx.fillStyle = '#7a4c3c';
                ctx.beginPath();
                ctx.moveTo(width/2-25, boatY-10); 
                ctx.lineTo(width/2-8, boatY-25);
                ctx.lineTo(width/2+20, boatY-25); 
                ctx.lineTo(width/2+35, boatY-10);
                ctx.closePath(); 
                ctx.fill();
                ctx.fillStyle = '#c9b79b';
                ctx.fillRect(width/2-3, boatY-45, 6, 20);
            }
        }

        // 动画循环（每帧更新时间并重绘）
        function animate() {
            time += 0.02;
            drawBridge(openRatio);
            requestAnimationFrame(animate);
        }
        animate();

        // 监听滑块输入，更新开启比例
        slider.addEventListener('input', function(e) {
            openRatio = parseFloat(e.target.value);
        });

        // 自动演示：定时增加滑块值
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

        // 停止自动演示
        document.getElementById('stopBtn').addEventListener('click', function() {
            if (autoInterval) {
                clearInterval(autoInterval);
                autoInterval = null;
            }
        });

        // 初始化画布大小并绘制
        resizeCanvas();
        drawBridge(openRatio);
    })();
</script>
"""
    html(html_code, height=400)
    st.markdown("")
    left_desc, right_desc = st.columns(2)
    with left_desc:
        st.markdown("**✅ 闭合状态功能**")
        st.markdown("""
        • 18艘梭船连成桥面  
        • 行人车马通行  
        • 桥市合一，商铺营业
        """)
    with right_desc:
        st.markdown("**🚢 开启状态功能**")
        st.markdown("""
        • 打通韩江主航道  
        • 大型商船通过  
        • 汛期快速泄洪
        """)

with col_right:
    st.subheader("✨ 启闭式设计开创性优势")
    
    # 指标卡片
    col_metric1, col_metric2 = st.columns(2)
    with col_metric1:
        st.metric("比西方早", "近400年", help="世界最早启闭式桥梁")
        st.metric("梭船数量", "18艘", help="中段浮桥由18艘梭船组成")
    with col_metric2:
        st.metric("桥墩数量", "23座", help="「廿四洲」")
        st.metric("桥长", "518米", help="古代一市里")
    
    st.divider()
    
    # 优势列表（带图标）
    st.markdown("""
    🌍 **水陆兼顾**：世界最早系统解决通行与通航矛盾  
    💧 **水文适配**：灵活适应韩江水位落差，汛期快速泄洪  
    🔧 **维护成本低**：浮桥可拆解维修，不影响全桥通行  
    🧠 **影响深远**：为南方多水地区桥梁提供范本
    """)
    
    # 游戏入口
    st.divider()
    if st.button("🎮 体验桥工日常（启闭式游戏）", use_container_width=True, type="primary"):
        st.switch_page("pages/5_启闭式桥梁交互游戏.py")

render_footer_nav()
# ========== 参考文献 ==========
render_references()