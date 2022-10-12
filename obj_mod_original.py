object_file = r'.\track__.obj'

def obj_line_mod(path):
    path_list = path.split('\\')
    file_name = path_list[-1].split('.')[0]
    with open(path,'r') as finp, open(f'modified_{file_name}.obj','w') as fout:
        n = 0
        contents = finp.readlines()
        new_contents = []
        for index, line in enumerate(contents):
            #read through the file line by line
            if line[0:2] != 'l ':
                #check to see if the line is a line declaration
                new_contents.append(line)
            elif line[0:2] == 'o ':
                pass
            else:
                #in which case, replace it with the necessary normal vector
                line = 'vn 0.0 0.0 -1.0\n'
                new_contents.append(line)
                continue
            if line[0:2] == 'v ':
                #find all vertex values in the file and create a copy of the line
                #with y offset +0.1
                vertex_string = line
                coordinates = vertex_string.split(' ')
                new_y = str(float(coordinates[2])+0.01)
                new_vertex = f'v {coordinates[1]} {new_y} {coordinates[3]}'
                new_contents.append(new_vertex)
                n += 1
        i=1
        while i < (2*n)-1:
            new_face = f'f {i}//1 {i+1}//1 {i+2}//1\n'
            new_contents.append(new_face)
            i+=1
        fout.writelines(new_contents)
        
obj_line_mod(object_file)
