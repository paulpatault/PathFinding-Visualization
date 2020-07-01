class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def id(self):
        return (self.x, self.y)

    def __eq__(self, node2):
        if type(node2) is Node:
            return self.id == node2.id
        return self.id == node2
