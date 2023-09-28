#!/usr/bin/bash
# Write a Bash script that displays numbers from 1 to 20 and:
#   displays 4 and then bad luck from China for the 4th loop iteration
#   displays 9 and then bad luck from Japan for the 9th loop iteration
#   displays 17 and then bad luck from italy
count=1
while [ $count -le 20 ]; do
	case "$count" in
	4)
		echo "$count bad luck from China"
		;;
	9)
		echo "$count bad luck from Japan"
		;;
	17)
		echo "$count bad luck from italy"
		;;
	*)
		echo "$count"
		;;
	esac
	((count++))
done
