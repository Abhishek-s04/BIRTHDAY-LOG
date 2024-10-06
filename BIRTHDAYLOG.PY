# create a birthday record log{using dictionary}
# Display
def display(Birthday_record):
    print("Current entries:")
    for name, birthdate in Birthday_record.items():
        print(f"{name}: {birthdate}")
# Search
def search(Birthday_record):
    name = input('Enter the name to search: ')
    if name in Birthday_record:
        print(f"{name}'s birthdate is: {Birthday_record[name]}")
    else:
        print('Name not found.')
# Add a new birthday
def add(Birthday_record):
    name = input('Enter the name to add: ')
    birth = input('Enter the birthdate (e.g., 14 July): ')
    Birthday_record[name] = birth
    print(f"Added {name}'s birthdate as {birth}.")
# Change the birth date of person.
def change(Birthday_record):
    name = input('Enter the name to update: ')
    if name in Birthday_record:
        birth = input(f'Enter the new birthdate for {name}: ')
        Birthday_record[name] = birth
        print(f"Updated {name}'s birthdate to {birth}.")
    else:
        print('Name not found.')
# delete the name and birthdate of person.
def delete(Birthday_record):
    name = input('Enter the name to delete: ')
    if name in Birthday_record:
        Birthday_record.pop(name)
        print(f"Deleted {name}'s record.")
    else:
        print('Name not found.')

Birthday_record={}
count=0
print("Enter 10 Name and Birthday that you want to add in your Birthday log")
while (count<10):
    name=input("Name: ")
    birth_date=input("Birth date :")
    Birthday_record[name]=birth_date
    count+=1
while True:
  print("\nMenu:")
  print("1. Display all")
  print("2. Search by name")
  print("3. Add a new entry")
  print("4. Change a birthdate")
  print("5. Delete an entry")
  print("6. Exit")
  choice=int(input('enter your choice : '))
  match choice:
    case 1:
      display(Birthday_record)
    case 2:
      search(Birthday_record)
    case 3:
      add(Birthday_record)
    case 4:
      change(Birthday_record)
    case 5:
      delete(Birthday_record)
    case 6:
     print("Thank you!! Have a nice day :)")
     break
    case _:
      print('invalid choice')