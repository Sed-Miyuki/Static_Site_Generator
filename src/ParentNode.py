from htmlnode import *
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):

        if self.children is None:
            raise ValueError("ParentNode must have a children")

        if self.tag is None:
            raise ValueError("ParentNode must have a tag")

        children_html = ""

        for child in self.children:
            children_html += child.to_html()

        return (
            f"<{self.tag}"
            f"{self.props_to_html()}>"
            f"{children_html}"
            f"</{self.tag}>"
        )