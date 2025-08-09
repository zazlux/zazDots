#!/usr/bin/bash 

 pkill redshift
 killall pipewire 
 killall pipewire-pulse 
 killall wireplumber
 killall pulseaudio


 sleep 0.3



pipewire &
pipewire-pulse &
wireplumber &

