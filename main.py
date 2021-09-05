import Processor
import config
import TreePrinter

import os

if not os.path.exists('tmp'):
    os.makedirs('tmp')

root = Processor.processNode(config.systemrepo, "tmp/")

TreePrinter.printTree(root, 0, True)
