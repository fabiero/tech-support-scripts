#!/bin/bash
echo "===== BACKUP STARTED ====="
mkdir -p ~/backups
cp ~/practice.txt ~/backups/
cp ~/fruits.txt ~/backups/
echo "Files backed up successfully!"
ls ~/backups
echo "===== BACKUP COMPLETE ====="
