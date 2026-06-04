import { downloadContent } from "../services/api";

export function ActionButtons({ content, html, title, onAnalyze, isAnalyzing }) {
  const handleDownload = (format) => {
    if (format === "html") {
      if (!html) return;
      downloadContent(html, title || "untitled", "html");
    } else {
      if (!content) return;
      downloadContent(content, title || "untitled", format);
    }
  };

  return (
    <div className="action-buttons">
      <div className="download-group">
        <span>下载：</span>
        <button onClick={() => handleDownload("markdown")} disabled={!content}>
          Markdown
        </button>
        <button onClick={() => handleDownload("txt")} disabled={!content}>
          TXT
        </button>
        <button onClick={() => handleDownload("html")} disabled={!html}>
          HTML
        </button>
      </div>
      <button className="analyze-btn" onClick={onAnalyze} disabled={!content || isAnalyzing}>
        {isAnalyzing ? "分析中..." : "AI 分析"}
      </button>
    </div>
  );
}