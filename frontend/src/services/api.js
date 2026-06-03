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
  const blob = new Blob([content], { type: "text/plain;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${title}.${format === "markdown" ? "md" : "txt"}`;
  a.click();
  URL.revokeObjectURL(url);
}