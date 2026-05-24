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
