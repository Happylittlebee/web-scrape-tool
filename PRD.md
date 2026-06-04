# 网页内容爬取工具 - 产品需求文档 (PRD)

## 1. 产品概述

**产品名称：** Web Scraper Tool
**产品类型：** 前后端分离 Web 应用工具
**一句话描述：** 一款简洁高效的网页内容爬取工具，支持内容预览、多格式下载和 AI 智能分析总结。

**目标用户：**
- 需要快速获取网页内容的研究人员
- 需要提取网页信息进行二次整理的工作者
- 希望借助 AI 快速理解长篇文章的读者

---

## 2. 功能需求

| 功能 | 描述 | 优先级 |
|------|------|--------|
| URL 输入 | 用户在前端页面输入目标网页链接 | P0 |
| 内容爬取 | 后端自动爬取网页，提取正文内容 | P0 |
| 内容预览 | 实时在页面展示爬取到的内容 | P0 |
| 格式下载 | 支持 Markdown / TXT / HTML 格式下载 | P1 |
| AI 分析 | 调用 AI 对网页内容进行总结分析 | P1 |

---

## 3. 技术架构

| 层级 | 技术选型 |
|------|----------|
| 前端框架 | React 18 + Vite |
| 后端框架 | Flask |
| 爬虫 | Playwright (Chromium) + BeautifulSoup4 |
| AI 服务 | Minimax API (Claude 兼容格式) |
| 格式转换 | markdownify |
| 跨域支持 | flask-cors |

**系统架构：**
```
用户浏览器 → React前端(5173) → Flask后端(5000) → Playwright爬虫 → AI分析
                                ↓
                           文件转换服务
```

---

## 4. 项目结构

```
web-scraper-tool/
├── backend/
│   ├── app.py              # Flask 入口
│   ├── config.py           # 配置
│   ├── .env                # 环境变量
│   ├── requirements.txt   # 依赖
│   ├── routes/             # API 路由
│   ├── services/           # 业务逻辑
│   └── utils/              # 工具函数
├── frontend/
│   ├── src/
│   │   ├── components/     # UI 组件
│   │   ├── hooks/          # React Hooks
│   │   └── services/       # API 调用
│   └── package.json
└── PRD.md / README.md
```

---

## 5. API 设计

### 接口列表

| 方法 | 路径 | 描述 |
|------|------|------|
| POST | `/api/scrape` | 爬取网页内容 |
| POST | `/api/analyze` | AI 分析内容 |
| POST | `/api/download` | 下载文件 |

### 详细设计

**POST /api/scrape**
```json
请求: {"url": "https://example.com"}
响应: {"success": true, "data": {"title": "", "content": "", "html": ""}}
```

**POST /api/analyze**
```json
请求: {"content": "网页正文"}
响应: {"success": true, "data": {"summary": "AI 总结"}}
```

**POST /api/download**
```json
请求: {"content": "", "html": "", "title": "", "format": "markdown|txt|html"}
响应: 文件流
```

---

## 6. 扩展性设计

| 模块 | 当前实现 | 可扩展方向 |
|------|----------|------------|
| 爬虫 | Playwright + BeautifulSoup | Playwright（支持 JS 渲染） |
| AI 模块 | Minimax API | OpenAI / Claude / 本地模型 |
| 下载格式 | Markdown / TXT / HTML | PDF / EPUB |

---

## 7. 环境要求

- Python 3.10+
- Node.js 18+
- npm
- Chromium (via Playwright)
- 代理（用于访问外网）

---

## 8. 快速开始

```bash
# 后端
cd backend
pip install -r requirements.txt
playwright install chromium
python app.py

# 前端
cd frontend
npm install
npm run dev
```

---

## 9. 里程碑

- [x] M1 - MVP（URL 输入、爬取、预览、Markdown/TXT 下载）
- [x] M2 - AI 增强版本（Minimax API 集成）
- [ ] M3 - 能力增强（JS 渲染页面、PDF 支持、批量爬取）

---

## 10. 许可证
MIT
