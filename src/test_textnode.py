import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is text", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is text", TextType.BOLD)
        node2 = TextNode("This is text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode(
            "This is text",
            TextType.LINK,
            "https://boot.dev"
        )

        node2 = TextNode(
            "This is text",
            TextType.LINK,
            "https://google.com"
        )

        self.assertNotEqual(node, node2)

    def test_eq_with_none_url(self):
        node = TextNode("Plain text", TextType.TEXT)
        node2 = TextNode("Plain text", TextType.TEXT)
        self.assertEqual(node, node2)



if __name__ == "__main__":
    unittest.main()