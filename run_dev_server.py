
from subprocess import check_call
import sys
import os

# Get path of this file
basePath = os.path.dirname(os.path.abspath(__file__))
managePath = os.path.join(basePath, basePath)

check_call([
    sys.executable,
    managePath,
    "--settings=wwustc.dev-settings"
])
