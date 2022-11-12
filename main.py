from solution import GenerateSchema
import unittest
import argparse


if __name__ == '__main__':
    

    # To take arguments from the command line
    parser = argparse.ArgumentParser(description='A program to generate Schema from a JSON file.',)

    parser.add_argument('-r', "--file_to_read", help="The JSON file to read.", default="./data/data_1.json", type=str)
    parser.add_argument('-w', "--file_to_write", help="The JSON file to write the results to.", default="./schema/schema_1.json", type=str)


    args = parser.parse_args()
    
    generate_schema = GenerateSchema(file_to_read=args.file_to_read, file_to_write=args.file_to_write)
    generate_schema.read_json()
    generate_schema.generate_full_schema()
    generate_schema.write_to_json()

    # To help in running tests
    unittest.main()