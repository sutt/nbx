def get_cell_outputs(cell):
    output_class_name = "output_subarea"
    output_elem = cell.find_elements_by_class_name(output_class_name)
    outputs = [elem.text for elem in output_elem]
    return outputs

def check_outputs_for_term(outputs, term):
    tmp = [output.find(term) > -1 for output in outputs]
    return any(tmp)

def flatten_outputs(outputs):
    tmp = ''
    for output in outputs:
        tmp += str(output)
    return tmp