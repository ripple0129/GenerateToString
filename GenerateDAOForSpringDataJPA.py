import os
class GenerateDAOForSpringDataJPA:
    def __init__(self):
        self.entity_file_postfix = ".java"
        self.entity_path = "C:\\_JSP\\workspaceHiber\\healthy\\src\\main\\java\\com\\massuer\\healthy\\model\\entity"
        self.entity_package_path = "com.massuer.healthy.model.entity"
        self.dao_package_path = "com.massuer.healthy.model.dao"
        self.dao_postfix = "DAO"

    def get_all_vo_files(self):
        filenames = [];
        for filename in os.listdir(self.entity_path):
            if(filename.endswith(self.entity_file_postfix)):
                filenames.append(filename)
        return filenames;

    def build_file_str(self, filename):
        package_str = "package "+self.dao_package_path +";\n\n"
        import_str = "import org.springframework.data.jpa.repository.JpaRepository;\n"+"import "+ self.entity_package_path +"."+ filename.strip(self.entity_file_postfix)+ ";\n\n"
        interface_str = "public interface "+filename.strip(self.entity_file_postfix)+ self.dao_postfix + " extends JpaRepository<"+filename.strip(self.entity_file_postfix)+", Integer>{\n}"
        return package_str+import_str+interface_str

    def build_file(self, filename, file_str):
        path = self.entity_path.replace('\\', '.')
        entity_package_path_len = len(self.entity_package_path)
        newfile = (path[:0-entity_package_path_len]+self.dao_package_path).replace('.', '\\')+"\\"+filename.strip(self.entity_file_postfix)+self.dao_postfix+".java"
        with open( newfile, 'w') as fp:
            fp.write(file_str)

if __name__ == '__main__':
    generator = GenerateDAOForSpringDataJPA()
    filenames = generator.get_all_vo_files()
    for filename in filenames:
        generator.build_file(filename, generator.build_file_str(filename))
