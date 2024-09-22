import os
import shutil
from markdown_html import *


exactPathRoot = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))




def generate_page(from_path, template_path, dest_path):
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_exactPath = relativePath_to_ExactPath(from_path)
    template_exactPath = relativePath_to_ExactPath(template_path)
    dest_exactPath = relativePath_to_ExactPath(dest_path)

    markdown = read_content(from_exactPath)
    htmlcode = markdown_to_html_node(markdown).to_html()
    template = read_content(template_exactPath)
    title = extract_title(markdown)
    template = template.replace(r"{{ Content }}", htmlcode).replace(r"{{ Title }}", title)
    print(f"Writing to File")
    write_content(dest_exactPath, template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_path_content_exactPath = relativePath_to_ExactPath(dir_path_content)
    
    listDir = os.listdir(dir_path_content_exactPath)
    for e in listDir:
        currentItem = os.path.join(dir_path_content, e)
        toItem = os.path.join(dest_dir_path, e)
        if currentItem.endswith('.md'):
            toItem = os.path.join(dest_dir_path, e[:-3] + ".html") #change ToITem from folder to file
            generate_page(currentItem, template_path, toItem)
            continue            
        if os.path.isfile(currentItem) == True: #file but not an markdown file
            print(f"{e} is not a md file")
            continue
        #if Folder RECURSIVE
        os.mkdir(toItem)
        generate_pages_recursive(currentItem, template_path, toItem)



def relativePath_to_ExactPath(path):
    return os.path.join(exactPathRoot, path)

def write_content(path, content):
    f = open(path,"w")
    f.write(content)
    f.close()

def read_content(path):
    f = open(path)
    contents = f.read()
    f.close()
    return contents

def Copy_srcTopublic(public_currentPath=None, static_currentPath=None):
    if public_currentPath == None and static_currentPath == None:
        static_currentPath = relativePath_to_ExactPath('static')
        public_currentPath = relativePath_to_ExactPath('public') #If first time
        shutil.rmtree(public_currentPath,ignore_errors=True) #delete public and everything underneath.
        os.mkdir(public_currentPath) #make public folder
    listDir = os.listdir(static_currentPath)
    for i in listDir:
        currentItem = os.path.join(static_currentPath, i)
        if os.path.isfile(currentItem) == True:
            shutil.copy(currentItem, public_currentPath)
            continue
        futurePath = os.path.join(public_currentPath, i)
        os.mkdir(futurePath)
        Copy_srcTopublic(os.path.join(public_currentPath, i),currentItem)
        
            
