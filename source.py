users = {}  

def create_account():
  print("Create An Account : ")
  u = input("Username: ")
  if u in users:
    print("User exists.")
  p = input("Password : ")
  users[u] = {"password": p, "docs": []}
  print("Account created")

def login():
  print("Login ")
  u = input("Username: ")
  p = input("Password: ")
  if u in users and users[u]["password"] == p:
    print("Login successful : ")
    return u
  print("Wrong Credentials.")

def upload_doc(u):
  print("Upload documents : ")
  name = input("Document name : ")
  dtype = input("Type (PDF/Image/etc): ")
  users[u]["docs"].append({"name": name, "type": dtype})
  print("Uploaded")

def view_docs(u):
  print(" Your Documents : ")
  docs = users[u]["docs"]
  if not docs:
    print("No documents : "); return
  for i, d in enumerate(docs, 1):
    print(f"{i}. {d['name']} ({d['type']})")
  print()

def search_doc(u):
  print(" Search Documents : ")
  k = input("Keyword: ").lower()
  found = False
  for d in users[u]["docs"]:
    if k in d["name"].lower():
      print(f"- {d['name']} ({d['type']})"); found = True
  if not found: print("No match.")
  print()

def delete_doc(u):
  print("Delete Documents : ")
  docs = users[u]["docs"]
  if not docs:
    print("No docs"); return
  view_docs(u)
  c = int(input("Doc number: "))
  if 1 <= c <= len(docs):
    print(docs.pop(c-1)["name"], "deleted")
  else:
    print("Invalid")

def user_menu(u):
  while True:
    print("Welcome{u.upper()}")
    print("1.Upload 2.View 3.Search 4.Delete 5.Logout")
    ch = input("Choice: ")
    if ch=="1": 
			upload_doc(u)
    elif ch=="2": 
			view_docs(u)
    elif ch=="3": 
			search_doc(u)
    elif ch=="4": 
			delete_doc(u)
    elif ch=="5": 
			print() 
			break
    else: 
			print("Invalid")

while True:
  print(" Mini Digilocker ")
  print("1.Create 2.Login 3.Exit")
  ch = input("Choice: ")
  if ch=="1": 
		create_account()
  elif ch=="2":
    u = login()
    if u: user_menu(u)
  elif ch=="3": 
		break
  else: 
		print("Invalid")
