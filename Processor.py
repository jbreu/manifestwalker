import glob
from XMLManifestRepo import XMLManifestRepo
from Repo import Repo


def processNode(reponame, folder, remote=''):

    repo = Repo()

    repo.CloneOrPull(folder, reponame, remote)

    systemmanifestfile = glob.glob(repo.repofolder + "/*system*.xml")
    repotoolmanifestfile = glob.glob(repo.repofolder + "/*default*.xml")

    if systemmanifestfile:
        systemmanifestrepo = XMLManifestRepo(systemmanifestfile[0], folder)
        repo.children.extend(systemmanifestrepo.children)
    elif repotoolmanifestfile:
        systemmanifestrepo = XMLManifestRepo(repotoolmanifestfile[0], folder)
        repo.children.extend(systemmanifestrepo.children)
        # repotoolrepo = RepotoolRepo(repo.repofolder, folder, repo.reponame)
        # repo.children.append(repotoolrepo)

    return repo
