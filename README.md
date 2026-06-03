# Web Scraper Tool

一个简洁的网页内容爬取工具，支持内容预览、格式下载和 AI 智能分析。

## 功能特性

- 输入链接，自动爬取网页内容
- 内容实时预览
- 多格式下载（Markdown / TXT）
- AI 驱动的网页内容分析总结

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | React 18 + Vite |
| 后端 | Flask |
| 爬虫 | requests + BeautifulSoup4 |
| AI 分析 | Minimax API（支持多模型扩展） |

## 项目结构

```
web-scraper-tool/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── routes/
│   │   ├── __init__.py               # 路由包初始化
│   │   ├── scrape.py
│   │   ├── analyze.py
│   │   └── download.py
│   ├── services/
│   │   ├── __init__.py               # 服务包初始化
│   │   ├── scraper_service.py
│   │   ├── analyzer_service.py
│   │   └── converter_service.py
│   └── utils/
│       ├── __init__.py               # 工具包初始化
│       ├── html_parser.py
│       └── text_cleaner.py
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       ├── App.css
│       ├── components/
│       ├── hooks/
│       ├── services/
│       └── utils/
└── README.md
```

## 快速开始

### 1. 克隆项目

```bash
git clone <repository-url>
cd web-scraper-tool
```

### 2. 安装后端依赖

```bash
cd backend
pip install -r requirements.txt
```

### 3. 配置环境变量

在 `backend/` 目录下创建 `.env` 文件：

```env
AI_PROVIDER=minimax
MINIMAX_API_KEY=your_api_key_here
MINIMAX_API_URL=https://api.minimax.chat/v1
FLASK_PORT=5000
```

### 4. 启动后端

```bash
python app.py
```

后端运行在 `http://localhost:5000`

### 5. 安装前端依赖并启动

```bash
cd frontend
npm install
npm run dev
```

前端运行在 `http://localhost:5173`

### 6. 配置 AI 模型

在 `.env` 文件中配置使用的 AI API：

```env
# Minimax API（当前默认）
AI_PROVIDER=minimax
MINIMAX_API_KEY=your_api_key_here
MINIMAX_API_URL=https://api.minimax.chat/v1

# 后续可扩展为 OpenAI / Claude 等
# AI_PROVIDER=openai
# OPENAI_API_KEY=your_api_key_here
```

## API 文档

### POST /api/scrape

爬取网页内容

**请求体：**
```json
{
  "url": "https://example.com"
}
```

**响应：**
```json
{
  "success": true,
  "data": {
    "title": "页面标题",
    "content": "提取的正文文本",
    "html": "原始 HTML"
  }
}
```

### POST /api/analyze

AI 分析网页内容

**请求体：**
```json
{
  "content": "网页正文内容"
}
```

**响应：**
```json
{
  "success": true,
  "data": {
    "summary": "AI 生成的分析总结"
  }
}
```

### POST /api/download

下载网页内容

**请求体：**
```json
{
  "content": "网页正文内容",
  "title": "页面标题",
  "format": "markdown" | "txt"
}
```

**响应：** 文件流

## 开发说明

- 前端开发使用 Vite 热更新，无需重启
- 后端修改后自动重载（启用 debug 模式）
- API 请求统一通过 `frontend/src/services/api.js` 封装

## 许可证

MIT
