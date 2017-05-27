#!/bin/bash

sudo python unset_proxy.py #bash,apt,apm,zsh
unset http_proxy
unset https_proxy
unset HTTP_PROXY
unset HTTPS_PROXY
gsettings set org.gnome.system.proxy mode 'none'


##if you turn on that optional line 15 in counterpart,
#apm config set strict-ssl true
