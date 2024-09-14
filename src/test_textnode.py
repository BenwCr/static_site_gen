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

class Test_split_nodes_delimiter(unittest.TestCase):

    def test1(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", text_type_text),TextNode("code block", text_type_code),TextNode(" word", text_type_text)])
    def test2(self):
        node = TextNode("This is an italic sentence with a *bold block* & a *2nd bold block* set of words", text_type_italic)
        new_nodes = split_nodes_delimiter([node], "*", text_type_bold)
        
        
        self.assertEqual(new_nodes, [
            TextNode("This is an italic sentence with a ", text_type_italic), 
            TextNode("bold block",text_type_bold),
            TextNode(" & a ", text_type_italic),
            TextNode("2nd bold block", text_type_bold),
            TextNode(" set of words", text_type_italic)           
            ])
        
    def test3(self):
        node = TextNode("*This is a sentence with a bold block* & a *2nd bold block set of words*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_bold)
        

        self.assertEqual(new_nodes, [
            TextNode("This is a sentence with a bold block",text_type_bold),
            TextNode(" & a ", text_type_text),
            TextNode("2nd bold block set of words", text_type_bold),        
            ])
    
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
