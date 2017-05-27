#!/bin/bash


export http_proxy="http://proxy22.iitd.ac.in:3128"
export https_proxy="https://proxy22.iitd.ac.in:3128"
export HTTP_PROXY="http://proxy22.iitd.ac.in:3128"
export HTTPS_PROXY="https://proxy22.iitd.ac.in:3128"

sudo python set_proxy.py # has bash, apt, apm, zsh
gsettings set org.gnome.system.proxy mode 'auto'

## apm proxy
# apm config set proxy $http_proxy
# apm config set https_proxy $https_proxy
#apm config set strict-ssl false
#above line ie 15 is optional if apm proxy still not working

# npm proxy
npm config set proxy $http_proxy
npm config set https-proxy $https_proxy
npm config set strict-ssl false
npm config set registry "http://registry.npmjs.org/"
