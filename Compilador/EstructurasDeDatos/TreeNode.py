class TreeNode:
    def __init__(self, x):
        self.value = x
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, children):
        for child in children:
            self.add_child(child)

    def print(self, level=0):
        print('\t' * level + repr(self.value))
        print('\t' * level + "Hijos: "+ repr(self.children))
        for child in self.children:
            if isinstance(child,TreeNode):
                child.print(level + 1)
