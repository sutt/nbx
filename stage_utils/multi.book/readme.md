# copy.lib

This stage is designed around:
- copy the nbx lib into directory at mkstage time.
- both the student and teachers notebook look the same, distingiugh via port number.

### Git initialize
Make stage initializing the teacher and remote repos from scratch.
 - git add book1 (but not nbx directory)
 - checkout dummy branch on remote
 - student clones the remote; this requires some remote jiggering
 

### Git configure
No changes in config on any brepo.

### Git Tracking
Track the primary notebook and nbx direcotry. So the student has the nbx library from cloning the remote, push to it from teacher.
 



