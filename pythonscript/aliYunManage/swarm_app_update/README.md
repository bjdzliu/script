# test env

## build image + push image + update app service's yaml :  
-s [member-api|member-api2|member-game]  
-v [v1]  when you deploy first version, use v1.  
[--nobuild | --build] . If you've built a image,   

```
./update.sh -s member-gamae -v v2 --nobuild
or
./update.sh -s member-gamae -v v2 --build

```

## update static file in oss
put staitc files into {script path}/lm-web
```
python upload.py
```


# production env

