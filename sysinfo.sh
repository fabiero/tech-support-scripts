#!/bin/bash
echo "===== SYSTEM INFO ====="
echo "Hostname: $(hostname)"
echo "Current User: $(whoami)"
echo "Date: $(date)"
echo ""
echo "===== MEMORY USAGE ====="
free -h
echo ""
echo "===== DISK USAGE ====="
df -h
echo ""
echo "===== IP ADDRESS ====="
ip addr | grep inet
