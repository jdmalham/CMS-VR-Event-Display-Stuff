object_file = r"C:\Users\Owner\Downloads\CERN obj files\track.obj"

def obj_line_mod(path):
    with open(path,'r') as finp, open('modified_track.obj',"w") as fout:
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
                line = "vn 0.0 0.0 1.0\n"
                another_line = "vn 0.0 0.0 -1.0\n"
                new_contents.append(line)
                new_contents.append(another_line)
                continue
            print(line)
            if line[0:2] == 'v ':
                #find all vertex values in the file and create a copy of the line
                #with y offset +0.1
                vertex_string = line
                coordinates = vertex_string.split(' ')
                new_y = str(float(coordinates[2])+0.01)
                new_vertex = f"v {coordinates[1]} {new_y} {coordinates[3]}"
                new_contents.append(new_vertex)
                n += 1
        #Hmmmmm.... How should I go about trying to declare the faces??? part of me is thinking
        #that I should do something that uses an index to 
        i=1
        while i < n-2:
            new_face = f"f {i}//1 {i+1}//1 {i+2}//1\n"
            new_contents.append(new_face)
            i+=1
        i=1
        """while i < n-2:
            face = f"f {i}//2 {i+1}//2 {i+2}//2\n"
            new_contents.append(face)
            i+=1"""
        print(new_contents)
        fout.writelines(new_contents)
        
obj_line_mod(object_file)