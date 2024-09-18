import re

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
        return "heading"
    elif re.match(r"^```[\s\S]*```$", block) != None:
        return "code"
    elif re.match(r"^(> .*\n?)+$", block) != None:
        return "quote"
    elif re.match(r"^(\* .*\n|-\s.*\n)*(\* .*$|-\s.*)$", block) != None:
        return "unordered_list"
    elif is_ordered_list(block) == True:
        return "ordered_list"
    return "paragraph"

def is_ordered_list(block):
    lines = block.strip().split('\n')
    
    for i, line in enumerate(lines, start=1):
        # Check if the line matches the format: <number>. <text>
        if not re.match(rf'^{i}\. .+$', line):
            return False
            
    return True