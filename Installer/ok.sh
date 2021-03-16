#!/bin/sh

chmod +x rr.py

mv rr.py rr

mkdir -p ~/bin

cp rr ~/bin

export PATH=$PATH":$HOME/bin"