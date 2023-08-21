#!/bin/zsh

path=$@

python3 -m pytest -o markers=task $path
