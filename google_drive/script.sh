#!/bin/bash
JOB=$1
TARGET=$2
FILE=$3

python3 main.py --job $JOB --target_dir $TARGET --file_name_or_path $FILE
