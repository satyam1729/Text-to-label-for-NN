#!/bin/bash
#add configuration files stuff here
echo "Downloading dataset from http://hts.sp.nitech.ac.jp/archives/2.3/HTS-demo_CMU-ARCTIC-SLT.tar.bz2"
cd data
wget http://hts.sp.nitech.ac.jp/archives/2.3/HTS-demo_CMU-ARCTIC-SLT.tar.bz2
echo "extracting dataset"
tar -xvf HTS-demo_CMU-ARCTIC-SLT.tar.bz2
cd ..
chmod 775 tools/setup_tools.sh
echo 'setting up tools required'
./tools/setup_tools.sh