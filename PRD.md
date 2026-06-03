# 网页内容爬取工具 - 产品需求文档 (PRD)

## 1. 产品概述

### 1.1 产品简介

**产品名称：** Web Scraper Tool

**产品类型：** 前后端分离的 Web 应用工具

**一句话描述：** 一款简洁高效的网页内容爬取工具，支持内容预览、多格式下载和 AI 智能分析总结。

### 1.2 目标用户

- 需要快速获取网页内容的研究人员
- 需要提取网页信息进行二次整理的工作者
- 希望借助 AI 快速理解长篇文章的读者

---

## 2. 功能需求

### 2.1 核心功能

| 功能 | 描述 | 优先级 |
|------|------|--------|
| URL 输入 | 用户在前端页面输入目标网页链接 | P0 |
| 内容爬取 | 后端自动爬取网页，提取正文内容 | P0 |
| 内容预览 | 实时在页面展示爬取到的内容 | P0 |
| 格式下载 | 支持 Markdown / TXT 格式下载 | P1 |
| AI 分析 | 调用 AI 对网页内容进行总结分析 | P1 |

### 2.2 用户交互流程

```
┌─────────────┐
│ 输入 URL    │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│ 点击爬取按钮      │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐     ┌─────────────────┐
│ 显示加载状态     │────▶│ 展示内容预览     │
└─────────────────┘     └────────┬────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
           ┌─────────────────┐       ┌─────────────────┐
           │ 点击「下载」按钮   │       │ 点击「AI 分析」按钮 │
           └────────┬────────┘       └────────┬────────┘
                    │                           │
                    ▼                           ▼
           ┌─────────────────┐       ┌─────────────────┐
           │ 选择格式并下载    │       │ 展示 AI 总结结果  │
           └─────────────────┘       └─────────────────┘
```

### 2.3 数据流转

```
URL 输入
    │
    ▼
前端 POST /api/scrape { url }
    │
    ▼
后端爬取网页 ──▶ 提取正文 ──▶ 返回 { title, content, html }
    │
    ▼
前端渲染 ContentPreview
    │
    ├──[下载]──▶ POST /api/download ──▶ 文件流
    │
    └──[分析]──▶ POST /api/analyze ──▶ AI 总结结果
```

---

## 3. 技术架构

### 3.1 技术栈

| 层级 | 技术选型 | 说明 |
|------|----------|------|
| 前端框架 | React 18 + Vite | 快速开发，热更新 |
| 前端状态 | React Hooks (useState/useEffect) | 轻量级，无需 Redux |
| 前端 HTTP | 原生 fetch API | 无需额外依赖 |
| 后端框架 | Flask | 轻量级 Python Web 框架 |
| 爬虫 | requests + BeautifulSoup4 | 成熟稳定的爬虫方案 |
| AI 服务 | Minimax API（支持多模型扩展） | 成本效益高的 AI 分析 |
| 格式转换 | markdownify | HTML 转 Markdown |
| 跨域支持 | flask-cors | 前后端分离部署 |

### 3.2 系统架构图

```
┌─────────────────────────────────────────────────────────┐
│                      用户浏览器                          │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │ URL 输入框  │  │  内容预览区域  │  │ 操作按钮区域   │  │
│  └──────┬──────┘  └──────▲───────┘  └───────▲───────┘  │
│         │                │                   │           │
└─────────┼────────────────┼───────────────────┼───────────┘
          │                │                   │
          │   HTTP 请求     │   JSON 响应       │
          ▼                │                   │
┌─────────────────┐         │                   │
│   React 前端     │─────────┘                   │
│  (localhost:5173)│                             │
└────────┬────────┘                              │
         │                                        │
         │ API 调用 (CORS)                        │
         ▼                                        │
┌─────────────────────────────────────────────────┐
│                  Flask 后端                      │
│  ┌────────────┐  ┌────────────┐  ┌──────────┐  │
│  │ /api/scrape │  │ /api/analyze│  │ /api/download│ │
│  └─────┬──────┘  └──────┬─────┘  └─────┬─────┘  │
│        │                │               │        │
└────────┼────────────────┼───────────────┼────────┘
         │                │               │
         ▼                ▼               ▼
    ┌─────────┐    ┌───────────┐   ┌──────────┐
    │ 爬虫模块 │    │ AI 分析模块 │   │ 文件转换 │
    │(requests)│    │(多模型支持)│   │ (Markdown)│
    └─────────┘    └───────────┘   └──────────┘
```

---

## 4. 项目结构

### 4.1 目录结构

