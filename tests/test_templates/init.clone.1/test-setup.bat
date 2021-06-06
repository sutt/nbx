REM # setting up a test environment:
REM # activate two separate notebook servers
REM # on different ports: 9200 (teacher), 9201 (student)
REM # conda activate base
cd teacher
start jupyter notebook --port=9200 --no-browser --NotebookApp.token='' --NotebookApp.password=''
cd ..
cd student
start jupyter notebook --port=9201 --no-browser --NotebookApp.token='' --NotebookApp.password=''

