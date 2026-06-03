export function ContentPreview({ content, isLoading }) {
  if (isLoading) return null;

  if (!content) return null;

  return (
    <div className="content-preview">
      <h3>内容预览</h3>
      <div className="preview-content">
        <pre>{content}</pre>
      </div>
    </div>
  );
}