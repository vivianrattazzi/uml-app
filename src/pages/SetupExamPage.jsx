import Navbar from "../components/Navbar";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function SetupExamPage({ savedExams, setSavedExams }) {
  const [examTitle, setExamTitle] = useState("");
  const [examText, setExamText] = useState("");
  const [solutionFile, setSolutionFile] = useState(null);
  const [exams, setExams] = useState([]);
  const navigate = useNavigate();

  const fetchExams = () => {
    fetch("http://127.0.0.1:5000/esercizi")
      .then((response) => response.json())
      .then((data) => {
        console.log("ESERCIZI DB:", data);

        setExams(data);
      });
  };

  useEffect(() => {
    fetchExams();
  }, []);

  const handleSaveExam = async () => {
    if (!examTitle || !examText || !solutionFile) {
      alert("Completa tutti i campi prima di salvare.");
      return;
    }

    const payload = {
      titolo: examTitle,
      testo: examText,
      soluzione_json: solutionFile.name,
    };

    console.log("PAYLOAD ESERCIZIO:", payload);

    try {
      const response = await fetch("http://127.0.0.1:5000/esercizi", {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify(payload),
      });

      const data = await response.json();

      console.log("RISPOSTA BACKEND:", data);

      alert("Esercizio salvato nel database!");
      fetchExams();

      setExamTitle("");
      setExamText("");
      setSolutionFile(null);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <div style={{ padding: "20px" }}>
        <h1>Setup Prova d'Esame</h1>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "1fr 2fr",
            gap: "20px",
            marginTop: "30px",
          }}
        >
          {/* COLONNA SINISTRA */}
          <div
            style={{
              border: "1px solid lightgray",
              padding: "20px",
              minHeight: "250px",
            }}
          >
            <h2>Prove salvate</h2>

            {exams.length > 0 ? (
              <div style={{ marginTop: "20px" }}>
                {exams.map((exam) => (
                  <div
                    key={exam.id}
                    style={{
                      border: "1px solid lightgray",
                      padding: "15px",
                      marginBottom: "15px",
                      backgroundColor: "#fafafa",
                    }}
                  >
                    <h3>{exam.titolo || "Prova senza titolo"}</h3>

                    <p>ID esercizio: {exam.id}</p>

                    <button onClick={() => navigate(`/evaluation/${exam.id}`)}>
                      Apri
                    </button>
                  </div>
                ))}
              </div>
            ) : (
              <p>Nessuna prova salvata</p>
            )}
          </div>

          {/* COLONNA DESTRA */}
          <div
            style={{
              border: "1px solid lightgray",
              padding: "20px",
              minHeight: "250px",
            }}
          >
            <h2>Titolo della prova</h2>

            <input
              type="text"
              value={examTitle}
              onChange={(event) => setExamTitle(event.target.value)}
              placeholder="Inserisci il titolo della prova"
              style={{
                width: "100%",
                padding: "10px",
                marginTop: "10px",
                boxSizing: "border-box",
              }}
            />

            <h2 style={{ marginTop: "30px" }}>Testo della prova</h2>

            <textarea
              value={examText}
              onChange={(event) => setExamText(event.target.value)}
              placeholder="Inserisci il testo della prova d'esame"
              rows={10}
              style={{
                width: "100%",
                padding: "10px",
                marginTop: "10px",
                boxSizing: "border-box",
                resize: "vertical",
              }}
            />

            <h2 style={{ marginTop: "40px" }}>Soluzione ufficiale JSON</h2>

            <input
              type="file"
              accept=".json"
              onChange={(event) => setSolutionFile(event.target.files[0])}
              style={{ marginTop: "15px" }}
            />

            {solutionFile ? (
              <div
                style={{
                  marginTop: "15px",
                  padding: "10px",
                  backgroundColor: "#f5f5f5",
                  border: "1px solid lightgray",
                }}
              >
                <strong>File caricato:</strong>

                <p>{solutionFile.name}</p>
              </div>
            ) : (
              <p style={{ marginTop: "10px" }}>Nessun file selezionato</p>
            )}

            <button
              onClick={handleSaveExam}
              style={{
                marginTop: "30px",
                padding: "10px 20px",
              }}
            >
              Salva prova
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default SetupExamPage;
