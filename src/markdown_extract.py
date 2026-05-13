import re

def extract_markdown_images(text):
    pattern=r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"  #([^\[\]]*) anything except [] and in [] capture group ()
    return re.findall(pattern,text)

def extract_markdown_links(text):
    pattern=r"\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern,text)