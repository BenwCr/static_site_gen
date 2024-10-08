import unittest
from htmlnode import *

class TestHTMLnode(unittest.TestCase):

    def test_repr(self):
        node = HTMLnode("p", "This is a sentence", [HTMLnode()], {"href":"https://www.google.com"})
        self.assertEqual("HTMLNode(p, This is a sentence, children: [HTMLNode(None, None, children: None, None)], {'href': 'https://www.google.com'})", repr(node))
    
    def test_props_toHTML(self):
        node = HTMLnode("p", "This is a sentence", [HTMLnode()], {"href":"https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
    
    def test_props_toHTML2(self):
        node = HTMLnode(props={"href":"https://www.google.com","para":"https://boot.dev","head":"www.ebay.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" para="https://boot.dev" head="www.ebay.com"')
    def test_props_toHTML3(self):
        node = HTMLnode()
        self.assertEqual(node.props_to_html(), "")
    #Leaf Node Tests
    def test_to_HTML(self):
        node = LeafNode(props={"href":"https://www.google.com","para":"https://boot.dev","head":"www.ebay.com"})
        with self.assertRaises(ValueError):
            node.to_html()
    def test_to_HTML2(self):    
        node = LeafNode("a", "This is a Sentence.")
        self.assertEqual(node.to_html(), "<a>This is a Sentence.</a>")
    def test_to_HTML3(self):
        node = LeafNode("p", "Good Morning America", props={"href":"www.google.com","target":"_blank"})
        self.assertEqual(node.to_html(), '<p href="www.google.com" target="_blank">Good Morning America</p>')
    
    #Parent Node Tests!
    def test_ParentNode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(),'<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    def test_ParentNode2(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "a",
                    [
                        
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),       
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(),'<p><a><b>Bold text</b>Normal text<i>italic text</i>Normal text</a><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')       
    def test_ParentNode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text",props={"leaf":"leaf.com"}),
                LeafNode(None, "Normal text"),
            ],{"href" : "www.google.com", "target":"_blank"}
        )

        self.assertEqual(node.to_html(),'<p href="www.google.com" target="_blank"><b>Bold text</b>Normal text<i leaf="leaf.com">italic text</i>Normal text</p>')
    
    def test_ParentNode3(self): #Error
        node = ParentNode(
            "a",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None)

            ]
        )
        with self.assertRaises(ValueError):
            node.to_html()
    def test_ParentNode4(self): #Error
        node = ParentNode(
            "a"
        )
        with self.assertRaises(ValueError):
            node.to_html()





if __name__ == "__main__":
    unittest.main()