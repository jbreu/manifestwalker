import git
import os
import glob
from xml.dom import minidom
import config
from pathlib import Path

repo_short = config.systemrepo[config.systemrepo.index("/")+1:]
if Path("tmp/level1/"+repo_short).is_dir():
    git.Git("tmp/level1/"+repo_short).pull()
else:
    Path("tmp/level1").mkdir(parents=True, exist_ok=True)
    git.Git("tmp/level1").clone(config.baseurl + config.systemrepo + ".git")

import fnmatch
from SystemManifest import SystemManifest

manifestfile = 'tmp/level1/'+config.systemmanifest
parent = 0

if fnmatch.fnmatch(manifestfile, "*system*.xml"):
    print("System Manifest")
    parent = SystemManifest(manifestfile, 'tmp/level1', 2)
else:
    print("NOK")