export const evaluateDiagram = (diagram) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const hasClasses = diagram.classes && diagram.classes.length > 0;

      if (!hasClasses) {
        reject(new Error("Il diagramma non contiene classi UML."));
        return;
      }

      resolve({
        score: 7,
        errors: [
          "Manca una relazione tra Studente ed Esame",
          "La classe Esame potrebbe avere un attributo codice"
        ],
        suggestions: [
          "Aggiungere un'associazione tra Studente ed Esame",
          "Specificare meglio le cardinalità"
        ]
      });
    }, 1500);
  });
};