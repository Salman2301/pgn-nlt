# PGN-NLT
This repo is create a Portable Game Notation in chess into Natural language text and hopefully convert it back from Natural Language text back to pgn.
Planning to use my [Chess Notation parser][chess-notation-parser] that convert the algebraic notation into a JSON format and than convert the JSON into natural language will be using that as training dataset for the AI.

The code is written in Jupyter notebook.

Step to reproduce:
1. Download any PGN zip files from [this website][pgn-download]
1. Clone this repo and cd `pgn-nlt` folder
1. Create a `raw-pgn` folder and move the zip files into it
1. Open the `extract.ipynb` and run the code. This will extract the pgn and get all the list of PGN and save it as JSON

# Sample NLT
To create training dataset use pgn_to_nlt to generate audio files.

<!-- Links -->
[pgn-download]: https://www.pgnmentor.com/files.html