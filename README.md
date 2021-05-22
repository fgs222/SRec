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
sudo apt install autoconf libtool automake bison python3-dev swig libpulse-dev

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
sudo apt-get install -qq python3 python3-pip build-essential git libasound2-dev pulseaudio swig

pip3 install --upgrade pip3 setuptools wheel
pip3 install --upgrade pocketsphinx
```
Una vez realizado estos pasos es necesario agregar el idioma español al reconocimiento de voz. Para eso es necesario ir a la siguiente dirección https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Spanish/ y descargarnos los siguientes archivos: [cmusphinx-es-5.2.tar.gz] (https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Spanish/cmusphinx-es-5.2.tar.gz/download) , es-20k.lm.gz, es.dict.

Descomprimimos los archivos cmusphinx-es5.2.tar.gz y es-20k.lm.g, los archivos que acabamos de descomprimir contienen los modelos y el diccionario que se va a utilizar para nuestro idioma.

Cabe recalcar que el modelo utilizado es el de hidden markov models [1][2]

Abrimos nuevamente nuestra consola:
python -c "from pocketsphinx import get_model_path; print(get_model_path())"
