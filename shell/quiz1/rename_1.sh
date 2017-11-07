for file in `ls /tmp/*.html`;do
newname=$(echo $file |sed -e 's/\_oldboy/\_oldgirl/' -e 's/.html/.HTML/')
mv $file $newname

done
