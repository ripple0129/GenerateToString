import os
class GenerateToString:
    def __init__(self):
        self.postfix = "VO.java"
        self.path = "C:\\_JSP\\workspaceHiber\\healthy\\src\\main\\java\\com\\massuer\\healthy\\model\\entity"
        self.field_types = ["int", "Integer", "Double", "double", "Float", "float", "Long", " long", "byte", "Byte", "short", "Short",
                        "boolean", "Boolean", "Char", "char", "Date", "String", "GirlMassageTypeVO"];

    def get_all_vo_files(self):
        filenames = [];
        for filename in os.listdir(self.path):
            if(filename.endswith(self.postfix)):
                filenames.append(filename)
        return filenames;

    def parse_fields(self, full_path_file_name):
        field_type_list = [];
        with open(full_path_file_name) as fp:
            for line in fp:
                for field_type in self.field_types:
                    if field_type in line and "(" not in line and ")" not in line and "import" not in line:
                        field_type_str = ''.join(line.replace(';', '').replace(",",'').split(' ')[-1:])
                        if field_type_str not in field_type_list:
                            field_type_list.append(field_type_str)
        fp.close()
        return field_type_list

    def build_tostring(self, field_type_list):
        tostring_str = ''.join('    public String toString(){\n       return ')
        tostring_str = tostring_str + ' \"' + field_type_list[0].strip('\n') + ':\"+' + field_type_list[0].strip('\n') +'+'
        for field_type in field_type_list[1:-1]:
            field_type = field_type.strip('\n')
            tostring_str = tostring_str + ' \" ,' + field_type + ':\"+' + field_type +'+'
        tostring_str = tostring_str + ' \" ,' + field_type_list[-1].strip('\n') + ':\"+' + field_type_list[-1].strip('\n') + ';\n    }\n}'
        return tostring_str

    def write_tostring(self, full_path_file_name, tostring_str):
        readFile = open(full_path_file_name, 'r')
        lines = readFile.readlines()
        readFile.close()
        writeFile = open(full_path_file_name, 'w')
        writeFile.writelines([item for item in lines[:-1]])
        writeFile.write(tostring_str)
        writeFile.close()

    # public void toString(){
    #     return "id:"+id;
    # }

if __name__ == '__main__':
    generator = GenerateToString()
    filenames = generator.get_all_vo_files()
    for filename in filenames:
        full_path_file_name = generator.path+"\\"+filename
        field_type_list = generator.parse_fields(full_path_file_name)
        tostring_str = generator.build_tostring(field_type_list)
        generator.write_tostring(full_path_file_name, tostring_str)
