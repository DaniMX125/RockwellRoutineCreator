# Rockwell Routine Creator

## Descrizione del Progetto

Rockwell Routine Creator è uno strumento sviluppato in Python per automatizzare la creazione di routine per i controllori logici programmabili (PLC) Rockwell Automation. Questo progetto mira a semplificare il processo di configurazione e gestione delle routine PLC, riducendo il tempo e gli errori manuali.

## Struttura della Cartella

La struttura della cartella del progetto è la seguente:

```
RockwellRoutineCreator/
│
├── README.md
├── main.py
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── routine_creator.py
│   ├── gestione_xml.py
│   ├── rung_generator.py
│   └── config.xml
├── tests/
│   ├── __init__.py
│   ├── test_routine_creator.py
│   ├── test_gestione_xml.py
│   └── test_rung_generator.py
└── docs/
  └── user_guide.md
```

### Descrizione dei File e delle Cartelle

- **README.md**: Questo file, che fornisce una panoramica del progetto.
- **main.py**: Il file principale per l'esecuzione del programma.
- **requirements.txt**: Elenco delle dipendenze Python necessarie per eseguire il progetto.
- **src/**: Contiene il codice sorgente del progetto.
  - **routine_creator.py**: Modulo principale per la creazione delle routine.
  - **gestione_xml.py**: Modulo per la gestione e lettura dei file XML di configurazione.
  - **rung_generator.py**: Modulo per la generazione delle stringhe di routine.
  - **config.xml**: File di configurazione XML contenente i dettagli delle routine.
- **tests/**: Contiene i test unitari per il progetto.
  - **test_routine_creator.py**: Test per il modulo routine_creator.
  - **test_gestione_xml.py**: Test per il modulo gestione_xml.
  - **test_rung_generator.py**: Test per il modulo rung_generator.
- **docs/**: Documentazione aggiuntiva del progetto.
  - **user_guide.md**: Guida utente per l'utilizzo del programma.

## Installazione

Per installare le dipendenze necessarie, eseguire il seguente comando:

```bash
pip install -r requirements.txt
```

## Utilizzo

Per eseguire il programma, utilizzare il seguente comando:

```bash
python main.py
```

### Utilizzo di `routine_creator.py`

Il modulo `routine_creator.py` può essere utilizzato per creare nuove routine PLC. Ecco un esempio di come utilizzarlo:

```python
from src.routine_creator import RoutineCreator

# Inizializza il creatore di routine con il file di configurazione
routine_creator = RoutineCreator('src/config.xml')

# Crea una nuova routine
routine_creator.create_routine('NomeRoutine')
```

### Esecuzione dei Test

Per eseguire i test unitari, utilizzare il seguente comando:

```bash
python -m unittest discover -s tests
```

## Contributi

I contributi sono benvenuti! Sentiti libero di aprire issue e pull request per migliorare il progetto.

## Licenza

Questo progetto è distribuito sotto la licenza MIT. Vedi il file [LICENSE](LICENSE) per ulteriori dettagli.