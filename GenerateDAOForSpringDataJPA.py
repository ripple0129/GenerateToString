import os
class GenerateDAOForSpringDataJPA:
    def __init__(self):
        self.entity_file_postfix = ".java"
        self.entity_path = "C:\\_JSP\\workspaceHiber\\healthy\\src\\main\\java\\com\\massuer\\healthy\\model\\entity"
        self.entity_package_path = "com.massuer.healthy.model.entity"
        self.dao_package_path = "com.massuer.healthy.model.dao"
        self.dao_postfix = "DAO"
        self.service_package_path = "com.massuer.healthy.service"

    def get_all_vo_files(self):
        filenames = [];
        for filename in os.listdir(self.entity_path):
            if(filename.endswith(self.entity_file_postfix)):
                filenames.append(filename)
        return filenames;

    def build_dao_str(self, filename):
        package_str = "package "+self.dao_package_path +";\n\n"
        import_str = "import org.springframework.data.jpa.repository.JpaRepository;\n"+"import "+ self.entity_package_path +"."+ filename.strip(self.entity_file_postfix)+ ";\n\n"
        interface_str = "public interface "+filename.strip(self.entity_file_postfix)+ self.dao_postfix + " extends JpaRepository<"+filename.strip(self.entity_file_postfix)+", Integer>{\n}"
        return package_str+import_str+interface_str

    def build_service_str(self, filename):
        service_str = self.build_service_import_str(filename)
        service_str += self.build_service_head_str(filename)
        service_str += self.build_service_method_findById_str(filename)
        service_str += self.build_service_method_findAll_str(filename)
        service_str += self.build_service_method_insert_str(filename)
        service_str += self.build_service_method_update_str(filename)
        service_str += self.build_service_method_delete_str(filename)
        service_str += "}"
        return service_str

    def build_service_import_str(self, filename):
        entity = filename.strip(self.entity_file_postfix+'.java')
        import_str = "package "+self.service_package_path +";\n\n" + "import java.util.List;\n"
        import_str += "import org.springframework.beans.factory.annotation.Autowired;\n"
        import_str += "import org.springframework.stereotype.Service;\n"
        import_str += "import " + self.dao_package_path + "." + entity + self.dao_postfix + ';\n'
        import_str += "import " + self.entity_package_path + "." + entity +';\n\n'
        return import_str

    def build_service_head_str(self, filename):
        entity = filename.strip(self.entity_file_postfix+'.java')
        body_str = "@Service\n"
        body_str += "public class " + entity + "Service {\n\n"
        body_str += "    @Autowired\n"
        body_str += "    private "+entity+ self.dao_postfix +" "+ entity[:1].lower()+entity[1:] +self.dao_postfix+";\n\n"
        return body_str

    def build_service_method_findById_str(self, filename):
        entity = filename.strip(self.entity_file_postfix+'.java')
        findById_str = "    public " + entity + " findById(Integer id){\n"
        findById_str += "        return " + entity[:1].lower()+entity[1:]+self.dao_postfix + ".findOne(id);\n"
        findById_str += "    }\n\n"
        return findById_str

    def build_service_method_findAll_str(self, filename):
        entity = filename.strip(self.entity_file_postfix+'.java')
        findAll_str = "    public List<" + entity + "> findAll(){\n"
        findAll_str += "        return " + entity[:1].lower()+entity[1:]+self.dao_postfix + ".findAll();\n"
        findAll_str += "    }\n\n"
        return findAll_str

    def build_service_method_insert_str(self, filename):
        entity = filename.strip(self.entity_file_postfix+'.java')
        insert_str = "    public void insert(" + entity + " " + entity[:1].lower()+entity[1:] + "){\n"
        insert_str += "        " + entity[:1].lower()+entity[1:]+self.dao_postfix + ".save("+ entity[:1].lower()+entity[1:] +");\n"
        insert_str += "    }\n\n"
        return insert_str

    def build_service_method_update_str(self, filename):
        entity = filename.strip(self.entity_file_postfix+'.java')
        update_str = "    public void update(" + entity + " " + entity[:1].lower()+entity[1:] + "){\n"
        update_str += "        " + entity[:1].lower()+entity[1:]+self.dao_postfix + ".save("+ entity[:1].lower()+entity[1:] +");\n"
        update_str += "    }\n\n"
        return update_str

    def build_service_method_delete_str(self, filename):
        entity = filename.strip(self.entity_file_postfix+'.java')
        delete_str = "    public void delete(Integer id){\n"
        delete_str += "        " + entity[:1].lower()+entity[1:]+self.dao_postfix + ".delete(id);\n"
        delete_str += "    }\n\n"
        return delete_str

    def generate_dao_file(self, filename, file_str):
        path = self.entity_path.replace('\\', '.')
        entity_package_path_len = len(self.entity_package_path)
        newfile = (path[:0-entity_package_path_len]+self.dao_package_path).replace('.', '\\')+"\\"+filename.strip(self.entity_file_postfix)+self.dao_postfix+".java"
        with open( newfile, 'w') as fp:
            fp.write(file_str)

    def generate_service_file(self, filename, file_str):
        path = self.entity_path.replace('\\', '.')
        entity_package_path_len = len(self.entity_package_path)
        newfile = (path[:0-entity_package_path_len]+self.service_package_path).replace('.', '\\')+"\\"+filename.strip(self.entity_file_postfix)+"Service.java"
        with open( newfile, 'w') as fp:
            fp.write(file_str)

if __name__ == '__main__':
    generator = GenerateDAOForSpringDataJPA()
    filenames = generator.get_all_vo_files()
    for filename in filenames:
        generator.generate_dao_file(filename, generator.build_dao_str(filename))
        generator.generate_service_file(filename, generator.build_service_str(filename))
