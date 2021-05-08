import pytest
import documents

GET_NAME_CASES = [
    ('2207 876234', 'Leia Organa'),
    ('11-2', 'Anakin Skywalker'),
    ('10006', 'Han Solo')
    ]

GET_SHELF_CASES = [
    ('2207 876234', 'document #2207 876234 stored on shelf#1'),
    ('11-2', 'document #11-2 stored on shelf#1'),
    ('10006', 'document #10006 stored on shelf#2')
]

ADD_SHELF_CASES = ['4', '5', '6', '7']

ADD_NEW_DOCUMENT_CASES = [
    ('11-04', 'invoice', 'Boba Fett', '4', '4'),
    ('2206 7468941', 'passport', 'Darth Vader', '5', '5')
]

DELETE_DOCUMENT_CASES = ['2207 876234', '11-2', '10006']

class TestApplication:

    @pytest.mark.parametrize('doc_number, expected_result', GET_NAME_CASES)
    def test_get_name_by_document_number(self, doc_number, expected_result):
        actual_result = documents.get_name_by_document_number(doc_number)
        assert actual_result == expected_result, 'Error'

    @pytest.mark.parametrize('doc_number, expected_result', GET_SHELF_CASES)
    def test_get_shelf_by_document_number(self, doc_number, expected_result):
        actual_result = documents.get_shelf_by_document_number(doc_number)
        assert actual_result == expected_result, 'Error'

    @pytest.mark.parametrize('shelf', ADD_SHELF_CASES)
    def test_add_new_shelf(self, shelf):
        assert documents.add_new_shelf(shelf) == (shelf, True)

    @pytest.mark.parametrize('document_number, document_type, name, shelf, expected_result', ADD_NEW_DOCUMENT_CASES)
    def test_add_new_document(self, document_number, document_type, name, shelf, expected_result):
        actual_result = documents.add_new_document(document_number, document_type, name, shelf)
        assert actual_result == expected_result, 'Error'

    @pytest.mark.parametrize('document_number', DELETE_DOCUMENT_CASES)
    def test_remove_document(self, document_number):
        assert documents.remove_document(document_number) == (document_number, True)




