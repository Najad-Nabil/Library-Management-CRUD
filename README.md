# Library Management System

## Overview

A console-based Library Management System built using Python and Object-Oriented Programming (OOP) principles. The application allows users to manage books and library members, track borrowed books, and persist data using JSON storage.

This project was developed to practice OOP concepts, data persistence, modular programming, and software design fundamentals.

## Features

### Book Management

* Add new books
* Search books by ID
* View all books
* Remove books
* Borrow books
* Return books
* Track book availability
* Track which member has borrowed a book

### Member Management

* Add new members
* Search members by ID
* Remove members
* Prevent deletion of members who currently have borrowed books
* View books borrowed by a member

### Data Persistence

* Save data automatically to a JSON file
* Load existing data when the application starts
* Maintain book and member records between sessions

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* JSON for data storage

## Concepts Practiced

* Classes and Objects
* Encapsulation
* Object Relationships
* Class Methods
* Data Serialization
* File Handling
* Error Handling
* CRUD Operations
* Modular Programming

## Example Workflow

1. Add books to the library.
2. Add members.
3. Borrow books using a member ID.
4. Track borrowed books for each member.
5. Return books.
6. Remove books or members when eligible.
7. Automatically save all changes to JSON storage.

## Future Improvements

* Search books by title
* View all members
* Database integration (SQLite)
* REST API implementation using FastAPI
* User authentication
* Due dates and fine calculation
* Graphical or web-based user interface

## Learning Outcomes

This project helped strengthen understanding of:

* Python programming
* Object-Oriented Design
* Data persistence with JSON
* Program organization across multiple modules
* Real-world entity relationships
* Debugging and problem-solving

## Author

Developed as a learning project to practice Python and software development fundamentals.
