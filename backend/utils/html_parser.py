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
    # 优先查找正文容器
    container = _find_content_container(soup)

    if not container:
        container = soup

    # 移除 header、footer、nav 等非内容标签
    for tag in container.find_all(["header", "footer", "nav", "aside", "form", "menu"]):
        tag.decompose()

    # 将 <br> 替换为换行符
    for br in container.find_all("br"):
        br.replace_with("\n")

    # 获取文本，用双换行分隔段落
    paragraphs = []
    seen_texts = set()  # 用于去重

    for tag in container.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "li",
                                   "div", "span", "td", "th", "blockquote", "pre"]):
        text = tag.get_text(strip=True)
        # 去重：跳过太短的文本和重复文本
        if text and len(text) > 5 and text not in seen_texts:
            paragraphs.append(text)
            seen_texts.add(text)

    if not paragraphs:
        # 兜底：递归获取所有文字节点
        paragraphs = _recursive_extract(container)

    return "\n\n".join(paragraphs)


def _find_content_container(soup: BeautifulSoup):
    """
    查找正文内容容器。

    尝试多种常见的选择器，找到包含实际文章内容的容器。
    """
    # 按优先级尝试不同的选择器
    selectors = [
        # 博客园
        {"id": "cnblogs_post_body"},
        # 知乎
        {"class": "RichText"},
        {"class": "article-content"},
        # CSDN
        {"id": "content_views"},
        {"class": "htmledit_views"},
        # 通用
        {"class": "article-content"},
        {"class": "post-content"},
        {"class": "entry-content"},
        {"class": "post-body"},
        {"id": "article-body"},
        # 标准标签
        "article",
        "main",
    ]

    for selector in selectors:
        if isinstance(selector, str):
            # 标签名
            element = soup.find(selector)
        elif isinstance(selector, dict):
            if "id" in selector:
                element = soup.find(id=selector["id"])
            elif "class" in selector:
                element = soup.find(class_=selector["class"])
            else:
                continue
        else:
            continue

        if element:
            return element

    return None


def _recursive_extract(element, depth=0) -> list:
    """递归提取所有文字节点"""
    if depth > 10:
        return []

    texts = []
    seen = set()
    for child in element.children:
        if hasattr(child, "name") and child.name:
            if child.name in ["script", "style", "noscript", "iframe", "svg"]:
                continue
            child_texts = _recursive_extract(child, depth + 1)
            for t in child_texts:
                if t not in seen:
                    texts.append(t)
                    seen.add(t)
        else:
            text = str(child).strip()
            if text and text not in seen:
                texts.append(text)
                seen.add(text)

    return texts
