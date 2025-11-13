from qa.topics.themes import Theme, Themes
from qa import resources_dir_path
import json

fauna_json_path = resources_dir_path / "themes.json"


def get_themes() -> Themes:
    with open(fauna_json_path, "r", encoding='utf-8') as f:
        json_data = json.loads(f.read())
    return Themes(**json_data)

class TestThemes:
    def test_create(self):
        themes = get_themes()
        path = ["Probatoire AMM", "Le milieu montagnard"]
        sub_theme = themes.get_theme_from_path(path)
        assert sub_theme.name == "Le milieu montagnard"
        assert sub_theme.id_path == path
