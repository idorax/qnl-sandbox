#!/bin/bash

FILE=$(readlink -f "${BASH_SOURCE[0]}")
CDIR=$(dirname "$FILE")
source $CDIR/../include/libsort.sh

make cl
make

UTIL02=$CDIR/bts
UTIL03=$CDIR/qnl-bts

# Test case 01
nints_fixed="6 7 5 4 3 2 1"
$UTIL02 $(echo $nints_fixed)
echo
$UTIL03 $(echo $nints_fixed)
echo

# Test case 02
nints_random=$(get_nints)
$UTIL02 $(echo $nints_random)
echo
$UTIL03 $(echo $nints_random)
echo

# Test case 03
export ISINT='false'
nchars_fixed='b u c k e t s o r t'
$UTIL02 $(echo $nchars_fixed)
echo
$UTIL03 $(echo $nchars_fixed)
echo

# Test case 04
nchars_random=$(get_nchars)
$UTIL02 $(echo $nchars_random)
echo
$UTIL03 $(echo $nchars_random)
echo
