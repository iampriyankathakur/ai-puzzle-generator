# 🧩 AI Puzzle Generator

This project generates **word puzzles** (word search, crosswords) from a word list or theme.  
It can also auto-generate **clues** using NLP.

## 🚀 Features
- Word Search Puzzle generation
- AI-powered clue generation
- Export puzzles as images
- Example word list included

## ⚙️ Installation
```bash
git clone https://github.com/yourusername/ai-puzzle-generator.git
cd ai-puzzle-generator
pip install -r requirements.txt
```

## ▶️ Usage

```
python src/pipeline.py --words data/sample_words.txt --mode wordsearch
```

## 📊 Tech Stack

Python

Visualization: matplotlib

NLP: nltk / WordNet (for clues)

## Requirements

matplotlib
numpy
nltk
pytest
