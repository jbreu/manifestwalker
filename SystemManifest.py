from Manifest import Manifest
import config
import Processor

class SystemManifest(Manifest):

    def __init__(self, manifestfile, folder, level):
        from xml.dom import minidom
        from pathlib import Path
        from git import Git

        xmldoc = minidom.parse(manifestfile)
        itemlist = xmldoc.getElementsByTagName('project')
        for s in itemlist:
            repo = s.attributes['name'].value
            repo_short = repo[repo.index("/")+1:]
            #print(s.attributes['name'].value)

            if Path(f"{folder}/{repo_short}").is_dir():
                Git(f"{folder}/{repo_short}").pull()
            else:
                Path(folder).mkdir(parents=True, exist_ok=True)
                Git(folder).clone(f"{config.baseurl}{repo}.git", depth=1)

            Processor.processNode(repo, folder, level+1)