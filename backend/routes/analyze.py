from flask import Blueprint, request, jsonify
from services import analyze_content

analyze_bp = Blueprint("analyze", __name__)


@analyze_bp.route("/api/analyze", methods=["POST"])
def analyze():
    """AI 分析网页内容"""
    data = request.get_json()

    if not data or "content" not in data:
        return jsonify({"success": False, "error": "缺少 content 参数"}), 400

    content = data["content"].strip()

    if not content:
        return jsonify({"success": False, "error": "内容不能为空"}), 400

    try:
        summary = analyze_content(content)
        return jsonify({
            "success": True,
            "data": {"summary": summary}
        })
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception:
        return jsonify({"success": False, "error": "AI 服务暂时不可用"}), 500