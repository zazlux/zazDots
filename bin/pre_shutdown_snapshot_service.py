#!/usr/bin/env python3
#
import subprocess
import sys
import os
from datetime import datetime

# Define the path for the log file
log_file = '/var/log/pre_shutdown_snapshot.log'

# Create the log file if it doesn't exist
if not os.path.exists(log_file):
    with open(log_file, 'w'):
        pass

# Redirect stdout and stderr to the log file
sys.stdout = open(log_file, 'a')
sys.stderr = sys.stdout

# Define the name for your snapshot and the default boot environment
SNAPSHOT_BASE_NAME = "pre-shutdown-snapshot-service"
MAX_SNAPSHOTS_RETAIN = 5  # Number of youngest snapshots to retain

# Generate a timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Define the snapshot name with timestamp
SNAPSHOT_NAME = f"{SNAPSHOT_BASE_NAME}_{timestamp}"

# Function to create the snapshot
def create_snapshot():
    subprocess.run(["bectl", "create", SNAPSHOT_NAME])
    print(f"Snapshot created: {SNAPSHOT_NAME}")

# Function to activate the new boot environment
def activate_snapshot():
    subprocess.run(["bectl", "activate", SNAPSHOT_NAME])
    print(f"{SNAPSHOT_NAME} activated as the default boot environment")

# Function to remove older snapshots, retaining the youngest ones
def remove_old_snapshots():
    snapshots = subprocess.check_output(["bectl", "list"]).decode().splitlines()[1:]
    snapshots.sort(key=lambda x: x.split()[-1], reverse=True)  # Sort by creation date
    snapshots_to_retain = snapshots[:MAX_SNAPSHOTS_RETAIN]
    for snapshot in snapshots:
        snapshot_name = snapshot.split()[0]
        if snapshot_name != SNAPSHOT_NAME and snapshot_name.startswith(SNAPSHOT_BASE_NAME) \
                and snapshot not in snapshots_to_retain:
            subprocess.run(["bectl", "destroy", snapshot_name])
            print(f"Snapshot removed: {snapshot_name}")

# Main script
print("Preparing to shutdown...")

# Call create_snapshot function before shutdown
create_snapshot()

# Activate the new boot environment
activate_snapshot()

# Remove older snapshots, retaining the youngest ones
remove_old_snapshots()
