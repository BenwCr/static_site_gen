class HTMLnode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #str
        self.value = value #str
        self.children = children #list
        self.props = props #dict

    def to_html(self): #will be overriden by child classes
        raise NotImplementedError
    
    def props_to_html(self): #return string representing the self.props property
        output_str = ""
        for value, key in self.props.items():
            output_str += value + '="' + key + '" '
        return output_str.strip()
    

    def __repr__(self):
        return f"HTMLnode object| tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
    
class LeafNode(HTMLnode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if tag == None:
            return self.value
        

    