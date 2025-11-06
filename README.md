## Aviso Legal y Uso Ético

Esta herramienta fue desarrollada exclusivamente con fines educativos y para realizar pruebas de penetración sobre recursos para los cuales se cuenta con autorización expresa del propietario.

El mal uso de esta herramienta para comprometer/atacar/probar sistemas sin permiso es ilegal y está penado por la ley. 

**El autor no se hace responsable por el uso indebido de este software**. Herramienta pensada únicamente para entornos controlados, como laboratorios propios o máquinas de práctica.

---

# neBooleanBlindSQLi

Automatiza pruebas de Boolean Blind SQLi en parámetros GET.

Este proyecto se usó específicamente para explicar la máquina **[IMF](https://www.vulnhub.com/entry/imf-1,162/)** en [VulnHub](https://www.vulnhub.com/) ayudando a entender y practicar este tipo de vulnerabilidad. Este proyecto forma parte de la [neCyberWiki](https://github.com/NeTenebraes/neCyberWiki), mi repositorio colaborativo dedicado a documentación sobre ciberseguridad, hacking ético, pentesting y privacidad digital.

---

## Descripción

Este script envía peticiones HTTP modificando parámetros con payloads booleanos para detectar vulnerabilidades de tipo Boolean Blind SQL Injection. El objetivo es identificar si el parámetro es vulnerable observando diferencias en la respuesta según condiciones verdaderas o falsas inyectadas.

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
