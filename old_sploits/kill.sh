#!/bin/bash
kill `ps aux|grep 5000_|sed "s/root *\([0-9]*\) .*/\1/"`
#rm flags.txt
#touch flags.txt
