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

mkdir -p ~/.rad_routes

cd ~/.rad_routes

curl https://github.com/shyaboi/rad-route-runner/archive/refs/heads/master.zip -O -J -L

unzip rad-route-runner-master.zip

cd rad-route-runner-master

chmod +x rr.py

mv rr.py rr

cp -r ./runners/ ~/.rad_routes

cp rr ~/.rad_routes

export PATH=$PATH":$HOME/.rad_routes/"

exit 0