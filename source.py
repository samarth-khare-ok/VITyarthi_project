users_db = {}

def create_account():
  print("Create An Account : ")
  new_user = input("Username: ").strip()
  if new_user in users_db:
    print("User already exists.")
    return
  new_pass = input("Password : ")
  users_db[new_user] = {"password": new_pass, "docs": []}
  print("Account created")

def login():
  print("Login")
  entered_user = input("Username: ")
  entered_pass = input("Password: ")
  if entered_user in users_db and users_db[entered_user]["password"] == entered_pass:
    print("Login successful")
    return entered_user
  print("Wrong Credentials")
  return None

def upload_doc(username):
  print("Upload Documents : ")
  file_name = input("Document name : ")
  file_type = input("Type (PDF/Image/etc): ")
  new_doc = {"name": file_name, "type": file_type}
  user_docs_list = users_db[username]["docs"]
  user_docs_list.append(new_doc)
  print("Document Uploaded")

def view_docs(username):
  print("Your Documents : ")
  all_docs = users_db[username]["docs"]
  if not all_docs:
    print("No documents found")
    return
  for idx, doc in enumerate(all_docs, 1):
    print(f"{idx}. {doc['name']} ({doc['type']})")
  print()

def search_doc(username):
  print("Search Documents : ")
  keyword = input("Keyword: ").lower()
  found_any = False
  for d in users_db[username]["docs"]:
    if keyword in d["name"].lower():
      print(f"- {d['name']} ({d['type']})")
      found_any = True
  if not found_any:
    print("No matching documents found.")
  print()

def delete_doc(username):
  print("Delete Documents : ")
  user_docs = users_db[username]["docs"]
  if not user_docs:
    print("No documents to delete")
    return
  view_docs(username)
  try:
    choice = int(input("Enter document number to delete: "))
    if 1 <= choice <= len(user_docs):
      removed_doc = user_docs.pop(choice - 1)
      print(f"{removed_doc['name']} deleted successfully")
    else:
      print("Invalid document number")
  except ValueError:
    print("Please enter a valid number")

def user_menu(username):
  while True:
    print(f"Welcome {username.upper()}")
    print("1. Upload  2. View   3. Search    4. Delete   5. Logout")
    user_choice = input("Choice: ")
    if user_choice == "1":
      upload_doc(username)
    elif user_choice == "2":
      view_docs(username)
    elif user_choice == "3":
      search_doc(username)
    elif user_choice == "4":
      delete_doc(username)
    elif user_choice == "5":
      print("Logged out")
      break
    else:
      print("Invalid choice. Try again")

while True:
  print("Mini Digilocker")
  print("1. Create Account\n2. Login\n3. Exit")
  main_choice = input("Choice: ")
  if main_choice == "1":
    create_account()
  elif main_choice == "2":
    active_user = login()
    if active_user:
      user_menu(active_user)
  elif main_choice == "3":
    print("Exiting program")
    break
  else:
    print("Invalid")

