from textnode import *
from markdown_extract import *
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes=[]
    for old_node in old_nodes:
        if old_node.text_type!=TextType.TEXT:
            new_nodes.append(old_node)
            continue
        parts=old_node.text.split(delimiter)
        if len(parts)%2==0:
            raise Exception("Invalid markdown syntax")
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            # even index = normal text
            if i%2==0:
                new_nodes.append(
                    TextNode(parts[i], TextType.TEXT)
                )
            # odd index = formatted text
            else:
                new_nodes.append(
                    TextNode(parts[i], text_type)
                )

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes=[]
    for old_node in old_nodes:
        if old_node.text_type!=TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text=old_node.text
        images = extract_markdown_images(text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for alt, url in images:
            sections = text.split(f"![{alt}]({url})", 1)
            if sections[0] != "":
                new_nodes.append(
                    TextNode(sections[0], TextType.TEXT)
                )
            new_nodes.append(
                TextNode(alt, TextType.IMAGE, url)
            )
            text = sections[1]
        if text != "":
            new_nodes.append(
                TextNode(text, TextType.TEXT)
            )
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes=[]
    for old_node in old_nodes:
        if old_node.text_type!=TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text=old_node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for anchor, url in links:
            sections = text.split(f"[{anchor}]({url})", 1)
            if sections[0] != "":
                new_nodes.append(
                    TextNode(sections[0], TextType.TEXT)
                )
            new_nodes.append(
                TextNode(anchor, TextType.LINK, url)
            )
            text = sections[1]
        if text != "":
            new_nodes.append(
                TextNode(text, TextType.TEXT)
            )

    return new_nodes

