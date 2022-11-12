from typing import Dict, TypeVar, List, Set
import json
from num2words import num2words

class GenerateSchema:
    def __init__(self, file_to_read: str, file_to_write: str):
        self.read_file_name: str = file_to_read
        self.write_file_name: str = file_to_write
        self.json_data: Dict = {}
        self.result: Dict[str, List[str]] = {}

    def read_json(self) -> None:
        """
        Reads the JSON and loads the data.
        """
        with open(self.read_file_name, "r") as file:
            data = json.load(file)
            self.json_data = data['message']
    
    def write_to_json(self) -> None:
        """Writes the result to the schema file."""
        with open(self.write_file_name, "w") as file:
            json.dump(self.result, file, indent=4)

    def get_attributes(self, item)-> List:
        """
        Gets an individual item from a dictionary or a list.
        """
        items: List = []
        for val in item.values():
            items.append(val)
        return items
    
    def get_type(self, item) -> str:
        """
        Gets the type of an item.
        """
        item_type = type(item).__name__
        if  item_type == 'str':
            return 'string'
        elif item_type == 'int':
            return 'integer'
        elif item_type == 'list':
            if item:
                if type(item[0]).__name__ == 'str':
                    return  'ENUM'
                if type(item[0]).__name__ == 'dict':
                    return 'ARRAY'
            else:
                return 'list'
        else:
            return item_type
        
        
    
    def generate_attribute_schema(self, attribute)-> Dict:
        item_type = self.get_type(attribute)
        item_details = {
            "type": item_type,
            "tag": "",
            "description": "",
            "required": False
        }
        
        return item_details
    

    def generate_full_schema(self)-> Dict:
        attributes = self.get_attributes(self.json_data)
        for idx, attribute in enumerate(attributes, start=1):
            item_schema = self.generate_attribute_schema(attribute)

            if item_schema['type'] == "dict":

                children = self.get_attributes(attribute)
                attributes.extend(children)
            self.result[f"key_{num2words(idx)}"] = item_schema
            

