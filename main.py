
links = []
def add_link():
    while True:
        link = {}
        print("\n\n")
        title = input("Enter the link title: ")
        url = input("Enter the URL: ")
        category = input("Enter the category: ")

        link["id"] = len(links)+1
        link["title"] = title
        link["url"] = url
        link["category"] = category

        links.append(link)
        print(f"\nURL with title '{link['title']}' added succesfully! ")

        ex = input("\nEnter yes/YES to add more links,Any other key to exit: ")
        if ex.lower() == "yes":
            continue
        else:
            print("Thank you!")
            break


def view_link():
    print("\n\n===== SAVED LINKS =====")
    for link in links:
        print("-----------------------------------")
        print(f"ID: {link['id']}\n Title:{link['title']}\n URL:{link['url']}\n Category:{link['category']}")



def search_link():
    key = input("\n\nEnter any keyword to search the url using title: ")
    found = False
    for link in links:
        if key.lower() in link['title'].lower():
            print("--------------------------------")
            print(f"ID: {link['id']}\n Title:{link['title']}\n URL:{link['url']}\n Category:{link['category']}")
            found = True

    if found is False:
        print("No Matching URL found")


  


def delete_link():
    link_id = int(input("Enter the link ID to be deleted: "))
    found = False
    for link in links:
        if link_id == link['id']:
            matched_link = link
            found = True
            break

    if found == True:
        links.remove(matched_link)
        print("URL deleted successfully!")
    else:
        print("Link Not found!")


while True:
    print("\n  ============================")
    print("\tPERSONAL LINK SAVER")
    print("  ============================")
    print("1. Add a new link")
    print("2. View all links")
    print("3. Search links")
    print("4. Delete a link")
    print("5. Exit\n")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_link()
        continue
    elif choice == 2:
        view_link()
        continue
    elif choice == 3:
        search_link()
        continue
    elif choice == 4:
        delete_link()
        continue
    elif choice == 5:
        print("\nThank you for using PERSONAL LINK SAVER!")
        break
    else:
        print("\nSelect the correct option from Menu")
        continue

