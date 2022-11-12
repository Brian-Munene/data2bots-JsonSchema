from solution import GenerateSchema
import unittest


if __name__ == '__main__':
    unittest.main()
    generate_schema = GenerateSchema(file_to_read='./data/data_1.json', file_to_write='./schema/schema_1.json')
    generate_schema.read_json()
    generate_schema.generate_full_schema()
    generate_schema.write_to_json()