#!/bin/bash
# get status code response
curl --silent --location --head "$1" --output /dev/null --write-out '%{http_code}'
