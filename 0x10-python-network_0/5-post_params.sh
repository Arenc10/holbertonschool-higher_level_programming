#!/bin/bash
#Script that sends a post request
curl -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
