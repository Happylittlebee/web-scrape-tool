from flask import Blueprint, request, jsonify, make_response
from services import convert_to_markdown, convert_to_txt

download_bp = Blueprint("download", __name__)


@download_bp.route("/api/download", methods=["POST"])
def download():
    """下载网页内容为指定格式"""
    data = request.get_json()

    if not data:
        return jsonify({"success": False, "error": "请求体不能为空"}), 400

    content = data.get("content", "").strip()
    html = data.get("html", "").strip()
    title = data.get("title", "untitled")
    fmt = data.get("format", "txt").lower()

    if not content and not html:
        return jsonify({"success": False, "error": "内容不能为空"}), 400

    # 生成安全文件名
    safe_title = "".join(c if c.isalnum() or c in " -_" else "_" for c in title)[:50]
    safe_title = safe_title or "untitled"

    try:
        if fmt == "markdown":
            file_content = convert_to_markdown(content, title)
            mimetype = "text/markdown"
            ext = "md"
        elif fmt == "txt":
            file_content = convert_to_txt(content, title)
            mimetype = "text/plain"
            ext = "txt"
        elif fmt == "html":
            file_content = html
            mimetype = "text/html; charset=utf-8"
            ext = "html"
        else:
            return jsonify({"success": False, "error": "不支持的下载格式"}), 400

        response = make_response(file_content)
        response.headers["Content-Type"] = mimetype
        response.headers["Content-Disposition"] = f"attachment; filename=\"{safe_title}.{ext}\""
        return response

    except Exception:
        return jsonify({"success": False, "error": "下载失败"}), 500