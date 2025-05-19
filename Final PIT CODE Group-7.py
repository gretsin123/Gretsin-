import os
from datetime import datetime

visitor_log = []

class bcolors:
    HEADER = '\033[95m'
    PINK = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    OKBLUE = '\033[94m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def header_art():
    print(bcolors.CYAN + bcolors.BOLD)
    print("\t\t\t\t\t\t\t  ,--. ,--. ,---. ,--------.,------. ")
    print("\t\t\t\t\t\t\t  |  | |  |'   .-''--.  .--'|  .--. '  ")
    print("\t\t\t\t\t\t\t  |  | |  |`.  `-.   |  |   |  '--' | ")
    print("\t\t\t\t\t\t\t  '  '-'  '.-'    |  |  |   |  | --' ")
    print("\t\t\t\t\t\t\t   `-----' `-----'   `--'   `--'" + bcolors.ENDC)

def show_menu():
    print("\n" + " " * 52 + bcolors.PINK + "=" * 46 + bcolors.ENDC)
    print(" " *52 + bcolors.YELLOW + "== WELCOME TO VISITOR LOG MANAGEMENT SYSTEM ==" + bcolors.ENDC)
    print(" " * 52 + bcolors.PINK + "=" * 46 + bcolors.ENDC)
    print(" " * 63 + bcolors.GREEN + "1. Log In Visitor" + bcolors.ENDC)
    print(" " * 63 + bcolors.GREEN + "2. Search Visitor by Name" + bcolors.ENDC)
    print(" " * 63 + bcolors.GREEN + "3. View All Visitors" + bcolors.ENDC)
    print(" " * 63 + bcolors.FAIL + "4. Exit" + bcolors.ENDC)

def get_input(prompt, field_name, validate_func=None):
    while True:
        value = input(" " * 28 + prompt).strip()
        if value == "":
            print(" " * 28 + bcolors.FAIL + f"Please enter your {field_name}." + bcolors.ENDC)
        elif validate_func and not validate_func(value):
            continue
        else:
            return value
def is_valid_name(name):
    parts = name.split()
    if len(parts) < 2:
        print(" " * 50 + bcolors.FAIL + "Please enter your full name (first and last name)." + bcolors.ENDC)
        return False
    return True

def capitalize_name(name):
    return ' '.join(word.capitalize() for word in name.split())

def is_valid_contact(number):
    if not number.isdigit():
        print(" " * 63 + bcolors.FAIL + "Please enter a valid contact number (numbers only)." + bcolors.ENDC)
        return False
    elif len(number) != 11:
        print(" " * 50 + bcolors.FAIL + "Contact number must be exactly 11 digits." + bcolors.ENDC)
        return False
    return True

def is_valid_address(address):
    if len(address) < 10:
        print(" " * 50 + bcolors.FAIL + "Please enter a complete address (at least 10 characters)." + bcolors.ENDC)
        return False
    return True

def save_visitor_to_file(visitor):
    with open("visitor_log.txt", "a", encoding="utf-8") as file:
        line = f"{visitor['name']} | {visitor['contact_number']} | {visitor['purpose']} |  {visitor['time_in']} | {visitor['date']} | {visitor['address']}\n" 

        file.write(line)       

