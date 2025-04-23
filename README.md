# 📚 Biblioteca  

✨ **Descripción**  
Aplicación web para gestionar operaciones de biblioteca (usuarios, libros, reservas, préstamos) con interfaz intuitiva y conexión a **SQL Server**. Incluye operaciones CRUD y diseño responsivo.  

---

## 🌟 Características Principales  
- 👥 Gestión completa: **usuarios, libros, reservas, préstamos**.  
- 🔄 **Operaciones CRUD** para todas las entidades.  
- 🖥️ Interfaz responsiva con **Bootstrap**.  
- 🔗 Conexión estable a **SQL Server** mediante `pyodbc`.  
- 🔍 Búsqueda avanzada en tablas.  

---

## 🛠️ Tecnologías Utilizadas  
| Backend           | Frontend       | Base de Datos   | Conexión        |  
|-------------------|----------------|-----------------|-----------------|  
| ![Python](https://img.shields.io/badge/Python-Flask-yellow) | ![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-blueviolet) | ![SQL Server](https://img.shields.io/badge/SQL_Server-2022-red) | ![PyODBC](https://img.shields.io/badge/pyodbc-5.0-green) |  

---

## ⚙️ Instalación  
1. **Clonar repositorio**:  
   ```bash  
   git clone https://github.com/tuusuario/biblioteca.git  
   cd biblioteca 
   ```

2. **Instalar dependencias:**
  ```bash
    pip install flask pyodbc  
  ```
3. **Configurar SQL Server:**
  - Modificar credenciales en `app.py` (ej: `server='TU_SERVER', database='TU_DB'`)

4. **Ejecutar aplicación:**
  ```bash
    python app.py
  ```
  - Abre: http://127.0.0.1:5000 en tu navegador.


## 🚀Uso

- **Secciones:**
  - 📖`Libros`: Añade, edita o elimina títulos.
  - 👥`Usuarios`:  Gestiona miembros de la biblioteca.
  - 🔄`Préstamos/Reservas`: Controla fechas y estados.
- **Búsqueda:** Filtra datos en cualquier tabla.

## 📸Capturas del aplicativo.
**Vista Principal**
![VistaPrincipal](https://github.com/fatbunny415/biblioteca_crud/blob/SQL/img/vistaPrincipal.png) 
**Vista CRUD/formulario usuarios**
![Usuarios](https://github.com/fatbunny415/biblioteca_crud/blob/SQL/img/usuarios.png)
**Vista CRUD/formulario libros**
![Libros](https://github.com/fatbunny415/biblioteca_crud/blob/SQL/img/libros.png)
**Vista CRUD/formulario prestamos**
![Prestamos](https://github.com/fatbunny415/biblioteca_crud/blob/SQL/img/prestamos.png)
**Vista CRUD/formulario reservas**
![Reservas](https://github.com/fatbunny415/biblioteca_crud/blob/SQL/img/reservas.png)
**Estructura Base de Datos**
![DB](https://github.com/fatbunny415/biblioteca_crud/blob/SQL/img/db.png)
## 📂 Estructura del Proyecto

```plaintext
biblioteca/
├── templates/          # Plantillas HTML
│   ├── index.html      # Página principal
│   ├── usuario_crud.html
│   ├── libro_crud.html
│   └── ...
├── static/             # Assets
│   ├── css/            # Estilos Bootstrap
│   └── js/             # Scripts (opcional)
├── app.py              # Lógica principal
└── README.md           # Documentación
```

## 🌐 Rutas de la Aplicación (Flask)

### 🔍 **Rutas Principales**
| Ruta                | Método | Descripción                          | Parámetros/Observaciones          |
|---------------------|--------|--------------------------------------|-----------------------------------|
| `/`                 | GET    | Página de inicio (Dashboard)         | -                                 |
| `/usuarios`         | GET    | Lista todos los usuarios             | -                                 |
| `/usuarios/agregar` | POST   | Añade un nuevo usuario               | `nombre`, `email`, `teléfono`     |
| `/usuarios/editar/<id>` | POST | Actualiza un usuario existente       | `id` (URL), campos editables      |
| `/usuarios/eliminar/<id>` | GET | Elimina un usuario               | `id` (URL)                        |
| `/libros`           | GET    | Muestra todos los libros             | -                                 |
| `/libros/buscar`    | GET    | Busca libros por título/autor        | `q` (query string)                |

## 🌐 Rutas de Préstamos y Reservas

### 📚 Préstamos
| Ruta                     | Método | Descripción                          | Parámetros                       |
|--------------------------|--------|--------------------------------------|----------------------------------|
| `/prestamos`             | GET    | Lista todos los préstamos activos    | -                                |
| `/prestamos/nuevo`       | POST   | Crea un nuevo préstamo               | `libro_id`, `usuario_id`, `fecha_devolucion` |
| `/prestamos/devolver/<id>` | POST | Registra devolución de préstamo      | `id` del préstamo                |
| `/prestamos/historial`   | GET    | Muestra histórico de préstamos       | `?usuario_id=X` (filtro opcional)|

### 📅 Reservas
| Ruta                     | Método | Descripción                          | Parámetros                       |
|--------------------------|--------|--------------------------------------|----------------------------------|
| `/reservas`              | GET    | Lista reservas pendientes            | -                                |
| `/reservas/nueva`        | POST   | Crea una nueva reserva               | `libro_id`, `usuario_id`, `fecha_reserva` |
| `/reservas/cancelar/<id>`| POST   | Cancela una reserva                  | `id` de la reserva               |


### 🛠️ **Ejemplo de Uso con `curl`**
```bash
# Obtener todos los libros:
curl -X GET http://127.0.0.1:5000/libros

# Añadir un nuevo usuario (JSON):
curl -X POST http://127.0.0.1:5000/usuarios/agregar \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Ana", "email": "ana@example.com"}'
```

## 🤝Contribuciones.

- 🍴 Haz un fork del proyecto.

- 🌿 Crea una rama:
    ```bash
      git checkout -b feature/nueva-funcionalidad  
    ```
- 💬 Envía un Pull Request con una descripción clara.

## 📜 Licencia.

MIT © 2024 - Libre uso y modificación.
- Creditos: Fatush🐂.
- Nequi: 3007973265 por si alguna donación.

