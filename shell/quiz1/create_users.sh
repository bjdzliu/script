i=0
while ((i<11))
do
echo $i
pass=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9'|head -c 8)
echo $pass
if (( $i < 10));then
echo oldboy0$i
useradd -p `openssl passwd -1 -salt  'bitsalt' $pass` oldboy0$i
else
echo oldboy$if
useradd -p `openssl passwd -1 -salt  'bitsalt' $pass` oldboy$if
fi
let i++
done
