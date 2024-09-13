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
        return f"HTMLnode object| tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
    
class LeafNode(HTMLnode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return "<" + self.tag + self.props_to_html() + ">" + self.value + "</" +self.tag + ">"
    
class ParentNode(HTMLnode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, "", children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid HTML: No Tag")
        if self.children == None:
            raise ValueError("Invalid HTML: No Children!")

        children_html = list(map(lambda x: x.to_html(), self.children))

        inner_html = "".join(children_html)

        return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"

        
        
        
        
        
        

    