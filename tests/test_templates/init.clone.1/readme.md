# init.clone

This stage is designed around:
- building a git saveable (non-submodule) stage template
- using a relative import of the nbx library via `sys.path.append('../../../')`
-  testing the pull.rebase bug

### Git initialize
Make stage initializing the teacher and remote repos from scratch.
 - git add book1 (but not nbx directory)
 - checkout dummy branch on remote
 - student clones the remote; this requires some remote jiggering

### Git configure
Student repo is configured to locally alter behavior of git to include:
    `git config pull.rebase true`

### Git Tracking
Track the primary notebook
 - this helps trigger the pull.rebase bug when nec.



