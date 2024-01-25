#!/bin/bash
# This script takes a URL, sends a POST request to the passed URL, and displays body of the response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
