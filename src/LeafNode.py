from htmlnode import *
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):

        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value

        return (
            f"<{self.tag}"
            f"{self.props_to_html()}>"
            f"{self.value}"
            f"</{self.tag}>"
        )

    def __repr__(self):
        return (
            f"LeafNode("
            f"tag={self.tag}, "
            f"value={self.value}, "
            f"props={self.props}"
            f")"
        )