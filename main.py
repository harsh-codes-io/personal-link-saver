from storage import load_links, save_links  # noqa: I001
from urllib.parse import urlparse


links = load_links()
def add_link(links:list) -> None:
    while True:
        link = {}
        print("\n\n")
        title = ""
        url = ""
        category = ""
        while not(title):
            title = input("Enter the link title: ").strip()
            if not title:
                print("\ntitle can not be empty\n")
        
        while not(url):
            url = input("Enter the URL: ").strip()
            if not url:
                print("\nurl can not be empty\n")
                continue
            if not is_valid_url(url):
                print("\nEnter an valid URL\n")
                url=""
                continue
            

        while not(category):       
            category = input("Enter the category: ").strip()
            if not category:
                print("\ncategory can not be empty\n")

        if links:
            new_id = max(link['id'] for link in links) + 1
        else:
            new_id = 1

        link["id"] = new_id
        link["title"] = title
        link["url"] = url
        link["category"] = category

        links.append(link)
        save_links(links)
        print(f"\nURL with title '{link['title']}' added succesfully! ")

        ex = input("\nEnter yes/YES to add more links,Any other key to exit: ")
        if ex.lower() == "yes":
            continue
        else:
            print("Thank you!")
            break


def view_link(links: list) -> None:
    if len(links) == 0:
        print("\nNo links saved yet. Add your first link!")
        return
    else:
        print("\n\n===== SAVED LINKS =====")
        for link in links:
            print("-----------------------------------")
            print(f"ID: {link['id']}\n Title:{link['title']}\n URL:{link['url']}\n Category:{link['category']}")



def search_link(links: list) -> None:
    key = input("\n\nEnter any keyword to search the url using title: ")
    found = False
    for link in links:
        if key.lower() in link['title'].lower():
            print("--------------------------------")
            print(f"ID: {link['id']}\n Title:{link['title']}\n URL:{link['url']}\n Category:{link['category']}")
            found = True

    if found is False:
        print("No Matching URL found")



def delete_link(links: list) ->None:
    link_id = int(input("Enter the link ID to be deleted: "))
    found = False
    for link in links:
        if link_id == link['id']:
            matched_link = link
            found = True
            break

    if found == True:
        links.remove(matched_link)
        save_links(links)
        print("URL deleted successfully!")
    else:
        print("Link Not found!")


def is_valid_url(url: str) -> bool:
    parsed_url = urlparse(url)

    if parsed_url.scheme in ("http", "https") and parsed_url.netloc:  # noqa: SIM103
        return True
    else:
        return False
    

def main():
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
            add_link(links)
        elif choice == 2:
            view_link(links)
        elif choice == 3:
            search_link(links)
        elif choice == 4:
            delete_link(links)
        elif choice == 5:
            print("\nThank you for using PERSONAL LINK SAVER!")
            break
        else:
            print("\nSelect the correct option from Menu")

        input("\nPress Enter to return to Main Menu...")

if __name__ == "__main__":
    main()

