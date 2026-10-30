# CHECKLIST_PR.md — BusTrack Machine Learning

> Constitución §3. 1 revisor obligatorio. Rama `main` protegida.

- [ ] Spec en `specs/` aprobada y enlazada (sin cambios de interfaz sin spec previa).
- [ ] Linter y formato limpio (`flake8`, `black --check`).
- [ ] Pruebas unitarias (`UnitTest/`) en verde.
- [ ] Pruebas de integración (`IntegrationTest/`) en verde.
- [ ] Pruebas de modelo (`ModelTest/`) con métricas por encima del umbral mínimo.
- [ ] Pruebas de seguridad (`SecurityTest/`) en verde.
- [ ] Semgrep SAST sin vulnerabilidades altas ni críticas.
- [ ] Sin archivos binarios pesados (`.pkl`, `.h5`, `.joblib`) en el commit.
- [ ] `Memoria.md` actualizada con métricas y decisiones técnicas.
- [ ] Sin secretos, tokens ni variables de entorno sensibles en el diff.
- [ ] Revisor asignado: ___________________  Fecha: ___________________
