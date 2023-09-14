# Library Management System

A simple library management system implemented in Python using Tkinter for the graphical user interface and MySQL for data storage. This project allows you to manage a library's collection of books and library members.

## Table of Contents 

- [Library Management System](#library-management-system)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)


## Features

- Add and remove books from the library collection.
- Add and manage library members.
- Graphical user interface for easy interaction.
- Data validation to ensure the integrity of stored information.
- Uses a MySQL database to store book and member data.


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- MySQL server installed and running.
- Required Python libraries installed. You can install them using pip:

```pip install mysql-connector-python tkinter```

## Installation 
1. Clone the repository:  
    ```git clone https://github.com/adi-pr/Library-Manager.git```

2. Navigate to the project directory:  
   ```cd Library-Manager```

3. Update the database connection settings in the Database class to match your MySQL server configuration:  
    Inside the Database class in database.py  
``` connection = mysql.connector.connect( ```  
&nbsp; &nbsp; ```host="localhost", user="root", password="root", database="library" ```  
   ``` ) ```
