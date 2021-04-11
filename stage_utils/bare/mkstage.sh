
# "C:\Program Files\Git\usr\bin\bash.exe" mkstage.sh

# update the remote url to new directory location
base=$(pwd)

cd teacher
git remote set-url origin $base/remote/main

cd ../student
git remote set-url origin $base/remote/main

# set remote onto dummy branch to enable push
cd ../remote/main
git checkout -b dummy
cd ..