from Manifest import Manifest
import Processor

class SystemManifest(Manifest):

    def __init__(self, manifestfile, folder):
        from xml.dom import minidom

        xmldoc = minidom.parse(manifestfile)
        itemlist = xmldoc.getElementsByTagName('project')
        self.children = []
        for s in itemlist:
            repo = s.attributes['name'].value

            self.children.append(Processor.processNode(repo, folder))