#!/usr/bin/env bash
set -x
#echo "=================="
#echo $1
#pullreq_msg=$1
projectname=$1
jsonfilename=$2

curl -u 'yhao:Rfv.1234' -H "Content-Type: application/json" http://stash.wrs.com/rest/api/1.0/projects/CCM-PS/repos/${projectname}/pull-requests -X POST --data-binary @${jsonfilename}

echo "=====end pull req"
