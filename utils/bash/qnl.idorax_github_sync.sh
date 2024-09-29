#!/bin/bash

function print { printf -- "$*\n"; }

function _isatty
{
	typeset -l isatty=$ISATTY
	[[ $isatty == "yes" ]] && return 0
	[[ $isatty ==  "no" ]] && return 1
	[[ -t 1 && -t 2 ]] && return 0 || return 1
}
function str2gray    { _isatty && print "\033[1;30m$@\033[m" || print "$@"; }
function str2red     { _isatty && print "\033[1;31m$@\033[m" || print "$@"; }
function str2green   { _isatty && print "\033[1;32m$@\033[m" || print "$@"; }
function str2yellow  { _isatty && print "\033[1;33m$@\033[m" || print "$@"; }
function str2blue    { _isatty && print "\033[1;34m$@\033[m" || print "$@"; }
function str2magenta { _isatty && print "\033[1;35m$@\033[m" || print "$@"; }
function str2cyan    { _isatty && print "\033[1;36m$@\033[m" || print "$@"; }
function str2white   { _isatty && print "\033[1;37m$@\033[m" || print "$@"; }

function run_git_cmd_prompt
{
	echo "$(id -un)@$(hostname):$(str2yellow $(pwd -P))\$ $(str2cyan $*)"
}

function run_git_cmd
{
	run_git_cmd_prompt "$@"
	eval "$*"
	typeset -i rc=$?
	echo
	return $rc
}

function _highlight
{
	typeset s=$(python3 -c "print('-' * 120)")
	echo
	str2blue "$s"
	echo
	sleep 2
}

function get_github_user
{
	typeset user=${GITHUB_USER}
	echo "$user"
}

function get_github_password
{
	typeset token='ghp_***************'
	echo "$token"
}

function git_push_prompt
{
	typeset -u s_input="NO"
	printf "\n>>> Are you sure you want to continue pushing (Yes/No)? "
	read s_input
	[[ $s_input == "Y" || $s_input == "YES" ]] && return 0 || return 1
}

function fatal
{
	echo "!! $*"
	exit 1
}

function setup
{
	rm -rf $g_wsroot
	mkdir $g_wsroot
}

function cleanup
{
	cd /tmp
	rm -rf $g_wsroot
}

function clone
{
	typeset branch=${DW_MAIN_BRANCH:-"main"}

	cd $g_wsroot
	run_git_cmd git clone $g_origin_master

	cd $g_wsroot/$g_repo
	run_git_cmd git checkout $branch

	cd /tmp
}

function sync
{
	typeset branch=${UP_MAIN_BRANCH:-"main"}
	cd $g_wsroot/$g_repo
	run_git_cmd git remote -v
	run_git_cmd git remote add upstream $g_upstream_master
	run_git_cmd git remote -v
	run_git_cmd git fetch upstream $branch
	run_git_cmd git rebase upstream/$branch
	cd /tmp
}

function push
{
	typeset branch=${DW_MAIN_BRANCH:-"master"}

	typeset user=$(get_github_user)
	typeset password=$(get_github_password)

	export SEXPECT_SOCKFILE=/tmp/sexpect-ssh-$$.sock
	trap '{ sexpect c && sexpect w; } > /dev/null 2>&1' EXIT

	cd $g_wsroot/$g_repo
	unset DISPLAY
	run_git_cmd_prompt '# ===>' $(str2red $g_origin_master)
	run_git_cmd_prompt git push origin $branch
	sexpect spawn      git push origin $branch

	while :; do
		sexpect expect -nocase -re 'Username.*:|Password.*:'
		typeset ret=$?
		if (( $ret == 0 )); then
			typeset out=$(sexpect expect_out)
			if [[ $out == "Username"* ]]; then
				sexpect send -enter "$user"
				continue
			else # "Password"
				git_push_prompt || exit 1

				sexpect send -enter "$password"
				break
			fi
		elif sexpect chkerr -errno $ret -is eof; then
			sexpect wait
			exit
		elif sexpect chkerr -errno $ret -is timeout; then
			sexpect close
			sexpect wait
			fatal "timeout waiting for username/password prompt"
		else
			fatal "unknown error: $ret"
		fi
	done

	sexpect interact
}

repo=${1:-"tmt"}
branch=${2:-"main"}
case $repo in
"sexpect")
	g_origin_master=https://github.com/idorax/sexpect.git
	g_upstream_master=https://github.com/clarkwang/sexpect.git
	g_repo=sexpect
	g_wsroot=/tmp/foo-$g_repo
	export DW_MAIN_BRANCH="master"
	export UP_MAIN_BRANCH="master"
	;;

"ltp")
	g_origin_master=https://github.com/idorax/ltp.git
	g_upstream_master=https://github.com/linux-test-project/ltp.git
	g_repo=ltp
	g_wsroot=/tmp/foo-$g_repo
	export DW_MAIN_BRANCH="master"
	export UP_MAIN_BRANCH="master"
	;;

"tmt")
	g_origin_master=git@github.com:idorax/tmt.git
	g_upstream_master=git@github.com:teemtee/tmt.git
	g_repo=tmt
	g_wsroot=/tmp/foo-$g_repo
	export DW_MAIN_BRANCH="main"
	export UP_MAIN_BRANCH="main"
	;;

*)
	echo "Oops, unknown repo" >&2
	exit 1
	;;
esac

#trap "cleanup" EXIT
setup $branch
_highlight
clone $branch
_highlight
sync $branch
_highlight
push $branch
