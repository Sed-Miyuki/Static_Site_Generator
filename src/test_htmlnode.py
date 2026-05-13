import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "Google",
            None,
            {
                "href": "https://google.com",
                "target": "_blank"
            }
        )

        self.assertEqual(
            node.props_to_html(),
            ' href="https://google.com" target="_blank"'
        )

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Hello")

        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none(self):
        node = HTMLNode("div", "Content", None, None)

        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("p", "Hello")

        self.assertEqual(
            repr(node),
            "HTMLNode(tag=p, value=Hello, children=None, props=None)"
        )


if __name__ == "__main__":
    unittest.main()