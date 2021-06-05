
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
git config user.name Teacher 1
git config user.email teacher@opensource.net

git add book1.ipynb book2.ipynb include/
git commit -m "root nbs and include/ subbooks added"

cp ../../../nbx ./ -r

git add nbx
git commit -m "nb + nbx added"

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
git config user.name Student 1
git config user.email Eager.Mind.1999@tikt.ok
git config pull.rebase true
cd ..