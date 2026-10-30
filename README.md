# BusTrack · Machine Learning — Spec-Driven ML Service

> Servicio de Detección de Patrones de Movimiento y Paradas — **Universidad Tecnológica de Tula-Tepeji**
> Desarrollado con **Spec-Driven Development (SDD)** y asegurado bajo prácticas de **DevSecOps** desde el día uno.

---

## 👥 Equipo de Desarrollo (BusTrack)
* **Fátima Ximena García González**
* **Diego Parra Cruz**
* **José De Jesús López Islas**
* **Melanie Joliee Bonilla Domínguez**

---

## 📋 Resumen del Repositorio
Este repositorio contiene el microservicio de **Machine Learning** de BusTrack (desarrollado en Python con FastAPI y scikit-learn). Se encarga de procesar los lotes de datos recopilados por los sensores de acelerómetro de la aplicación móvil (con consentimiento del usuario), extraer características cinemáticas (aceleraciones, desaceleraciones, tiempos de reposo) y clasificar patrones para **identificar paradas candidatas** y validar secuencias de recorrido.

* **Metodología:** Spec-Driven Development (SDD) basada en especificaciones en `/specs`.
* **Seguridad y DevSecOps:** Validación de esquemas de datos, anonimización de lecturas de sensores, SAST con Semgrep, pruebas de modelo y CI con GitHub Actions.
* **Integración:** Se comunica con la API principal (`bustrack-api`) mediante llamadas HTTP internas protegidas.

---

## 🏛️ Componentes de Gobernanza y SDD

| Componente | Ruta | Propósito |
|---|---|---|
| **Constitución (Fuente de verdad)** | `constitution.md` (espejo en `.specify/memory/constitution.md`) | Principios no negociables del pipeline de ML y directrices de ingeniería |
| **Manual operativo para Agentes** | `AGENTS.md` | Lineamientos para agentes de IA que desarrollen modelos y pipelines |
| **Especificaciones (Specs)** | `specs/` | Historias de ML desglosadas (`000-base-ml`, `001-preprocessing`, `002-detection-model`, etc.) |
| **Plantillas SDD** | `.specify/templates/` (y `specs/_template.md`) | Plantillas oficiales para nuevas especificaciones de ML |
| **Agentes y Habilidades IA** | `.opencode/agents/` y `.opencode/skills/` | Configuración de agentes OpenCode / WARP |
| **Seguridad SAST** | `.semgrep/semgrep.yaml` | Reglas de análisis estático para Python |
| **Checklist de PR** | `CHECKLIST_PR.md` | Comprobación obligatoria de calidad, métricas de modelo y seguridad antes de cada PR |
| **Memoria técnica** | `Memoria.md` | Historial de experimentos, métricas de desempeño (F1, precisión, recall) y decisiones |

---

## 🧪 Estructura del Código y Pruebas

```text
bustrack-ml/
├── src/
│   ├── api/          # Endpoints FastAPI para inferencia y salud del servicio
│   ├── core/         # Configuraciones, seguridad y constantes
│   ├── data/         # Ingesta, limpieza y normalización de acelerómetro
│   ├── models/       # Clasificadores y algoritmos de clustering/detección
│   └── pipelines/    # Pipelines de preprocesamiento e inferencia por lotes
├── UnitTest/         # Pruebas unitarias de preprocesadores y matemáticas
├── IntegrationTest/  # Pruebas de integración de la API FastAPI
├── ModelTest/        # Validación de umbrales de precisión, recall y estabilidad
└── SecurityTest/     # Validación de sanitización de inputs y autenticación interna
```

---

## 🚀 Integración Continua (CI)
El workflow `.github/workflows/ci-pr.yml` valida formateo (`black`), estilo (`flake8`), seguridad (`semgrep`), cobertura de pruebas (`pytest`) y consistencia de especificaciones SDD en cada Pull Request.
