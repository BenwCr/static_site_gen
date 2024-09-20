from htmlnode import * #Class HTMLNode, LeafNode, ParentNode #Node.to_html() Returns HTML str
from markdown_blocks import (
    markdown_to_blocks, 
    block_to_block_type, 
    heading_block_type,
    block_type_heading,
    block_type_code,
    block_type_olist,
    block_type_paragraph,
    block_type_quote,
    block_type_ulist
)
from textnode import (
    TextNode,
    text_node_to_html_node,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text
)

from inline_markdown import(split_nodes_delimiter, text_to_textnodes)


#block -> [Textnode (type)], 



def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    texttypes_func = {
        text_type_bold: None,
        text_type_code: None,
        text_type_image: None,
        text_type_italic: None,
        text_type_link: None,
        text_type_text: None
    }
    blocktype_func = {
        block_type_heading: None,
        block_type_code: None,
        block_type_quote: None,
        block_type_paragraph: None,
        block_type_ulist: None,
        block_type_olist: None
    }
    numOfBlocks = len(blocks)
    currentItteration = 0
    for block in blocks:
        currentItteration += 1 #keep track of iterations, last block will use leafnode instead of parent
        blocktype = block_to_block_type(block)


