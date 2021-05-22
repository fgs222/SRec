# Tecnologias de Apoyo de Construccion Ciudadana
## Repositorio de desarrollo Speech Recognition

<img src="https://www.frba.utn.edu.ar/wp-content/uploads/2016/08/logo-utn.ba-horizontal-e1471367724904.jpg" alt="UTN FRBA" width="500"/>

* ***Alumno***: *Francisco Guillermo Stahl*
* ***Correo***: fsthal@frba.utn.edu.ar
* ***Universidad***: *UTN-FRBA, Departamento de Ingeniería Electrónica*
* ***Año***: 2021

## Estructura del repositorio

* ***tbd***: tbd.

## Acceso rapido del Repositorio

* [tbd](tbd)

## Instalación de los paquetes

Primero es necesario descargar las librerías base Sphinxbase y Pocketsphinx, creamos un directorio en donde descargaremos los archivos y copiamos las librerías, para eso se abre la consola y se escriben los siguientes comandos:

```console
sudo apt install autoconf libtool automake bison python-dev swig libpulse-dev
mkdir sphinx
cd sphinx
git clone https://github.com/cmusphinx/sphinxbase
git clone https://github.com/cmusphinx/pocketsphinx
```
Se procede a instalarlas en el sistema:

```console
cd sphinxbase
./autogen.sh
make
sudo make install
```

Una vez instalado Sphinxbase, se procede a instalar Pocketsphinx:

```console
cd ../pocketsphinx
./autogen.sh
make
sudo make install
```

Se procede a instalar la interfaz que permitirá usar Pocketsphinx con Python (asegurar que esten instalados los siguientes paquetes):

```console
sudo apt-get install -qq python3 python3-dev python3-pip build-essential swig git libpulse-dev libasound2-dev pulseaudio swig
pip install --upgrade pip setuptools wheel
pip install --upgrade pocketsphinx
```
