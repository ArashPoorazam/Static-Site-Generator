import os
import shutil
from generate_page import generate_page

def main():
    # paths
    static_dir_path = os.getcwd() + "/static"
    public_dir_path = os.getcwd() + "/public"
    from_path = os.getcwd() + "/content/index.md"
    destination_path = os.getcwd() + "/public/index.html"
    template_path = os.getcwd() + "/template.html"

    # Steps
    move_static_to_public(static_dir_path, public_dir_path)
    generate_page(from_path, template_path, destination_path)

def move_static_to_public(source_path, destination_path):
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