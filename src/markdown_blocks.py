import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    if len(re.findall(r"^(#{1,6})\s",block)) != 0:
        return block_type_heading
    elif re.match(r"^```[\s\S]*```$", block) != None:
        return block_type_code
    elif re.match(r"^(> .*\n?)+$", block) != None:
        return block_type_quote
    elif re.match(r"^(\* .*\n|-\s.*\n)*(\* .*$|-\s.*)$", block) != None:
        return block_type_ulist
    elif is_ordered_list(block) == True:
        return block_type_olist
    return block_type_paragraph

def is_ordered_list(block):
    lines = block.strip().split('\n')
    
    for i, line in enumerate(lines, start=1):
        # Check if the line matches the format: <number>. <text>
        if not re.match(rf'^{i}\. .+$', line):
            return False
            
    return True