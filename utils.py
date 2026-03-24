# utils.py 广济桥科普系统公共工具函数
import streamlit as st
import os

# ====================== 路径统一管理 ======================
def get_base_path() -> str:
    """
    统一获取项目根目录（桥文件夹）的绝对路径
    因为「代码」、「图片素材」、「数据集」是同级文件夹
    """
    # 调用方的文件路径
    import inspect
    caller_file = inspect.stack()[1].filename
    caller_dir = os.path.dirname(os.path.abspath(caller_file))
    
    # 判断当前位置
    if os.path.basename(caller_dir) == "pages":
        # 在 pages 文件夹内：代码/pages/xxx.py -> 向上两级到「桥」
        return os.path.dirname(os.path.dirname(caller_dir))
    elif os.path.basename(caller_dir) == "代码":
        # 在 代码 文件夹内：代码/首页.py -> 向上一级到「桥」
        return os.path.dirname(caller_dir)
    else:
        # 兜底
        return caller_dir

def get_img_path(relative_path: str) -> str:
    """
    获取图片素材的完整路径
    :param relative_path: 相对于「图片素材」文件夹的路径，比如 "始建阶段/初始浮桥.jpg"
    :return: 图片完整绝对路径
    """
    base_path = get_base_path()
    return os.path.join(base_path, "图片素材", relative_path)

def get_puzzle_assets_path() -> str:
    """获取拼图素材文件夹的路径"""
    return os.path.join(get_base_path(), "图片素材","广济桥拼图")

def get_data_path(file_name: str) -> str:
    """获取数据集文件的完整路径"""
    base_path = get_base_path()
    return os.path.join(base_path, "数据集", file_name)

# ====================== 页面通用组件 ======================
def back_to_home_btn():
    """统一的返回首页按钮"""
    if st.button("← 返回首页", use_container_width=False):
        st.switch_page("首页.py")

def render_references():
    """统一渲染参考文献，避免每个页面重复写"""
    st.divider()
    st.subheader("📚 参考文献与史料来源")
    st.caption("""
    本作品所有史料、技术内容均来自权威学术文献与官方资料，具体如下：
    1.  庄志平,陈皓瑾. 宋至清潮州广济桥营造技术考析[J]. 岭南文史, 2024(04):44-54.
    2.  吴国智. 广济桥亭台楼阁复建设计[J]. 古建园林技术, 2006(01):52-58.
    3.  杜娟. 潮州广济桥建筑装饰艺术的审美向度与文化意蕴[J]. 美术大观, 2012(06):238-239.
    4.  黄挺. 古代桥梁的代表作广济桥[J]. 广东史志, 1998(02):6-10.
    5.  沈启绵. 别具特色的潮州人文景观(三则)[J]. 广东史志, 1996(02):73-76.
    6.  广济桥百度百科权威词条
    """)

def safe_load_image(relative_path: str, caption: str = "", use_container_width: bool = True):
    """
    安全加载图片，自带容错处理
    """
    img_path = get_img_path(relative_path)
    try:
        st.image(img_path, caption=caption, use_container_width=use_container_width)
    except Exception as e:
        st.warning(f"⚠️ 图片加载失败，请检查路径：{relative_path}，错误信息：{str(e)}")

def render_footer_nav():
    """在所有分页底部渲染快速导航按钮，方便跳转到其他页面"""
    st.divider()
    st.subheader("🚀 快速跳转")
    cols = st.columns(5)
    with cols[0]:
        if st.button("🏗️ 建造历程", use_container_width=True):
            st.switch_page("pages/1_建造技艺全流程拆解.py")
    with cols[1]:
        if st.button("🎮 启闭模拟", use_container_width=True):
            st.switch_page("pages/2_启闭式桥梁交互模拟.py")
    with cols[2]:
        if st.button("❓ 科普问答", use_container_width=True):
            st.switch_page("pages/3_广济桥科普问答.py")
    with cols[3]:
        if st.button("🧩 建造拼图", use_container_width=True, type="primary"):
            st.switch_page("pages/4_广济桥建造拼图.py")
    with cols[4]:
        if st.button("🎯 交互游戏", use_container_width=True, type="primary"):
            st.switch_page("pages/5_启闭式桥梁交互游戏.py")