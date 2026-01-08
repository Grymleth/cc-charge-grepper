#!/bin/bash

python main.py | grep -A 2 "$1" --color=always