function DiagramEditorMock({ diagramText, setDiagramText }) {
  return (
    <section>
      <h2>Editor UML</h2>
      <p>Per ora modifichiamo manualmente il JSON. In futuro qui ci sarà Apollon.</p>

      <textarea
        value={diagramText}
        onChange={(event) => setDiagramText(event.target.value)}
        rows={12}
        cols={70}
      />
    </section>
  );
}

export default DiagramEditorMock;