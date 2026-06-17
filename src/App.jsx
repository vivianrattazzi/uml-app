import { BrowserRouter, Routes, Route } from "react-router-dom";

import SetupExamPage from "./pages/SetupExamPage";
import EvaluationPage from "./pages/EvaluationPage";
import { useState } from "react";

function App() {
  const [savedExams, setSavedExams] = useState([]);
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <SetupExamPage
              savedExams={savedExams}
              setSavedExams={setSavedExams}
            />
          }
        />
        <Route path="/evaluation/:id" element={<EvaluationPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
