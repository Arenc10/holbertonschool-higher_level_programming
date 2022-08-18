#!/bin/bash
#Script that sends a post request
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
