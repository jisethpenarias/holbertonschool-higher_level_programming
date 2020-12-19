#!/bin/bash
# get status code response
# --silent Dont show progress or error messages
# --location if a page was moved to a different location 
# this will re do the curl to the right location
# --head just get the headers of the response
# --output file where you want the output
# --write-out  the format of the output in this case we only need the http code
curl --silent --location --head "$1" --output /dev/null --write-out '%{http_code}'
