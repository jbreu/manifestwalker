from Manifest import Manifest
import config

class SystemManifest(Manifest):

    def __init__(self, manifestfile, parentfolder, level):
        from xml.dom import minidom
        from pathlib import Path
        from git import Git

        currentfolder = f"{parentfolder}/level{level}"
        Path(currentfolder).mkdir(parents=True, exist_ok=True)

        xmldoc = minidom.parse(manifestfile)
        itemlist = xmldoc.getElementsByTagName('project')
        for s in itemlist:
            repo = s.attributes['name'].value
            repo_short = repo[repo.index("/")+1:]
            print(s.attributes['name'].value)
            if Path(f"{currentfolder}/{repo_short}").is_dir():
                Git(f"{currentfolder}/{repo_short}").pull()
            else:
                Git(f"{currentfolder}").clone(f"{config.baseurl}{repo}.git", depth=1)