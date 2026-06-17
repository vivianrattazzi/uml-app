import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";

function EvaluationPage({ savedExams }) {
  const [examData, setExamData] = useState(null);
  const [selectedStudentFile, setSelectedStudentFile] = useState(null);
  const [studentJsonContent, setStudentJsonContent] = useState("");
  const [aiEvaluation, setAiEvaluation] = useState(null);
  const [aiLoading, setAiLoading] = useState(false);
  const [studentFiles, setStudentFiles] = useState([]);
  const [studentSubmissions, setStudentSubmissions] = useState([]);
  const [showTrace, setShowTrace] = useState(false);

  const { id } = useParams();
  const navigate = useNavigate();
  useEffect(() => {
    fetch(`http://127.0.0.1:5000/esercizi/${id}`)
      .then((response) => response.json())
      .then((data) => {
        console.log("ESERCIZIO:", data);

        setExamData(data);
      });
  }, [id]);

  const fetchStudentSubmissions = () => {
    fetch(`http://127.0.0.1:5000/prove_studenti/${id}`)
      .then((response) => response.json())
      .then((data) => {
        console.log("PROVE STUDENTI:", data);

        setStudentSubmissions(data);
      });
  };

  useEffect(() => {
    fetchStudentSubmissions();
  }, [id]);
  console.log("ID ESERCIZIO:", id);
  const handleStudentFileClick = (file) => {
    setSelectedStudentFile(file);

    const reader = new FileReader();

    reader.onload = (event) => {
      setStudentJsonContent(event.target.result);
    };

    reader.readAsText(file);
  };
  const handleStudentUpload = async (event) => {
    const files = Array.from(event.target.files);

    setStudentFiles(files);

    for (const file of files) {
      const alreadyExists = studentSubmissions.some(
        (submission) => submission.nome_file === file.name,
      );

      if (alreadyExists) {
        alert(`La prova ${file.name} è già presente`);

        continue;
      }
      const reader = new FileReader();

      reader.onload = async (e) => {
        const contenutoJson = e.target.result;

        const payload = {
          id_esercizio: id,

          nome_file: file.name,

          contenuto_json: contenutoJson,
        };

        console.log("UPLOAD STUDENTE:", payload);

        try {
          const response = await fetch("http://127.0.0.1:5000/prove_studenti", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
          });

          const data = await response.json();

          console.log("RISPOSTA BACKEND:", data);
          fetchStudentSubmissions();
        } catch (error) {
          console.error("Errore upload:", error);
        }
      };

      reader.readAsText(file);
    }
  };
  const handleEvaluateWithAI = async () => {
    setAiLoading(true);
    setAiEvaluation(null);

    const payload = {
      examTitle: examData.titolo,
      examText: examData.testo,
      officialSolution: examData.soluzione_json,
      studentSubmission: studentJsonContent,
    };

    console.log("PAYLOAD AI:", payload);

    try {
      const response = await fetch("http://127.0.0.1:5000/evaluate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      console.log("RISPOSTA BACKEND:", data);

      setAiEvaluation(data);
    } catch (error) {
      console.error("Errore backend:", error);
    } finally {
      setAiLoading(false);
    }
  };
  return (
    <>
      <div
        onClick={() => navigate("/")}
        style={{
          marginBottom: "20px",
          cursor: "pointer",
          fontWeight: "bold",
        }}
      >
        ← Torna alle prove
      </div>
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "300px 1fr",
          gap: "30px",
          padding: "20px",
        }}
      >
        {/* COLONNA SINISTRA */}

        <div
          style={{
            border: "1px solid lightgray",
            padding: "20px",
            minHeight: "500px",
          }}
        >
          {examData ? (
            <>
              <h2>Prova d'esame</h2>

              <h3>{examData.titolo}</h3>

              <button
                onClick={() => setShowTrace(!showTrace)}
                style={{
                  marginTop: "10px",
                  padding: "8px 15px",
                  cursor: "pointer",
                }}
              >
                {showTrace ? "Nascondi traccia" : "Vedi traccia"}
              </button>

              {showTrace && (
                <div
                  style={{
                    marginTop: "15px",
                    padding: "15px",
                    border: "1px solid lightgray",
                    backgroundColor: "#fafafa",
                    maxHeight: "250px",
                    overflowY: "auto",
                  }}
                >
                  <p>{examData.testo}</p>
                </div>
              )}

              <h2 style={{ marginTop: "40px" }}>Prove studenti</h2>

              <input
                type="file"
                multiple
                accept=".json"
                onChange={handleStudentUpload}
                style={{ marginTop: "15px" }}
              />

              <div style={{ marginTop: "20px" }}>
                {studentSubmissions.length > 0 ? (
                  studentSubmissions.map((file) => (
                    <div
                      key={file.id}
                      onClick={() => {
                        setSelectedStudentFile(file);

                        setStudentJsonContent(file.contenuto_json);
                      }}
                      style={{
                        border: "1px solid lightgray",
                        padding: "10px",
                        marginBottom: "10px",
                        cursor: "pointer",
                        backgroundColor:
                          selectedStudentFile?.id === file.id
                            ? "#eaeaea"
                            : "white",
                      }}
                    >
                      {file.nome_file}
                    </div>
                  ))
                ) : (
                  <p>Nessuna prova presente</p>
                )}
              </div>
            </>
          ) : (
            <p>Caricamento esercizio...</p>
          )}
        </div>

        {/* COLONNA DESTRA */}

        <div
          style={{
            flex: 1,
            border: "1px solid lightgray",
            padding: "20px",
            backgroundColor: "#fafafa",
          }}
        >
          <h2>Dettaglio elaborato</h2>

          {selectedStudentFile ? (
            <>
              <h3>{selectedStudentFile.nome_file}</h3>

              <h4 style={{ marginTop: "20px" }}>JSON studente</h4>

              <pre
                style={{
                  backgroundColor: "white",
                  padding: "15px",
                  border: "1px solid lightgray",
                  overflowX: "auto",
                  maxHeight: "300px",
                }}
              >
                {studentJsonContent}
              </pre>

              <h4 style={{ marginTop: "20px" }}>Valutazione AI</h4>

              <div
                style={{
                  backgroundColor: "white",
                  padding: "15px",
                  border: "1px solid lightgray",
                  minHeight: "120px",
                }}
              >
                {aiEvaluation ? (
                  <p>{aiEvaluation}</p>
                ) : (
                  <p>Nessuna valutazione disponibile</p>
                )}
              </div>

              <button
                onClick={handleEvaluateWithAI}
                disabled={aiLoading}
                style={{
                  marginTop: "20px",
                  padding: "10px 20px",
                  cursor: "pointer",
                }}
              >
                {aiLoading ? "Valutazione AI in corso..." : "Valuta con AI"}
              </button>
            </>
          ) : (
            <p>Seleziona un elaborato studente.</p>
          )}
        </div>
      </div>
    </>
  );
}

export default EvaluationPage;
