import unittest

from block_to_block_type import (
    BlockType,
    block_to_block_type,
)


class TestBlockType(unittest.TestCase):

    def test_heading(self):
        block = "# Heading"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING
        )

    def test_heading_level_6(self):
        block = "###### Heading"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.HEADING
        )

    def test_code_block(self):
        block = "```\nprint('hello')\n```"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.CODE
        )

    def test_quote_block(self):
        block = "> quote\n> another line"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.QUOTE
        )

    def test_unordered_list(self):
        block = "- item 1\n- item 2\n- item 3"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.UNORDERED_LIST
        )

    def test_ordered_list(self):
        block = "1. item\n2. item\n3. item"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.ORDERED_LIST
        )

    def test_invalid_ordered_list(self):
        block = "1. item\n3. item"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )

    def test_paragraph(self):
        block = "This is a paragraph."
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )

    def test_invalid_heading(self):
        block = "####### invalid"
        self.assertEqual(
            block_to_block_type(block),
            BlockType.PARAGRAPH
        )


if __name__ == "__main__":
    unittest.main()