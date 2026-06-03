import { useState } from "react";
import { analyzeContent } from "../services/api";

export function useAnalyzer() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [summary, setSummary] = useState(null);

  const analyze = async (content) => {
    setLoading(true);
    setError(null);

    try {
      const data = await analyzeContent(content);
      setSummary(data.summary);
      return data.summary;
    } catch (err) {
      setError(err.message);
      return null;
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setSummary(null);
    setError(null);
  };

  return { loading, error, summary, analyze, reset };
}