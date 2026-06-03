from bs4 import BeautifulSoup


def extract_main_content(html: str) -> tuple[str, str]:
    """
    从 HTML 中提取正文内容和标题。

    Returns:
        tuple: (title, content) - 页面标题和纯文本正文
    """
    soup = BeautifulSoup(html, "html.parser")

    # 移除脚本、样式和注释
    for tag in soup(["script", "style", "noscript", "iframe", "svg"]):
        tag.decompose()

    # 提取标题
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else ""

    # 尝试从 meta 标签获取备用标题
    if not title:
        og_title = soup.find("meta", property="og:title")
        if og_title:
            title = og_title.get("content", "")

    # 提取正文
    content = _extract_text(soup)

    return title, content


def _extract_text(soup: BeautifulSoup) -> str:
    """从 soup 对象中提取纯文本"""
    # 优先查找 article 或 main 标签
    main = soup.find("article") or soup.find("main") or soup.find("body")

    if not main:
        main = soup

    # 移除 header、footer、nav 等非内容标签
    for tag in main.find_all(["header", "footer", "nav", "aside"]):
        tag.decompose()

    # 获取文本，用双换行分隔段落
    paragraphs = []
    for p in main.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "li"]):
        text = p.get_text(strip=True)
        if text:
            paragraphs.append(text)

    return "\n\n".join(paragraphs)