# src/test_inline_markdown.py

import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_code_delimiter(self):

        node = TextNode(
            "This is text with a `code block` word",
            TextType.TEXT
        )

        result = split_nodes_delimiter(
            [node],
            "`",
            TextType.CODE
        )

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_bold_delimiter(self):

        node = TextNode(
            "This is **bold** text",
            TextType.TEXT
        )

        result = split_nodes_delimiter(
            [node],
            "**",
            TextType.BOLD
        )

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_italic_delimiter(self):

        node = TextNode(
            "This is _italic_ text",
            TextType.TEXT
        )

        result = split_nodes_delimiter(
            [node],
            "_",
            TextType.ITALIC
        )

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_no_delimiter(self):

        node = TextNode(
            "plain text only",
            TextType.TEXT
        )

        result = split_nodes_delimiter(
            [node],
            "`",
            TextType.CODE
        )

        expected = [
            TextNode("plain text only", TextType.TEXT)
        ]

        self.assertEqual(result, expected)

    def test_invalid_markdown(self):

        node = TextNode(
            "This is `broken markdown",
            TextType.TEXT
        )

        with self.assertRaises(Exception):
            split_nodes_delimiter(
                [node],
                "`",
                TextType.CODE
            )


if __name__ == "__main__":
    unittest.main()