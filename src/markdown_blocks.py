from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"


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
    if re.match(r"^(#{1,6}) ", block):
        return BlockType.HEADING
    if re.fullmatch(r"```([\s\S]*?)```", block, re.M):
        return BlockType.CODE
    if re.match(r"^>", block, re.M):
        return BlockType.QUOTE
    if re.match(r"^- ", block, re.M):
        return BlockType.ULIST
    if not False in [
        [f"{ind + 1}. "] == re.findall(r"^\d+. ", val)
        for ind, val in enumerate(block.split("\n"))
    ]:
        return BlockType.OLIST
    return BlockType.PARAGRAPH
