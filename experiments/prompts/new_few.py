Valuta il seguente diagramma UML confrontando la soluzione dello studente con la soluzione ufficiale.

========================================================================
ESEMPIO 1
========================================================================

SOLUZIONE UFFICIALE

{
  "diagramType": "ClassDiagram",
  "classes": [
    {
      "name": "Athlete",
      "attributes": [
        {
          "name": "name",
          "visibility": "",
          "type": "string"
        },
        {
          "name": "surname",
          "visibility": "",
          "type": "string"
        },
        {
          "name": "points",
          "visibility": "",
          "type": "int"
        }
      ],
      "methods": []
    },
    {
      "name": "Competition",
      "attributes": [
        {
          "name": "name",
          "visibility": "",
          "type": "string"
        },
        {
          "name": "date",
          "visibility": "",
          "type": "Date"
        }
      ],
      "methods": []
    },
    {
      "name": "Heat",
      "attributes": [
        {
          "name": "id",
          "visibility": "",
          "type": "string"
        }
      ],
      "methods": []
    },
    {
      "name": "Judge",
      "attributes": [
        {
          "name": "name",
          "visibility": "",
          "type": "string"
        },
        {
          "name": "surname",
          "visibility": "",
          "type": "string"
        }
      ],
      "methods": []
    },
    {
      "name": "Round",
      "attributes": [
        {
          "name": "id",
          "visibility": "",
          "type": "string"
        }
      ],
      "methods": []
    }
  ],
  "associations": [
    {
      "type": "Association",
      "name": "applies to",
      "source": "Competition",
      "target": "Athlete",
      "sourceMultiplicity": "*",
      "targetMultiplicity": "1...*",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "heat judge",
      "source": "Competition",
      "target": "Judge",
      "sourceMultiplicity": "*",
      "targetMultiplicity": "3",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "head judge",
      "source": "Competition",
      "target": "Judge",
      "sourceMultiplicity": "*",
      "targetMultiplicity": "1",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "",
      "source": "Round",
      "target": "Competition",
      "sourceMultiplicity": "1...*",
      "targetMultiplicity": "1",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "",
      "source": "Round",
      "target": "Heat",
      "sourceMultiplicity": "1",
      "targetMultiplicity": "1...*",
      "sourceRole": "",
      "targetRole": ""
    }
  ],
  "inheritance": [],
  "reference": {
    "classes": [
      {
        "name": "Competition",
        "synonyms": [],
        "weight": "STRONG",
        "attributes": [
          {
            "name": "name",
            "synonyms": [],
            "types": [
              "string"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          },
          {
            "name": "date",
            "synonyms": [],
            "types": [
              "Date"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          }
        ],
        "forbiddenAttributes": []
      },
      {
        "name": "Athlete",
        "synonyms": [],
        "weight": "STRONG",
        "attributes": [
          {
            "name": "name",
            "synonyms": [],
            "types": [
              "string"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          },
          {
            "name": "surname",
            "synonyms": [],
            "types": [
              "string"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          },
          {
            "name": "points",
            "synonyms": [],
            "types": [
              "int"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          }
        ],
        "forbiddenAttributes": []
      },
      {
        "name": "Heat",
        "synonyms": [],
        "weight": "STRONG",
        "attributes": [
          {
            "name": "id",
            "synonyms": [],
            "types": [
              "string"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          }
        ],
        "forbiddenAttributes": []
      },
      {
        "name": "Scores",
        "synonyms": [],
        "weight": "STRONG",
        "attributes": [
          {
            "name": "judge1",
            "synonyms": [],
            "types": [
              "int"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          },
          {
            "name": "judge2",
            "synonyms": [],
            "types": [
              "int"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          },
          {
            "name": "judge3",
            "synonyms": [],
            "types": [
              "int"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          },
          {
            "name": "total",
            "synonyms": [],
            "types": [
              "int"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          }
        ],
        "forbiddenAttributes": []
      },
      {
        "name": "Judge",
        "synonyms": [],
        "weight": "STRONG",
        "attributes": [
          {
            "name": "name",
            "synonyms": [],
            "types": [
              "string"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          },
          {
            "name": "surname",
            "synonyms": [],
            "types": [
              "string"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          }
        ],
        "forbiddenAttributes": []
      },
      {
        "name": "Round",
        "synonyms": [],
        "weight": "STRONG",
        "attributes": [
          {
            "name": "id",
            "synonyms": [],
            "types": [
              "string"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          }
        ],
        "forbiddenAttributes": []
      }
    ],
    "associations": [
      {
        "type": "ClassBidirectional",
        "name": "",
        "source": "Heat",
        "target": "Scores",
        "sourceMultiplicity": [
          ""
        ],
        "targetMultiplicity": [
          ""
        ],
        "sourceRole": "",
        "targetRole": "",
        "weight": "STRONG"
      },
      {
        "type": "ClassBidirectional",
        "name": "",
        "source": "Athlete",
        "target": "Scores",
        "sourceMultiplicity": [
          ""
        ],
        "targetMultiplicity": [
          ""
        ],
        "sourceRole": "",
        "targetRole": "",
        "weight": "STRONG"
      },
      {
        "type": "ClassBidirectional",
        "name": "",
        "source": "Competition",
        "target": "Judge",
        "sourceMultiplicity": [
          "*"
        ],
        "targetMultiplicity": [
          "3"
        ],
        "sourceRole": "",
        "targetRole": "",
        "weight": "STRONG"
      },
      {
        "type": "ClassBidirectional",
        "name": "",
        "source": "Competition",
        "target": "Judge",
        "sourceMultiplicity": [
          "*"
        ],
        "targetMultiplicity": [
          "1"
        ],
        "sourceRole": "",
        "targetRole": "",
        "weight": "STRONG"
      },
      {
        "type": "ClassBidirectional",
        "name": "",
        "source": "Round",
        "target": "Competition",
        "sourceMultiplicity": [
          "1...*"
        ],
        "targetMultiplicity": [
          "1"
        ],
        "sourceRole": "",
        "targetRole": "",
        "weight": "STRONG"
      },
      {
        "type": "ClassBidirectional",
        "name": "",
        "source": "Round",
        "target": "Heat",
        "sourceMultiplicity": [
          "1"
        ],
        "targetMultiplicity": [
          "1...*"
        ],
        "sourceRole": "",
        "targetRole": "",
        "weight": "STRONG"
      },
      {
        "type": "ClassBidirectional",
        "name": "",
        "source": "Competition",
        "target": "Athlete",
        "sourceMultiplicity": [
          "*"
        ],
        "targetMultiplicity": [
          "1...*"
        ],
        "sourceRole": "",
        "targetRole": "",
        "weight": "STRONG"
      }
    ],
    "forbiddenClasses": [],
    "forbiddenAssociations": []
  }
}

------------------------------------------------------------------------

SOLUZIONE DELLO STUDENTE

{
  "diagramType": "ClassDiagram",
  "classes": [
    {
      "name": "application",
      "attributes": [
        {
          "name": "initial ranking",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    },
    {
      "name": "athete",
      "attributes": [
        {
          "name": "name",
          "visibility": "",
          "type": ""
        },
        {
          "name": "surname",
          "visibility": "",
          "type": ""
        },
        {
          "name": "id",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    },
    {
      "name": "grid",
      "attributes": [
        {
          "name": "name",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    },
    {
      "name": "head judge",
      "attributes": [
        {
          "name": "name",
          "visibility": "",
          "type": ""
        },
        {
          "name": "id",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    },
    {
      "name": "heats",
      "attributes": [
        {
          "name": "duration",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    },
    {
      "name": "judge",
      "attributes": [
        {
          "name": "id",
          "visibility": "",
          "type": ""
        },
        {
          "name": "name",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    },
    {
      "name": "round",
      "attributes": [
        {
          "name": "number of participants",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    },
    {
      "name": "score",
      "attributes": [
        {
          "name": "value",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    }
  ],
  "associations": [
    {
      "type": "Association",
      "name": "",
      "source": "application",
      "target": "athete",
      "sourceMultiplicity": "*",
      "targetMultiplicity": "1",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "",
      "source": "application",
      "target": "grid",
      "sourceMultiplicity": "32",
      "targetMultiplicity": "1",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "",
      "source": "grid",
      "target": "round",
      "sourceMultiplicity": "1",
      "targetMultiplicity": "5",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "modifies",
      "source": "head judge",
      "target": "grid",
      "sourceMultiplicity": "",
      "targetMultiplicity": "",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "evaluates",
      "source": "head judge",
      "target": "score",
      "sourceMultiplicity": "1",
      "targetMultiplicity": "*",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "",
      "source": "heats",
      "target": "score",
      "sourceMultiplicity": "*",
      "targetMultiplicity": "*",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "",
      "source": "judge",
      "target": "heats",
      "sourceMultiplicity": "3",
      "targetMultiplicity": "5",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "",
      "source": "judge",
      "target": "score",
      "sourceMultiplicity": "1",
      "targetMultiplicity": "*",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "",
      "source": "round",
      "target": "heats",
      "sourceMultiplicity": "*",
      "targetMultiplicity": "1",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "",
      "source": "score",
      "target": "athete",
      "sourceMultiplicity": "*",
      "targetMultiplicity": "*",
      "sourceRole": "",
      "targetRole": ""
    }
  ],
  "inheritance": []
}

--------------------------------------------------
VALUTAZIONE

CLASSI

Presenti:
- Athlete (athete)
- Heat (heats)
- Scores (score)
- Judge
- Round

Assenti:
-Competition

Extra:
- application
- grid
- head judge

ATTRIBUTI DELLE CLASSI EQUIVALENTI

Presenti:
Nessuno

Presenti con errore di tipo:
- Athlete: name — tipo atteso string, tipo non specificato
- Athlete: surname — tipo atteso string, tipo non specificato
- Judge: name — tipo atteso string, tipo non specificato

Assenti:
- Athlete: points
- Heat: id
- Scores: judge1, judge2, judge3, total
- Judge: surname
- Round: id

Extra:
- Athlete: id
- Heat: duration
- Scores: value
- Judge: id
- Round: number of participants

Gli attributi delle classi classificate come extra non vengono confrontati.

EREDITARIETÀ

Presenti:
Nessuna

Assenti:
Nessuna

Extra:
Nessuna

RELAZIONI

Presenti:
- Heat — Scores
- Athlete — Scores
- Round — Heat

Assenti:
- Competition — Judge, relazione con tre giudici
- Competition — Judge, relazione con un giudice principale
- Round — Competition
- Competition — Athlete

Extra:
- application — Athlete
- application — grid
- grid — Round
- head judge — grid
- Judge — Heat
- Judge — Scores
- head judge — Scores

MOLTEPLICITÀ

Presenti:
Nessuna

Assenti:
- Competition (*) — Judge (3)
- Competition (*) — Judge (1)
- Round (1...*) — Competition (1)
- Round (1) — Heat (1...*)
- Competition () — Athlete (1...)

Extra:
Nessuna

Le molteplicità delle relazioni Heat — Scores e Athlete — Scores non vengono classificate, poiché nella soluzione ufficiale non sono specificate. La relazione Round — Heat è presente, ma le molteplicità inserite dallo studente non coincidono con quelle attese.

========================================================================
ESEMPIO 2
========================================================================

SOLUZIONE UFFICIALE

{
  "diagramType": "ClassDiagram",
  "classes": [
    {
      "name": "Athlete",
      "attributes": [
        {
          "name": "name",
          "visibility": "",
          "type": "string"
        },
        {
          "name": "surname",
          "visibility": "",
          "type": "string"
        },
        {
          "name": "points",
          "visibility": "",
          "type": "int"
        }
      ],
      "methods": []
    },
    {
      "name": "Competition",
      "attributes": [
        {
          "name": "name",
          "visibility": "",
          "type": "string"
        },
        {
          "name": "date",
          "visibility": "",
          "type": "Date"
        }
      ],
      "methods": []
    },
    {
      "name": "Heat",
      "attributes": [
        {
          "name": "id",
          "visibility": "",
          "type": "string"
        }
      ],
      "methods": []
    },
    {
      "name": "Judge",
      "attributes": [
        {
          "name": "name",
          "visibility": "",
          "type": "string"
        },
        {
          "name": "surname",
          "visibility": "",
          "type": "string"
        }
      ],
      "methods": []
    },
    {
      "name": "Round",
      "attributes": [
        {
          "name": "id",
          "visibility": "",
          "type": "string"
        }
      ],
      "methods": []
    }
  ],
  "associations": [
    {
      "type": "Association",
      "name": "applies to",
      "source": "Competition",
      "target": "Athlete",
      "sourceMultiplicity": "*",
      "targetMultiplicity": "1...*",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "heat judge",
      "source": "Competition",
      "target": "Judge",
      "sourceMultiplicity": "*",
      "targetMultiplicity": "3",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "head judge",
      "source": "Competition",
      "target": "Judge",
      "sourceMultiplicity": "*",
      "targetMultiplicity": "1",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "",
      "source": "Round",
      "target": "Competition",
      "sourceMultiplicity": "1...*",
      "targetMultiplicity": "1",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "",
      "source": "Round",
      "target": "Heat",
      "sourceMultiplicity": "1",
      "targetMultiplicity": "1...*",
      "sourceRole": "",
      "targetRole": ""
    }
  ],
  "inheritance": [],
  "reference": {
    "classes": [
      {
        "name": "Competition",
        "synonyms": [],
        "weight": "STRONG",
        "attributes": [
          {
            "name": "name",
            "synonyms": [],
            "types": [
              "string"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          },
          {
            "name": "date",
            "synonyms": [],
            "types": [
              "Date"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          }
        ],
        "forbiddenAttributes": []
      },
      {
        "name": "Athlete",
        "synonyms": [],
        "weight": "STRONG",
        "attributes": [
          {
            "name": "name",
            "synonyms": [],
            "types": [
              "string"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          },
          {
            "name": "surname",
            "synonyms": [],
            "types": [
              "string"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          },
          {
            "name": "points",
            "synonyms": [],
            "types": [
              "int"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          }
        ],
        "forbiddenAttributes": []
      },
      {
        "name": "Heat",
        "synonyms": [],
        "weight": "STRONG",
        "attributes": [
          {
            "name": "id",
            "synonyms": [],
            "types": [
              "string"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          }
        ],
        "forbiddenAttributes": []
      },
      {
        "name": "Scores",
        "synonyms": [],
        "weight": "STRONG",
        "attributes": [
          {
            "name": "judge1",
            "synonyms": [],
            "types": [
              "int"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          },
          {
            "name": "judge2",
            "synonyms": [],
            "types": [
              "int"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          },
          {
            "name": "judge3",
            "synonyms": [],
            "types": [
              "int"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          },
          {
            "name": "total",
            "synonyms": [],
            "types": [
              "int"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          }
        ],
        "forbiddenAttributes": []
      },
      {
        "name": "Judge",
        "synonyms": [],
        "weight": "STRONG",
        "attributes": [
          {
            "name": "name",
            "synonyms": [],
            "types": [
              "string"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          },
          {
            "name": "surname",
            "synonyms": [],
            "types": [
              "string"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          }
        ],
        "forbiddenAttributes": []
      },
      {
        "name": "Round",
        "synonyms": [],
        "weight": "STRONG",
        "attributes": [
          {
            "name": "id",
            "synonyms": [],
            "types": [
              "string"
            ],
            "weight": "STRONG",
            "allowsForeignKeyName": false
          }
        ],
        "forbiddenAttributes": []
      }
    ],
    "associations": [
      {
        "type": "ClassBidirectional",
        "name": "",
        "source": "Heat",
        "target": "Scores",
        "sourceMultiplicity": [
          ""
        ],
        "targetMultiplicity": [
          ""
        ],
        "sourceRole": "",
        "targetRole": "",
        "weight": "STRONG"
      },
      {
        "type": "ClassBidirectional",
        "name": "",
        "source": "Athlete",
        "target": "Scores",
        "sourceMultiplicity": [
          ""
        ],
        "targetMultiplicity": [
          ""
        ],
        "sourceRole": "",
        "targetRole": "",
        "weight": "STRONG"
      },
      {
        "type": "ClassBidirectional",
        "name": "",
        "source": "Competition",
        "target": "Judge",
        "sourceMultiplicity": [
          "*"
        ],
        "targetMultiplicity": [
          "3"
        ],
        "sourceRole": "",
        "targetRole": "",
        "weight": "STRONG"
      },
      {
        "type": "ClassBidirectional",
        "name": "",
        "source": "Competition",
        "target": "Judge",
        "sourceMultiplicity": [
          "*"
        ],
        "targetMultiplicity": [
          "1"
        ],
        "sourceRole": "",
        "targetRole": "",
        "weight": "STRONG"
      },
      {
        "type": "ClassBidirectional",
        "name": "",
        "source": "Round",
        "target": "Competition",
        "sourceMultiplicity": [
          "1...*"
        ],
        "targetMultiplicity": [
          "1"
        ],
        "sourceRole": "",
        "targetRole": "",
        "weight": "STRONG"
      },
      {
        "type": "ClassBidirectional",
        "name": "",
        "source": "Round",
        "target": "Heat",
        "sourceMultiplicity": [
          "1"
        ],
        "targetMultiplicity": [
          "1...*"
        ],
        "sourceRole": "",
        "targetRole": "",
        "weight": "STRONG"
      },
      {
        "type": "ClassBidirectional",
        "name": "",
        "source": "Competition",
        "target": "Athlete",
        "sourceMultiplicity": [
          "*"
        ],
        "targetMultiplicity": [
          "1...*"
        ],
        "sourceRole": "",
        "targetRole": "",
        "weight": "STRONG"
      }
    ],
    "forbiddenClasses": [],
    "forbiddenAssociations": []
  }
}

------------------------------------------------------------------------

SOLUZIONE DELLO STUDENTE
{
  "diagramType": "ClassDiagram",
  "classes": [
    {
      "name": "Application",
      "attributes": [],
      "methods": []
    },
    {
      "name": "ATHLET",
      "attributes": [
        {
          "name": "Name",
          "visibility": "",
          "type": ""
        },
        {
          "name": "SSN",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    },
    {
      "name": "Competition",
      "attributes": [
        {
          "name": "N_rounds",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    },
    {
      "name": "HEAD JUDGE",
      "attributes": [
        {
          "name": "Name",
          "visibility": "",
          "type": ""
        },
        {
          "name": "SSN",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    },
    {
      "name": "Heat",
      "attributes": [
        {
          "name": "N_athletes",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    },
    {
      "name": "HEAT JUDGE",
      "attributes": [
        {
          "name": "Name",
          "visibility": "",
          "type": ""
        },
        {
          "name": "SSN",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    },
    {
      "name": "Round",
      "attributes": [
        {
          "name": "N_heats",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    },
    {
      "name": "score",
      "attributes": [
        {
          "name": "quantity",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    },
    {
      "name": "SURF LEAGUE",
      "attributes": [
        {
          "name": "date",
          "visibility": "",
          "type": ""
        }
      ],
      "methods": []
    }
  ],
  "associations": [
    {
      "type": "Association",
      "name": "enroll",
      "source": "ATHLET",
      "target": "Application",
      "sourceMultiplicity": "N",
      "targetMultiplicity": "N",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "composed by",
      "source": "Competition",
      "target": "Round",
      "sourceMultiplicity": "1",
      "targetMultiplicity": "N",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "read",
      "source": "HEAD JUDGE",
      "target": "Application",
      "sourceMultiplicity": "1",
      "targetMultiplicity": "N",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "define",
      "source": "HEAD JUDGE",
      "target": "Round",
      "sourceMultiplicity": "1",
      "targetMultiplicity": "N",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "check",
      "source": "HEAD JUDGE",
      "target": "score",
      "sourceMultiplicity": "1",
      "targetMultiplicity": "N",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "assign",
      "source": "HEAT JUDGE",
      "target": "score",
      "sourceMultiplicity": "N",
      "targetMultiplicity": "N",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "composed by",
      "source": "Round",
      "target": "Heat",
      "sourceMultiplicity": "N",
      "targetMultiplicity": "N",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "To",
      "source": "score",
      "target": "ATHLET",
      "sourceMultiplicity": "N",
      "targetMultiplicity": "N",
      "sourceRole": "",
      "targetRole": ""
    },
    {
      "type": "Association",
      "name": "organized",
      "source": "SURF LEAGUE",
      "target": "Competition",
      "sourceMultiplicity": "1",
      "targetMultiplicity": "1",
      "sourceRole": "",
      "targetRole": ""
    }
  ],
  "inheritance": []
}


------------------------------------------------------------------------


VALUTAZIONE

CLASSI

Presenti:
- Athlete (ATHLET)
- Competition
- Heat
- Scores (score)
- Round

Assenti:
- Judge

Extra:
- Application
- HEAD JUDGE
- HEAT JUDGE
- SURF LEAGUE

Le classi HEAD JUDGE e HEAT JUDGE non vengono considerate equivalenti alla classe ufficiale Judge, poiché rappresentano due ruoli specifici modellati separatamente, mentre la soluzione ufficiale prevede un’unica classe generale.

ATTRIBUTI DELLE CLASSI EQUIVALENTI

Presenti:
Nessuno

Presenti con errore di tipo:
- Athlete: name — tipo atteso string, tipo non specificato

Assenti:
- Athlete: surname, points
- Competition: name, date
- Heat: id
- Scores: judge1, judge2, judge3, total
- Judge: name, surname
- Round: id

Extra:
- Athlete: SSN
- Competition: N_rounds
- Heat: N_athletes
- Scores: quantity
- Round: N_heats

Gli attributi delle classi classificate come extra non vengono confrontati. Di conseguenza, l’attributo date della classe SURF LEAGUE non può essere considerato equivalente all’attributo date previsto nella classe Competition.

EREDITARIETÀ

Presenti:
Nessuna

Assenti:
Nessuna

Extra:
Nessuna

RELAZIONI

Presenti:
- Round — Competition
- Round — Heat
- Athlete — Scores

Assenti:
- Heat — Scores
- Competition — Judge, relazione con tre giudici
- Competition — Judge, relazione con un giudice principale
- Competition — Athlete

Extra:
- Athlete — Application
- HEAD JUDGE — Application
- HEAD JUDGE — Round
- HEAD JUDGE — Scores
- HEAT JUDGE — Scores
- SURF LEAGUE — Competition

MOLTEPLICITÀ

Presenti:
Nessuna

Assenti:
- Round (1...*) — Competition (1)
- Round (1) — Heat (1...*)
- Competition (*) — Judge (3)
- Competition (*) — Judge (1)
- Competition () — Athlete (1...)

Extra:
Nessuna

Le molteplicità N e * sono considerate equivalenti in quanto indicano una cardinalità multipla. Tuttavia, N non è equivalente a 1...*, poiché non esprime il vincolo minimo pari a uno.

Le relazioni Heat — Scores e Athlete — Scores non presentano molteplicità specificate nella soluzione ufficiale. La relazione Athlete — Scores è quindi riconosciuta come presente senza effettuare il confronto delle cardinalità, mentre Heat — Scores risulta assente.