# Memoria técnica — BusTrack ML

> Registro vivo. No se borra historial. Última actualización: 2026-10-30.

## 1. Estado real

- **Repositorio:** `bustrack-ml-main` (raíz interior; el árbol está anidado `X-main/X-main`).
- **Tecnología actual:** Python 3.11, FastAPI, scikit-learn, pandas/numpy/scipy, joblib (esqueleto sin código).
- **Tecnología objetivo:** Python 3.11 + FastAPI + scikit-learn para detección de paradas y patrones de movimiento.
- **Git:** no hay repositorio Git local; los tags/releases no son verificables.

## 2. Funcionalidades implementadas

- Estructura src/{api,core,data,models,pipelines} (solo .gitkeep).
- requirements.txt con FastAPI, scikit-learn, pandas, numpy, scipy, joblib y pytest.
- Gobernanza Python/ML en constitution, AGENTS, Memoria y CHECKLIST.

## 3. Funcionalidades pendientes

- Todo el código del servicio: app FastAPI, endpoints internos, modelos y pipelines.
- Procesamiento y anonimización de acelerómetro.
- Entrenamiento, evaluación, versionado y predicción.
- Pruebas unitarias, de integración, de modelo y de seguridad.
- Dockerfile, CI bloqueante y despliegue Azure.

## 4. Arquitectura actual

src/{api,core,data,models,pipelines}; suites UnitTest, IntegrationTest, ModelTest, SecurityTest

## 5. Migraciones

No aplica una migración de stack en este repositorio.

## 6. Decisiones arquitectónicas

- Se adopta SDD y DevSecOps.
- La API central es la fuente autorizada de datos.
- Cosmos DB for NoSQL es la persistencia objetivo.
- ML y GenAI son servicios internos FastAPI.
- OpenAI API es el proveedor GenAI objetivo; Google GenAI queda inactivo.
- Flutter + Dart y Angular + TypeScript son los objetivos de cliente.
- No se declaran recursos Azure desplegados.

## 7. Dependencias entre repositorios

API central -> ML por HTTP interno; ML devuelve clasificaciones y características.

## 8. Problemas conocidos

- Documentación previa desalineada con el código (corregida en esta reorganización).
- Specs históricas conservadas como referencia; ver `specs/README.md`.
- Gates CI/SAST incompletos o no bloqueantes en el estado previo.
- Deuda de pruebas y despliegue documentada en cada spec.

## 9. Historial

- **2026-10-29:** estructura SDD original y primeras fases.
- **2026-10-30:** auditoría completa, corrección documental y reorganización SDD.
  Se separan specs históricas de canónicas, se corrigen afirmaciones de stack y se
  documentan migraciones, contratos y Azure propuesto.
