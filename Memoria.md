# Memoria técnica — BusTrack ML

> Registro vivo. No se borra historial. Última actualización: 2026-11-11.

## 1. Estado real

- **Repositorio:** `bustrack0102/bustrack-ml`
- **Tecnología actual:** Python 3.11+, FastAPI, Pydantic v2, NumPy, scikit-learn, pytest, Docker.
- **Tecnología objetivo:** Python 3.11 + FastAPI + scikit-learn para detección de paradas y anomalías de movimiento.
- **Git:** conectado a `https://github.com/bustrack0102/bustrack-ml.git` en rama `main`.

## 2. Funcionalidades implementadas

- Estructura completa `src/{api,core,data,models,pipelines}` implementada y operativa:
  - `src/main.py`: Aplicación FastAPI, middleware `X-Correlation-ID` y manejadores de errores uniformes (`422`, `500`).
  - `src/core/{config.py,schemas.py,security.py}`: Validación Pydantic v2 de muestras inerciales (`accelX/Y/Z` finitos, consentimiento explícito obligatorio) y autenticación interna (`X-Internal-Key` / `Bearer`).
  - `src/data/anonymizer.py`: Anonimización determinista SHA-256 sin PII ni rastreo GPS.
  - `src/pipelines/signal_pipeline.py`: Ordenamiento cronológico, ventaneo deslizante reproducible y extracción estadística (magnitud RMS, pico, desviación estándar y cruces por cero).
  - `src/models/classifier.py`: Clasificador versionado (`1.0.0`) para detección de baches severos, vibración moderada, paradas y vía óptima.
  - `src/api/routes.py`: Endpoints `GET /health` (`14-endpoint-health`) y `POST /inference` (`15-endpoint-inference`) con límite de lote (`413`).
- Suites de pruebas reales: `UnitTest/test_unit.py`, `IntegrationTest/test_integration.py`, `ModelTest/test_model.py`, `SecurityTest/test_security.py`.
- `Dockerfile` multietapa con usuario no-root (`appuser`) y `HEALTHCHECK` (`spec-13`).

## 3. Funcionalidades pendientes

- Entrenamiento supervisado continuo sobre dataset de campo etiquetado de la región Tula-Tepeji (`spec-07`/`spec-08`).
- Despliegue del contenedor en Azure Container Instances cuando se habilite instancia dedicada.

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
- **2026-11-11:** implementación del servicio FastAPI (`GET /health`, `POST /inference`), anonimizador SHA-256 sin PII, pipeline de ventaneo y extracción de características, clasificador versionado `1.0.0`, `Dockerfile`, 16 pruebas reales (`UnitTest`, `IntegrationTest`, `ModelTest`, `SecurityTest`) y reparación integral de SDD (`check_sdd.ps1`, `docs/endpoints.md`, bloques de aprobación y `checklists/`).
- **2026-11-11 (Etapa 0 — v0.2.0 SemVer y CD ACR):** agregada matriz `docs/versionamiento.md` y `.github/workflows/cd-azure.yml` para construir/publicar imagen real en `bustrackacr0102` (evitando crear ACI adicional previo a Container Apps). Verificado local: `pytest -q` (16/16), `check_sdd.ps1` (`SDD-OK`).
