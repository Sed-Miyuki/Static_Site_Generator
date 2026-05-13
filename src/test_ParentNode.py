import unittest

from ParentNode import *
from LeafNode import *


class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")

        parent_node = ParentNode(
            "div",
            [child_node]
        )

        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")

        child_node = ParentNode(
            "span",
            [grandchild_node]
        )

        parent_node = ParentNode(
            "div",
            [child_node]
        )

        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_multiple_children(self):

        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                LeafNode(None, " normal "),
                LeafNode("i", "italic"),
            ]
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold</b> normal <i>italic</i></p>"
        )

    def test_parent_with_props(self):

        node = ParentNode(
            "a",
            [
                LeafNode(None, "Click me")
            ],
            {"href": "https://google.com"}
        )

        self.assertEqual(
            node.to_html(),
            '<a href="https://google.com">Click me</a>'
        )

    def test_no_children(self):

        node = ParentNode("div", None)

        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_tag(self):

        node = ParentNode(None, [])

        with self.assertRaises(ValueError):
            node.to_html()

    def test_nested_multiple_levels(self):

        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Hello"),
                        LeafNode(None, " world")
                    ]
                )
            ]
        )

        self.assertEqual(
            node.to_html(),
            "<div><p><b>Hello</b> world</p></div>"
        )

if __name__ == "__main__":
    unittest.main()