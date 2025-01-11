# Use this script to install DuplexPDF from pip (if not installed yet) and run it as a module

import subprocess
import sys
from packaging.version import Version

print("Starting DuplexPDF by Andreas B.")

try:
    import duplexPDF

    if Version(duplexPDF.__version__) <= Version("1.0.1"):
        print(subprocess.check_call([sys.executable, "-m", "pip", "install", "duplexPDF", "--upgrade"]))
except ModuleNotFoundError:
    print(subprocess.check_call([sys.executable, "-m", "pip", "install", "duplexPDF"]))

