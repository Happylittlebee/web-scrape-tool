import { useState } from "react";
import { UrlInput } from "./components/UrlInput";
import { ContentPreview } from "./components/ContentPreview";
import { ActionButtons } from "./components/ActionButtons";
import { LoadingSpinner } from "./components/LoadingSpinner";
import { ErrorMessage } from "./components/ErrorMessage";
import { useScraper } from "./hooks/useScraper";
import { useAnalyzer } from "./hooks/useAnalyzer";
import "./App.css";

function App() {
  const { loading: scrapeLoading, error: scrapeError, result, scrape, reset } = useScraper();
  const { loading: analyzeLoading, error: analyzeError, summary, analyze, reset: resetAnalyze } = useAnalyzer();

  const handleScrape = async (url) => {
    reset();
    resetAnalyze();
    await scrape(url);
  };

  const handleAnalyze = async () => {
    if (!result?.content) return;
    await analyze(result.content);
  };

  const handleDismissError = () => {
    reset();
  };

  const loading = scrapeLoading || analyzeLoading;

  return (
    <div className="app">
      <header className="header">
        <h1>Web Scraper Tool</h1>
        <p>输入链接，爬取并分析网页内容</p>
      </header>

      <main className="main">
        <UrlInput onSubmit={handleScrape} loading={scrapeLoading} />

        {scrapeLoading && <LoadingSpinner />}

        {scrapeError && <ErrorMessage message={scrapeError} onDismiss={handleDismissError} />}

        {result && (
          <>
            <ContentPreview content={result.content} />
            <ActionButtons
              content={result.content}
              html={result.html}
              title={result.title}
              onAnalyze={handleAnalyze}
              isAnalyzing={analyzeLoading}
            />
          </>
        )}

        {analyzeError && <ErrorMessage message={analyzeError} onDismiss={resetAnalyze} />}

        {summary && (
          <div className="summary-result">
            <h3>AI 分析结果</h3>
            <pre>{summary}</pre>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
