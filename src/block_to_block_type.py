from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")
    # heading
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    # code block
    if (
        block.startswith("```")
        and block.endswith("```")
    ):
        return BlockType.CODE

    # quote block
    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break

    if is_quote:
        return BlockType.QUOTE

    # unordered list
    is_unordered = True
    for line in lines:
        if not line.startswith("- "):
            is_unordered = False
            break

    if is_unordered:
        return BlockType.UNORDERED_LIST

    # ordered list
    is_ordered = True
    for i in range(len(lines)):
        expected = f"{i+1}. "
        if not lines[i].startswith(expected):
            is_ordered = False
            break

    if is_ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH