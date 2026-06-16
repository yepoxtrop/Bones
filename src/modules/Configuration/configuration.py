import os;

def configuration_windows():
    discs = os.listdrives();
    os.environ.get("USERNAME")

    for disc in discs:

        if disc.startswith("C"):# -> Unidad C

            addres_folder = os.path.join(disc.replace("\\\\", "\\"), "ProgramData", "Bot");
            addres_folder_log = os.path.join(addres_folder, ".Logs");
            addres_file_env = os.path.join(addres_folder, ".env");

            if not os.path.exists(addres_folder):
                os.makedirs(addres_folder);

            if not os.path.exists(addres_folder_log):
                os.makedirs(addres_folder_log);

            if not os.path.exists(addres_file_env):
                with open(addres_file_env,"a", encoding="utf-8") as env_file:
                    env_file.write("FIRST_NAME = NONE");
                    env_file.write("SECOND_NAME = NONE");
                    env_file.write("LAST_NAME = NONE");
            else:
                archivo_contenido = '';
                with open(addres_file_env, "r", encoding="utf-8") as env_file:
                    archivo_contenido = env_file.read();

                if archivo_contenido == "" :
                    with open(addres_file_env, "a", encoding="utf-8") as env_file:
                        env_file.write("FIRST_NAME = NONE");
                        env_file.write("SECOND_NAME = NONE");
                        env_file.write("LAST_NAME = NONE");