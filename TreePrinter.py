PIPE = "│"
ELBOW = "└──"
PIPE_PREFIX = "│   "
SPACE = "    "
TEE = "├──"


def whitespace(level, lastentry=False):
    if lastentry:
        return SPACE * level
    else:
        return SPACE + PIPE_PREFIX * (level - 1)


def printTree(node, level=0, lastentry=False):

    if hasattr(node, 'reponame'):
        if lastentry:
            if level == 0:
                print(whitespace(level, True) + ELBOW + node.reponame)
            else:
                print(whitespace(level, False) + ELBOW + node.reponame)
        else:
            print(whitespace(level, False) + TEE + node.reponame)

    if hasattr(node, 'children'):
        for r in node.children:
            if r == node.children[-1]:
                printTree(r, level + 1, True)
            else:
                printTree(r, level + 1, False)