```
web-scraper-tool/
│
├── backend/                          # Flask 后端
│   ├── app.py                        # Flask 主入口，路由注册
│   ├── config.py                     # 配置文件（API 密钥、端口等）
│   ├── requirements.txt              # Python 依赖
│   │
│   ├── routes/                       # 路由层（接收请求）
│   │   ├── __init__.py               # 路由包初始化
│   │   ├── scrape.py                 # /api/scrape - 爬取网页
│   │   ├── analyze.py                # /api/analyze - AI 分析
│   │   └── download.py               # /api/download - 文件下载
│   │
│   ├── services/                     # 业务逻辑层（核心处理）
│   │   ├── __init__.py               # 服务包初始化
│   │   ├── scraper_service.py        # 爬虫核心逻辑
│   │   ├── analyzer_service.py       # AI 分析逻辑
│   │   └── converter_service.py       # 格式转换逻辑
│   │
│   └── utils/                        # 工具函数层
│       ├── __init__.py               # 工具包初始化
│       ├── html_parser.py            # HTML 解析工具
│       └── text_cleaner.py           # 文本清洗工具
│
├── frontend/                         # React 前端
│   ├── package.json                  # npm 依赖配置
│   ├── vite.config.js                # Vite 构建配置
│   ├── index.html                    # HTML 入口
│   │
│   ├── src/
│   │   ├── main.jsx                  # React 入口文件
│   │   ├── App.jsx                   # 主应用组件
│   │   ├── App.css                   # 主样式文件
│   │   │
│   │   ├── components/               # UI 组件目录
│   │   │   ├── UrlInput.jsx          # URL 输入框组件
│   │   │   ├── ContentPreview.jsx    # 内容预览组件
│   │   │   ├── ActionButtons.jsx     # 操作按钮组组件
│   │   │   ├── LoadingSpinner.jsx     # 加载状态组件
│   │   │   └── ErrorMessage.jsx       # 错误提示组件
│   │   │
│   │   ├── hooks/                    # 自定义 Hooks 目录
│   │   │   ├── useScraper.js         # 爬取逻辑 Hook
│   │   │   └── useAnalyzer.js         # 分析逻辑 Hook
│   │   │
│   │   ├── services/                 # API 调用目录
│   │   │   └── api.js                # 统一封装后端 API 调用
│   │   │
│   │   └── utils/                    # 工具函数目录
│   │       └── formatters.js         # 格式化工具
│   │
│   └── public/                      # 静态资源目录
│
├── .gitignore                        # Git 忽略配置
└── README.md                          # 项目说明文档
```

### 4.2 文件职责矩阵

#### 后端文件

| 文件路径 | 职责 | 依赖模块 |
|----------|------|----------|
| `app.py` | Flask 应用启动，注册蓝图，配置 CORS | flask, flask-cors |
| `config.py` | 存储 API 密钥、端口等配置 | os |
| `routes/scrape.py` | 接收 URL 参数，调用爬虫服务 | flask, scraper_service |
| `routes/analyze.py` | 接收文本内容，调用 AI 服务 | flask, analyzer_service |
| `routes/download.py` | 接收内容和格式，返回文件流 | flask, converter_service |
| `services/scraper_service.py` | 用 requests 爬取网页，BeautifulSoup 解析 | requests, bs4 |
| `services/analyzer_service.py` | 调用 AI API（支持多模型）进行内容总结 | requests, 支持多AI提供商 |
| `services/converter_service.py` | 将 HTML 转为 Markdown/TXT | markdownify |
| `utils/html_parser.py` | 提取正文、去除广告脚本、样式标签 | bs4 |
| `utils/text_cleaner.py` | 清洗多余空白、特殊字符 | re |

#### 前端文件

| 文件路径 | 职责 | 依赖 |
|----------|------|------|
| `main.jsx` | React 挂载到 DOM | react, react-dom |
| `App.jsx` | 状态管理（URL、content、summary、loading、error） | react, hooks, components |
| `components/UrlInput.jsx` | URL 输入框，带校验和提交 | react |
| `components/ContentPreview.jsx` | 渲染爬取到的网页内容，支持 HTML 渲染 | react, dompurify |
| `components/ActionButtons.jsx` | 下载按钮（Markdown/TXT）、AI 分析按钮 | react |
| `components/LoadingSpinner.jsx` | 加载动画组件 | react |
| `components/ErrorMessage.jsx` | 错误提示展示组件 | react |
| `hooks/useScraper.js` | 管理爬取请求的 Hook，封装 loading/error 状态 | react |
| `hooks/useAnalyzer.js` | 管理分析请求的 Hook，封装 loading/error 状态，支持多 AI 模型 | react |
| `services/api.js` | 统一封装 fetch 调用后端 API | 原生 fetch |
| `utils/formatters.js` | 文本截断、格式规范化等工具函数 | - |

