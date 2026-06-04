import asyncio
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from utils import extract_main_content, clean_text

PROXIES = {
    "http": "http://127.0.0.1:7897",
    "https": "http://127.0.0.1:7897",
}


def scrape_url(url: str) -> tuple[str, str, str]:
    """
    使用 Playwright 爬取指定 URL 的网页内容。

    Args:
        url: 目标网页 URL

    Returns:
        tuple: (title, content, html) - 标题、正文、原始 HTML

    Raises:
        Exception: 无法访问网页时抛出
    """
    extra_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
    }

    def _scrape():
        with sync_playwright() as p:
            print(f"[DEBUG] 启动浏览器，代理: {PROXIES}")
            browser = p.chromium.launch(
                headless=True,
                proxy={
                    "server": "http://127.0.0.1:7897",
                    "bypass": "",
                }
            )
            context = browser.new_context(
                extra_http_headers=extra_headers,
                ignore_https_errors=True,
            )
            page = context.new_page()

            try:
                print(f"[DEBUG] 访问 URL: {url}")
                page.goto(url, wait_until="networkidle", timeout=30000)
                print(f"[DEBUG] 页面加载完成，等待 JS 执行...")
                page.wait_for_load_state("domcontentloaded")
                page.wait_for_timeout(2000)

                html = page.content()
                title = page.title()
                print(f"[DEBUG] 获取到 HTML 长度: {len(html)}, title: {title}")

                # 保存 HTML 到文件
                with open("debug.html", "w", encoding="utf-8") as f:
                    f.write(html)
                print("[DEBUG] HTML 已保存到 debug.html")

                # 调试：统计标签数量
                debug_soup = BeautifulSoup(html, "html.parser")
                articles = debug_soup.find_all("article")
                mains = debug_soup.find_all("main")
                divs = debug_soup.find_all("div")
                print(f"[DEBUG] article 数量: {len(articles)}, main 数量: {len(mains)}, div 数量: {len(divs)}")

                return title, html
            except Exception as e:
                print(f"[DEBUG] 浏览器访问失败: {e}")
                raise
            finally:
                browser.close()
                print(f"[DEBUG] 浏览器已关闭")

    try:
        title, html = _scrape()
    except Exception as e:
        print(f"[DEBUG] 爬取异常: {e}")
        raise Exception(f"无法访问该 URL: {str(e)}")

    print(f"[DEBUG] 提取正文...")
    extracted_title, content = extract_main_content(html)
    if not title:
        title = extracted_title
        print(f"[DEBUG] 使用提取的标题: {title}")

    content = clean_text(content)
    print(f"[DEBUG] 正文长度: {len(content)}")

    if not content:
        print(f"[DEBUG] 正文为空")
        raise ValueError("无法提取网页正文内容")

    return title, content, html
