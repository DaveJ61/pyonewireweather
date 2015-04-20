# Initial test using pyonewire (https://code.google.com/p/pyonewire)
# Still need to figure out linix permissions for the DS2490 (USB)
# but does work using sudo

from pyonewire.master import ds2490
>>> master = ds2490.DS2490Master()
>>> for ib in master.Search(master.SEARCH_NORMAL):
...   print hex(ib)
