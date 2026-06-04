# Web Scraper Tool

一个简洁的网页内容爬取工具，支持内容预览、多格式下载和 AI 智能分析。

## 功能特性

- 输入链接，自动爬取网页内容
- 内容实时预览
- 多格式下载（Markdown / TXT / HTML）
- AI 驱动的网页内容分析总结

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | React 18 + Vite |
| 后端 | Flask |
| 爬虫 | Playwright (Chromium) + BeautifulSoup4 |
| AI 分析 | Minimax API (Claude 兼容格式) |

## 项目结构

```
web-scraper-tool/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── .env
│   ├── requirements.txt
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── scrape.py
│   │   ├── analyze.py
│   │   └── download.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── scraper_service.py
│   │   ├── analyzer_service.py
│   │   └── converter_service.py
│   └── utils/
│       ├── __init__.py
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
│       └── services/
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
playwright install chromium
```

### 3. 配置环境变量
创建 `backend/.env` 文件：
```env
AI_PROVIDER=minimax
MINIMAX_API_KEY=your_key_here
MINIMAX_API_URL=https://api.minimaxi.com/anthropic/v1
FLASK_PORT=5000
PROXY_PORT=7897
```

### 4. 启动后端
```bash
python app.py
```
后端运行在 `http://localhost:5000`

### 5. 启动前端
```bash
cd frontend
npm install
npm run dev
```
前端运行在 `http://localhost:5173`

## API 文档

### POST /api/scrape
**请求：**
```json
{"url": "https://example.com"}
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
**请求：**
```json
{"content": "网页正文内容"}
```
**响应：**
```json
{
  "success": true,
  "data": {"summary": "AI 分析总结"}
}
```

### POST /api/download
**请求：**
```json
{
  "content": "正文内容",
  "html": "原始 HTML（可选）",
  "title": "页面标题",
  "format": "markdown" | "txt" | "html"
}
```
**响应：** 文件流

## 注意事项

- 爬虫使用 Playwright，需安装 Chromium 并确保代理正常
- 百度/知乎等网站有强反爬机制，可能无法爬取
- HTML 下载可获取原始页面（保留完整格式）
- AI 分析使用 Claude 兼容格式，需使用正确的 API Key

## 许可证
MIT
