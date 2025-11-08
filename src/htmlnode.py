class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return None
        formatted_string = ""
        for key, val in self.props.items():
            formatted_string += f'{key}="{val}" '
        return formatted_string.strip()
    
    def __repr__(self):
        all_children = [child.tag for child in self.children] if self.children else []
        return (
            f"\n{self.__class__.__name__}"
            f"\ntag: {self.tag}"
            f"\nprops: {self.props_to_html()}" 
            f"\nvalue: {self.value}"
            f"\nlist of children tag: {all_children}\n"
        )


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props or {})

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is missing")
        elif None in self.children:
            raise ValueError("One or all children missing")
        else:
            formated_html = ""
            for child in self.children:
                formated_html += child.to_html()
            return f"<{self.tag}{' ' + self.props_to_html() if self.props else ''}>{formated_html}</{self.tag}>"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=[], props=props or {})

    def to_html(self):
        if self.value is None:
            raise ValueError("Value is missing")
        elif self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{' ' + self.props_to_html() if self.props else ''}>{self.value}</{self.tag}>"
    