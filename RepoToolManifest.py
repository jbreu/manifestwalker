from Manifest import Manifest
import config
import Processor
from pathlib import Path
from git import Git
import os
import RepoTool

class RepoToolManifest(Manifest):

    def __init__(self, repo, folder, level):
        repo_short = repo[repo.index("/")+1:]

        fldr = folder+repo_short
        Path(fldr).mkdir(parents=True, exist_ok=True)

        RepoTool.Init(fldr)

        # ./../../../repo sync --no-clone-bundle -c --optimized-fetch -j 10")

        pass

        #Processor.processNode(repo, folder, level+1)