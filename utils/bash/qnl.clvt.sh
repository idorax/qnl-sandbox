#!/bin/bash
#
# clean up /var/tmp and /tmp
#

################################################################################

function print { printf -- "$*\n"; }

function _isatty
{
    typeset -l isatty=${ISATTY:-"auto"}
    [[ $isatty == "yes" ]] && return 0         # yes
    [[ $isatty == "no" ]] && return 1          # no
    [[ -t 1 && -t 2 ]] && return 0 || return 1 # auto
}

function str2gray    { _isatty && print "\033[1;30m$@\033[m" || print "$@"; }
function str2red     { _isatty && print "\033[1;31m$@\033[m" || print "$@"; }
function str2green   { _isatty && print "\033[1;32m$@\033[m" || print "$@"; }
function str2yellow  { _isatty && print "\033[1;33m$@\033[m" || print "$@"; }
function str2blue    { _isatty && print "\033[1;34m$@\033[m" || print "$@"; }
function str2magenta { _isatty && print "\033[1;35m$@\033[m" || print "$@"; }
function str2cyan    { _isatty && print "\033[1;36m$@\033[m" || print "$@"; }
function str2white   { _isatty && print "\033[1;37m$@\033[m" || print "$@"; }

################################################################################

function get_ps1
{
    echo "$(id -un)@$(hostname):$(pwd)"
}

cd /var/tmp

for i in $(ls -1); do
    [[ $i == "sandbox" ]] && continue
    [[ $i == "demo" ]] && continue

    echo "remove $i ..."
    #sudo rm -rf $i
    rm -rf $i
done
echo "$(str2cyan $(get_ps1))$(str2red \$) $(str2yellow ls --color -l)"
ls --color -l
echo

if [[ $1 == '-v' ]]; then
    cd /tmp

    #sudo rm -rf /tmp/*
    rm -rf /tmp/*

    echo "$(str2cyan $(get_ps1))$(str2red \$) $(str2yellow ls --color -l)"
    ls --color -l
    echo
fi
