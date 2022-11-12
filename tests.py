import unittest
from solution import GenerateSchema

class TestGenerateSchema(unittest.TestCase):
    """
    TestCases for the GenerateSchema class.
    """
    @classmethod
    def setUpClass(cls):
        cls.schema = GenerateSchema()
        cls.test_data = {
            "id": "ABCDEFGHIJKLMNOPQR",
            "name": "ABCDEFGHIJKLMNOPQRSTUVWX",
            "orientation": "ABCDEFGHIJKLMNO",
            "settings": {
                "minParticipants": 942,
                "maxParticipants": 641,
                "battleType": "ABCDEFGHIJKLMN",
                "wagerType": "ABCDEFGHIJKLMNOPQRSTUVW",
                "countdown": 69,
                "duration": 200,
                "archetype": {
                    "name": "ABCDEFGHIJKLMNOPQRS",
                    "iconId": "ABCDEFGHIJKLMNOPQRST"
                    }
                }
            }
    def test_get_attributes(self):
        """
        Test if the get attributes returns a list.
        """
        attributes = self.schema.get_attributes(self.test_data)

        self.assertEqual(type(attributes).__name__, 'list')
    
    def test_get_type_return_string(self):
        """
        Test get type returns a string
        """
        get_type = self.schema.get_type(self.test_data)

        self.assertEqual(get_type, 'dict')




