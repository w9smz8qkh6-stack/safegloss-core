# Contributing to SafeGloss Core

Thank you for helping improve transparent language support for schools.

## Before starting

- Search existing issues before opening a new one.
- For material schema, security, privacy, or product-boundary changes, open a design issue first.
- Never include real student, teacher, school, credential, or assessment data in code, fixtures, logs, screenshots, or pull requests.

## Development workflow

1. Fork the repository and create a focused branch.
2. Install `requirements-dev.txt` and use PostgreSQL.
3. Add or update tests for changed behavior.
4. Review and update the durable documentation affected by the finished change.
5. Run all commands listed under “Quality gates” in the README.
6. Open a pull request describing behavior, documentation, tests, data/schema impact, and rollback considerations.

Prefer small, cohesive changes. Avoid combining feature work with unrelated formatting or refactoring.

## Documentation completion

Documentation is part of implementation, not a later follow-up. Every change to
code, behavior, interfaces, tests, scripts, dependencies, configuration,
security, deployment, operations, architecture, or user-visible output must
include the relevant documentation updates in the same task. Follow
[`docs/development/DOCUMENTATION_MAINTENANCE.md`](docs/development/DOCUMENTATION_MAINTENANCE.md)
for the documentation map, semantic review procedure, cross-repository rule,
generated-artifact limits, and incomplete-handoff requirements.

Run `python scripts/check_documentation_updates.py` before submitting. Its
path-based result is evidence only and does not replace comparing the documents
with the finished behavior.

## Database changes

- Generate migrations with `python manage.py makemigrations`.
- Do not edit an applied migration; add a new migration.
- Include a reversible data migration when persisted data must change.
- Verify `python manage.py makemigrations --check --dry-run` is clean.

## Security reports

Do not open a public issue for a suspected vulnerability. Follow [SECURITY.md](SECURITY.md).

## Contributor license

By submitting a contribution, you agree that it may be distributed under this repository's MIT License and that you have the right to submit it.
