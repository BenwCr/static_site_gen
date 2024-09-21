from textnode import * #TextNode(text, text_type, url=None)
import re




def text_to_textnodes(text):
    text_Node = TextNode(text,text_type_text)
    return split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(split_nodes_image(split_nodes_link([text_Node])),"`",text_type_code),"**",text_type_bold),"*", text_type_italic)

#### Internal func for most HTML Conversions below

def split_nodes_delimiter(old_nodes, delimiter, text_type, exlude_index=0): # of node.text: 0 = use all, 2 = [2:], -2 = [:-2]
    output = []
    for node in old_nodes:
        exluded_index_node = node.copy()
        if exlude_index >= 0:
            exluded_index_node.text = node.text[exlude_index:] #Node text without the exluded index
            exluded_text = node.text[:exlude_index]
        else:
            exluded_index_node.text = node.text[:exlude_index]
            exluded_text = node.text[exlude_index:]

        texts = exluded_index_node.text.split(delimiter) #List of split texts based on delimiter using Exluded_index_node
        if node.text_type == text_type_image or node.text_type == text_type_link:
            output.append(node)
            continue
        for i in range(len(texts)):
            if texts[i]== "": #don't create a TextNode for an empty string
                continue
            if (i+1) % 2 != 0: #if text is text outside of delimiter
                output.append(TextNode(texts[i],node.text_type))
            else:
                output.append(TextNode(texts[i],text_type))
        if exlude_index > 0: #Postitive Exlude_index, insert exluded text back into output as a Text_node
            output.insert(0, TextNode(exluded_text, node.text_type))
        elif exlude_index < 0:
            output.append(0, TextNode(exluded_text, node.text_type))
    return output

def extract_markdown_images(text): #output [("rick roll", "https://i.imgur.com/aKaOqIh.gif)""] input: "![rick roll](https://i.imgur.com/aKaOqIh.gif)"
    return re.findall(r"!\[(.*?)\]\((.*?)\)",text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)

def split_nodes_image(old_nodes): #imageNodes(alttext, img, www.***.com), textNodes(text, text_type, None)
    output = [] 
    for node in old_nodes:
        image_texts = extract_markdown_images(node.text)
        if node.text_type == text_type_image or image_texts == []: #base case: node is an image node OR contains no image inline text
            output.append(node)
            continue
        else:
            alt_text = image_texts[0][0]
            img_url = image_texts[0][1]
            split_node_text = node.text.split(f"![{alt_text}]({img_url})", 1) #expected 2 items in list
            node_list = []
            if split_node_text[0] != "":
                node_list.append(TextNode(split_node_text[0],node.text_type))
            node_list.append(TextNode(alt_text, text_type_image, img_url))
            if split_node_text[1] != "":
                node_list.append(TextNode(split_node_text[1], node.text_type))
            output += (split_nodes_image(node_list)) #RECURSION!!!!
    return output
            
def split_nodes_link(old_nodes): #linkNodes(text, link, www.***.com), textNodes(text, text_type, None)
    output = []
    for node in old_nodes:
        link_texts = extract_markdown_links(node.text)
        if node.text_type == text_type_link or link_texts == []: #base case: node is an link node OR contains no link inline text
            output.append(node)
            continue
        else:
            alt_text = link_texts[0][0]
            url = link_texts[0][1]
            split_node_text = node.text.split(f"[{alt_text}]({url})", 1) #expected 2 items in list
            node_list = []
            if split_node_text[0] != "":
                node_list.append(TextNode(split_node_text[0],node.text_type))
            node_list.append(TextNode(alt_text, text_type_link, url))
            if split_node_text[1] != "":
                node_list.append(TextNode(split_node_text[1], node.text_type))
            output += (split_nodes_link(node_list))#RECURSION
    return output
    


