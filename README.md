# PGN-NLP
The aim for this repo is for converting Natural Language audio to chess algebraic notation that we can feed into any chess engine.

So, if the user says

"pawn takes c8 and promote to queen with check" => `bxc8=Q+`


The most of the code is written in Jupyter notebook / python3.

My idea is everywhere at this point... [training](./src/training.ipynb) notebook will create a lot of testing audio files to feed into ML and train it. so, when the ML listen to "b4" it's should not be returning "before" but it is actually giving us desire answer "b4". same has "h8" not "hate"... To overcome this.. We will be training data with lot of different chess position.


### Files and uses
1. [asr](./src/asr.ipynb) use for training audio and create a simple ML model
1. [extract](./src/extract.ipynb) use for extracting the [pgn][pgn-download] from the internet and extracting into algebraic notation in an large array may be used for real world game data
1. [notation_parser](./src/notation_parser.py) a simple lib that takes the algebraic notation and convert into a standard dict. taken from npm chess-notation-parser lib written by me. (todo: Take a standard dict. and convert back to notation?)
1. [tokenizer](./src/tokenzier.ipynb) a simple spaCy's tokenizer that take a natural language text and label the entity like `place` for c4 and `piece` etc.
1. [training](./src/training.ipynb) generate 1000's of audio of possible moves that use most likely say for the purpose of training.
  - In the future, Need to use local audio generator and create audio using different voices.


### My idea 
1. Train a model with possible user moves (training.ipynb)
1. Listen for a audio (server)
1. Convert audio into text using the trained model (asr.ipynb)
1. Use tokenizer to label the text (tokenizer.ipynb)
1. Create a simple engine to validate the text (notation_parser.pt or nlt_to_pgn )

### Todo
Not sure if all this objective will be handled by this repo most likely not. Will create a chess server. To follow along check my github page
- [] Create a server that listen to audio and send an signal when it listen to write action
- [] Create a chess engine that tracks the current move and ask user questions
- [] Create a simple chess ui to test the engine
- [] Handle ambigous move if found. For example if the user says knight to g5 and both knight can move into that square ask more question or ask the user to be more specific or better use place1 to place2
- [] Find and run a test chess engine


### Few of the oversight on this repo
- Chopping Audio streams. I have not thought about it. The server most likely will be a continuos audio streams picked up by mic and sending back and forth the signal. It will be very engage audio streams. Need to train few action words and tokenizer to for the user handle the chess engine start and stop.
- Can't wait to train with different voices
- Handling over-fitting
  - The issue is I am keep over writing the training data and there should be a better way to do it. Separate the training data for example for places and based on voice. So we don't have to over-write it. So, during the ML training i can use different set of dataset to train and test it

<!-- Links -->
[pgn-download]: https://www.pgnmentor.com/files.html