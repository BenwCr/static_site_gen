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
        

def text_node_to_html_node(text_node):
    text_types = {
        "text": (None, text_node.text),
        "bold": ("b" , text_node.text),
        "italic": ("i", text_node.text),
        "code": ("code", text_node.text),
        "link": ("a", text_node.text, {"href": text_node.url}),
        "image": ("img", None, {"src": text_node.url, "alt": text_node.text})
    }
    if text_node.text_type in text_types:
        return LeafNode(*text_types[text_node.text_type])
    raise Exception("Not valid text type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    output = []
    for node in old_nodes:
        texts = node.text.split(delimiter) #List of split texts based on delimiter
        for i in range(len(texts)):
            if texts[i]== "":
                continue
            if (i+1) % 2 != 0: #if text is text outside of delimiter
                output.append(TextNode(texts[i],node.text_type))
            else:
                output.append(TextNode(texts[i],text_type))
    return output



