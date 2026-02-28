# ==========================================
# Project Name    : Contact Book
# Description     : User-friendly CLI application
# Developed by    : Samiksha Mund
# ==========================================

contacts = []


def header(title):
    print("\n" + "=" * 45)
    print(f"{title.center(45)}")
    print("=" * 45)


def pause():
    input("\nPress Enter to continue...")


def show_menu():
    header("CONTACT BOOK MENU")
    print("1️⃣  Add Contact")
    print("2️⃣  View All Contacts")
    print("3️⃣  Search Contact")
    print("4️⃣  Update Contact")
    print("5️⃣  Delete Contact")
    print("6️⃣  Exit")
    print("-" * 45)


def add_contact():
    header("ADD NEW CONTACT")

    name = input("👤 Name        : ").strip()
    phone = input("📞 Phone       : ").strip()
    email = input("📧 Email       : ").strip()
    address = input("🏠 Address     : ").strip()

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    print("\n✅ Contact added successfully!")
    pause()


def view_contacts():
    header("CONTACT LIST")

    if not contacts:
        print("📭 No contacts available.")
        pause()
        return

    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']}  |  {c['phone']}")

    pause()


def search_contact():
    header("SEARCH CONTACT")

    keyword = input("🔍 Enter name or phone: ").strip()
    found = False

    for c in contacts:
        if keyword.lower() in c["name"].lower() or keyword in c["phone"]:
            print("\n📇 Contact Found")
            print("-" * 30)
            print("Name    :", c["name"])
            print("Phone   :", c["phone"])
            print("Email   :", c["email"])
            print("Address :", c["address"])
            found = True

    if not found:
        print("\n❌ No matching contact found.")

    pause()


def update_contact():
    header("UPDATE CONTACT")

    phone = input("📞 Enter phone number to update: ").strip()

    for c in contacts:
        if c["phone"] == phone:
            print("\nLeave blank to keep old value")

            new_name = input("New Name    : ").strip()
            new_email = input("New Email   : ").strip()
            new_address = input("New Address : ").strip()

            if new_name:
                c["name"] = new_name
            if new_email:
                c["email"] = new_email
            if new_address:
                c["address"] = new_address

            print("\n✅ Contact updated successfully!")
            pause()
            return

    print("\n❌ Contact not found.")
    pause()


def delete_contact():
    header("DELETE CONTACT")

    phone = input("📞 Enter phone number to delete: ").strip()

    for c in contacts:
        if c["phone"] == phone:
            contacts.remove(c)
            print("\n🗑️ Contact deleted successfully!")
            pause()
            return

    print("\n❌ Contact not found.")
    pause()


def main():
    header("WELCOME TO CONTACT BOOK")

    while True:
        show_menu()
        choice = input("👉 Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            header("THANK YOU")
            print("Exiting Contact Book... 👋")
            break
        else:
            print("\n❌ Invalid choice. Try again.")
            pause()


main()