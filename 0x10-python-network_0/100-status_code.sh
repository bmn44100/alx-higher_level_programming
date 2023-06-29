#!/bin/bash
# a Bash script that sends a request to a URL and displays the status code of the response
curl -so "$1"/dev/null -w "%{http_code}" "$1"
