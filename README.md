# Tablas Hash en Python

Implementación de **tablas hash** desde cero con las dos estrategias principales para resolver colisiones. Proyecto de la materia de Estructuras de Datos.

## Archivos
| Archivo | Estrategia | Descripción |
|---|---|---|
| `hash1.py` | **Encadenamiento** | Cada posición guarda una lista; las colisiones se agregan a esa lista. |
| `hash2.py` | **Dirección abierta (sondeo lineal)** | Si la posición está ocupada se busca la siguiente libre; usa un marcador de "borrado" para que las búsquedas no se corten al eliminar. |

Ambas usan la función hash `clave % tamaño` e incluyen un menú en consola para **insertar, buscar, eliminar y mostrar** la tabla.

## Ejecutar
```bash
python hash1.py   # encadenamiento
python hash2.py   # dirección abierta
```

> Nota: estas tablas hash son estructuras de datos para búsqueda rápida. No son lo mismo que las funciones hash criptográficas (como SHA-256 o bcrypt) que se usan para proteger contraseñas.
