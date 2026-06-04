const API_BASE = "/api";

async function request(endpoint, body) {
  const res = await fetch(`${API_BASE}${endpoint}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  const data = await res.json();

  if (!res.ok || !data.success) {
    throw new Error(data.error || "请求失败");
  }

  return data.data;
}

export const scrapeUrl = (url) => request("/scrape", { url });

export const analyzeContent = (content) => request("/analyze", { content });

export function downloadContent(content, title, format) {
  let mimeType = "text/plain;charset=utf-8";
  let ext = "txt";

  if (format === "markdown") {
    ext = "md";
  } else if (format === "html") {
    mimeType = "text/html;charset=utf-8";
    ext = "html";
  }

  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${title}.${ext}`;
  a.click();
  URL.revokeObjectURL(url);
}