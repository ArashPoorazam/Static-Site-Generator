import re
import os
from block_markdown import markdown_to_html_node

def extract_title(markdown):
    match = re.search(r"^# .+", markdown.strip()).group().strip()
    if match:
        return match[2:]
    else:
        raise ValueError("title not found")
    

def generate_page(from_path, template_path, dest_path):
    print(f"Generate page from {from_path} to {dest_path} using {template_path}")

    # read the markdown and the template
    with open (template_path, "r") as f:
        template = f.read()
    with open (from_path, "r") as m:
        markdown = m.read()

    # extract title and html string
    title = extract_title(markdown)
    html_nodes = markdown_to_html_node(markdown)
    html = ""
    for node in html_nodes:
        html += node.to_html()

    # replace title and content ( HTML ) in template
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    # create a new generated html file
    direct_path = os.path.join(os.getcwd, dest_path)
    with open(direct_path, "w") as w:
        w.write(template)

