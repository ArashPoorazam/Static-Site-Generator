import os
import sys
import shutil
from generate_page import generate_pages_recursive, generate_page


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    # paths
    dir_path_static = "./static"
    dir_path_docs = "./docs"
    dir_path_content = "./content"
    template_path = "./template.html"   

    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating page...")
    generate_pages_recursive(
        basepath, 
        dir_path_content,
        template_path,
        dir_path_docs,
    )


def copy_files_recursive(source_path, destination_path):
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir("docs")
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