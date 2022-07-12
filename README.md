#    Deploy python
****
**Установка питона (убунту)**

$ sudo apt-get update

$ sudo apt-get install python3

****

**Проверка версии**

$ python3 -V

****

**Установка / проверка pip**

$ sudo apt-get install python3-pip

$ pip --version

****

**Установка venv**

$ sudo apt install python3-venv

****

****

### **Создание папки venv в проекте**

$ cd ~/project (project - имя директории со скриптом) 

путь до исполняемого файла питона 

$ /usr/bin/python3 -m venv venv  

или 

$ python3 -m venv venvRandomName (произвольное имя папки)  

****

**Активация venv** 

C:\folderprogect\venv\Scripts\activate.bat *(windows)*
	
source ./venv/bin/activate (директория venv может называться произвально)

****

**Деактивация venv**

(venv) $ deactivate

****

**Загрузка пакетов**

pip install -r requirements.txt
****

**Создание requirements**

pip freeze > requirements.txt
