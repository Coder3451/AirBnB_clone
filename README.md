# AirBnB Clone

This project is a simplified clone of the AirBnB website. It includes a a command interpreter to manage AirBnB objects (such as Users, Places, etc.) that can later be extended to include a web interface, API, and more.

## Command Interpreter

The command interpreter (or console) is designed to:

- create new objects (e.g., `create User`)
- Retrieve existing objects
- Update object attributes
- Delete objects
- List all objects, etc.

### How to Start the Console

1. Make sure the file `console.py is executable.
2. Run the following command:
   ```bash
   ./console.py
You should see a prompt like (hbnb).

Basic Usage Examples
- Create an Object:
  ``` (hbnb) create User
- Show an Object:
  ``` (hbnb) show User <object_id>
- Update an Object:
  ``` (hbnb) update User <object_id> <attribute_name> "<attribute_value>"
- Delete an Object:
  ``` (hbnb) destroy User <object_id>
Feel free to expand on these examples as you add more commands and functionality.

Project Structure
This repository will eventually include:
- A command interpreter for managing objects.
- A set of models (like BaseModel, User, Place, etc.).
- A storage engine for serialization/deserialization.
- Unit tests for all functionalities.

How to Contribute
- Use branches and pull requests to manage changes.
- Write clear commit messages.
- Follow the coding style guidelines.
