from Repo import Repo
import Processor
import config

class XMLManifestRepo(Repo):

    def __init__(self, manifestfile, folder):
        from xml.dom import minidom

        xmldoc = minidom.parse(manifestfile)
        itemlist = xmldoc.getElementsByTagName('project')
        self.children = []
        for s in itemlist:
            if s.attributes['remote'].value==config.valid_remote:
                repo = s.attributes['name'].value
                self.children.append(Processor.processNode(repo, folder))