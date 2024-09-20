import unittest
from markdown_html import *

class Markdown_HTML(unittest.TestCase):

    def test_markdown_to_html_node(self):
        markdown = """
# My Heading

This is a paragraph with some *italic* and **bold** text.

* List item 1
* List item 2
"""
        HTML = "<div><h1>My Heading</h1><p>This is a paragraph with some <em>italic</em> and <strong>bold</strong> text.</p><ul><li>List item 1</li><li>List item 2</li></ul></div>"
        self.assertEqual(markdown_to_html_node(markdown),HTML)

    def test_markdown_to_html_node2(self):
        markdown = "This is a paragraph with a [link](https://www.example.com) in it."
        HTML = '<p>This is a paragraph with a <a href="https://www.example.com">link</a> in it.</p>'
        self.assertEqual(markdown_to_html_node(markdown),HTML)


if __name__ == "__main__":
    unittest.main()