def test_get_by_category(collection_with_memes):
    memes = collection_with_memes.get_by_category("ситуация")
    assert len(memes) > 0


def test_empty_category(collection_with_memes):
    memes = collection_with_memes.get_by_category("спорт")
    assert memes == []
