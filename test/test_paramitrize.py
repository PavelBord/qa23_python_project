import pytest


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
