import streamlit as st
import streamlit.components.v1 as components
import base64
from utils import get_puzzle_assets_path, back_to_home_btn,render_footer_nav

# ---------------------- 工具函数：图片转base64 ----------------------
def image_to_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    except Exception as e:
        st.warning(f"图片加载失败：{image_path}，请检查文件名/路径是否正确")
        return ""

# ---------------------- 页面全局配置 ----------------------
st.set_page_config(
    page_title="广济桥建造拼图挑战",
    page_icon="🧩",
    layout="wide"
)

# 返回首页按钮
back_to_home_btn()
st.divider()

# ---------------------- 核心配置---------------------
ASSETS_FOLDER = get_puzzle_assets_path()  # 动态获取正确路径
BG_ORIGIN_SIZE = {"width": 2732, "height": 1534}
MAX_DISPLAY_WIDTH = 1400

# 4个关卡完整配置
LEVEL_CONFIG = [
    # 关卡1：南宋初创·江心浮桥
    {
        "level_id": 1,
        "level_name": "第一关：南宋初创·江心浮桥",
        "history_desc": "南宋乾道七年（1171年），潮州知州曾汪在韩江之上造舟为梁，联86艘木船为浮桥，并筑石洲于江心，定名「康济桥」，开创了广济桥的建造历史。",
        "bg_image": f"{ASSETS_FOLDER}/base map1.png",
        "pieces": {
            "左浮船": {
                "image": f"{ASSETS_FOLDER}/part1_1.png",
                "position": {"x": 780, "y": 950},
                "clue": "西段浮船，采用木质船体，以铁链联缀固定，是广济桥最早的浮桥组成部分，为西岸提供通行通道。"
            },
            "石洲": {
                "image": f"{ASSETS_FOLDER}/part1_2.png",
                "position": {"x": 1410, "y": 750},
                "clue": "江心石洲，位于水势稍缓处，作为浮桥的中间锚点，有效分散水流冲击力，是连接东西两段浮船的关键枢纽。"
            },
            "右浮船": {
                "image": f"{ASSETS_FOLDER}/part1_3.png",
                "position": {"x": 2020, "y": 540},
                "clue": "东段浮船，与西段对称布局，通过石洲串联形成完整通道，破解了韩江「沙平水落，一苇可航；雨积江涨，则波急岸远」的通行难题。"
            }
        }
    },
    # 关卡2：石梁成型·二十二洲
    {
        "level_id": 2,
        "level_name": "第二关：石梁成型·二十二洲",
        "history_desc": "南宋淳熙元年（1174年）至绍定元年（1228年），历代州官接力修建，西岸筑10墩，东岸筑12墩，共22座石墩屹立韩江，梁桥格局基本形成，江心仍以浮舟连结。",
        "bg_image": f"{ASSETS_FOLDER}/base map2.png",
        "pieces": {
            "左石洲": {
                "image": f"{ASSETS_FOLDER}/part2_1.png",
                "position": {"x": 660, "y": 950},
                "clue": "西岸石墩群，由知州丁允元等主持修建，共10座，墩体用巨大规整的石块砌成，石缝间凿有卯榫相连接，异常坚固。"
            },
            "浮船": {
                "image": f"{ASSETS_FOLDER}/part2_2.png",
                "position": {"x": 1280, "y": 740},
                "clue": "衔接东西石墩的浮船，采用铁链固定于两岸矶头墩，可随潮势起伏，既保证通行连续性，又具备应对汛期的灵活性。"
            },
            "右石洲": {
                "image": f"{ASSETS_FOLDER}/part2_3.png",
                "position": {"x": 1950, "y": 540},
                "clue": "东岸石墩群，由知州沈宗禹、陈宏规等主持修建，共12座，与西岸石墩遥相呼应，形成分段架梁的基础格局。"
            }
        }
    },
    # 关卡3：元代增墩·二十三洲
    {
        "level_id": 3,
        "level_name": "第三关：元代增墩·二十三洲",
        "history_desc": "元大德十年（1306年），潮州总管常怀德在东桥最前端增建一墩，使东桥石墩由12座增至13座，全桥石墩总数达到23座，为明代「廿四洲」之说奠定了基础。",
        "bg_image": f"{ASSETS_FOLDER}/base map3.png",
        "pieces": {
            "增建石墩": {          
                "image": f"{ASSETS_FOLDER}/part3_2.png", 
                "position": {"x": 1560, "y": 680},         
                "clue": "元大德十年（1306年），潮州总管常怀德在东桥最前端增建一墩，使东桥由12墩增至13墩，全桥石墩总数达到23座，为明代「廿四洲」格局打下基础。"
            },
            "左板砖": {
                "image": f"{ASSETS_FOLDER}/part3_1.png",
                "position": {"x": 700, "y": 900},
                "clue": "西段桥面铺砖，采用本地坚质砖石，砖缝以灰勾缝防火防潮，铺设于木质梁架之上，是明代桥面加固的典型工艺。"
            },
            "右板砖": {
                "image": f"{ASSETS_FOLDER}/part3_3.png",
                "position": {"x": 2050, "y": 500},
                "clue": "东段桥面铺砖，与西侧工艺一脉相承，砖石铺设平整致密，形成贯通的步行通道，配合亭台楼阁，构成完整风貌。"
            },
            "西侧楼台": {
                "image": f"{ASSETS_FOLDER}/part3_4.png",
                "position": {"x": 700, "y": 900},
                "clue": "西岸石洲上的楼阁，明代王源所建，命名有「奇观」「凌霄」「得月」「乘驷」「涉川」等，飞檐翘角，风格各异，是「廿四楼台廿四样」的西端代表。"
            },
            "东侧楼台": {
                "image": f"{ASSETS_FOLDER}/part3_5.png",
                "position": {"x": 2050, "y": 500},
                "clue": "东岸石洲上的楼阁，命名有「左达」「济川」「云衢」「冰壶」「小蓬莱」「摘星」「仰韩」等，形制多样，既可供行人休憩，又成为韩江沿岸的标志性景观。"
            }
        }
    },
    # 关卡4：明代定型·十八梭船廿四洲
    {
        "level_id": 4,
        "level_name": "第四关：明代定型·十八梭船廿四洲",
        "history_desc": "明正德八年（1513年），知府谭伦将浮舟由24艘减为18艘，并增建一墩一楼，最终形成「十八梭船廿四洲，廿四楼台廿四样」的经典格局，广济桥从此名扬天下。",
        "bg_image": f"{ASSETS_FOLDER}/base map4.png",
        "pieces": {
            "十八浮船桥": {
                "image": f"{ASSETS_FOLDER}/part4.png",
                "position": {"x": 1340, "y": 730},
                "clue": "明正德八年（1513年）定型后的浮桥部分，由18艘梭船组成，每三艘一组，用铁链联缀，东西矶头各有一组锚定不动，中间四组可定时启闭，实现了「十八梭船廿四洲」的最终形制。"
            }
        }
    }
]

