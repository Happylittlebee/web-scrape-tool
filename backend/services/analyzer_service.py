import requests
from config import Config


def analyze_content(content: str) -> str:
    """
    调用 AI API 分析网页内容并生成总结。

    Args:
        content: 网页正文内容（限制 5000 字符）

    Returns:
        str: AI 生成的总结内容

    Raises:
        Exception: AI 服务不可用时抛出
    """
    # 截断内容
    content = content[:5000]

    if Config.AI_PROVIDER == "minimax":
        return _analyze_with_minimax(content)
    else:
        raise ValueError(f"不支持的 AI 提供商: {Config.AI_PROVIDER}")


def _analyze_with_minimax(content: str) -> str:
    """使用 Minimax API 分析内容"""
    headers = {
        "Authorization": f"Bearer {Config.MINIMAX_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "minimax",
        "messages": [
            {
                "role": "user",
                "content": f"请简要总结以下网页内容，用中文输出关键信息：\n\n{content}"
            }
        ],
        "max_tokens": 500,
    }

    response = requests.post(
        f"{Config.MINIMAX_API_URL}/text/chatcompletion_v2",
        headers=headers,
        json=payload,
        timeout=30,
    )
    response.raise_for_status()

    result = response.json()
    return result.get("choices", [{}])[0].get("message", {}).get("content", "分析失败")