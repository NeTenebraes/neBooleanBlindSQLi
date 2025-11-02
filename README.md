# blind-boolean-sqli-python
Herramienta básica en Python para automatizar pruebas de Boolean Blind SQLi en parámetros GET.  

Este proyecto se usó específicamente para explicar la máquina **IMF** de VulnHub, ayudando a entender y practicar este tipo de vulnerabilidad.

## Aviso Legal y Uso Ético

Esta herramienta fue desarrollada exclusivamente con fines educativos y para realizar pruebas de penetración sobre sistemas para los cuales se cuenta con autorización expresa del propietario.

El mal uso de esta herramienta para comprometer/atacar/probar sistemas sin permiso es ilegal y está penado por la ley.

El autor no se hace responsable por el uso indebido de este software.

Se recomienda usar esta herramienta únicamente en entornos controlados, como laboratorios propios o máquinas de práctica (por ejemplo, VulnHub IMF).

---

## Descripción

Este script envía peticiones HTTP modificando parámetros con payloads booleanos para detectar vulnerabilidades de tipo Boolean Blind SQL Injection.  
El objetivo es identificar si el parámetro es vulnerable observando diferencias en la respuesta según condiciones verdaderas o falsas inyectadas.

Perfecto para quienes inician en auditoría web y quieren practicar pruebas manuales automatizadas con Python.

---

## Características

- Automatiza la prueba de payloads booleanos simples para detección rápida.
- Permite evaluar respuestas para inferir vulnerabilidades.
- Base para extender con extracción de datos por inyección.
- Fácil de entender y modificar para principiantes en Python.

---

## Requisitos

- Python 3.x
- Librería `requests` (`pip install requests`)

---

## Uso básico


El script hará pruebas con payloads booleanos para detectar vulnerabilidades.

---

## Licencia

Este proyecto está licenciado bajo la **MIT License**.  
Consulta el archivo `LICENSE` para más detalles.

---

## Contribuciones

Si quieres mejorar o extender este proyecto, ¡eres bienvenido!  
Por favor, mantén el propósito ético y responsable del uso.

---

## Contacto

Puedes abrir issues o contactarme para dudas o sugerencias.

