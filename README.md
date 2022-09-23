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

**Nota:** `DEV_SERVER_NAME` y `SERVER_NAME` usan el siguiente formato `0.0.0.0:Port`.

Puede usar el siguiente comando para generar una nueva SECRET_KEY.

```powershell
python -c 'import secrets; print(secrets.token_hex())'
```

**`Importante:`** Cada vez que cambie los valores del archivo .env debe obligatoriamente reiniciar el servidor.

### **2. Entorno virtual.**

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

### **3. Instalar dependencias.**

---

```powershell
python -m pip install -r requirements.txt
```

**Nota:** puede verificar las dependencias instaladas usando el comando `pip list`.

### **4. Ejecutar.**

---

- En Windows.

```powershell
python .\src\app.py
```

- En Linux.

```bash
python src/app.py
```

### **5. Despliegue básico.**

---

En el archivo app.py cambie la configuración cambie el parametro de configuración de la aplicación de `"config.DevelopmentConfig"` a `"config.ProductionConfig"`. El resultado debe ser como se muestra en el siguiente ejemplo.

```
... something above ...

app.config.from_object("config.ProductionConfig")

... something below ..
```
