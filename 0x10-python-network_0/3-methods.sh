#!/bin/bash
# Bash script that displays all HTTP methods
curl -sI OPTIONS "$1" | grep 'Allow' | cut -d " " -f 2-
