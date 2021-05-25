from Repo import Repo
import Processor
import config

class XMLManifestRepo(Repo):

    def __init__(self, manifestfile, folder):
        from xml.dom import minidom

        xmldoc = minidom.parse(manifestfile)

        remotes = {}

        xmlremotes = xmldoc.getElementsByTagName('remote')
        for r in xmlremotes:
            name = r.attributes['name'].value
            fetch = r.attributes['fetch'].value
            if not fetch.endswith('/'):
                fetch += '/'
            remotes[name]=fetch
        
        self.children = []
        xmlprojects = xmldoc.getElementsByTagName('project')
        for s in xmlprojects:
            repo = s.attributes['name'].value
            self.children.append(Processor.processNode(repo, folder, remotes[s.attributes['remote'].value]))