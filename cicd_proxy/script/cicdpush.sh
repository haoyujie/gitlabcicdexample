#!/usr/bin/env bash
set -x

# sample: $1="test-cicd"
repo_name="$1"
# sample: $2="refs/heads/xxx_master"
personal_branch=${2##*/}
# sample: personal_branch=xxx_master
account="${personal_branch%%_*}"
# Hard coded as "CCM-PS" now
# project_name="$3"
project_name="CCM-PS"
username="yhao"
password="Rfv.1234"

#gitlab	ssh://git@pek-lpd-huawei.wrs.com:2223/ccm-ps/test-cicd.git (push)
#origin	ssh://git@stash.wrs.com:7999/ccm-ps/test-cicd.git (fetch)

base_dir="/buildarea1"
repo_storage="${base_dir}/repo_storage/${repo_name}"
repo_merge_dir="${base_dir}/repo_merge/${repo_name}_${account}"

rm -rf $repo_merge_dir
cp -r $repo_storage $repo_merge_dir

cd $repo_merge_dir

bitbucket_origin="origin"
# Add CI/CD origin
cicd_origin="gitlab"
git remote add $cicd_origin ssh://git@pek-lpd-huawei.wrs.com:2223/ccm-ps/${repo_name}.git

official_branch=${personal_branch#${account}_}
if [ -z "$personal_branch" ]; then
   echo -e "Please use below format to push:\n
            git push <origin> <branch>\n"
   exit 1
fi
personal_cicd_branch=${personal_branch}_cicd
official_cicd_branch="pipeline" # solid cicd pipeline branch , prevent be demaged.

# sync with repo
# git fetch ${cicd_origin}
git fetch --all

# Construct JSON data for pull request
REST_URL="http://stash.wrs.com/rest/default-reviewers/1.0/projects/${project_name}/repos/${repo_name}/conditions"
remotes_personal_branch="remotes/${bitbucket_origin}/${personal_branch}"
remotes_official_branch="remotes/${bitbucket_origin}/${official_branch}"
push_commit="$(git show ${remotes_personal_branch} -s --format=\"%H\")"
pull_request_title="$(git show ${remotes_personal_branch} -s --format=%s)"
pull_request_description="$(git log ${remotes_official_branch}..${remotes_personal_branch} | sed ':label;N;s/\n/\\n/;b label')"
pull_request_default_reviewers=$(curl -u "${username}:${password}" -H "Content-Type: application/json" ${REST_URL} -X GET | jq '[{ user: .[] | {name: .reviewers[].name} }]')
[ -n "${pull_request_default_reviewers}" ] && reviewers="\"reviewers\": ${pull_request_default_reviewers}," || reviewers=""
pull_request_JSON=$(cat <<PullRequestEnd
{
    "title": "${pull_request_title}",
    "description": "${pull_request_description}",
    "state": "OPEN",
    "open": true,
    "closed": false,
    "fromRef": {
        "id": "refs/heads/${personal_branch}",
        "repository": {
            "slug": "${repo_name}",
            "name": "${repo_name}",
            "project": {
                "key": "${project_name}"
            }
        }
    },
    "toRef": {
        "id": "refs/heads/${official_branch}",
        "repository": {
            "slug": "${repo_name}",
            "name": "${repo_name}",
            "project": {
                "key": "${project_name}"
            }
        }
    },
    "locked": false,
    ${reviewers} 
    "links": {
        "self": [
            null
        ]
    }
}
PullRequestEnd
)

# Clean up old local and remote cicd branch
git branch -D ${personal_cicd_branch} || true
git push ${cicd_origin} :${personal_cicd_branch} --force

# prepare merge, create personal CI/CD branch
git checkout -b ${personal_cicd_branch}
git reset --hard ${cicd_origin}/${official_cicd_branch}

# merge personal branch to personal CI/CD branch
git merge --no-ff --no-edit $bitbucket_origin/${personal_branch} -m "Merge remote-tracking branch '${bitbucket_origin}/${personal_branch}' into ${personal_cicd_branch}

${pull_request_JSON}"

# push to CI/CD repo, since old personal CI/CD branch has been
# removed, so we no need '--force' here.
git push ${cicd_origin} ${personal_cicd_branch}
