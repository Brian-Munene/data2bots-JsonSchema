# Generate JSON Schema Solution

The program in this repository generates a JSON schema from a JSON from and outputs a JSON document containing the generated schema.

## Setting up the project

To set up the project you will need to create a virtual environment within which the program will run. To do this cd into the project directory and then run the following command.

``virtualenv venv``

To activate the virtual environment, run the following command:
Linux/MacOS

``source venv/activate``

Windows

``venv\Scripts\activate``

Next step is to install re dependencies. To do this run the following command.

``pip install -r requirements.txt``

## Running the program

To run the program, run the following command:

``python main.py``

## Testing the program

To test the program, run the following command:

``python -m unittest test``

To get a more verbose test run, run the following command:

``python -m unittest -v tests``
