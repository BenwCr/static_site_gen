import unittest
from markdown_blocks import *


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block(self):
        block = "#### This is a Heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
    def test_block_to_block1(self):
        block = "``` This is a Heading```"
        self.assertEqual(block_to_block_type(block), block_type_code)
    def test_block_to_block2(self):
        block = "This is a paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
    def test_block_to_block3(self):
        block = """> This as a Quote
> Quote"""
        self.assertEqual(block_to_block_type(block), block_type_quote)
    def test_block_to_block4(self):
        block = """* List
* List2"""
        self.assertEqual(block_to_block_type(block), block_type_ulist)
    def test_block_to_block45(self):
        block = """- List
- List2"""
        self.assertEqual(block_to_block_type(block), block_type_ulist)
    def test_block_to_block(self):
        block = """1. item
2. item
3. item"""
        self.assertEqual(block_to_block_type(block), block_type_olist)
if __name__ == "__main__":
    unittest.main()
