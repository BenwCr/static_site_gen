from textnode import *

class HTMLnode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #str or None
        self.value = value #str or None
        self.children = children #list or None
        self.props = props #dict or None

    def to_html(self): #will be overriden by child classes
        raise NotImplementedError
    
    def props_to_html(self): #return string representing the self.props property
        if self.props == None:
            return ""
        output_str = ""
        for value, key in self.props.items():
            output_str += f' {value}="{key}"'
        return output_str
    

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLnode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return "<" + self.tag + self.props_to_html() + ">" + self.value + "</" +self.tag + ">"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLnode):
    def __init__(self, tag, children=None, props=None):
        super().__init__(tag, "", children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid HTML: No Tag")
        if self.children == None:
            raise ValueError("Invalid HTML: No Children!")

        children_html = list(map(lambda x: x.to_html(), self.children))

        inner_html = "".join(children_html)

        return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

def text_node_to_html_node(text_node):
    # Valid types "text", "bold", "italic", "code", "link", "image"
    if text_node.text_type is "text":
        return LeafNode(None, text_node.text)
    elif text_node.text_type is "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type is "italic":
        return LeafNode("i",text_node.text)
    elif text_node.text_type is "code":
        return LeafNode("code",text_node.text)
    elif text_node.text_type is "link":
        return LeafNode("a",text_node.text,{"href": text_node.url})
    elif text_node.text_type is "image":
        return LeafNode("img",props={"src": text_node.url, "alt" : text_node.text})
    raise Exception("Not valid text type")
