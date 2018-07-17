#!/bin/bash

split_size=128M

# split the files into chunks
mkdir -p tmp_folder_for_files
for file in `ls ./input/ | grep -v README.md`
do
    split -C${split_size} ./input/$file tmp_folder_for_files/${file}_
done

# do the python
python3 ./src/root.py
# clean up
rm -rf tmp_folder_for_files
echo Done.

