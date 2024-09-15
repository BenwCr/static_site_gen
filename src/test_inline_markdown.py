import unittest
from textnode import *
from inline_markdown import *

class Test_split_nodes_delimiter(unittest.TestCase):

    def test1(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", text_type_text),TextNode("code block", text_type_code),TextNode(" word", text_type_text)])
    def test2(self):
        node = TextNode("This is an italic sentence with a *bold block* & a *2nd bold block* set of words", text_type_italic)
        new_nodes = split_nodes_delimiter([node], "*", text_type_bold)
        
        
        self.assertEqual(new_nodes, [
            TextNode("This is an italic sentence with a ", text_type_italic), 
            TextNode("bold block",text_type_bold),
            TextNode(" & a ", text_type_italic),
            TextNode("2nd bold block", text_type_bold),
            TextNode(" set of words", text_type_italic)           
            ])
        
    def test3(self):
        node = TextNode("*This is a sentence with a bold block* & a *2nd bold block set of words*", text_type_text)
        node2 = TextNode("Node2: *This is a sentence with a bold block* & a *2nd bold block set of words*", text_type_italic)
        new_nodes = split_nodes_delimiter([node,node2], "*", text_type_bold)
        

        self.assertEqual(new_nodes, [
            TextNode("This is a sentence with a bold block",text_type_bold),
            TextNode(" & a ", text_type_text),
            TextNode("2nd bold block set of words", text_type_bold),  
            TextNode("Node2: ", text_type_italic),
            TextNode("This is a sentence with a bold block",text_type_bold),
            TextNode(" & a ", text_type_italic),
            TextNode("2nd bold block set of words", text_type_bold)
            ])
    
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

class Test_markdowns(unittest.TestCase):
    def test_img_markdown(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text),[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
    
    def test_img_markdown2(self): 
        text = "This is text with a !rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan]https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text),[])

    def test_lnk_markdown(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text),[("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_split_node_img(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",text_type_text)
        new_nodes = split_nodes_image([node])


        self.assertEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", text_type_text),
                TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            new_nodes
        )

    def test_split_node_img2(self):
        node = TextNode("![icon](www.youtube.com) and 2nd video ![vid](www.vimeo.com)", text_type_bold)
        node2 = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",text_type_text)
        test_case = split_nodes_image([node, node2])




        self.assertEqual(
            [
                TextNode("icon", text_type_image, "www.youtube.com"),
                TextNode(" and 2nd video ", text_type_bold),
                TextNode("vid",text_type_image, "www.vimeo.com"),
                TextNode("This is text with a ", text_type_text),
                TextNode("rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", text_type_text),
                TextNode("obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            test_case
        )
    
    def test_split_node_lnk(self):
        node = TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",text_type_text)
        new_nodes = split_nodes_link([node])


        self.assertEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("rick roll", text_type_link, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", text_type_text),
                TextNode("obi wan", text_type_link, "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            new_nodes
        )
    def test_split_node_lnk2(self):
        node = TextNode("[icon](www.youtube.com) and 2nd video [vid](www.vimeo.com)", text_type_bold)
        node2 = TextNode("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",text_type_text)
        test_case = split_nodes_link([node, node2])




        self.assertEqual(
            [
                TextNode("icon", text_type_link, "www.youtube.com"),
                TextNode(" and 2nd video ", text_type_bold),
                TextNode("vid",text_type_link, "www.vimeo.com"),
                TextNode("This is text with a ", text_type_text),
                TextNode("rick roll", text_type_link, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", text_type_text),
                TextNode("obi wan", text_type_link, "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            test_case
        )
    
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", text_type_image, "https://www.example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("another link", text_type_link, "https://blog.boot.dev"),
                TextNode(" with text that follows", text_type_text),
            ],
            new_nodes,
        )

    
if __name__ == "__main__":
    unittest.main()