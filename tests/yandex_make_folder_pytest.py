import yandex_make_folder
import pytest

MAKE_FOLDER_CASES = [
    ("folder 01", 201),
    ("//folder 02", 404),
    ("folder 01", 409),
    ("folder 03/subfolder", 409),
]

class TestYandexMakeFolder:
    @pytest.mark.parametrize("folder_name, expected_result", MAKE_FOLDER_CASES)
    def test_folder_status_code_argument(self, folder_name, expected_result):
        assert yandex_make_folder.make_folder(folder_name) == expected_result, 'Error'
