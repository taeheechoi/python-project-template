import os
import sys
from pathlib import Path 

PROJECT_DIR = Path(__file__).parents[1]
sys.path.append(os.fspath(PROJECT_DIR))

DIST_DIR = PROJECT_DIR / 'dist'
sys.path.append(os.fspath(DIST_DIR))