# Copy Chess

Copy Chess is a chess engine and game interface inspired by the tutorial in [this video](https://www.youtube.com/watch?v=OpL0Gcfn4B4&t=1248s). The goal is to create a functional chess game with potential API integration for AI or online play.

## Features
- Chess game implementation with standard rules.
- Possible API module for move generation and game history.
- Can be extended with AI (Stockfish) or online multiplayer.

## Setup in GitHub Codespaces
### 1. Clone the Repository
Open a terminal in **GitHub Codespaces** and run:
```sh
git clone https://github.com/YOUR_USERNAME/CopyChess.git
cd Chess
```

### 2. Install Dependencies
If you're using Python, create a `requirements.txt` with your dependencies (e.g. `pygame`). Then run:
```sh
pip install -r requirements.txt
```

### 3. Run the Program
To start the chess game:
```sh
python main.py  # Example if using Python
./chess         # If compiled from C
```

## API Integration (Optional)
To integrate an API for move validation or AI support, you can create a Flask server:
```sh
python api.py
```
Then send a request to:
```sh
curl -X POST http://127.0.0.1:5000/api/move -d '{"move": "e2e4"}'
```

## Future Enhancements
- Implement **Stockfish AI** for move suggestions.
- Add **online multiplayer** via a Flask or FastAPI backend.
- Improve UI/UX with a web-based interface.

## License
This project is open-source under the **MIT License**.
