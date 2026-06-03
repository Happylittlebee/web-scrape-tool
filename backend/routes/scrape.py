from flask import Blueprint, request, jsonify
from services import scrape_url

scrape_bp = Blueprint("scrape", __name__)


@scrape_bp.route("/api/scrape", methods=["POST"])
def scrape():
    """爬取指定 URL 的网页内容"""
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"success": False, "error": "缺少 url 参数"}), 400

    url = data["url"].strip()

    if not url.startswith(("http://", "https://")):
        return jsonify({"success": False, "error": "URL 必须以 http:// 或 https:// 开头"}), 400

    try:
        title, content, html = scrape_url(url)
        return jsonify({
            "success": True,
            "data": {
                "title": title,
                "content": content,
                "html": html,
            }
        })
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception:
        return jsonify({"success": False, "error": "无法访问该 URL 或内容为空"}), 500