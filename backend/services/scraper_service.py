import requests
from utils import extract_main_content, clean_text

PROXIES = {
    "http": "http://127.0.0.1:7897",
    "https": "http://127.0.0.1:7897",
}


def scrape_url(url: str) -> tuple[str, str, str]:
    """
    爬取指定 URL 的网页内容。

    Args:
        url: 目标网页 URL

    Returns:
        tuple: (title, content, html) - 标题、正文、原始 HTML

    Raises:
        Exception: 无法访问网页时抛出
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }

    response = requests.get(url, headers=headers, proxies=PROXIES, timeout=15)
    response.raise_for_status()

    # 自动检测编码，避免中文乱码
    encoding = response.apparent_encoding
    if encoding.lower() in ("gb2312", "gbk", "gb18030"):
        encoding = "gbk"
    else:
        encoding = "utf-8"

    html = response.content.decode(encoding, errors="replace")
    title, content = extract_main_content(html)
    content = clean_text(content)

    if not content:
        raise ValueError("无法提取网页正文内容")

    return title, content, html
