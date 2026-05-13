# src/test_textnode_to_htmlnode.py

import unittest

from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node


class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text(self):

        node = TextNode(
            "This is a text node",
            TextType.TEXT
        )

        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(
            html_node.value,
            "This is a text node"
        )

    def test_bold(self):

        node = TextNode(
            "Bold text",
            TextType.BOLD
        )

        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")

    def test_italic(self):

        node = TextNode(
            "Italic text",
            TextType.ITALIC
        )

        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")

    def test_code(self):

        node = TextNode(
            "print('hello')",
            TextType.CODE
        )

        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "code")

    def test_link(self):

        node = TextNode(
            "Google",
            TextType.LINK,
            "https://google.com"
        )

        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Google")
        self.assertEqual(
            html_node.props,
            {"href": "https://google.com"}
        )

    def test_image(self):

        node = TextNode(
            "Cat image",
            TextType.IMAGE,
            "cat.png"
        )

        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")

        self.assertEqual(
            html_node.props,
            {
                "src": "cat.png",
                "alt": "Cat image"
            }
        )


if __name__ == "__main__":
    unittest.main()