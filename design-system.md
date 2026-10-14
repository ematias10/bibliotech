# 🎨 Guía de Diseño: [Nombre del Proyecto]

## 1. Introducción
- **Proyecto:** [Nombre del proyecto o plataforma]
- **Versión:** [1.0.0]
- **Objetivo:** Definir los lineamientos visuales, la jerarquía y los componentes base para mantener la consistencia en el desarrollo del frontend.

---

## 2. Identidad de Marca y Tono
- **Logotipo:** [Ruta del asset, ej: `/public/logo.svg`]
- **Variaciones de Logo:** Usar versión blanca sobre fondos oscuros, versión a color sobre fondos claros.
- **Tono de Comunicación:** [Ej: Profesional, directo, técnico pero amigable].

---

## 3. Paleta de Colores
Definición de los colores base de la aplicación. *(Idealmente mapeados a variables CSS o la configuración de tu framework de CSS)*.

### Colores Principales (Brand)
- **Primary:** `#HEX` - Uso en botones de acción principal (CTA), enlaces y estados activos.
- **Secondary:** `#HEX` - Elementos de apoyo, fondos destacados o botones secundarios.
- **Accent:** `#HEX` - Detalles visuales, insignias (badges) o elementos que requieran atención.

### Colores Semánticos (Estados)
- **Success:** `#HEX` - Mensajes de éxito, confirmaciones (Ej: `bg-green-500`).
- **Warning:** `#HEX` - Advertencias, acciones que requieren cuidado.
- **Danger/Error:** `#HEX` - Borrado de datos, errores de formulario.
- **Info:** `#HEX` - Mensajes informativos neutrales.

### Escala de Grises y Fondos (Neutrales)
- **Background Base:** `#HEX` - Fondo principal del sitio (`body`).
- **Surface/Cards:** `#HEX` - Fondo para contenedores, modales y tarjetas.
- **Text Primary:** `#HEX` - Títulos y texto principal (Ej: `text-gray-900`).
- **Text Secondary:** `#HEX` - Texto de apoyo, placeholders y descripciones (Ej: `text-gray-500`).
- **Borders:** `#HEX` - Separadores y bordes de inputs.

---

## 4. Tipografía
- **Fuente Principal (Sans-serif):** [Ej: Inter, Roboto, Montserrat]
- **Fuente Secundaria / Monospace:** [Ej: Fira Code, JetBrains Mono - *Solo para fragmentos de código o IDs*]

### Jerarquía y Escala
- **H1 (Título de página):** `4rem` (48px) | `font-bold` | `leading-tight`
- **H2 (Subtítulos de sección):** `3rem` (36px) | `font-semibold`
- **H3 (Títulos de tarjetas):** `2rem` (24px) | `font-medium`
- **Body (Texto base):** `1.6rem` (16px) | `font-normal` | `leading-relaxed`
- **Small (Texto de apoyo/Metadatos):** `1.4rem` (14px) | `text-gray-500`

---

## 5. Espaciado y Layout (Grid)
- **Sistema de espaciado:** Basado en una escala de `4px / 8px` (Ej: `0.5rem`, `1rem`, `2rem`).
- **Contenedor Principal:** Ancho máximo de `1280px` (Ej: `max-w-7xl` con `mx-auto`).

### Breakpoints (Responsive)
- **Mobile (sm):** `640px` (Diseño por defecto - Mobile First).
- **Tablet (md):** `768px`.
- **Desktop (lg):** `1024px`.
- **Large Desktop (xl):** `1280px`.

---

## 6. Iconografía e Imágenes
- **Librería de Iconos:** [Ej: Lucide Icons, Heroicons, Material Symbols].
- **Estilo de Iconos:** [Ej: Outline (línea), `stroke-width: 2`, tamaño estándar `24x24px`].
- **Imágenes:**
  - Bordes redondeados en todas las imágenes de contenido (`rounded-lg`).
  - Las imágenes decorativas deben usar un overlay negro al 30% si llevan texto encima.

---

## 7. Componentes UI Base
*(Directrices para estilizar los componentes atómicos o modificar librerías de UI)*

- **Botones (Buttons):**
  - *Primary:* Fondo `primary`, texto blanco, sin borde, redondeado suave (`rounded-md`).
  - *Outline:* Borde sólido `primary`, fondo transparente, texto `primary`.
  - *Ghost:* Sin fondo, sin borde, color `primary` al hacer hover.
  - *Estados:* Todos los botones deben tener un cambio visual en `:hover` y `:disabled` (opacidad 50% y cursor `not-allowed`).

- **Tarjetas (Cards):**
  - Fondo `surface`, padding interno de `24px` (`p-6`), borde sutil (`border-gray-200`) y sombra base (`shadow-sm`).
  
- **Formularios (Inputs):**
  - Altura mínima `40px`, borde gris, label en negrita por encima del input.
  - **Focus:** Anillo de enfoque (`focus:ring-2`) usando el color `primary` con opacidad.

---

## 8. Accesibilidad (a11y)
- Contraste de texto mínimo comprobado (AA - 4.5:1).
- Todo elemento interactivo (enlaces, botones, inputs) debe tener un estado `:focus-visible`.
- Atributos `aria-label` obligatorios en botones que solo contengan iconos.
- Uso de etiquetas semánticas (`<header>`, `<main>`, `<article>`, `<nav>`).

---

## 9. Recursos y Enlaces
- **Figma / Penpot / Mockups:** [Enlace al diseño visual]
- **Directorio de Assets:** [Ej: `/assets/images/`]
- **Librerías Externas UI:** [Ej: Tailwind CSS, PrimeVue]