#!/bin/bash
outfile=${1:-creatures.md}
python scour.py > "$outfile"
