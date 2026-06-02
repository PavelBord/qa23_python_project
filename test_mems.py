import pytest
from mems import MemeCollection


@pytest.fixture
def empty_collection():
    return MemeCollection()


@pytest.fixture
def collection_with_memes():
    collection = MemeCollection()

    collection.add_meme("Наташ,мы все уронили", "ситуация", "950")
    collection.add_meme("Ждун", "реакция", "870")
    collection.add_meme("Это фиаско,братан", "животные", "760")
    collection.add_meme("Узбагойся", "котики", "690")

    return collection


@pytest.fixture
def clean_collection():
    collection = MemeCollection()
    yield collection

    collection.clear()


def test_clear_collection(collection_with_memes):
    collection_with_memes.clear()
    assert collection_with_memes.memes == []


def test_get_by_category(collection_with_memes):
    memes = collection_with_memes.get_by_category("ситуация")
    assert len(memes) == 1
    assert memes[0]["title"] == "Наташ,мы все уронили"
    assert memes[0]["category"] == "ситуация"


def test_no_category(collection_with_memes):
    memes = collection_with_memes.get_by_category("спорт")
    assert memes == []


def test_empty_collection(empty_collection):
    assert empty_collection.memes == []


def test_collection_not_empty(collection_with_memes):
    assert len(collection_with_memes.memes) != 0


def test_new_meme_added(empty_collection):
    empty_collection.add_meme("Ждун", "мем", "440")
    assert len(empty_collection.memes) == 1
    added_meme = empty_collection.memes[0]
    assert added_meme["title"] == "Ждун"
    assert added_meme["category"] == "мем"


def test_meme_count(empty_collection):
    count = len(empty_collection.memes)
    empty_collection.add_meme("Узбагойся", "котики", "270")
    assert len(empty_collection.memes) == count + 1


def test_meme_data(empty_collection):
    empty_collection.add_meme("Наташа,мы все уронили", "ситуация", "600")
    meme = empty_collection.memes[0]
    assert meme["title"] == "Наташа,мы все уронили"
    assert meme["category"] == "ситуация"
    assert meme["likes"] == "600"


def test_no_memes(empty_collection):
    assert empty_collection.get_most_popular() is None


def test_popular_meme(collection_with_memes):
    meme = collection_with_memes.get_most_popular()
    assert meme["likes"] == "950"


def test_same_likes():
    collection = MemeCollection()
    collection.add_meme("Мем 1", "мем", "500")
    collection.add_meme("Мем 2", "мем", "500")

    meme = collection.get_most_popular()
    assert meme["likes"] == "500"


@pytest.mark.parametrize("title,category,likes",
                         [
                             (123, "мем", "150"),
                             ("Ждун", 123, "150"),
                             ("Ждун", "мем", "abc"),
                             ("", "мем", "100"),
                             ("Ждун", "", "100"),
                             ("Ждун", "мем", "-5"),
                         ]
                         )
def test_invalid_data(empty_collection, title, category, likes):
    result = empty_collection.add_meme(title, category, likes)

    assert result != "Success"
