"""
Module to hold a few general settings that will be used by several steps of the reduction procedure
"""

from pathlib import Path

# Path to the raw data files (we follow good practice and won't modify these files):
data_dir = Path.home() / ".testsmt/UBC/UBC_telescope"

# The above should be mostly self-explanatory, but for reference, the doc to pathlib is here:
# https://docs.python.org/3/library/pathlib.html

# Path to a directory where intermediate files and results can be written:
work_dir = Path.home() / ".testsmt/UBC/workdir"
work_dir.mkdir(parents=True, exist_ok=True) # We create this directory in case it does not yet exist.

# Our FITS files have long headers.
# Just to make some summary tables easier to read, we give a list of the few important header keywords we care about:
ifc_header_keywords = ["imagetyp", "filter", "exptime", "object", "xbinning", "ybinning", "naxis1", "naxis2", "DATE-OBS", "UTSTART"]

