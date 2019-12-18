#!/usr/bin/env bash
set -x
#echo "=================="
#echo $1
pullreq_msg=$1

#echo $pullreq_msg
#echo "$pullreq_msg"
#echo "$pullreq_msg" > test.json
echo "*****************************"
#val=$(echo `"curl -u '"yhao:Rfv.1234"' -H '"Content-Type: application/json"' -X POST -d '"$pullreq_msg"'  http://stash.wrs.com/rest/api/1.0/projects/CCM-PS/repos/test-cicd/pull-requests`)

#tmp=echo "aaaabccccadfgsd" 
#echo $tmp

val="curl -u 'yhao:Rfv.1234' -H 'Content-Type: application/json' -X POST -d '$pullreq_msg'  http://stash.wrs.com/rest/api/1.0/projects/CCM-PS/repos/$2/pull-requests"

eval "$val"
