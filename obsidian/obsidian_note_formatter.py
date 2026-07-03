from pathlib import Path

title = input("Note title: ")
summary = input("Summary: ")

key_ideas = []

print()
print("Enter key ideas one at a time.")
print("Type done when finished.")

while True:
    key_idea = input("Key idea: ").strip()

    if key_idea.lower() == "done":
        break

    key_ideas.append(key_idea)

action_items = []

print()
print("Enter action items one at a time.")
print("Type done when finished.")

while True:
    action_item = input("Action item: ").strip()

    if action_item.lower() == "done":
        break

    action_items.append(action_item)

related_note = input("Related note: ")

print()
print("Choose destination folder:")
print("A. 06 AI")
print("K. 03 Knowledge")
print("P. 04 Projects")
print("S. 02 Systems")

folder_choice = input("Folder choice: ").strip().lower()

if folder_choice == "a":
    vault_folder = Path(r"C:\Users\colew\OneDrive\Documents\Cole OS\06 AI")
elif folder_choice == "k":
    vault_folder = Path(r"C:\Users\colew\OneDrive\Documents\Cole OS\03 Knowledge")
elif folder_choice == "p":
    vault_folder = Path(r"C:\Users\colew\OneDrive\Documents\Cole OS\04 Projects")
elif folder_choice == "s":
    vault_folder = Path(r"C:\Users\colew\OneDrive\Documents\Cole OS\02 Systems")
else:
    raise SystemExit("Invalid folder choice. Run the script again.")

key_ideas_markdown = "\n".join("- " + idea for idea in key_ideas)
action_items_markdown = "\n".join("- " + item for item in action_items)

markdown = f"""# {title}

## Summary

{summary}

## Key Ideas

{key_ideas_markdown}

## Action Items

{action_items_markdown}

## Related

- [[{related_note}]]
"""

filename = title + ".md"
file_path = vault_folder / filename

print()
print("----- PREVIEW -----")
print(markdown)
print("----- END PREVIEW -----")
print()
print("Destination:", file_path)
print()

save_choice = input("Save this note? yes/no: ").strip().lower()

if save_choice == "yes":
    if file_path.exists():
        overwrite_choice = input("This file already exists. Overwrite it? yes/no: ").strip().lower()

        if overwrite_choice != "yes":
            raise SystemExit("Note not saved. Existing file was not overwritten.")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(markdown)

    print("Markdown note created:", file_path)
else:
    print("Note not saved.")