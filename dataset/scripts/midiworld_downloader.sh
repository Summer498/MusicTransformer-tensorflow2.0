#!/bin/bash

[ ! "$1" ] && echo 'Error: please specify output dir' && exit
[ ! "$2" ] && echo 'Error: please specify page url' && exit
dir=$1
url=$2
mkdir -p $dir
echo "$(curl -s $url | egrep -o 'http.+download/[^"]+' | uniq)" \
    | wget --content-disposition -P $dir -i -

cd $dir
ls | egrep -i -v '\.mid$' | xargs rm
file * | grep -v 'Standard MIDI' | awk -F ':' '{print $1}' | xargs rm
