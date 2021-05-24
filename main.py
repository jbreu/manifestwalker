import Processor
import config

root = Processor.processNode(config.systemrepo, "tmp/")

def whitespace(level):
    return ''.join([' '*level])

def printTree(node, level=0):
    if hasattr(node, 'reponame'):
        print(whitespace(level) + node.reponame)
    if hasattr(node, 'children'):
        for r in node.children:
            printTree(r, level+1)


printTree(root)