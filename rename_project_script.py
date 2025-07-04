import os
import sys
import shutil

def replace_in_file(file_path, old_name, new_name):
    with open(file_path, "r") as f:
        content = f.read()
    content = content.replace(old_name, new_name)
    with open(file_path, "w") as f:
        f.write(content)

def main(old_name, new_name):
    project_root = os.getcwd()
    
    old_project_path = os.path.join(project_root, old_name)
    new_project_path = os.path.join(project_root, new_name)

    if not os.path.isdir(old_project_path):
        print(f"❌ Error: '{old_name}' folder not found.")
        return

    if os.path.exists(new_project_path):
        print(f"❌ Error: '{new_name}' folder already exists.")
        return

    print(f"🔄 Renaming '{old_name}' → '{new_name}'")

    # Rename the folder
    shutil.move(old_project_path, new_project_path)

    # Files to update
    files_to_update = [
        "manage.py",
        os.path.join(new_name, "wsgi.py"),
        os.path.join(new_name, "asgi.py"),
        os.path.join(new_name, "settings.py"),
    ]

    for file_path in files_to_update:
        full_path = os.path.join(project_root, file_path)
        if os.path.exists(full_path):
            print(f"✏️  Updating {file_path}")
            replace_in_file(full_path, old_name, new_name)

    print("✅ Project renamed successfully.")
    print("🚀 Try running: python manage.py runserver")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rename_django_project.py <old_project_name> <new_project_name>")
    else:
        old, new = sys.argv[1], sys.argv[2]
        main(old, new)
