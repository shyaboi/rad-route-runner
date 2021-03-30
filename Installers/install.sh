#!/bin/sh

# read -r -p "Do you want to install Rad Route Runner? [y/N] " response

# case "$response" in
#     [yY][eE][sS]|[yY]) 

    # curl -o py.pkg 'https://www.python.org/ftp/python/3.9.2/python-3.9.2-macos11.pkg'
    # echo donne downloading
    # echo see the py installer pop up.
    #     start py.pkg
    # read -n 1 -s -r -p "When node is done installing, Press any key to continue"
    #   npx npop  ;;
    # *)
    #    echo byeeeeeeeeeee
    #     ;;
# esac


chmod +x rr.py

mv rr.py rr

mkdir -p ~/bin

cp -r ./runners/ ~/bin

cp rr ~/bin

export PATH=$PATH":$HOME/bin/"

exit 0