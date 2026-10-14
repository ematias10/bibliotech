# 📚 Guía de Diseño: Sistema de Gestión de Biblioteca

## 1. Introducción
- **Proyecto:** Aplicación web de Biblioteca (Ejemplo Académico).
- **Stack Tecnológico:** Django (Backend/Templates) + Bootstrap 5 (Frontend).
- **Objetivo:** Definir una interfaz limpia, accesible y fácil de implementar para estudiantes. El diseño debe transmitir tranquilidad, conocimiento y orden, facilitando tanto la búsqueda de libros por parte de los usuarios como la gestión por parte de los bibliotecarios.

---

## 2. Identidad y Tono
- **Concepto Visual:** "Moderno Clásico". Combinaremos tipografías tradicionales para encabezados (evocando la lectura y los libros) con una interfaz limpia y sin distracciones.
- **Tono de Comunicación:** Claro, educativo, respetuoso y directo.
- **Público Objetivo:** Usuarios de todas las edades (lectores) y personal administrativo.

---

## 3. Paleta de Colores (Adaptación Bootstrap)
Aprovecharemos las variables semánticas de Bootstrap, pero sugerimos personalizarlas (sobrescribiendo variables SCSS o usando CSS customizado) con los siguientes tonos:

### Colores Principales (Brand)
- **Primary (`$primary`):** `#1E3A8A` (Azul Noche) - Transmite confianza, academia y seriedad. Uso: Navbar principal, botones de acción clave ("Buscar", "Prestar").
- **Secondary (`$secondary`):** `#D97706` (Ámbar Oscuro / Ocre) - Evoca el color del papel antiguo o marcapáginas. Uso: Detalles, botones secundarios, iconos destacados.
- **Accent/Info (`$info`):** `#0891B2` (Cian Muted) - Para enlaces o tags de categorías/géneros literarios.

### Colores de Estado y Fondos
- **Background (`body-bg`):** `#F8FAFC` (Blanco Humo) - Más suave para los ojos que un blanco puro, ideal para leer listados de libros.
- **Surface (`card-bg`):** `#FFFFFF` (Blanco) - Para tarjetas de libros y modales.
- **Success (`$success`):** `#16A34A` - Verde para "Libro Disponible" o acciones exitosas.
- **Danger (`$danger`):** `#DC2626` - Rojo para "Libro Prestado/No Disponible" o borrar registros.

---

## 4. Tipografía
Recomendamos importar estas fuentes desde Google Fonts para darle personalidad al proyecto base de Bootstrap.

- **Títulos y Encabezados (Serif):** `Merriweather` o `Lora`.
  - *Propósito:* Le da el toque "literario" a la aplicación.
  - *Uso:* Clases `h1` a `h6`, títulos de libros en las tarjetas, nombre de la aplicación.
- **Cuerpo de Texto y UI (Sans-serif):** `Inter` o la fuente por defecto de Bootstrap (System UI).
  - *Propósito:* Máxima legibilidad en pantallas pequeñas, tablas de datos y formularios.
  - *Uso:* Párrafos, menús, botones, inputs.

---

## 5. Espaciado y Layout (Bootstrap Grid)
- **Contenedores:** 
  - Usar `.container` para las vistas principales (Catálogo, Perfil) para mantener un ancho máximo legible.
  - Usar `.container-fluid` para el panel de administración (Dashboard) para aprovechar el espacio en tablas grandes.
- **Grid de Catálogo:** Para mostrar libros, usar el sistema de columnas de Bootstrap:
  - Móviles: `.col-12` (1 libro por fila).
  - Tablets: `.col-md-6` (2 libros por fila).
  - Desktop: `.col-lg-3` o `.col-lg-4` (3-4 libros por fila).
- **Espaciado:** Utilizar las clases utilitarias de Bootstrap (`mt-4`, `p-3`, `gap-3`) para mantener la consistencia sin escribir CSS extra.

---

## 6. Componentes UI Base (Implementación en Bootstrap)

### 📖 Tarjetas de Libros (Cards)
El componente central del catálogo. Debe usar la clase `.card` de Bootstrap con un estilo limpio:
- **Estructura:** `.card.h-100` (para alturas iguales en el grid) + `.shadow-sm`.
- **Imagen:** `.card-img-top` con un `object-fit: cover; height: 250px;` para que todas las portadas se alineen perfectamente aunque tengan distintos tamaños originales.
- **Cuerpo (`.card-body`):** Título del libro (Serif), Nombre del autor en texto secundario (`.text-muted`), y un "Badge" (`.badge`) indicando la disponibilidad.
- **Footer (`.card-footer`):** Fondo blanco o transparente con un botón `.btn.btn-primary.w-100` para "Ver Detalles" o "Solicitar".

### 📝 Formularios y Filtros
Usar las clases nativas de Bootstrap para formularios limpios.
- Barra de búsqueda prominente en el header o hero section (`.form-control-lg`).
- Formularios de agregar/editar libros (Django ModelForms): Usar el paquete `django-crispy-forms` o `django-widget-tweaks` para renderizar automáticamente las clases `.form-control` y `.form-label` de Bootstrap.

### 📋 Tablas (Panel Admin)
Para el listado de préstamos y gestión de inventario:
- Clases recomendadas: `.table`, `.table-hover` (para seguir el cursor), y `.table-striped` (facilita la lectura de muchos registros).

### 🔔 Notificaciones (Django Messages)
Mapear el framework de mensajes de Django a las alertas de Bootstrap:
- `messages.success` -> `.alert.alert-success.alert-dismissible`
- `messages.error` -> `.alert.alert-danger.alert-dismissible`

---

## 7. Iconografía
- **Librería sugerida:** **Bootstrap Icons** (fácil integración web font o SVG).
- **Casos de uso:** 
  - `bi-book` o `bi-journal-bookmark` para el logo.
  - `bi-search` en la barra de búsqueda.
  - `bi-person-circle` para el perfil de usuario/bibliotecario.
  - `bi-pencil` y `bi-trash` para acciones en las tablas del CRUD.

---

## 8. Consideraciones para Estudiantes (Django + Bootstrap)
- **Herencia de Templates:** Tener un `base.html` donde se carga el CDN de Bootstrap, el Navbar y el Footer. El resto de las vistas (`catalogo.html`, `detalle_libro.html`) solo deben sobreescribir el block `{% block content %}`.
- **Archivos Estáticos:** Mantener el CSS personalizado al mínimo (idealmente solo para cambiar la tipografía o pequeños ajustes) en `static/css/styles.css`. Fomentar el uso de clases utilitarias de Bootstrap para resolver problemas de diseño.