 Statement of Purpose and Functionality
This program creates a basic simulation of a digital document storage application, similar in concept to India's Digilocker.

Core Functionality : 

The program's main features revolve around user management and document operations:

~User Management:

1. It uses a global dictionary, users, to store user data, where the username is the key.

2. The create_account function registers new users by taking a username and password.

3. The login function authenticates a user by checking the provided username and password against the stored data.

~Document Management:

1. Each user's data includes a list of documents ("docs"), where each document is a dictionary with a name and type.

2. The upload_doc function lets a logged-in user add a new document entry to their account.

3. The view_docs function displays all documents associated with the logged-in user.

4. The search_doc function finds documents based on a keyword match in the document name.

5. The delete_doc function allows a user to remove a document entry by selecting its number from the displayed list.

~Menu System:

1. A primary while loop presents the main Create/Login/Exit menu.

2. The user_menu function, accessible upon successful login, provides a separate menu for document operations (Upload, View, Search, Delete, Logout).

Limitations (Security and Persistence)
Non-Persistence: The data (users and documents) is stored only in memory (the users dictionary). When the program is terminated, all data is lost.

Security: Passwords are stored in plain text, which is highly insecure. There is no hashing or encryption.

Data Integrity: The document operations only manage metadata (name and type); no actual files are handled, uploaded, or stored on the disk.
