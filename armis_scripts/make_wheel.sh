#!/bin/bash

python3 setup.py bdist_wheel

echo
echo "======================================"
echo "Make sure you update the setup.py version first before uploading, and then match it in armis' requirement.in"