# ---------------------- 初始化游戏状态 ----------------------
if "unlocked_level" not in st.session_state:
    st.session_state.unlocked_level = 1
if "current_level" not in st.session_state:
    st.session_state.current_level = 1
if "level_confirmed" not in st.session_state:
    st.session_state.level_confirmed = {}
if "reset_trigger" not in st.session_state:
    st.session_state.reset_trigger = False

# ---------------------- 生成拼图HTML（增加 is_confirmed 参数，分离显示顺序） ----------------------
def generate_puzzle_html(level_data, reset_flag, is_confirmed):
    current_pieces = level_data["pieces"]
    origin_w = BG_ORIGIN_SIZE["width"]
    origin_h = BG_ORIGIN_SIZE["height"]
    max_w = MAX_DISPLAY_WIDTH
    total = len(current_pieces)

    # 逻辑顺序（拼图必须按此顺序放置）
    logic_order = list(current_pieces.keys())
    # 显示顺序（底部待选池的排列）——根据不同关卡自定义乱序
    if level_data["level_id"] == 1:
        display_order = ["石洲", "右浮船", "左浮船"]  # 第一关
    elif level_data["level_id"] == 2:
        display_order = ["左石洲", "右石洲", "浮船"]  # 第二关
    elif level_data["level_id"] == 3:
        display_order = ["增建石墩","东侧楼台", "左板砖",  "西侧楼台", "右板砖"]  # 第三关
    else:  # 第四关只有一个部件，无所谓顺序
        display_order = logic_order

    # 图片转base64
    bg_base64 = image_to_base64(level_data["bg_image"])
    bg_url = f"data:image/png;base64,{bg_base64}"
    pieces_base64 = {name: f"data:image/png;base64,{image_to_base64(info['image'])}" for name, info in
                     current_pieces.items()}

    # 动态生成HTML
    drop_zones_html = ""
    puzzle_pieces_html = ""
    for name, info in current_pieces.items():
        left_percent = (info["position"]["x"] / origin_w) * 100
        top_percent = (info["position"]["y"] / origin_h) * 100
        drop_zones_html += f'''
        <div class="drop-zone" 
             id="zone_{name}"
             data-name="{name}"
             style="left: {left_percent}%; top: {top_percent}%;">
        </div>
        '''
        puzzle_pieces_html += f'''
        <img class="puzzle-piece" 
             id="piece_{name}"
             src="{pieces_base64[name]}"
             style="left: 0; top: 0;"
             draggable="true"
             data-name="{name}">
        '''

    html_code = f"""
    <!-- 重置标记：{reset_flag} 强制iframe刷新 -->
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{level_data['level_name']}</title>
        <style>
            * {{ 
                margin: 0; 
                padding: 0; 
                box-sizing: border-box;
                -webkit-user-select: none;
                -moz-user-select: none;
                -ms-user-select: none;
                user-select: none;
            }}
            body {{ 
                overflow-x: hidden; 
                font-family: "SimHei", "Microsoft YaHei", serif;
                background-color: transparent;
            }}

            .puzzle-wrapper {{
                width: 100%;
                max-width: {max_w}px;
                margin: 0 auto;
                overflow-x: auto;
                overflow-y: hidden;
            }}
            .puzzle-box {{
                width: {origin_w}px;
                max-width: 100%;
                margin: 0 auto;
                position: relative;
            }}

            .bg-container {{
                width: 100%;
                aspect-ratio: {origin_w} / {origin_h};
                position: relative;
                border: 3px solid #8b4513;
                border-radius: 8px;
                overflow: hidden;
                background-image: url("{bg_url}");
                background-size: contain;
                background-repeat: no-repeat;
                background-position: center;
                background-color: #f9f6f0;
            }}

            /* 核心修改1：默认所有drop-zone完全隐藏 */
            .drop-zone {{
                position: absolute;
                width: 12%;
                height: 20%;
                border: 2px dashed transparent;
                border-radius: 4px;
                z-index: 999;
                transform: translate(-50%, -50%);
                transition: all 0.2s ease;
                opacity: 0; /* 默认完全透明 */
                pointer-events: none; /* 默认不可点击 */
            }}
            /* 只有当前可放置的zone才开启交互 */
            .drop-zone.current-zone {{
                pointer-events: auto;
            }}
            /* 光标悬浮时高亮 */
            .drop-zone.current-zone:hover,
            .drop-zone.current-zone.drag-over {{
                opacity: 1; /* 显示框 */
                border-color: #ffd700;
                background-color: rgba(255, 215, 0, 0.15);
                box-shadow: 0 0 15px #ffd700;
            }}
            /* 已完成的zone样式 */
            .drop-zone.completed {{
                opacity: 1;
                border-color: #2ecc71;
                background-color: rgba(46, 204, 113, 0.1);
                box-shadow: 0 0 10px #2ecc71;
            }}

            .puzzle-piece {{
                position: absolute;
                width: 100%;
                height: 100%;
                cursor: grab;
                z-index: 50;
                transition: all 0.2s ease;
                border-radius: 4px;
                object-fit: contain;
                display: none;
                pointer-events: none;
            }}

            .puzzle-piece.correct {{
                cursor: default;
                animation: gold-border 1.5s ease-in-out forwards;
            }}
            @keyframes gold-border {{
                0% {{ outline: 2px solid transparent; }}
                50% {{ outline: 3px solid #ffd700; box-shadow: 0 0 25px #ffd700; }}
                100% {{ outline: 2px solid #ffd700; }}
            }}

            .pieces-pool {{
                width: 100%;
                max-width: {max_w}px;
                margin: 20px auto;
                display: flex;
                flex-wrap: wrap;
                gap: 15px;
                justify-content: center;
                padding: 15px;
                border: 2px solid #d2b48c;
                border-radius: 8px;
                background-color: #f9f6f0;
            }}

            /* --- 悬浮提示容器 --- */
            .pool-item-wrapper {{
                position: relative;
                display: inline-block;
            }}

            .pool-item {{
                width: auto;
                height: 100px;
                max-width: 150px;
                cursor: grab;
                border-radius: 4px;
                transition: all 0.2s ease;
                object-fit: contain;
                draggable: true;
            }}
            .pool-item:hover {{
                box-shadow: 0 0 15px #ffd700;
                transform: scale(1.05);
            }}
            .pool-item.dragging {{
                opacity: 0.6;
                transform: scale(0.95);
            }}
            .pool-item.used {{
                opacity: 0.3;
                pointer-events: none;
                filter: grayscale(100%);
            }}

            .pool-item:active {{
                height: 180px;
                max-width: 250px;
                transition: none;
            }}

            /* --- Tooltip 悬浮提示气泡样式 --- */
            .tooltip {{
                visibility: hidden;
                opacity: 0;
                position: absolute;
                z-index: 1000;
                bottom: 110%;
                left: 50%;
                transform: translateX(-50%);
                background-color: rgba(0, 0, 0, 0.85);
                color: #fff;
                text-align: center;
                padding: 6px 12px;
                border-radius: 6px;
                font-size: 14px;
                font-weight: bold;
                white-space: nowrap;
                pointer-events: none;
                transition: opacity 0.2s ease-in-out;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            }}

            /* 气泡小尾巴 */
            .tooltip::after {{
                content: "";
                position: absolute;
                top: 100%;
                left: 50%;
                margin-left: -5px;
                border-width: 5px;
                border-style: solid;
                border-color: rgba(0, 0, 0, 0.85) transparent transparent transparent;
            }}

            /* 鼠标悬浮时显示 */
            .pool-item-wrapper:hover .tooltip {{
                visibility: visible;
                opacity: 1;
            }}

            .iframe-progress {{
                width: 100%;
                max-width: {max_w}px;
                margin: 0 auto 10px auto;
                padding: 8px 12px;
                background-color: #f0f2f6;
                border-radius: 8px;
                border: 1px solid #d2d6dc;
            }}
            .iframe-progress-bar {{
                width: 100%;
                height: 16px;
                background-color: #e0e0e0;
                border-radius: 8px;
                overflow: hidden;
                margin-top: 6px;
            }}
            .iframe-progress-fill {{
                height: 100%;
                background: linear-gradient(90deg, #ffd700, #ffb347);
                width: 0%;
                transition: width 0.5s ease;
                border-radius: 8px;
            }}

            .iframe-toast {{
                position: fixed;
                top: 20px;
                left: 50%;
                transform: translateX(-50%);
                background-color: #2ecc71;
                color: white;
                padding: 12px 28px;
                border-radius: 8px;
                font-size: 20px;
                font-weight: bold;
                z-index: 99999;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                display: none;
                animation: slideDown 0.3s ease;
            }}
            @keyframes slideDown {{
                from {{ opacity: 0; transform: translateX(-50%) translateY(-20px); }}
                to {{ opacity: 1; transform: translateX(-50%) translateY(0); }}
            }}
        </style>
    </head>
    <body>
        <div class="iframe-progress">
            <div style="font-weight: bold; color: #333; font-size: 15px;">
                🧩 本关建造进度：<span id="progress-text">0/{total}</span>
            </div>
            <div class="iframe-progress-bar">
                <div class="iframe-progress-fill" id="progress-fill"></div>
            </div>
        </div>

        <div class="iframe-toast" id="iframe-toast"></div>

        <div class="puzzle-wrapper">
            <div class="puzzle-box">
                <div class="bg-container">
                    {drop_zones_html}
                    {puzzle_pieces_html}
                </div>
            </div>
        </div>

        <div class="pieces-pool" style="{'' if level_data['level_id'] !=3 else 'flex-wrap: nowrap; justify-content: flex-start; min-width: 680px;'}">
            {''.join([f'''
            <div class="pool-item-wrapper">
                <img class="pool-item" 
                     id="pool_{name}"
                     src="{pieces_base64[name]}"
                     draggable="true"
                     data-name="{name}">
                <div class="tooltip">{name}</div>
            </div>
            ''' for name in display_order])}  <!-- 使用 display_order 控制显示顺序 -->
        </div>

        <script>
            const completedPieces = [];
            const totalPieces = {total};
            const progressText = document.getElementById('progress-text');
            const progressFill = document.getElementById('progress-fill');
            const toast = document.getElementById('iframe-toast');
            // 逻辑顺序（拼图必须按此顺序放置）——保持原样
            const pieceOrder = {str(logic_order)};
            const levelConfirmed = {'true' if is_confirmed else 'false'};

            // 核心修改2：初始化当前可放置的zone
            function setCurrentZone() {{
                // 如果已通关，不设置任何current-zone
                if (levelConfirmed) return;
                // 移除所有zone的current-zone类
                document.querySelectorAll('.drop-zone').forEach(zone => {{
                    zone.classList.remove('current-zone');
                }});
                // 获取当前该放置的部件名称
                const nextPieceIndex = completedPieces.length;
                if (nextPieceIndex < pieceOrder.length) {{
                    const currentPieceName = pieceOrder[nextPieceIndex];
                    // 给当前zone添加current-zone类（开启交互）
                    const currentZone = document.getElementById(`zone_${{currentPieceName}}`);
                    if (currentZone) {{
                        currentZone.classList.add('current-zone');
                    }}
                }}
            }}

            // 页面加载时初始化
            // 如果是已通关关卡，直接设置所有部件为已完成
            function initConfirmedLevel() {{
                if (!levelConfirmed) return;
                // 将所有部件标记为已完成
                pieceOrder.forEach(name => {{
                    completedPieces.push(name);
                    const targetPiece = document.getElementById(`piece_${{name}}`);
                    const poolItem = document.getElementById(`pool_${{name}}`);
                    const zone = document.getElementById(`zone_${{name}}`);
                    if (targetPiece) targetPiece.style.display = 'block';
                    if (poolItem) poolItem.classList.add('used');
                    if (zone) {{
                        zone.classList.add('completed');
                        zone.classList.remove('current-zone');
                    }}
                }});
                // 更新进度
                progressText.textContent = `${{totalPieces}}/${{totalPieces}}`;
                progressFill.style.width = '100%';
                // 禁用所有部件的拖拽（可选，但pool-item已添加used类，无法拖拽）
                // 移除拖拽事件监听（避免意外）
                document.querySelectorAll('.pool-item').forEach(item => {{
                    item.setAttribute('draggable', 'false');
                }});
            }}

            // 页面加载时，把解锁下一关按钮设为禁用
            function initConfirmBtn() {{
                try {{
                    const btnWrapper = window.parent.document.getElementById('confirm-btn-wrapper');
                    if (btnWrapper) {{
                        const confirmBtn = btnWrapper.querySelector('button');
                        if (confirmBtn) {{
                            confirmBtn.disabled = true;
                            confirmBtn.style.opacity = '0.5';
                            confirmBtn.style.cursor = 'not-allowed';
                        }}
                    }}
                }} catch (e) {{}}
            }}
            initConfirmBtn();

            // 显示提示
            function showToast(message, isSuccess = true) {{
                toast.textContent = message;
                toast.style.backgroundColor = isSuccess ? '#2ecc71' : '#e74c3c';
                toast.style.display = 'block';
                setTimeout(() => {{
                    toast.style.display = 'none';
                }}, 2500);
            }}

            // 更新进度
            function updateProgress() {{
                const count = completedPieces.length;
                progressText.textContent = `${{count}}/${{totalPieces}}`;
                const percent = (count / totalPieces) * 100;
                progressFill.style.width = percent + '%';

                // 进度完成，自动解锁「解锁下一关」按钮
                if (count === totalPieces) {{
                    try {{
                        const btnWrapper = window.parent.document.getElementById('confirm-btn-wrapper');
                        if (btnWrapper) {{
                            const confirmBtn = btnWrapper.querySelector('button');
                            if (confirmBtn) {{
                                confirmBtn.disabled = false;
                                confirmBtn.style.opacity = '1';
                                confirmBtn.style.cursor = 'pointer';
                            }}
                        }}
                    }} catch (e) {{}}
                }}
            }}

            // 拖拽事件（如果已通关，不添加监听）
            const poolItems = document.querySelectorAll('.pool-item');
            const dropZones = document.querySelectorAll('.drop-zone');

            if (!levelConfirmed) {{
                poolItems.forEach(item => {{
                    item.addEventListener('dragstart', (e) => {{
                        e.stopPropagation();
                        const pieceName = item.dataset.name;
                        e.dataTransfer.effectAllowed = 'move';
                        e.dataTransfer.dropEffect = 'move';
                        e.dataTransfer.setData('text/plain', pieceName);
                        e.dataTransfer.setDragImage(item, item.offsetWidth/2, item.offsetHeight/2);
                        item.classList.add('dragging');
                    }});
                    item.addEventListener('dragend', (e) => {{
                        e.stopPropagation();
                        item.classList.remove('dragging');
                    }});
                }});

                dropZones.forEach(zone => {{
                    zone.addEventListener('dragover', (e) => {{
                        e.preventDefault();
                        e.stopPropagation();
                        e.dataTransfer.dropEffect = 'move';
                        zone.classList.add('drag-over');
                    }});
                    zone.addEventListener('dragleave', (e) => {{
                        e.preventDefault();
                        e.stopPropagation();
                        zone.classList.remove('drag-over');
                    }});
                    zone.addEventListener('drop', (e) => {{
                        e.preventDefault();
                        e.stopPropagation();
                        zone.classList.remove('drag-over');

                        const pieceName = e.dataTransfer.getData('text/plain');
                        const zoneName = zone.dataset.name;

                        const nextPieceIndex = completedPieces.length;
                        const expectedPiece = pieceOrder[nextPieceIndex];

                        if (completedPieces.includes(pieceName)) {{
                            showToast('⚠️ 这个部件已经拼过啦！', false);
                        }} else if (pieceName !== expectedPiece) {{
                            showToast(`⚠️ 请先按顺序放置「${{expectedPiece}}」！`, false);
                        }} else if (pieceName !== zoneName) {{
                            showToast('❌ 位置不对哦，再试试！', false);
                        }} else {{
                            const targetPiece = document.getElementById(`piece_${{pieceName}}`);
                            const poolItem = document.getElementById(`pool_${{pieceName}}`);

                            targetPiece.style.display = 'block';
                            poolItem.classList.add('used');
                            targetPiece.classList.add('correct');

                            // 核心修改3：标记当前zone为已完成
                            zone.classList.add('completed');
                            zone.classList.remove('current-zone');

                            completedPieces.push(pieceName);
                            updateProgress();
                            showToast(`✅ 「${{pieceName}}」拼对了！`, true);

                            // 核心修改4：更新下一个可放置的zone
                            setCurrentZone();

                            if (completedPieces.length === totalPieces) {{
                                setTimeout(() => {{
                                    showToast('🎉 恭喜！本关已完成！请点击左侧「解锁下一关」按钮！', true);
                                }}, 800);
                            }}
                        }}
                    }});
                }});
            }}

            // 初始化
            setCurrentZone();
            initConfirmedLevel();  // 如果已通关，初始化已完成状态
        </script>
    </body>
    </html>
    """
    return html_code

