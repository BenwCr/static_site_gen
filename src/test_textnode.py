import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node2", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "italic", "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", "italic", "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "text", "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

class Test_TextNode_to_HTMLNode(unittest.TestCase):
    def test_Text_toHTMLNodeI(self):

        text_node = TextNode("Italic Sentence","italic")
        HTML_node = LeafNode("i", "Italic Sentence")

        self.assertEqual(repr(text_node_to_html_node(text_node)),repr(HTML_node))
    def test_Text_toHTMLNodeB(self):

        text_node = TextNode("bold Sentence","bold")
        HTML_node = LeafNode("b", "bold Sentence")

        self.assertEqual(repr(text_node_to_html_node(text_node)),repr(HTML_node))

    def test_Text_toHTMLNodeC(self):

        text_node = TextNode("code Sentence","code","www.google.com")
        HTML_node = LeafNode("code", "code Sentence")

        self.assertEqual(repr(text_node_to_html_node(text_node)),repr(HTML_node))

    def test_Text_toHTMLNodeL(self):

        text_node = TextNode("link Sentence","link","www.google.com")
        HTML_node = LeafNode("a", "link Sentence",{"href":"www.google.com"})

        self.assertEqual(repr(text_node_to_html_node(text_node)),repr(HTML_node))
    def test_Text_toHTMLNodeImage(self):

        text_node = TextNode("alt Image Sentence","image","www.google.com")
        HTML_node = LeafNode("img", props={"src":"www.google.com","alt":"alt Image Sentence"})

        self.assertEqual(repr(text_node_to_html_node(text_node)),repr(HTML_node))
    def test_Text_toHTMLNodeImage2(self):

        text_node = TextNode(None, text_type="image",url="www.google.com")
        HTML_node = LeafNode("img", props={"src":"www.google.com", "alt": None})

        self.assertEqual(repr(text_node_to_html_node(text_node)),repr(HTML_node))
    
    def test_expection(self):
        text_node = TextNode(None, text_type="Unk",url="www.google.com")
        with self.assertRaises(Exception):
            text_node_to_html_node(text_node)



if __name__ == "__main__":
    unittest.main()
