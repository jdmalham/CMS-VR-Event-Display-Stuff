#I don't know how to make a command line application in python so for right now we're just gonna have to define the file path by editing the code
#Very important that you use an r-string for the path
object_file = r".\track__.obj"
def obj_line_mod(path):
    path_list = path.split('\\')
    with open(path,'r') as finp, open(f'modified_{path_list[-1]}.obj',"w") as fout:
        n = 0
        contents = finp.readlines()
        new_contents = []
        for index, line in enumerate(contents):
            #read through the file line by line
            if line[0:2] != 'l ':
                #check to see if the line is a line declaration. 
                #If the above is true, then it is either an object or vertex declaration, which we want to save
                new_contents.append(line)
            elif line[0:2] == 'o ':
                #if it is the name of the object, we don't want to modify that so we just pass over it
                pass
            else:
                #in which case, replace it with the necessary normal vector
                line = "vn 0.0 0.0 1.0\n"
                new_contents.append(line)
                #another_line = "vn 0.0 0.0 -1.0\n"
                #new_contents.append(another_line)
                #Currently the "another_line" data just makes it flip upside down 
                #but I feel like this is *probably* the right track to getting the triangles fixed. idk
                continue
            if line[0:2] == 'v ':
                #find all vertex values in the file and create a copy of the line
                #with y offset +0.1
                vertex_string = line
                coordinates = vertex_string.split(' ')
                new_y = str(float(coordinates[2])+0.01)
                new_vertex = f"v {coordinates[1]} {new_y} {coordinates[3]}"
                new_contents.append(new_vertex)
                n += 1
        i=1
        while i < n-2:
            #define faces
            new_face = f"f {i}//1 {i+1}//1 {i+2}//1\n"
            new_contents.append(new_face)
            i+=1
        fout.writelines(new_contents)
obj_line_mod(object_file)
