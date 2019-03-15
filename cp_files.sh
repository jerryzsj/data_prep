#!/bin/bash

FORDER=../data/ycb/ycb_1/
LIST=filelist


CPFILE=filelist


IFS="
"
for F in $(cat $FORDER$LIST) ; do
	echo $F
	for G in $(cat $FORDER$F$LIST) ; do
		echo $G
		cp $CPFILE $FORDER$F$G$CPFILE
	done

done
IFS=$OLDIFS