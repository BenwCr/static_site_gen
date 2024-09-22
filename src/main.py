from textnode import *
from build_site import *

#Relative to where the rooth of the project is
from_path = "content"
template_path = "template.html"
to_path = "public"

def main():
    Copy_srcTopublic()
    generate_pages_recursive(from_path, template_path, to_path)




main()