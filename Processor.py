import git
import glob
import config
from pathlib import Path
from XMLManifestRepo import XMLManifestRepo
from RepotoolRepo import RepotoolRepo
from Repo import Repo

def processNode(reponame, folder):

    repo = Repo()

    repo.CloneOrPull(folder, reponame)

    systemmanifestfile = glob.glob(repo.repofolder+"/*system*.xml")
    repotoolmanifestfile = glob.glob(repo.repofolder+"/*default*.xml")

    if systemmanifestfile:
        systemmanifestrepo = XMLManifestRepo(systemmanifestfile[0], folder)
        repo.children.extend(systemmanifestrepo.children)
    elif repotoolmanifestfile:
        systemmanifestrepo = XMLManifestRepo(repotoolmanifestfile[0], folder)
        repo.children.extend(systemmanifestrepo.children)
        #repotoolrepo = RepotoolRepo(repo.repofolder, folder, repo.reponame)
        #repo.children.append(repotoolrepo)

    return repo