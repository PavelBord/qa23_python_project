def test_empty_collection(empty_collection):
    assert empty_collection.memes == []


def test_collection_not_empty(collection_with_memes):
    assert len(collection_with_memes.memes) != 0


def test_new_meme_added(empty_collection):
    empty_collection.add_meme("Ждун", "мем", "440")
    assert len(empty_collection.memes) == 1


def test_meme_count(empty_collection):
    count = len(empty_collection.memes)
    empty_collection.add_meme("Узбагойся", "котики", "270")
    assert len(empty_collection.memes) == count + 1

def test_meme_data(empty_collection):
    empty_collection.add_meme("Наташа,мы все уронили","ситуация","350")
    meme = empty_collection.memes [0]
    assert meme["title"] == "Наташа,мы все уронили"
    assert meme["category"] == "ситуация"
    assert meme["likes"] == 600