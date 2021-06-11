# `nbx` - Notebook Exchange
Collaborate by passing cells between notebooks on different machines.

  - No git merge issues on notebooks.
  
  - Does not disrupt active kernel.
  
  - No custom server or config required.

##### The two notebooks represent notebooks on different machines.
<img src='./docs/assets/quick-graph-2.gif'/>

**above:** 
*on the left:* we type in the answer (code for a histogram) and run the cell. Now we want to send it to the machine so we use `send_answer()` in the cell below to send it to the git remote. <br>
*on the right:* we want to get that answer so we run `receive_answer()` and then the answer appears in the notebook.

##### Try a demo repository [here](https://github.com/sutt/nbx-demo-1).
------------------------------
### Quickstart

   1. Drop the nbx module directory into a git repository.
  
   2. Push the nbx module to the remote.

   3. Have the collaborator clone the repository. 
  
   4. Both of you should import at top: `from nbx import nbx`. You are now ready to use nbx to collaborate.
   
   5. Type in an "answer" into your notebook, a cell you want to share, go to the cell below and type in `nbx.send_answer()`It will print "send answer: done". 

   6. Have the collaborator type `nbx.receive_answer()` in the cell below where they want the answer. then runs the receive_answer cell. A new cell - the answer cell - will appear in the collaborator's notebook.

---------------------------------------------

### Further explanation

  - **No git merge issues on notebooks:**
   Instead of trying to merge two notebooks which is difficult because .ipynb's are json formatted, and each machine will have different meta-data in that json, we don't use git merge. Instead:
    - *to send an answer* we isolate the answer cell and append the data from the input and output attributes into with `.nbx/master.json` in the root of the git repo. We then git push only the `.nbx` directory. 
    - *to receive an answer*  we pull the `.nbx` directory and insert the last cell into our notebook's .ipynb file, then reload the DOM to show the new cell.
    

  - **Does not disrupt active kernel:** The notebook's DOM representation and .ipynb representation will be changed but this does not affect "what python knows". You need to run the received cell for any new variables to be added or set.
    - Accepting an answer does not actually run the cell into your kernel, even though the output of it displays. For example if you received a cell with where a new variable was created, you would have to run that received cell to be able to use the new variable elsewhere in your code.

  
  - **No custom server or config required:** No need to setup another account, or spin up a server, as long as you have push and pull access ot a git repository, you'll be able to collaborate via nbx.
    - But you will need to be able to push/pull from the git server without typing in your password.
   

---------------------------------------------
### Limitations

 - Communication only works one way: one pusher and \[multiple] pullers.

 - Notebook must be at root of git repository.

 - `jupyter notebook` must be run at the git root.

 - Can only send one cell at a time.

 - Can only receive most recent answer.

 - Can only have one cell with input code `send_answer` or `receive_answer`, otherwise the answer may be inserted in the wrong place.

