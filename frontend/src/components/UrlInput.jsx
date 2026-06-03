import { useState } from "react";

export function UrlInput({ onSubmit, loading }) {
  const [value, setValue] = useState("");
  const [isValid, setIsValid] = useState(true);

  const handleSubmit = (e) => {
    e.preventDefault();
    const url = value.trim();

    if (!url) {
      setIsValid(false);
      return;
    }

    if (!url.startsWith("http://") && !url.startsWith("https://")) {
      setIsValid(false);
      return;
    }

    setIsValid(true);
    onSubmit(url);
  };

  return (
    <form onSubmit={handleSubmit} className="url-input-form">
      <div className="input-wrapper">
        <input
          type="text"
          value={value}
          onChange={(e) => {
            setValue(e.target.value);
            setIsValid(true);
          }}
          placeholder="输入网页链接，如 https://example.com"
          disabled={loading}
          className={!isValid ? "invalid" : ""}
        />
        <button type="submit" disabled={loading}>
          {loading ? "爬取中..." : "爬取"}
        </button>
      </div>
      {!isValid && <span className="error-hint">请输入有效的 URL（以 http:// 或 https:// 开头）</span>}
    </form>
  );
}
