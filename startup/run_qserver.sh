#!/bin/bash --login

# source activate bsgui


if [ ! -f ~/.config/databroker/qserver_test.yml ]; then
    echo "Copying in a databroker config..."
    mkdir -p ~/.config/databroker
    cp sample_config/db.conf ~/.config/databroker/qserver_test.yml
fi

echo "Running the queue server..."

# Ensure you set the backend appropriately, or the queue server subprocess
# may segfault:
export MPLBACKEND=Agg

start-re-manager --startup-dir . --databroker-config qserver_test
