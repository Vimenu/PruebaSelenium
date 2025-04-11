# Historias de Usuario – Proyecto Selenium Amazon

## Historia 1: Buscar un producto

**Como** usuario de Amazon,  
**quiero** poder escribir el nombre de un producto en el buscador,  
**para** ver los resultados relacionados con mi búsqueda.

-  Criterios de aceptación:
  - Se debe mostrar una lista de productos relacionados.
-  Criterios de rechazo:
  - No se debe ejecutar búsqueda si el campo está vacío.

---

## Historia 2: Aplicar filtro de envío gratis

**Como** usuario,  
**quiero** aplicar un filtro de envío gratis,  
**para** reducir los resultados a los productos que no me cobren envío.

-  Criterios de aceptación:
  - Al activar el filtro, los resultados deben actualizarse correctamente.
-  Criterios de rechazo:
  - No debe aplicar si el filtro no está disponible.

---

## Historia 3: Ver detalles de un producto

**Como** usuario,  
**quiero** acceder a los detalles de un producto al hacer clic,  
**para** conocer su descripción, precio y calificación.

-  Criterios de aceptación:
  - La página del producto debe mostrar toda la información detallada.
-  Criterios de rechazo:
  - Si no se carga correctamente la página del producto, se debe notificar.

---

## Historia 4: Captura de cada paso del proceso

**Como** tester,  
**quiero** que se tomen capturas automáticas en cada paso del proceso,  
**para** documentar los escenarios de prueba de forma visual.

-  Criterios de aceptación:
  - Cada paso debe guardar una imagen con nombre descriptivo.
-  Criterios de rechazo:
  - Si no hay capturas, no se considera válida la prueba.

---

## Historia 5: Reporte de resultados

**Como** desarrollador QA,  
**quiero** que las pruebas generen un reporte HTML,  
**para** presentar los resultados de manera clara y profesional.

-  Criterios de aceptación:
  - El archivo HTML debe mostrar si la prueba pasó o falló.
-  Criterios de rechazo:
  - Si el reporte está vacío o no se genera, se considera incompleto.
