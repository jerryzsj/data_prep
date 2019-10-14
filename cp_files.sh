#!/bin/bash

FORDER=../data/ycb/stl_files_14cam/
LIST=filelist


CPFILE=origin.pcd
COUNT=0
PCD=.pcd
SLASH=/
IFS="
"
for F in $(cat $FORDER$LIST) ; do
	# echo $FORDER$F$SLASH$CPFILE
	# echo $FORDER$COUNT$PCD
	cp $FORDER$F$SLASH$CPFILE $FORDER$COUNT$PCD
	let COUNT+=1
	# echo $COUNT
	# for G in $(cat $FORDER$F$LIST) ; do
	# 	echo $G
	# 	cp $CPFILE $FORDER$F$G$CPFILE
	# done

done
IFS=$OLDIFS