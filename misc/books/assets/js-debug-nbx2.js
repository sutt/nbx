
var date0 = new Date();
var t0 = date0.getTime();
var py_cmd = '';
py_cmd += 'my_time = ';

Promise.resolve(
//IPython.notebook.save_notebook(true)
1+1
).then(function(){
return theFinal();
}
);

function theFinal() {
var date1 = new Date();
var t1 = date1.getTime();
var tDiff = t1 - t0;
py_cmd += tDiff.toString();
console.log(tDiff);
IPython.notebook.kernel.execute(py_cmd);
}
