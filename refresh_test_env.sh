#!/usr/bin/env bash
#Mac hack for realpath program
name='homeautomation'
test $(which realpath) || realpath() {
   [[ $1 = /* ]] && echo "$1" || echo "$PWD/${1#./}"
}
mydir=$(dirname $(realpath $0))
test -d ${mydir}/test && rm -rfv ${mydir}/test
test -d ${mydir}/dist && rm -rfv ${mydir}/dist
virtualenv venv
source venv/bin/activate || {
    echo "Error, could not activate test environment"
}
python ${mydir}/setup.py sdist
dfile=$(find ${mydir}/dist -type f -name '*.gz')
pip uninstall ${name}
pip install ${dfile}
echo "Be sure to issue a \`source venv/bin/activate\`"
