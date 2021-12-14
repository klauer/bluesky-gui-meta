import os.path
import pathlib
import sys

from typing import List

from ophyd.ophydobj import OphydObject

from hutch_python.load_conf import load
from hutch_python.log_setup import setup_logging
from pcdsdaq.sim import set_sim_mode

# run_path = pathlib.Path(__file__).parent.resolve()
run_path = pathlib.Path("/Users/klauer/Repos/bluesky-gui-meta/startup")
test_path = pathlib.Path("/reg/g/pcds/pyps/apps/hutch-python/tst")

if test_path.exists():
    config_path = test_path / "conf.yml"
else:
    config_path = run_path / "sample_config" / "conf.yml"

sys.path.insert(0, str(config_path.parent))

# Do the normal hutch-python loading
set_sim_mode(True)
setup_logging()

objs = load(cfg=str(config_path))

# Make some post-adjustments for queue-server
# Disable the bec plots for the server process (keep the table)
objs["bec"].disable_plots()
# Make all objects available to queue-server
globals().update(objs)

# Additionally expand the plan namespace so that the queue-server sees it
globals().update(vars(objs["bp"]))

# Additionally expand the experiment object so that the queue-server sees it
try:
    globals().update(vars(objs["user"]))
except KeyError:
    pass
