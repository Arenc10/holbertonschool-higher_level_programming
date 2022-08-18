#!/bin/bash
#Script that sends a post request
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
