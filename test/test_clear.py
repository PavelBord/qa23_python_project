def test_clear_collection(collection_with_memes):
    collection_with_memes.clear()
    assert collection_with_memes.memes == []
