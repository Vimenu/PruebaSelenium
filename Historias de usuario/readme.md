# Historias de Usuario

## Historia 1: Ingreso a la página de Amazon

**Como** usuario,  
**quiero** abrir la página principal de Amazon,  
**para** comenzar el proceso de navegación y búsqueda de productos.

- **Criterios de aceptación:**
  - El navegador debe abrir correctamente la página de Amazon.
  - Se debe tomar una captura de pantalla inicial (`01_inicio.png`).
- **Criterios de rechazo:**
  - Si la página no carga o no se toma la captura, la prueba debe fallar.

---

## Historia 2: Búsqueda de productos

**Como** usuario,  
**quiero** ingresar un término de búsqueda en la barra,  
**para** encontrar productos relacionados con mis intereses.

- **Criterios de aceptación:**
  - Se debe ingresar el texto "wireless headphones" y ejecutar la búsqueda.
  - Se debe capturar la pantalla de los resultados (`02_busqueda.png`).
- **Criterios de rechazo:**
  - Si no se encuentra la barra o no carga la página de resultados, la prueba debe fallar.

---

## Historia 3: Aplicación de filtro de envío gratis

**Como** usuario,  
**quiero** aplicar el filtro "Free Shipping by Amazon",  
**para** visualizar únicamente productos que no cobren envío.

- **Criterios de aceptación:**
  - Si el filtro está disponible, debe aplicarse correctamente.
  - Se debe capturar la pantalla del resultado filtrado (`03_filtro_envio_gratis.png`).
- **Criterios de rechazo:**
  - Si el filtro no está disponible, la prueba continúa sin fallar, pero se notifica en consola.

---

## Historia 4: Selección y acceso al producto

**Como** usuario,  
**quiero** hacer clic en uno de los productos listados,  
**para** ver más detalles del mismo.

- **Criterios de aceptación:**
  - Se debe hacer clic en el primer producto de la lista.
  - La página del producto debe abrirse en una nueva pestaña.
  - Se debe tomar una captura (`04_producto_seleccionado.png`).
- **Criterios de rechazo:**
  - Si no se encuentran productos, la prueba debe fallar.

---

## Historia 5: Visualización de información del producto

**Como** usuario,  
**quiero** ver el nombre, precio y calificación de un producto,  
**para** evaluar si cumple con mis expectativas.

- **Criterios de aceptación:**
  - Se debe extraer el título, el precio y la calificación.
  - Se debe capturar la pantalla final (`05_info_producto.png`).
- **Criterios de rechazo:**
  - Si no se puede extraer alguna información, se guarda captura de error y la prueba falla.
