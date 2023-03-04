from typing import Union


class node:
    def __init__(self,
                 funcName=None,
                 parent: Union['node', None] = None,
                 children: Union[list['node'], None] = None):
        self.name = funcName
        self.parent = parent
        if children is None:
            self.children = []
        else: self.children = children
        self.head = False
        if self.parent is None:
            self.head = True

    def __repr__(self):
        if self.name is None:
            return f'main = ({self.children})'
        return f'{self.name} = ({self.children})'

    def addChild(self, node: 'node'):
        self.children.append(node)


class ValNode(node):
    def __init__(self,
                 parent: 'node',
                 type: str,
                 value):
        super().__init__(parent)
        self.type = type
        self.val = value

    def __repr__(self):
        return f'<ValNode of type {self.type} = {self.val}>'


class BinOpNode(node):
    def __init__(self,
                 type: str,
                 parent: 'node',
                 children: Union[list['ValNode', 'ValNode'], None] = None):
        super().__init__(parent, children)
        self.type = type

    def addChild(self, node: 'node'):
        if len(self.children) < 2:
            self.children.append(node)
        else:
            raise RuntimeError('Cannot have greater than two children on a binary operation node')

    def __repr__(self):
        return f'({self.children[0]}) {self.type} ({self.children[1]})'


nodeTree = node()
nodeTree.addChild(BinOpNode('/', nodeTree))
nodeTree.children[0].addChild(ValNode(nodeTree.children[0], 'int', 1))
nodeTree.children[0].addChild(ValNode(nodeTree.children[0], 'int', 2))

print(nodeTree)
