Mini DigiLocker (Python Project)

Mini DigiLocker is a simple Python-based document storage system where users can:

1) Create an account

2) Log in

3) Upload documents

4) View their saved documents

5) Search documents

6) Delete documents

This project simulates a very basic version of India's DigiLocker system.

 Features
 
 1. User Account System

 2. Create a new account

 3. Secure login using username and password

 4. Document Management

Users can:

1. Upload documents (PDF/Image/etc.)

2. View all uploaded documents

3. Search documents by name

4. Delete documents

All documents are stored inside the user’s profile in Python dictionaries.

   How the Program Works
 1. Create an Account

 2. Users can register by entering a username and password.

 3. Login

 4. Password is checked before allowing access.

User Dashboard

After login, users can choose:

1. Upload Document
2. View Documents
3. Search Document
4. Delete Document
5. Logout

Uploading Documents

Each document entry stores:

{"name": "Aadhaar", "type": "PDF"}

Searching Documents

Users can search by keyword (case-insensitive).

Deleting Documents

Users can delete by selecting the document number from the list.

Code Structure

create_account() → Register new user

login() → Authenticate user

upload_doc() → Add document

view_docs() → Show all documents

search_doc() → Search by keyword

delete_doc() → Remove a document

user_menu() → Dashboard for logged-in user

Running the Program

Just run the Python file:

python digilocker.py


Follow the menu on screen.

Technologies Used

1. Python

2. Dictionary-based storage

3. Basic loops and functions

4. Future Improvements

You can add the following later:

Save data permanently using JSON or database

Add password hashing

Add document preview

Add user roles (Admin/User)
