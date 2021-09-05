from Repo import Repo
from pathlib import Path
import os
import config


class RepotoolRepo(Repo):

    def Init(self, repo_long, folder):
        repo = repo_long[repo_long.rfind("/") + 1:]
        repourl = config.baseurl + repo_long + ".git"

        unwindfolder = folder + repo + "_repounwind/"
        self.repofolder = unwindfolder

        Path(unwindfolder).mkdir(parents=True, exist_ok=True)
        os.system(f"cp repo {unwindfolder}")

        cwd = os.getcwd()
        os.chdir(unwindfolder)

        os.system(f"./repo init -u {repourl} -b master >> ../repotoollog.txt")

        os.chdir(cwd)

    def Sync(self):
        cwd = os.getcwd()
        os.chdir(self.repofolder)

        os.system("./repo sync --no-clone-bundle -c --optimized-fetch -j 10 >> ../repotoollog.txt")

        os.chdir(cwd)

    def __init__(self, manifestfolder, folder, repo):

        self.Init(repo, folder)
        self.Sync()

        self.reponame = repo
        self.children = []

        # TODO continue unfolding from here
        # Processor.processNode(repo, folder, level+1)
