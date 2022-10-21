#!/bin/bash
#display http methds
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
