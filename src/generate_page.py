import os

from block_to_html import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path, basepath):

    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}"
    )

    with open(from_path) as f:
        markdown = f.read()

    with open(template_path) as f:
        template = f.read()

    node = markdown_to_html_node(markdown)

    html = node.to_html()

    title = extract_title(markdown)

    page = template.replace(
        "{{ Title }}",
        title
    )

    page = page.replace(
        "{{ Content }}",
        html
    )

    # github pages basepath fix
    page = page.replace(
        'href="/',
        f'href="{basepath}'
    )

    page = page.replace(
        'src="/',
        f'src="{basepath}'
    )

    directory = os.path.dirname(dest_path)

    if directory != "":
        os.makedirs(directory, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(page)


def generate_pages_recursive(
    dir_path_content,
    template_path,
    dest_dir_path,
    basepath,
):

    for entry in os.listdir(dir_path_content):

        from_path = os.path.join(
            dir_path_content,
            entry
        )

        dest_path = os.path.join(
            dest_dir_path,
            entry
        )

        # recurse into directories
        if os.path.isdir(from_path):

            generate_pages_recursive(
                from_path,
                template_path,
                dest_path,
                basepath,
            )

        # generate html from markdown
        elif from_path.endswith(".md"):

            dest_html = dest_path.replace(
                ".md",
                ".html"
            )

            generate_page(
                from_path,
                template_path,
                dest_html,
                basepath,
            )