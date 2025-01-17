# StartupEditor

StartupEditor is a Python program that allows detailed editing and management of startup items to speed up boot times on Windows. It provides functionality to list, add, and remove startup items from both the Windows Registry and the Startup Folder.

## Features

- List all startup items from the Windows Registry and Startup Folder.
- Add new programs to start automatically at boot via the Registry or Startup Folder.
- Remove existing startup items from the Registry or Startup Folder.

## Requirements

- Windows operating system
- Python 3.x
- Administrative privileges to modify Registry and Startup Folder

## Installation

1. Clone the repository or download the `StartupEditor.py` file.
2. Ensure you have Python 3.x installed on your system.

## Usage

Run the script from the command line:

```bash
python StartupEditor.py
```

You can modify the script to add or remove specific startup items by using the `add_startup_item` and `remove_startup_item` methods.

### Example

To add a new startup item via the registry:

```python
editor.add_startup_item("MyApp", "C:\\Path\\To\\MyApp.exe", location='registry')
```

To remove an existing startup item:

```python
editor.remove_startup_item("MyApp", location='registry')
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any bugs or improvements.

## License

This project is licensed under the MIT License.