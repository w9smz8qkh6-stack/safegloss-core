# Repository guidance

SafeGloss Core is the vendor-neutral open-source glossary and exam-access application.

- Keep dissertation research, hosted billing, provider credentials, production deployment state, and customer data outside this repository.
- Use PostgreSQL for development and CI.
- Keep authorization checks server-side and cover them with tests.
- Treat Exam Mode as content restriction, not secure-browser enforcement.
- Do not add curriculum PDFs, copied webpages, assessment content, provider payloads, or real user data.
- Add migrations and tests for model changes.
- Run Django checks, migration checks, pytest, Ruff, dependency audit, and secret scanning before handoff.
