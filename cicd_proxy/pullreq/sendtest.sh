#!/usr/bin/env bash
#set -x
pullreq_msg=$(cat ./create_pr_POST.fmt.json)
echo $pullreq_msg
echo "$pullreq_msg"
./sendpullreq.sh "$pullreq_msg"

