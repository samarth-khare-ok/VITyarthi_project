users = {}

def create_account():
    print("Create An Account : ")
    u = input("Username: ")
    if u in users:
        print("User already exists. Try another username.")
        return
    p = input("Password : ")
    users[u] = {"password": p, "docs": []}
    print("Account created successfully.\n")


def login():
    print("Login")
    u = input("Username: ")
    p = input("Password: ")
    if u in users and users[u]["password"] == p:
        print("Login successful!\n")
        return u
    print("Wrong Credentials.\n")
    return None


def upload_doc(u):
    print("Upload Documents : ")
    name = input("Document name : ")
    dtype = input("Type (PDF/Image/etc): ")
    users[u]["docs"].append({"name": name, "type": dtype})
    print("Document Uploaded.\n")


def view_docs(u):
    print("Your Documents : ")
    docs = users[u]["docs"]
    if not docs:
        print("No documents found.\n")
        return
    for i, d in enumerate(docs, 1):
        print(f"{i}. {d['name']} ({d['type']})")
    print()


def search_doc(u):
    print("Search Documents : ")
    k = input("Keyword: ").lower()
    found = False
    for d in users[u]["docs"]:
        if k in d["name"].lower():
            print(f"- {d['name']} ({d['type']})")
            found = True
    if not found:
        print("No matching documents found.")
    print()


def delete_doc(u):
    print("Delete Documents : ")
    docs = users[u]["docs"]
    if not docs:
        print("No documents to delete.\n")
        return
    view_docs(u)
    try:
        c = int(input("Enter document number to delete: "))
        if 1 <= c <= len(docs):
            deleted = docs.pop(c-1)
            print(f"{deleted['name']} deleted successfully.\n")
        else:
            print("Invalid document number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def user_menu(u):
    while True:
        print(f"Welcome {u.upper()}")
        print("1. Upload\n2. View\n3. Search\n4. Delete\n5. Logout")
        ch = input("Choice: ")

        if ch == "1":
            upload_doc(u)
        elif ch == "2":
            view_docs(u)
        elif ch == "3":
            search_doc(u)
        elif ch == "4":
            delete_doc(u)
        elif ch == "5":
            print("Logged out.\n")
            break
        else:
            print("Invalid choice. Try again.\n")

while True:
    print("==== Mini Digilocker ====")
    print("1. Create Account\n2. Login\n3. Exit")
    ch = input("Choice: ")

    if ch == "1":
        create_account()
    elif ch == "2":
        u = login()
        if u:
            user_menu(u)
    elif ch == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")
