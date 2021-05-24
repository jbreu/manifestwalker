import git
import glob
import config
from pathlib import Path
from SystemManifest import SystemManifest
from RepoToolManifest import RepoToolManifest
from Repo import Repo

def processNode(reponame, folder):

    repo = Repo()

    repo.CloneOrPull(folder, reponame)

    systemmanifestfile = glob.glob(repo.repofolder+"/*system*.xml")
    #repotoolmanifestfile = glob.glob(folder+repo_short+"/*default*.xml")

    if systemmanifestfile:
        #print(whitespace(level)+"Unfolding System Manifest")
        systemmanifest = SystemManifest(systemmanifestfile[0], folder)
        repo.children.extend(systemmanifest.children)

    #elif repotoolmanifestfile:
    #    print(whitespace(level)+"Unfolding Google Repo Tool Manifest")
    #    return RepoToolManifest(repo, subfolder, level)
    #else:
    #    print("Leaf repo")

    return repo