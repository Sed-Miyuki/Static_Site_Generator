from ParentNode import ParentNode
from LeafNode import LeafNode
from textnode import TextNode, TextType
from text_to_textnode import text_to_textnodes
from textnode_to_htmlnode import text_node_to_html_node
from blocks import markdown_to_blocks
from block_to_block_type import BlockType, block_to_block_type

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(
            text_node_to_html_node(node)
        )

    return children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        # paragraph                hello \n world -> hello world
        if block_type == BlockType.PARAGRAPH:
            paragraph = block.replace("\n", " ")
            node = ParentNode(
                "p",
                text_to_children(paragraph)
            )
            children.append(node)

        # heading                    count no of #
        elif block_type == BlockType.HEADING:
            level = 0
            while block[level] == "#":
                level += 1
            text = block[level + 1:]
            node = ParentNode(
                f"h{level}",
                text_to_children(text)
            )
            children.append(node)

        # code              remove ``` front and back
        elif block_type == BlockType.CODE:
            text = block[4:-3]
            text_node = TextNode(
                text,
                TextType.CODE
            )
            code_node = text_node_to_html_node(text_node)
            pre_node = ParentNode(
                "pre",
                [code_node]
            )
            children.append(pre_node)

        # quote                         > quote->quote
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            cleaned = []
            for line in lines:
                cleaned.append(
                    line.lstrip("> ").strip()
                )
            text = " ".join(cleaned)
            node = ParentNode(
                "blockquote",
                text_to_children(text)
            )
            children.append(node)

        # unordered list            - apple \n - banana-> apple banana
        elif block_type == BlockType.UNORDERED_LIST:
            items = []
            lines = block.split("\n")
            for line in lines:
                text = line[2:]
                items.append(
                    ParentNode(
                        "li",
                        text_to_children(text)
                    )
                )
            node = ParentNode(
                "ul",
                items
            )
            children.append(node)

        # ordered list                   1. apple \n 2. banana-> apple banana
        elif block_type == BlockType.ORDERED_LIST:
            items = []
            lines = block.split("\n")
            for line in lines:
                split_line = line.split(". ", 1)
                text = split_line[1]
                items.append(
                    ParentNode(
                        "li",
                        text_to_children(text)
                    )
                )
            node = ParentNode(
                "ol",
                items
            )
            children.append(node)

    return ParentNode("div", children)