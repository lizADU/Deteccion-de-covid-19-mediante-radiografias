Entrar al USB:
- mount(permite ver los volumenes montados en el sistema)
1. en una terminal escribimos: mount
2. entramos en el USB: cd /media/valentin/8 GB
3. entramos en covid: cd covid/

Instalar VS Code
1. en una terminal: sudo snap install --classic code
2. abrir el programa en la terminal: code
3. abrir el archivo 'covid' en VS Code
4. instalar las extensiones necesarias

Instalar Miniconda
1. ir a la pagina web: Miniconda
2. descargar el instalador de Linux: Miniconda3 Linux 64-bit
3. dar permisos de administrador al instalador: chmod + x Miniconda3-latest-Linux-x86_64.sh.
4. ejecutar el instalador: ./Miniconda3-latest-Linux-x86_64.sh.
5. escribir 'yes' cuando sea necesario
6. reiniciar el equipo
7. en la terminal creamos un environment: conda create -n covid
(/home/valentin/miniconda/envs/covid)
8. activamos el environment: conda activate covid

Instalar librerias
1. instalar PyTorch: conda install pytorch torchvision cudatoolkit=10.2 -c pytorch
2. instalar Matplotlib: conda install -c conda-forge matplotlib
3. instalar PyQt5: conda install -c anaconda pyqt
4. instalar mysql-connector: pip install mysql-connector-python
5. instalar mysql: 
	-> conda install -c conda-forge mysql
	#-> sudo -i (entrar en modo superusuario)
	#-> apt-get update (actualizamos el repositorio)
	#-> apt-get install mysql-server
	#-> instalar Workbench desde la tienda
	#-> entramos a mysql: mysql -u root -p
	#-> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_passwor BY '12345'; 

IMPORTANTE: en el archivo Conexion.py cambiar DOCTORES a doctores y PACIENTES a pacientes.
-> En caso de instalar mal un paquete usar: pip uninstall nombrepaquete