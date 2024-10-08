from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )
    
    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type}, {self.url})")
    
    def copy(self):
        return TextNode(self.text,self.text_type,self.url)
    


def text_node_to_html_node(text_node):
    text_types = {
        text_type_text: (None, text_node.text),
        text_type_bold: ("b" , text_node.text),
        text_type_italic: ("i", text_node.text),
        text_type_code: ("code", text_node.text),
        text_type_link: ("a", text_node.text, {"href": text_node.url}),
        text_type_image: ("img", None, {"src": text_node.url, "alt": text_node.text})
    }
    if text_node.text_type in text_types:
        return LeafNode(*text_types[text_node.text_type])
    raise Exception("Not valid text type")




