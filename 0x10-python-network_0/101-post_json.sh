#!/bin/bash
# sends a json POST request
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
