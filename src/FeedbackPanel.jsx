function FeedbackPanel({ feedback }) {
  return (
    <section>
      <h2>Feedback AI</h2>

      {feedback ? (
        typeof feedback === "string" ? (
          <p>{feedback}</p>
        ) : (
          <div>
            <p>Punteggio: {feedback.score}/10</p>

            <h3>Errori</h3>
            <ul>
              {feedback.errors.map((error, index) => (
                <li key={index}>{error}</li>
              ))}
            </ul>

            <h3>Suggerimenti</h3>
            <ul>
              {feedback.suggestions.map((suggestion, index) => (
                <li key={index}>{suggestion}</li>
              ))}
            </ul>
          </div>
        )
      ) : (
        <p>Nessuna valutazione ancora disponibile.</p>
      )}
    </section>
  );
}

export default FeedbackPanel;