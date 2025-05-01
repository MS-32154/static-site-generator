from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []

    def find_images(original_text):
        images = extract_markdown_images(original_text)
        if not images:
            if original_text:
                return [TextNode(original_text, TextType.TEXT)]
            else:
                return []
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", maxsplit=1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            result = (
                find_images(sections[0])
                + [TextNode(image[0], TextType.IMAGE, image[1])]
                + find_images(sections[1])
            )
        return result

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        new_nodes.extend(find_images(node.text))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    def find_links(original_text):
        links = extract_markdown_links(original_text)
        if not links:
            if original_text:
                return [TextNode(original_text, TextType.TEXT)]
            else:
                return []
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", maxsplit=1)
            result = (
                find_links(sections[0])
                + [TextNode(link[0], TextType.LINK, link[1])]
                + find_links(sections[1])
            )
        return result

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        new_nodes.extend(find_links(node.text))
    return new_nodes


if __name__ == "__main__":
    node = TextNode(
        "This is ![second image](https://i.imgur.com/3elNhQu.png) text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    print(new_nodes)

    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    print(new_nodes)
