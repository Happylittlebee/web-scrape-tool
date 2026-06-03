import re


def clean_text(text: str) -> str:
    """
    清洗文本：去除多余空白、特殊字符、控制符。
    """
    if not text:
        return ""

    # 替换多个空白字符为单个空格
    text = re.sub(r"[ \t]+", " ", text)

    # 替换多个换行符为最多两个换行
    text = re.sub(r"\n{3,}", "\n\n", text)

    # 去除控制字符
    text = re.sub(r"[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f]", "", text)

    # 去除行首行尾空白
    lines = [line.strip() for line in text.split("\n")]
    text = "\n".join(lines)

    return text