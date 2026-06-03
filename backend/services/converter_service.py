from markdownify import markdownify


def convert_to_markdown(html: str, title: str = "") -> str:
    """
    将 HTML 转换为 Markdown 格式。

    Args:
        html: 原始 HTML 内容
        title: 页面标题（用作标题）

    Returns:
        str: Markdown 格式文本
    """
    md = markdownify(html, heading_style="atx")

    # 添加标题
    if title:
        md = f"# {title}\n\n{md}"

    return md


def convert_to_txt(html: str, title: str = "") -> str:
    """
    将 HTML 转换为纯文本格式。

    Args:
        html: 原始 HTML 内容
        title: 页面标题（用作标题）

    Returns:
        str: 纯文本格式
    """
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")

    # 移除非内容标签
    for tag in soup(["script", "style", "nav", "header", "footer"]):
        tag.decompose()

    # 提取文本
    text = soup.get_text(separator="\n\n")

    # 清理空白
    import re
    text = re.sub(r"\n{3,}", "\n\n", text)

    # 添加标题
    if title:
        text = f"{title}\n{'=' * len(title)}\n\n{text}"

    return text.strip()