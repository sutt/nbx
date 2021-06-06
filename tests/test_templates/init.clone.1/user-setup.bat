REM # activate two separate notebook servers
REM # on different ports: 9000 (teacher), 9001 (student)
REM # leaves you with 4 cmd windows
REM # conda activate base
cd teacher
dir
start jupyter notebook --port=9000
cd ..
cd student
start jupyter notebook --port=9001
start cmd
cd ..
cd teacher
