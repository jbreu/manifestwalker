import git
import os
import glob
from xml.dom import minidom
import config

#empty the tmp folder
# TODO dont do it, rather pull the repo
import os, shutil
folder = 'tmp'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

git.Git("tmp").clone(config.baseurl + config.systemrepo)

import fnmatch
from SystemManifest import SystemManifest

manifestfile = 'tmp/'+config.systemmanifest
parent = 0

if fnmatch.fnmatch(manifestfile, "*system*.xml"):
    print("System Manifest")
    parent = SystemManifest(manifestfile)
else:
    print("NOK")