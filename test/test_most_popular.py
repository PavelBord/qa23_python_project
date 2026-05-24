from mems import MemeCollection


def test_no_memes(empty_collection):
    assert empty_collection.get_most_popular() is None


def test_popular_meme(collection_with_memes):
    meme = collection_with_memes.get_most_popular()
    assert meme["likes"] == 950


def test_same_likes():
    collection = MemeCollection()
    collection.add_meme("Мем 1", "мем", "500")
    collection.add_meme("Мем 2", "мем", "500")

    meme = collection.get_most_popular()
    assert meme["likes"] == 500
