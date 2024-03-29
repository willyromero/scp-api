# **SCP API.**

## 📘 **Documentación.**

### **1. Formato del archivo .env**

---

Cree un archivo .env en la raíz del proyecto con nombre .env y añada lo siguiente.

```.env
# ip y puerto del servidor (desarrollo)
DEV_SERVER_NAME=""

# ip y puerto del servidor (producción)
SERVER_NAME=""

SESSION_COOKIE_DOMAIN=False

# default timeout a usar si no se establece el parametro timeout en la consulta
DEFAULT_TIMEOUT=

# url para el robot (scraping)
SCRAP_URL=""

# clave secreta para usar la api
SECRET_KEY=
```

**Nota:** `DEV_SERVER_NAME` y `SERVER_NAME` usan el siguiente formato `0.0.0.0:Port`. `DEFAULT_TIMEOUT` acepta únicamente valores numéricos enteros (segundos de espera) o none (sin límite de espera).

Puede usar el siguiente comando para generar una nueva SECRET_KEY.

```powershell
python -c 'import secrets; print(secrets.token_hex())'
```

**`Importante:`** Cada vez que cambie los valores del archivo .env debe obligatoriamente reiniciar el servidor.

### **2. Entorno conda.**

---

- Crear un nuevo entorno en conda, cambie ruta_de_tu_directorio por la ruta del directorio en el que se encuentra el proyecto.

```bash
conda create -p C:\ruta_de_tu_directorio\scp-api\.venv
```

- Acceder al entorno virtual.

```bash
conda activate C:\{ruta_de_tu_directorio}\scp-api\.venv
```

- Instalar python3 (una vez se haya creado y activado el entorno).

```
conda install python=3.10
```

### **3. Entorno virtual (si no usa conda).**

---

Cree un nuevo entorno virtual usando el comando.

```powershell
virtualenv .venv
```

Acceda al entorno virtual usando el siguiente comando.

- En Windows.

```powershell
.\.venv\Scripts\activate
```

- En Linux.

```bash
source .venv/bin/activate
```

**Nota:** para salir del entorno virtual use el comando `deactivate`.

### **4. Instalar dependencias.**

---

Dirigirse al directorio en el que se encuentra el proyecto scp-api y use el siguiente comando.

```powershell
python -m pip install -r requirements.txt
```

**Nota:** puede verificar las dependencias instaladas usando el comando `pip list`.

### **5. Ejecutar.**

---

- En Windows.

```powershell
python .\src\app.py
```

- En Linux.

```bash
python src/app.py
```

### **5. Endpoints.**

---

Vamos a suponer que esta haciendo pruebas locales para lo cual establece la variable `DEV_SERVER_NAME` en el archivo .env como `127.0.0.1:4000`.

Puede usar dos endpints:

- http://127.0.0.1:4000/scp/api/{cedula}

  Descripción:

  - **cedula**: es el número de CI de la persona que se desea optener los datos.
    Este endpoint hace uso de la variable `DEFAULT_TIMEOUT` en el archivo .env.

- http://127.0.0.1:4000/scp/api/{cedula}/{timeout}

  Descripción:

  - **timeout**: es el tiempo de espera usado para la consulta, tiene las mismas características de `DEFAULT_TIMEOUT` del archivo .env.

### **6. Despliegue básico.**

---

En el archivo app.py cambie la configuración cambie el parametro de configuración de la aplicación de `"config.DevelopmentConfig"` a `"config.ProductionConfig"`. El resultado debe ser como se muestra en el siguiente ejemplo.

```
... something above ...

app.config.from_object("config.ProductionConfig")

... something below ..
```

# **Descargar certificado ssl.**

Siga los pasos a continuacion para descargar el certificado ssl del sitio.

## Paso 1.

---

![Paso 1](./img/step_1.png)

## Paso 2.

---

![Paso 2](./img/step_2.png)

## Paso 3.

---

![Paso 3](./img/step_3.png)

## Paso 4.

---

![Paso 4](./img/step_4.png)

## Paso 5.

---

Una vez haya descargado el certificado ubíquelo en la carpeta **`cert`** (la ruta es src/services/cert) y pegue el certificado.

**Nota:** la api hace uso del primer archivo `.cert` ubicado en la carpeta `cert`. Es preferible tener un único certificado en esa carpeta.
