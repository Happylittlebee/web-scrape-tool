import { useState } from "react";
import { scrapeUrl } from "../services/api";

export function useScraper() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  const scrape = async (url) => {
    setLoading(true);
    setError(null);

    try {
      const data = await scrapeUrl(url);
      setResult(data);
      return data;
    } catch (err) {
      setError(err.message);
      return null;
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setResult(null);
    setError(null);
  };

  return { loading, error, result, scrape, reset };
}
