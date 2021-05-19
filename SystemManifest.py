from Manifest import Manifest
import config


class SystemManifest(Manifest):

    def __init__(self, manifestfile):
        from xml.dom import minidom
        from pathlib import Path
        from git import Git

        xmldoc = minidom.parse(manifestfile)
        itemlist = xmldoc.getElementsByTagName('project')
        for s in itemlist:
            repo = s.attributes['name'].value
            repo_short = repo[repo.index("/")+1:]
            print(s.attributes['name'].value)
            if Path(f"tmp/{repo_short}").is_dir():
                Git(f"tmp/{repo_short}").pull()
            else:
                Git("tmp").clone(f"{config.baseurl}{repo}.git", depth=1)