def load_visitors_from_file():
    if os.path.exists("visitor_log.txt"):
        with open("visitor_log.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 6:
                    visitor_log.append({
                        "name": parts[0], 
                        "contact_number": parts[1],
                        "purpose": parts[2],
                        "time_in": parts[3],
                        "date": parts[4],
                        "address": parts[5]
                    })

def log_in_visitor():
    print("\n" + " " * 50 + bcolors.PINK + "=" * 48 + bcolors.ENDC)
    print(" " * 63 + bcolors.YELLOW + "=== VISITOR LOG IN ===" + bcolors.ENDC)
    print( " " * 50 + bcolors.PINK + "=" * 48 + bcolors.ENDC)

    name_raw = get_input(" " * 22 + bcolors.BOLD +"Enter full name: ","full name", is_valid_name)
    name = capitalize_name(name_raw)

    contact_number = get_input(" " * 22 + bcolors.BOLD +"Enter contact number: ", "contact number", is_valid_contact)
    purpose = get_input(" " * 22 + bcolors.BOLD +"Enter purpose of visit: ", "purpose")
    address = get_input(" " * 22 + bcolors.BOLD +"Enter address: ", "address", is_valid_address)   
    now = datetime.now()
    time_in = now.strftime("%H:%M")
    date = now.strftime("%Y-%m-%d")    
    print(" " * 50 + bcolors.BOLD + f"Time In: {time_in} | Date: {date}" + bcolors.ENDC)

    visitor = {
        "name": name,
        "contact_number": contact_number,
        "purpose": purpose,
        "time_in": time_in,
        "date": date,
        "address": address
    }

    visitor_log.append(visitor)
    save_visitor_to_file(visitor)
    print(" " * 50 + bcolors.YELLOW + f"Visitor '{name}' logged successfully." + bcolors.ENDC)
    input(" " * 50 + "Press Enter to continue...")
def search_visitor():
    print("\n" + " " * 50 + bcolors.PINK + "=" * 48 + bcolors.ENDC)
    print(" " * 63 + bcolors.YELLOW + "=== SEARCH VISITOR ===" + bcolors.ENDC)
    print("\n" + " " * 50 + bcolors.PINK + "=" * 48 + bcolors.ENDC)

    search_name = input(" " * 50 + "Enter name to search: ").strip().lower()
    found = False

    for visitor in visitor_log:
        if search_name in visitor["name"].strip().lower():
            print(" " * 50 + bcolors.GREEN + f"Name: {visitor['name']}"+ bcolors.ENDC)
            print(" " * 50 + bcolors.GREEN + f"Contact_number: {visitor['contact_number']}"+ bcolors.ENDC)
            print(" " * 50 + bcolors.GREEN + f"Purpose: {visitor['purpose']}"+ bcolors.ENDC)
            print(" " * 50 + bcolors.GREEN + f"Time_in: {visitor['time_in']}"+ bcolors.ENDC)
            print(" " * 50 + bcolors.GREEN + f"Date: {visitor['date']}"+ bcolors.ENDC)
            print(" " * 50 + bcolors.GREEN + f"Address: {visitor['address']}"+ bcolors.ENDC)
            print(" " * 50 + "-" * 40)
            found = True
    if not found:
            print(" " * 50 + bcolors.FAIL + "No visitor found with that name." + bcolors.ENDC) 

    input(" " *50 + "Press Enter to Continue..") 

def view_all_visitors():
    clear_screen()
     
    print("\n" + " " * 50 + bcolors.PINK + "=" * 48 + bcolors.ENDC)
    print(" " * 63 + bcolors.YELLOW + "=== VIEW ALL VISITORS ===" + bcolors.ENDC)
    print("\n" + " " * 50 + bcolors.PINK + "=" * 48 + bcolors.ENDC)
    if not visitor_log:
        print(" " * 63 + bcolors.FAIL + bcolors.FAIL + "No visitors logged yet." + bcolors.ENDC)
    else:
        print(" " * 63 + bcolors.GREEN + " === VISITOR LISTS ===")
        for i, visitor in enumerate(visitor_log, 1):
            print(" " * 10 + bcolors.YELLOW +
                  f"{i}. Name: {visitor['name']} | Contact_Number: {visitor['contact_number']} | "
                  f"Purpose: {visitor['purpose']} | Time In: {visitor['time_in']} | "
                  f"Date: {visitor['date']} | Address: {visitor['address']}" + bcolors.ENDC)
    input(" " * 50 + "Press Enter to continue...")

load_visitors_from_file() 

while True:
    clear_screen()
    header_art()
    show_menu()
    choice = input("\n" + " " * 53 + bcolors.BOLD + "Choose an option (1-4): " + bcolors.ENDC)

    if choice == '1':
        clear_screen()
        log_in_visitor()
    elif choice == '2':
        clear_screen()
        search_visitor()
    elif choice == '3':
        clear_screen()
        view_all_visitors()
    elif choice == '4':
        print(" " * 63 + bcolors.YELLOW+ "Thank You! Come Again!" + bcolors.ENDC)
        print(" " * 63 + bcolors.YELLOW + "EXITING THE SYSTEM" + bcolors.ENDC)
        break
    else:
        print(" " * 53 + bcolors.FAIL + "Invalid choice. Please try again." + bcolors.ENDC)
        input(" " * 53 + bcolors.FAIL + "Press Enter to continue..." + bcolors.ENDC)