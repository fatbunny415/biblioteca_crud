# 📚 Biblioteca

## ✨ Descripción  
Aplicación web para gestionar operaciones de biblioteca (**usuarios**, **libros**, **reservas**, **préstamos**) con interfaz intuitiva y conexión a **MongoDB**. Incluye operaciones CRUD y diseño responsivo.

---

## 🌟 Características Principales  
- 👥 **Gestión completa:** usuarios, libros, reservas, préstamos.  
- 🔄 **Operaciones CRUD** para todas las entidades.  
- 🖥️ **Interfaz responsiva** con Bootstrap.  
- 🍃 **Conexión estable** a MongoDB mediante pymongo.  
- 🔍 **Búsqueda avanzada** en colecciones.  

---

# 🛠️ Tecnologías Utilizadas  
| **Backend** | **Frontend** | **Base de Datos** | **Conexión** |  
|-------------|--------------|-------------------|--------------|  
| Python      | Bootstrap    | MongoDB           | PyMongo      |  

---

## ⚙️ Instalación  
1. **Clonar repositorio**:  
   ```bash  
   git clone https://github.com/tuusuario/biblioteca.git  
   cd biblioteca  


- Instalar dependencias:pip install flask pymongo  

- Configurar MongoDB:
Modifica la URI de conexión en app.py (ejemplo: mongodb://localhost:27017).
- Ejecutar aplicación:python app.py  
Abre: http://127.0.0.1:5000 en tu navegador.


# 🚀 Uso
## Secciones:
- 📖 Libros: Añade, edita o elimina títulos.
- 👥 Usuarios: Gestiona miembros de la biblioteca.
- 🔄 Préstamos/Reservas: Controla fechas y estados.
- 🔍 Búsqueda: Filtra datos en cualquier colección.


# 📸 Capturas del Aplicativo
**Vista Principal del aplicativo**
![VistaPrincipal](https://github.com/fatbunny415/biblioteca_crud/blob/main/img/VistaPrincipa.png)
---

**Vista de usuarios**
![usuarios](https://github.com/fatbunny415/biblioteca_crud/blob/main/img/usuario.png)
---

**Vista libros**
![libros](https://github.com/fatbunny415/biblioteca_crud/blob/main/img/libro.png)
---

**Vista reservas**
![reservas](https://github.com/fatbunny415/biblioteca_crud/blob/main/img/reserva.png)
---

# 📂 Estructura del Proyecto
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



## 🌐 Rutas de la Aplicación (Flask)

### 🔍 Rutas Principales
| **Ruta**             | **Método** | **Descripción**                  | **Parámetros/Observaciones**     |
|----------------------|------------|----------------------------------|----------------------------------|
| `/`                 | GET        | Página de inicio (Dashboard)     | -                                |
| `/usuarios`         | GET        | Lista todos los usuarios         | -                                |
| `/usuarios/agregar` | POST       | Añade un nuevo usuario           | `nombre`, `email`, `teléfono`    |
| `/usuarios/editar/<id>` | POST   | Actualiza un usuario existente   | `id` (URL), campos editables     |
| `/usuarios/eliminar/<id>` | GET  | Elimina un usuario               | `id` (URL)                       |
| `/libros`           | GET        | Muestra todos los libros         | -                                |
| `/libros/buscar`    | GET        | Busca libros por título/autor    | `q` (query string)               |

---

### 📚 Rutas de Préstamos
| **Ruta**             | **Método** | **Descripción**                  | **Parámetros**                   |
|----------------------|------------|----------------------------------|----------------------------------|
| `/prestamos`         | GET        | Lista todos los préstamos activos | -                                |
| `/prestamos/nuevo`   | POST       | Crea un nuevo préstamo           | `libro_id`, `usuario_id`, `fecha_devolucion` |
| `/prestamos/devolver/<id>` | POST | Registra devolución de préstamo  | `id` del préstamo                |
| `/prestamos/historial` | GET     | Muestra histórico de préstamos   | `?usuario_id=X` (filtro opcional)|

---

### 📅 Rutas de Reservas
| **Ruta**             | **Método** | **Descripción**                  | **Parámetros**                   |
|----------------------|------------|----------------------------------|----------------------------------|
| `/reservas`          | GET        | Lista reservas pendientes        | -                                |
| `/reservas/nueva`    | POST       | Crea una nueva reserva           | `libro_id`, `usuario_id`, `fecha_reserva` |
| `/reservas/cancelar/<id>` | POST | Cancela una reserva              | `id` de la reserva               |


# 🤝 Contribuciones
- 🍴 Haz un fork del proyecto.
- 🌿 Crea una rama:git checkout -b feature/nueva-funcionalidad  

- 💬 Envía un Pull Request con una descripción clara.


# 📜 Licencia
MIT © 2024 - Libre uso y modificación.
- Créditos: Fatush🐂.
- Nequi: 3007973265 por si alguna donación.



---
                                           Diagrama caso de usos

![Imagen de WhatsApp 2025-04-09 a las 12 32 38_bfba2ae9](https://github.com/user-attachments/assets/fa621c84-f42e-43e6-aee2-f9103971f4d4)


                                            Diagrama de clases 

![Imagen de WhatsApp 2025-04-09 a las 13 04 11_d5e2c6e9](https://github.com/user-attachments/assets/5bf6dab3-23ed-4b7e-aa28-50201e07656a)
                                           



