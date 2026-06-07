# CLAUDE.md

本文件为 Claude Code 在本代码仓库中工作时提供指导。

## 项目概述

Web Scraper Tool - 网页内容爬取工具，支持内容预览、多格式下载和 AI 智能分析。

## 项目结构

```
web-scraper-tool/
├── backend/                    # Flask 后端 (Python)
│   ├── app.py                  # 应用入口
│   ├── config.py               # 配置
│   ├── .env                    # 环境变量
│   ├── requirements.txt        # Python 依赖
│   ├── routes/                 # API 路由
│   ├── services/               # 业务逻辑
│   └── utils/                  # 工具函数
├── frontend/                   # React + Vite 前端
│   ├── src/
│   │   ├── components/         # UI 组件
│   │   ├── hooks/              # React Hooks
│   │   ├── services/           # API 调用
│   │   └── App.jsx             # 主组件
│   └── package.json
└── PRD.md / README.md          # 文档
```

## 开发环境

### 后端
```bash
cd backend
pip install -r requirements.txt
playwright install chromium    # 安装浏览器
python app.py                   # 启动后端 http://localhost:5000
```

### 前端
```bash
cd frontend
npm install
npm run dev                    # 启动前端 http://localhost:5173
```

### 环境变量 (backend/.env)
```
# AI 提供商：minimax / openai / claude 等
AI_PROVIDER=minimax

# AI API Key（必填）
MINIMAX_API_KEY=your_key_here

# AI API URL（根据提供商填写）
# Minimax: https://api.minimaxi.com/anthropic/v1
# OpenAI: https://api.openai.com/v1
# Claude: https://api.anthropic.com/v1
MINIMAX_API_URL=https://api.minimaxi.com/anthropic/v1

# Flask 端口（默认 5000）
FLASK_PORT=5000

# 代理端口（如需访问外网则配置）
PROXY_PORT=7897
```

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | React 18 + Vite |
| 后端 | Flask |
| 爬虫 | Playwright (Chromium) + BeautifulSoup |
| AI 分析 | Minimax API (Claude 兼容格式) |

## API 接口

| 方法 | 路径 | 描述 |
|------|------|------|
| POST | /api/scrape | 爬取网页内容 |
| POST | /api/analyze | AI 分析内容 |
| POST | /api/download | 下载（支持 markdown/txt/html） |

## 注意事项

- 爬虫使用 Playwright，需安装 Chromium 并确保代理正常
- 百度/知乎等网站有强反爬机制，可能无法爬取
- HTML 下载可获取原始页面（保留完整格式）
- AI 分析使用 Claude 兼容 API 格式（/messages 端点）
- 遇到 402 错误需检查 API Key 是否正确
