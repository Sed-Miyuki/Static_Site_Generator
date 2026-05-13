import unittest

from textnode import TextNode, TextType
from inline_markdown import *


class TestSplitImagesLinks(unittest.TestCase):

    def test_split_images(self):

        node = TextNode(
            "This is text with an "
            "![image](https://i.imgur.com/zjjcJKZ.png) "
            "and another "
            "![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode(
                    "This is text with an ",
                    TextType.TEXT
                ),

                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://i.imgur.com/zjjcJKZ.png"
                ),

                TextNode(
                    " and another ",
                    TextType.TEXT
                ),

                TextNode(
                    "second image",
                    TextType.IMAGE,
                    "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):

        node = TextNode(
            "This is a link "
            "[to boot dev](https://www.boot.dev) "
            "and "
            "[to youtube](https://youtube.com)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_links([node])

        self.assertListEqual(
            [
                TextNode(
                    "This is a link ",
                    TextType.TEXT
                ),

                TextNode(
                    "to boot dev",
                    TextType.LINK,
                    "https://www.boot.dev"
                ),

                TextNode(
                    " and ",
                    TextType.TEXT
                ),

                TextNode(
                    "to youtube",
                    TextType.LINK,
                    "https://youtube.com"
                ),
            ],
            new_nodes,
        )

    def test_no_images(self):

        node = TextNode(
            "plain text only",
            TextType.TEXT
        )

        result = split_nodes_image([node])

        self.assertListEqual(
            [node],
            result
        )

    def test_no_links(self):

        node = TextNode(
            "plain text only",
            TextType.TEXT
        )

        result = split_nodes_links([node])

        self.assertListEqual(
            [node],
            result
        )


if __name__ == "__main__":
    unittest.main()