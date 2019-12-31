
Promise.resolve(
IPython.notebook.save_notebook(true)
).then(function(){
return theFinal();
}
);

function theFinal() {

var nb_name = IPython.notebook.notebook_name;

var py_cmd = '';
py_cmd += 'nbx2.ImportClass.merge_give_answer("' + nb_name + '")';

IPython.notebook.kernel.execute(py_cmd);
console.log(py_cmd);

var py_cmd = '';
py_cmd += 'nbx2.ImportClass.gitcomm_push_answer()';

IPython.notebook.kernel.execute(py_cmd);
console.log(py_cmd);

}
