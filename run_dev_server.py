
from subprocess import check_call
import sys
import os

# Get path of this file
basePath = os.path.dirname(os.path.abspath(__file__))
managePath = os.path.join(basePath, "manage.py")

check_call([
    sys.executable,
    managePath,
    "runserver",
    "--settings=wwustc.dev-settings"
])
