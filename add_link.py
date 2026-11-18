
links = []

while True:
    link = {}
    title = input("Enter the link title: ")
    url = input("Enter the URL: ")
    category = input("Enter the category: ")

    link["id"] = len(links)+1
    link["title"] = title
    link["url"] = url
    link["category"] = category

    links.append(link)

    ex = input("Enter yes/YES to add more links,Any other key to exit: ")
    if ex.lower() == "yes":
        continue
    else:
        print("Thank you!")
        break

v = input("Enter 'view' to display saved links ")
print("===== SAVED LINKS =====")
if v.lower() == "view":
    for link in links:
        print("-----------------------------------")
        print(f"ID: {link["id"]}\n Title:{link['title']}\n URL:{link['url']}\n Category:{link['category']}")


key = input("\nEnter any keyword to search the url using title: ")
found = False
for link in links:
    if key.lower() in link['title'].lower():
        found = True

if found:
    print(f"ID: {link['id']}\n Title:{link['title']}\n URL:{link['url']}\n Category:{link['category']}")
else:
    print("No matching title found")


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


    





