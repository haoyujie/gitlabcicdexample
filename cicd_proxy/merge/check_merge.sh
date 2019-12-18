#!/usr/bin/env bash
set -x

# sample: $1="test-cicd"
repo_name="$1"
# sample: $2="refs/heads/xxx_master_cicd"
personal_branch=${2##*/}
# remove the suffix "_cicd"
personal_branch=${personal_branch%_cicd}
# sample: personal_branch=xxx_master
account="${personal_branch%%_*}"

base_dir="/buildarea1"
repo_storage="${base_dir}/repo_storage/${repo_name}"
repo_merge_dir="${base_dir}/repo_merge/${repo_name}_${account}"
cd $repo_merge_dir

official_branch=${personal_branch#${account}_}
if [ -z "$personal_branch" ]; then
   echo -e "Please use below format to push:\n
            git push <origin> <branch>\n"
   exit 1
fi

whoami

bitbucket_origin="origin"
remotes_personal_branch="remotes/${bitbucket_origin}/${personal_branch}"
remotes_official_branch="remotes/${bitbucket_origin}/${official_branch}"

remotes_personal_commit="$(git show ${remotes_personal_branch} -s --format=%H)"
branches_contain_personal_commit="$(git branch -a --contains ${remotes_personal_commit})"

until echo "$branches_contain_personal_commit" | grep "$remotes_official_branch" 
do
    sleep 1
    git fetch --all
    branches_contain_personal_commit="$(git branch -a --contains ${remotes_personal_commit})"
done
