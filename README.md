# TM Fibonacci
---
Christian Echeverría 221441
Gustavo Cruz 22779
---

# Ejecución
Para ejecutar el proyecto es necesario contar con Python 3.12 en adelante, o Docker. Adicionalmente, contar con un archivo **tm_conf.json** para brindar a la Turing Machine de una configuración específica.
*Ejecución: Python*
```sh
python main.py
```
*Ejecución: Docker*
```sh
docker buildx build -t fibonacci .
sudo docker run -it fibonacci bash
```
