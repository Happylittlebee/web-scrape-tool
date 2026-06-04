import requests
from config import Config

PROXIES = {
    "http": "http://127.0.0.1:7897",
    "https": "http://127.0.0.1:7897",
}


def analyze_content(content: str) -> str:
    content = content[:5000]

    if Config.AI_PROVIDER == "minimax":
        return _analyze_with_minimax(content)
    else:
        raise ValueError(f"不支持的 AI 提供商: {Config.AI_PROVIDER}")


def _analyze_with_minimax(content: str) -> str:
    headers = {
        "Authorization": f"Bearer {Config.MINIMAX_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "MiniMax-M2.7",
        "messages": [
            {
                "role": "user",
                "content": f"请简要总结以下网页内容，用中文输出关键信息：\n\n{content}"
            }
        ],
        "max_tokens": 500,
    }

    response = requests.post(
        f"{Config.MINIMAX_API_URL}/messages",
        headers=headers,
        json=payload,
        proxies=PROXIES,
        timeout=30,
    )
    response.raise_for_status()

    result = response.json()
    content_list = result.get("content", [])
    for item in content_list:
        if item.get("type") == "text":
            return item.get("text", "分析失败")
    return "分析失败"
