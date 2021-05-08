import unittest
import yandex_make_folder


class TestYandexMakeFolder(unittest.TestCase):

    def test_folder_status_code_201(self):
        self.assertEqual(yandex_make_folder.make_folder('folder 01'), 201)

    def test_folder_status_code_404(self):
        self.assertEqual(yandex_make_folder.make_folder('//folder 02'), 404)

    def test_folder_status_code_409(self):
        self.assertEqual(yandex_make_folder.make_folder('folder 01'), 409)
