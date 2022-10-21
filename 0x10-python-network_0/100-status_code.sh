#!/bin/bash
# send get request
curl -s -o /dev/null -w "%{http_code}" "$1"
