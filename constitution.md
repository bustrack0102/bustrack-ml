# Constitución — BusTrack ML

> Fuente de verdad del repositorio. Versión 2.0.0 (2026-10-30). Todo cambio de arquitectura
> exige spec y registro en `Memoria.md`.

## 1. Propósito

BusTrack ML forma parte del ecosistema BusTrack. Servicio de Machine Learning tiene como responsabilidad:
API central -> ML por HTTP interno; ML devuelve clasificaciones y características.

## 2. Responsabilidades

- Mantener una responsabilidad delimitada dentro de BusTrack.
- Consumir o exponer contratos HTTP documentados.
- No duplicar datos ni lógica que pertenecen a otro servicio.
- Aplicar SDD: toda funcionalidad nace de un spec aprobado.

## 3. Arquitectura y tecnologías

- **Actual:** Python 3.11, FastAPI, scikit-learn, pandas/numpy/scipy, joblib (esqueleto sin código).
- **Objetivo:** Python 3.11 + FastAPI + scikit-learn para detección de paradas y patrones de movimiento.
- Cambiar la tecnología objetivo requiere autorización explícita y un spec de migración.

- El servicio ML no expone endpoints públicos; solo es consumido por la API.
- Procesa lotes de acelerómetro anonimizados y con consentimiento.
- No inventa paradas ni rutas: clasifica patrones sobre datos recibidos.
- Los modelos se versionan y evalúan con métricas reproducibles.
- No hay rastreo GPS ni identificación de usuarios.

## 4. Principios de diseño

- Separación de responsabilidades y dependencias dirigidas al dominio.
- Contratos explícitos, validados y versionados.
- Configuración por entorno y cero secretos en el repositorio.
- Real-first: no se declara implementado lo que no existe en código o pruebas.
- `Memoria.md` refleja el estado real, no el deseado.

## 5. Seguridad

Validación Pydantic, anonimización, límites de tamaño, sin secretos y sin pickle de origen no confiable.

- Prohibido registrar tokens, contraseñas, claves o PII.
- Los secretos viven en variables de entorno o Azure Key Vault.
- Toda entrada externa se valida y toda salida se codifica.

## 6. Calidad y pruebas

- pytest, pytest-cov, pruebas de modelo (F1/precisión/recall), contrato y seguridad.
- Sin pruebas y evidencia de ejecución no hay terminado.
- Los gates de CI para lint, pruebas y SAST son bloqueantes.
- Los tests triviales no cuentan como cobertura.

## 7. Convenciones

- Código e identificadores en inglés; documentación y mensajes de usuario en español.
- Formato y lint según el stack objetivo.
- PR pequeños y trazables a un spec.
- Prohibido `TODO` sin issue asociado.

## 8. Restricciones

- No rastreo GPS continuo de usuarios ni unidades.
- No acceso directo de clientes a Cosmos DB.
- No invención de rutas, horarios, tarifas, empresas o destinos por parte de IA.
- No recolección de sensores sin consentimiento explícito.
- No se declaran recursos Azure desplegados.

## 9. Integración con BusTrack

- Contratos transversales: `docs/contratos-integracion.md`.
- La API central es la fuente autorizada de datos de transporte.
- ML y GenAI son servicios internos.

## 10. Gobernanza

- Obligatorios: este documento, `AGENTS.md`, `Memoria.md`, `CHECKLIST_PR.md` y `specs/`.
- Las decisiones no resueltas se registran como pendientes; no se inventan respuestas.
