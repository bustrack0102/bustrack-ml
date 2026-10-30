# Memoria técnica — BusTrack Machine Learning

> Registro de experimentos, decisiones de modelado, métricas de desempeño y deuda técnica del servicio de Machine Learning.

---

## 📌 Fase ML-00 — Inicialización y Estructura SDD (2026-10-29)

- **Estado:** Estructura base Spec-Driven Development (SDD) creada para el servicio de Machine Learning en Python.
- **Decisión 1 (Tecnología):** Adopción de Python + FastAPI para la capa de servicio y scikit-learn / scipy para los pipelines de preprocesamiento y detección de paradas por acelerómetro.
- **Decisión 2 (Flujo de Acelerómetro):** La detección operará por lotes de lecturas enviadas por la app móvil. Se clasificarán eventos de desaceleración y reposo para generar "paradas candidatas".
- **Decisión 3 (Validación de Modelos):** Se establece la suite `ModelTest/` para certificar que ningún modelo se integre a la rama principal si no supera las métricas de prueba mínimas.
- **Deuda Técnica Documentada:** Recolección de datos reales de prueba y calibración de umbrales cinemáticos a definirse una vez se inicien las pruebas de campo.
