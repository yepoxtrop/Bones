# BONES

### Description

### Structure
```
Bones/
├── main.py                           # Principal script to start the application
├── src/                              # Folder for source code of the application, organized in modules, classes and functions
│   ├── config/                       # Folder for configuration files and settings
│   │   └── settings.py               # Configuration settings for the application
│   ├── core/           
│   │   └── engine.py
│   ├── tasks/
│   |   ├── classes/                  # Folder for classes related to tasks
|   |   |   ├── addresses/            # Folder for classes related to addresses
|   |   |   |   ├── __init__.py       # Initialization file for the addresses package
|   |   |   |   └── address.py        # Class for handling addresses
|   |   |   ├── logs/                 # Folder for classes related to logs
|   |   |   |   ├── __init__.py       # Initialization file for the logs package
|   |   |   |   ├── log_writer.py     # Class for handling log writing
|   |   |   |   ├── logs.py           # Class for handling logs
|   |   |   |   └── address.py        # Class for handling addresses
|   |   |   └── tasks/                # Folder for classes related to tasks
|   |   └── modules/                  # Folder for modules related to tasks
|   └── utils/                        # Folder for utility functions
|       └── logger.py                 # Utility functions for logging      
└── tests/                           # Unit tests for the application
```

### Functions
- [ ] Update operative systema
    - [ ] Windows
    - [ ] Linux

### NOTES
- [ ] Program tasks to run this app in diferents computers under a network or domains

### TODO
- [X] Create a basic structure for the app
- [X] Create a basic script to start the application
- [X] Create a folder for source code and organize it in modules, classes and functions
- [X] Create logs classes to handle logs in the application
- [ ] Create a configuration script and define environment variables
- [ ] Create the app XD
- [ ] Create a GUI for the app