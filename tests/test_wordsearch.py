from src.wordsearch import generate_wordsearch

def test_generate_wordsearch():
    words = ["python", "ai"]
    grid = generate_wordsearch(words, grid_size=10)
    assert grid.shape == (10, 10)
