# src/test_markdown_extract.py

import unittest

from markdown_extract import (
    extract_markdown_images,
    extract_markdown_links,
)


class TestMarkdownExtract(unittest.TestCase):

    def test_extract_markdown_images(self):

        matches = extract_markdown_images(
            "This is text with an "
            "![image](https://i.imgur.com/zjjcJKZ.png)"
        )

        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches
        )

    def test_extract_multiple_images(self):

        text = (
            "This is ![rick](rick.png) "
            "and ![obi](obi.jpeg)"
        )

        matches = extract_markdown_images(text)

        self.assertListEqual(
            [
                ("rick", "rick.png"),
                ("obi", "obi.jpeg"),
            ],
            matches
        )

    def test_extract_markdown_links(self):

        text = (
            "This is a link "
            "[to boot dev](https://www.boot.dev)"
        )

        matches = extract_markdown_links(text)

        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev")
            ],
            matches
        )

    def test_extract_multiple_links(self):

        text = (
            "[google](https://google.com) "
            "and [youtube](https://youtube.com)"
        )

        matches = extract_markdown_links(text)

        self.assertListEqual(
            [
                ("google", "https://google.com"),
                ("youtube", "https://youtube.com"),
            ],
            matches
        )

    def test_extract_no_images(self):

        matches = extract_markdown_images(
            "plain text only"
        )

        self.assertListEqual([], matches)

    def test_extract_no_links(self):

        matches = extract_markdown_links(
            "plain text only"
        )

        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()