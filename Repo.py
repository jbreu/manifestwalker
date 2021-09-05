import config
import git
from pathlib import Path
import shutil


# https://stackoverflow.com/questions/19687394/python-script-to-determine-if-a-directory-is-a-git-repository
def is_git_repo(path):
    try:
        _ = git.Repo(path).git_dir
        return True
    except git.exc.InvalidGitRepositoryError:
        return False


class Repo:

    def CloneOrPull(self, folder, reponame, remote=''):
        repo_short = reponame[reponame.rfind("/") + 1:]
        print(repo_short)

        if Path(folder + repo_short).is_dir():
            if is_git_repo(folder + repo_short):
                git.Git(folder + repo_short).pull()
            else:
                shutil.rmtree(folder + repo_short, ignore_errors=True)

        if not Path(folder + repo_short).is_dir():
            if remote == '':
                git.Git(folder).clone(config.baseurl + reponame + ".git", depth=1)
            else:
                git.Git(folder).clone(remote + reponame + ".git", depth=1)

        self.repofolder = folder + repo_short
        self.reponame = reponame
        self.children = []
