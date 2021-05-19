import git
import glob
import config
from pathlib import Path
from SystemManifest import SystemManifest
from RepoToolManifest import RepoToolManifest

def whitespace(level):
    return ''.join([' '*level])

def processNode(repo, folder, level):

    subfolder = f"{folder}level{level}/"
    repo_short = repo[repo.index("/")+1:]
    #print(whitespace(level)+folder)
    print(whitespace(level)+repo)
    
    # TODO put in separate function/class
    if level==1:
        if Path(folder+repo_short).is_dir():
            git.Git(folder+repo_short).pull()
        else:
            Path(folder).mkdir(parents=True, exist_ok=True)
            git.Git(folder).clone(config.baseurl + config.systemrepo + ".git")

    systemmanifestfile = glob.glob(folder+repo_short+"/*system*.xml")
    repotoolmanifestfile = glob.glob(folder+repo_short+"/*default*.xml")

    if systemmanifestfile:
        print(whitespace(level)+"Unfolding System Manifest")
        return SystemManifest(systemmanifestfile[0], subfolder, 1)
    elif repotoolmanifestfile:
        print(whitespace(level)+"Unfolding Google Repo Tool Manifest")
        return RepoToolManifest(repotoolmanifestfile[0], subfolder, 1)
    else:
        print(whitespace(level)+"NOK")