# SGSSI-21.Minado.G21232535

En la asignatura SGSSI el resumen criptográfico de cada trabajo que se entrega se almacena en un bloque. Cada bloque guarda los resúmenes *sha256* de cada trabajo de cada alumno correspondientes a esa actividad. La estructura de un bloque es la siguiente:

- Numero de bloque

- Titulo de tarea + numero de elementos

- Identificador del bloque anterior

- Resúmenes sha256

El objetivo del minero en es conseguir que el resumen del ultimo bloque tenga la mayor cantidad de ceros al principio del resumen sha256 del bloque. Mediante este programa, se calculan resúmenes dependiendo de los parámetros que se le pongan al principio.

## Instrucciones de uso

Para ejecutar los programas:

- *hash_checker*:

```shell
python3 hash_checker.py <inputfile>
```
- *hashmining*:

```shell
python3 hashmining.py <inputfilename> <outputfilename> <zeroint>
```
- *hashminingTime*:

```shell
python3 hashminingTime.py <inputfile> <outputfilename> <timeint>
```

## Problemas frecuentes

En caso de error en hashminingTime.py con el *import progress* ejecutar en *shell*:

```shell
pyp3 install progress
```

## Integridad de los archivos

- *hash_checker.py*: a48f80062abefd16fc0c80ad55451aee
- *hashmining.py*: 503a1dea14e1d8960b7a9e822ed487b4
- *hashminingTime.py*: 48fa93396d6ac68626618834222f5ac7