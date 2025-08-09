#!/bin/sh

url='http://api.maps.yahoo.com/ajax/geocode'
args='?appid=onestep&qt=1&id=m&qs='
converter="$url$args"

addr="$(echo $* | sed 's/ /+/g')"
curl -s "$converter$addr"
exit 0