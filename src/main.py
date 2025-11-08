import os
import shutil
from generate_page import generate_pages_recursive, generate_page


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )


def copy_files_recursive(source_path, destination_path):
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir("public")
    recursive_copy(source_path, destination_path)
    

def recursive_copy(source_path, destination_path):
    ls = os.listdir(source_path)
    for item in ls:
        item_path = source_path + f"/{item}"
        if os.path.isfile(item_path):
            shutil.copy(item_path, destination_path)
            print("copied:", item)
        else:
            os.mkdir(destination_path + f"/{item}")
            print("copied:", item)
            recursive_copy(item_path, destination_path + f"/{item}")


if __name__ == "__main__":
    main()