---

## 5. API 设计与数据格式

### 5.1 接口列表

| 方法 | 路径 | 描述 |
|------|------|------|
| POST | `/api/scrape` | 爬取指定 URL 的网页内容 |
| POST | `/api/analyze` | AI 分析网页内容并返回总结 |
| POST | `/api/download` | 下载网页内容为指定格式文件 |

### 5.2 接口详细设计

#### POST /api/scrape

爬取网页内容

**请求：**
```json
{
  "url": "https://example.com/article"
}
```

**成功响应 (200)：**
```json
{
  "success": true,
  "data": {
    "title": "页面标题",
    "content": "提取的正文文本（纯文本）",
    "html": "原始 HTML 内容"
  }
}
```

**失败响应 (400/500)：**
```json
{
  "success": false,
  "error": "无法访问该 URL 或内容为空"
}
```

#### POST /api/analyze

AI 分析网页内容

**请求：**
```json
{
  "content": "网页正文内容，限制 5000 字符"
}
```

**成功响应 (200)：**
```json
{
  "success": true,
  "data": {
    "summary": "AI 生成的分析总结内容"
  }
}
```

**失败响应 (400/500)：**
```json
{
  "success": false,
  "error": "AI 服务暂时不可用"
}
```

#### POST /api/download

下载网页内容

**请求：**
```json
{
  "content": "网页正文内容",
  "title": "页面标题（用作文件名）",
  "format": "markdown" | "txt"
}
```

**成功响应 (200)：**
- Content-Type: `text/markdown` 或 `text/plain`
- Content-Disposition: `attachment; filename="页面标题.md"`

**失败响应 (400/500)：**
```json
{
  "success": false,
  "error": "不支持的下载格式"
}
```

---

## 6. 前端组件设计

### 6.1 组件结构

```
App
├── UrlInput (URL 输入框)
├── ContentPreview (内容预览)
│   └── [条件渲染] LoadingSpinner / ErrorMessage
└── ActionButtons (操作按钮组)
    ├── DownloadDropdown (下载格式选择)
    │   ├── DownloadMarkdown
    │   └── DownloadTxt
    └── AnalyzeButton (AI 分析)
```

### 6.2 组件状态

| 组件 | 状态 |
|------|------|
| App | url, content, html, title, summary, loading, error |
| UrlInput | inputValue, isValid |
| ContentPreview | content, html, isLoading |
| ActionButtons | isAnalyzing, isDownloading |
| LoadingSpinner | - |
| ErrorMessage | message, type |

---

## 7. 扩展性设计

### 7.1 模块可替换性

| 模块 | 当前实现 | 可扩展方向 |
|------|----------|------------|
| 爬虫模块 | requests + BeautifulSoup | Playwright（支持 JS 渲染页面） |
| AI 模块 | Minimax API（支持多模型扩展） | OpenAI / Claude / 本地模型 |
| 下载格式 | Markdown / TXT | PDF / EPUB / DOCX |
| 内容解析 | BeautifulSoup | Readability / Mozilla Readability |

### 7.2 扩展场景

1. **支持 JavaScript 渲染页面** — 替换 `scraper_service.py` 使用 Playwright
2. **切换 AI 提供商** — 替换 `analyzer_service.py` 使用 OpenAI / Claude / 本地 LLM
3. **增加下载格式** — 在 `converter_service.py` 添加 PDF 生成（pdfkit）
4. **前端组件复用** — 各组件独立，可单独增强样式或功能

---

## 8. 环境要求

### 8.1 后端环境

- Python 3.10+
- pip

### 8.2 前端环境

- Node.js 18+
- npm

### 8.3 外部服务

- Minimax API Key（用于 AI 分析功能，当前默认）

---

## 9. 快速开始

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
# 后续可扩展
# AI_PROVIDER=openai
# OPENAI_API_KEY=your_api_key_here
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

---

## 10. 里程碑规划

### M1 - 最小可用版本 (MVP)

- [x] URL 输入与校验
- [x] 网页内容爬取
- [x] 内容预览展示
- [x] Markdown 格式下载
- [x] TXT 格式下载

### M2 - AI 增强版本

- [ ] Minimax API 集成
- [ ] AI 内容分析总结
- [ ] 分析结果展示

### M3 - 能力增强版本

- [ ] 支持 JavaScript 渲染页面
- [ ] PDF 下载支持
- [ ] 批量爬取功能

---

## 11. 许可证

MIT
