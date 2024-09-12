import unittest
from htmlnode import HTMLnode

class TestHTMLnode(unittest.TestCase):
    def test_repr(self):
        node = HTMLnode("p", "This is a sentence", [HTMLnode()], {"href":"https://www.google.com"})
        self.assertEqual("HTMLnode object| tag: p, value: This is a sentence, children: [HTMLnode object| tag: None, value: None, children: None, props: None], props: {'href': 'https://www.google.com'}", repr(node))
    
    def test_props_toHTML(self):
        node = HTMLnode("p", "This is a sentence", [HTMLnode()], {"href":"https://www.google.com"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com"')
    
    def test_props_toHTML2(self):
        node = HTMLnode(props={"href":"https://www.google.com","para":"https://boot.dev","head":"www.ebay.com"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" para="https://boot.dev" head="www.ebay.com"')

if __name__ == "__main__":
    unitest.main()