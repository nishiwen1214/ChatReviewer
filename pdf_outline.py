import fitz
import re
from collections import Counter
import json

doc = fitz.open("input_file/ijcai23.pdf")

# 获取文档中所有字体大小
font_sizes = []
for page in doc:
    blocks = page.get_text("dict")["blocks"]
    for block in blocks:
        if 'lines' not in block:
            continue
        lines = block["lines"]
        for line in lines:
            for span in line["spans"]:
                font_sizes.append(span["size"])

# 计算出现最频繁的字体大小
most_common_size, _ = Counter(font_sizes).most_common(1)[0]

# 按照最频繁的字体大小确定标题字体大小的阈值
threshold = most_common_size * 1

subheadings = []
# 遍历每一页并查找子标题
headings = {i: [] for i in range(2)}
title_font_size = [-1, -1]
found_abstract = False
for page in doc:
    blocks = page.get_text("dict")["blocks"]
    for block in blocks:
        if not found_abstract:
            text = json.dumps(block)
            if re.search(r"\bAbstract\b", text, re.IGNORECASE):
                found_abstract = True
        if found_abstract:
            if 'lines' not in block:
                continue
            lines = block["lines"]
            for line in lines:
                for span in line["spans"]:
                    if span["size"] > threshold and re.match(r"[A-Z][a-z]+(?:\s[A-Z][a-z]+)*", span["text"].strip()):
                        if title_font_size[0] == -1:  # 第一级标题都没有找到
                            title_font_size[0] = span["size"]
                        elif span["size"] < title_font_size[0] and title_font_size[1] == -1:  # 第二级标题都没有找到
                            title_font_size[1] = span["size"]
                        if span["size"] == title_font_size[0]:
                            headings[0].append(span["text"].strip())
                        elif span["size"] == title_font_size[1]:
                            headings[1].append(span["text"].strip())

# 打印分级的标题
for i, level_headings in headings.items():
    print(f"Level {i} Headings:")
    for heading in level_headings:
        print(heading)
print(subheadings)
