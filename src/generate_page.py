import re
import os
from block_markdown import markdown_to_html_node

def extract_title(markdown):
    match = re.search(r"^# .+", markdown.strip()).group().strip()
    if match:
        return match[2:]
    else:
        raise ValueError("title not found")
    

def generate_page(basepath, from_path, template_path, dest_path):
    print(f"Generate page from {from_path} to {dest_path} using {template_path}")

    # read the markdown and the template
    with open (template_path, "r") as f:
        template = f.read()
    f.close()
    with open (from_path, "r") as m:
        markdown = m.read()
    m.close()

    # extract title and html string
    title = extract_title(markdown)
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    # replace title and content ( HTML ) in template 
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    # make it able to be hosted on github
    template = template.replace('href="/', 'href="' + basepath)
    template = template.replace('src="/', 'src="' + basepath)

    # create a new generated html file
    with open(dest_path, "w") as w:
        w.write(template)


def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    current_dir = dir_path_content
    ls = os.listdir(current_dir)
    for item in ls:
        item_path = current_dir + f"/{item}"
        if item.endswith(".md"):
            new_dest_path = dest_dir_path + "/index.html"
            generate_page(
                basepath,
                item_path,
                template_path,
                new_dest_path 
            )
        elif os.path.isdir(item_path):
            new_dest_path = dest_dir_path + f"/{item}"
            os.mkdir(new_dest_path)
            print("made directory:", new_dest_path)
            generate_pages_recursive(basepath, item_path, template_path, new_dest_path)
        else:
            continue