# ---------------------- 页面渲染 ----------------------
st.title("🧩 广济桥建造闯关拼图")
st.markdown("#### 跨越千年，亲手还原广济桥的完整建造历程")
st.divider()

# 左右分栏
col_sidebar, col_main = st.columns([2, 3])

# 左侧边栏整合所有操作按钮
with col_sidebar:
    st.subheader("📚 关卡选择")
    for level in LEVEL_CONFIG:
        level_id = level["level_id"]
        if level_id <= st.session_state.unlocked_level:
            if st.button(
                    level["level_name"],
                    use_container_width=True,
                    type="primary" if level_id == st.session_state.current_level else "secondary",
                    key=f"level_btn_{level_id}"
            ):
                st.session_state.current_level = level_id
                st.rerun()
        else:
            st.button(f"🔒 {level['level_name']}", use_container_width=True, disabled=True, key=f"lock_btn_{level_id}")

    st.divider()
    current_level = LEVEL_CONFIG[st.session_state.current_level - 1]
    st.subheader("📜 本关历史背景")
    st.info(current_level["history_desc"])

    st.subheader("🔍 部件线索")
    for piece_name, piece_info in current_level["pieces"].items():
        with st.expander(f"「{piece_name}」线索", expanded=False):
            st.write(piece_info["clue"])

    st.divider()
    # 重置本关按钮（增加：清除通关状态）
    if st.button("🔄 重置本关", use_container_width=True, key="reset_btn"):
        # 如果当前关卡已通关，从 level_confirmed 中移除
        current_level_id = current_level["level_id"]
        if current_level_id in st.session_state.level_confirmed:
            del st.session_state.level_confirmed[current_level_id]
        st.session_state.reset_trigger = not st.session_state.reset_trigger
        st.rerun()

    # 解锁下一关按钮
    current_level_id = current_level["level_id"]
    is_confirmed = current_level_id in st.session_state.level_confirmed
    total_levels = len(LEVEL_CONFIG)

    st.markdown('<div id="confirm-btn-wrapper">', unsafe_allow_html=True)
    if not is_confirmed:
        if st.button("✅ 解锁下一关", use_container_width=True, type="primary", key="confirm_btn"):
            st.session_state.level_confirmed[current_level_id] = True
            if current_level_id < total_levels:
                next_level_id = current_level_id + 1
                if next_level_id > st.session_state.unlocked_level:
                    st.session_state.unlocked_level = next_level_id
            st.balloons()
            st.rerun()
    else:
        if current_level_id < total_levels:
            if st.button("➡️ 前往下一关", use_container_width=True, type="primary", key="next_btn"):
                st.session_state.current_level = current_level_id + 1
                st.rerun()
        else:
            st.button("🏆 已通关全部关卡", use_container_width=True, disabled=True, key="final_btn")
    st.markdown('</div>', unsafe_allow_html=True)

    # 最终通关提示
    if is_confirmed and current_level_id == total_levels:
        st.divider()
        st.success("🏆 恭喜你通关所有关卡！完整还原了广济桥的千年建造历程！")
        # 添加前往其他页面的按钮
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🏠 返回首页", use_container_width=True):
                st.switch_page("首页.py")
        with col2:
            if st.button("🎮 体验启闭式桥梁游戏", use_container_width=True):
                st.switch_page("pages/5_启闭式桥梁交互游戏.py")

# 右侧主内容区
with col_main:
    st.header(current_level["level_name"])
    #游戏规则说明
    with st.expander("🎮 游戏玩法说明（点击展开）", expanded=False):
        st.markdown("""
        - 每个关卡必须按**历史顺序**放置部件。
        - 将下方待选池的图片**拖拽**到背景图的对应区域。
        - 放置正确后部件会固定并高亮。
        - 完成所有部件后，左侧的「解锁下一关」按钮会亮起。
        - 点击「重置本关」可重新开始当前关卡。
        """)

    if is_confirmed:
        st.success(f"✅ 本关已确认通关！", icon="🎉")
    else:
        st.info("💡 提示：拼完所有部件后，左侧「解锁下一关」按钮会自动解锁")

    st.divider()

    # 渲染拼图iframe（传入 is_confirmed 参数）
    html_content = generate_puzzle_html(current_level, st.session_state.reset_trigger, is_confirmed)
    components.html(
        html_content,
        height=BG_ORIGIN_SIZE["height"] * 0.8 + 150,
        width=MAX_DISPLAY_WIDTH
    )

render_footer_nav()