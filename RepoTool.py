import os
from pathlib import Path
import subprocess

def Init(folder, repourl):
    Path(folder+"repounwind/").mkdir(parents=True, exist_ok=True)
    os.system(f"cp repo {folder}repounwind")

    cwd = os.getcwd()
    print(cwd)
    os.chdir(folder)

    os.chdir("repounwind")

    os.system(f"./repo init -u {repourl} -b master")

    os.chdir(cwd)

def Sync():
    pass