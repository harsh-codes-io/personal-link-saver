# Personal Link Saver

A simple command-line application built with Python to save, organize, search, and manage useful URLs.

The project focuses on practicing Python fundamentals, file handling, JSON persistence, input validation, modular programming, and basic software engineering practices.

## Features

- **Add Links:** Save URLs with a title and category.
- **View Links:** Display all saved links.
- **Search Links:** Search saved links using keywords in their titles.
- **Delete Links:** Delete saved links using their unique IDs.
- **URL Validation:** Validate URL structure using Python's `urllib.parse`.
- **Input Validation:** Prevent empty or whitespace-only inputs.
- **Unique IDs:** Automatically generate unique IDs for saved links.
- **Data Persistence:** Store and retrieve links using JSON.
- **Error Handling:** Handle missing or invalid JSON files.
- **Interactive CLI:** Navigate through a menu-driven interface.

## Project Structure

```text
personal-link-saver/
│
├── main.py          # Main application and CLI operations
├── storage.py       # JSON data storage and retrieval
├── links.json       # Persistent link storage
├── README.md
└── .gitignore
```

## Technologies Used

- Python
- JSON
- pathlib
- urllib.parse
- Git and GitHub

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd personal-link-saver
```

### 2. Run the application

```bash
python main.py
```

### 3. Use the menu

```text
===== PERSONAL LINK SAVER =====

1. Add a new link
2. View all links
3. Search links
4. Delete a link
5. Exit
```

Follow the prompts to manage your saved links.

## Data Storage

All saved links are stored locally in `links.json` using JSON format.

Each link follows this structure:

```json
{
    "id": 1,
    "title": "Python Documentation",
    "url": "https://docs.python.org/3/",
    "category": "Learning"
}
```

## Learning Outcomes

Through this project, I practiced:

- Python functions and modular programming
- Lists and dictionaries
- Loops and conditional statements
- Exception handling
- Type hints
- File handling with `pathlib`
- JSON serialization and deserialization
- URL parsing and validation
- Git version control

## Future Improvements

- Automated testing using pytest
- Improved URL and domain validation
- Better input handling and error messages
- Database integration using PostgreSQL
- GUI or web-based interface

---

**Project Status:** Initial CLI version completed. Further improvements planned.