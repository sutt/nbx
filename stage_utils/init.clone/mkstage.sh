
# "C:\Program Files\Git\usr\bin\bash.exe" mkstage.sh

# update the remote url to new directory location
base=$(pwd)

cd remote
cd main
git init
git checkout -b dummy
cd ..
cd ..

cd teacher
git init
git remote add origin $base/remote/main
git add book1.ipynb
git commit -m "nb added"
# git add nbx
# git commit -m "nb + nbx added"
git push origin master

sleep 1

# this, otherwise student can't clone properly
cd ..
cd remote
cd main
git checkout master
git checkout -b dummy
cd ..
cd ..

git clone $base/remote/main student
cd student
git config pull.rebase true
cd ..