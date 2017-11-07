cd /tmp
for file in `ls *.html`;do
newname=$(echo $file |cut -c 1-10)
echo $newname
mv $file ${newname}_oldgirl.HTML

done
