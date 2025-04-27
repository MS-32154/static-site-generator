from textnode import TextType, TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    html_node = HTMLNode("a", "this is a link", props={"href":"#", "target":"_blank"})
    parent_node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    print(text_node)
    print(html_node)
    print(parent_node.to_html())

main()