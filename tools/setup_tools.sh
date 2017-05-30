#!/bin/bash
echo "extracting speech_tools"
tar -xvf speech_tools-2.4-release.tar.gz
echo "installing speech_tools"
cd speech_tools
./configure
make
make test
echo "speech_tools installed"
cd ..
echo "extracting festival"
tar -xvf festival-2.4-release.tar.gz
cd festival
make
echo "festival installed"

