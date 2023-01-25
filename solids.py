import time

start = time.time()

def solid_dual_render(path):
    path_list = path.split('\\')
    file_name = path_list[-1].split('.')[0]
    with open(path, 'r+') as file, open(f'test_{file_name}.obj','w') as fout:
        contents = file.readlines()
        new_contents = []
        for index, item in enumerate(contents):
            new_contents.append(item)
            if item[0:2] == "f ":
                line_items = item.split(' ')
                print(line_items)
                line_escape_removed = line_items[3].replace('\n','')
                added_line = f'f {line_escape_removed} {line_items[2]} {line_items[1]}\n'
                new_contents.append(added_line)
        fout.writelines(new_contents)

solid_dual_render(r"C:\Users\Owner\Downloads\MuonChambers_V1 (2).obj")

end = time.time()
print(end-start)
