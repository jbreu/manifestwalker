import Processor
import config
import TreePrinter

root = Processor.processNode(config.systemrepo, "tmp/")

TreePrinter.printTree(root)