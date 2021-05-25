import os
import pathlib

PIPE = "│"
ELBOW = "└──"
PIPE_PREFIX = "│   "
SPACE = "    "
TEE = "├──"


def whitespace(level, lastentry=False):
    if lastentry:
        return ''.join([SPACE*level])
    else:
        return ''.join([PIPE_PREFIX*level])

def printTree(node, level=0, lastentry=False):

    if hasattr(node, 'reponame'):
        if level==0:
            print(whitespace(level, True) + node.reponame)
        else:
            if lastentry:
                print(whitespace(level, True) + TEE + node.reponame)
            else:
                print(whitespace(level, True) + ELBOW + node.reponame)
        
    if hasattr(node, 'children'):
        for r in node.children:
            if r == node.children[-1]:
                printTree(r, level+1)
            else:
                printTree(r, level+1, True)