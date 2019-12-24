
var b_save = false;
var b_scroll = true;
var b_select = true;
var b_flash = true;
var b_log = true;


var nb_path = IPython.notebook.notebook_path;
var cell_index = IPython.notebook.get_selected_index() - 1;

if (b_log) {console.log('selected_index: ' + cell_index);}

//save notebook waits for finish
if (b_save) {
Promise.resolve(
IPython.notebook.save_notebook(true)
).then(function(){
// this is where we'll call to python kernel
return console.log('done with save')
}
).then(function() {
return theRest();
}
);

} else {
theRest();
}

function theRest() {

IPython.notebook.load_notebook(nb_path);

if (b_log) {console.log('after load');}

setTimeout(basicFunc, 500);
function basicFunc() {

console.log('in basicFunc');
var orig_cell = IPython.notebook.get_cell(cell_index);
var html_cell = $(orig_cell.element)[0];

if (b_scroll) {
$(orig_cell.element)[0].scrollIntoViewIfNeeded({inline:'center'});}

if (b_select) {IPython.notebook.select(cell_index);}

function flash(ms_flash) {
Promise.resolve(
$(html_cell).stop().animate({backgroundColor:'#008000'}, ms_flash).promise()
).then(function(){
return $(html_cell).stop().animate(
{backgroundColor:'#FFFFFF'}, ms_flash);
}
);
}
if (b_flash) {flash(500);}

if (b_log) {console.log('end of basicFunc')}
} // end basicFunc ------------

if (b_log) {console.log('done with theRest()');}
} // end theRest---------------

if (b_log) {console.log('end of js payload');}
