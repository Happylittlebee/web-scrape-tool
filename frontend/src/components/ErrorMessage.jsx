export function ErrorMessage({ message, onDismiss }) {
  if (!message) return null;

  return (
    <div className="error-message">
      <span>{message}</span>
      <button onClick={onDismiss}>&times;</button>
    </div>
  );
}