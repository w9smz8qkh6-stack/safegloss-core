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
4. Run all commands listed under “Quality gates” in the README.
5. Open a pull request describing behavior, tests, data/schema impact, and rollback considerations.

Prefer small, cohesive changes. Avoid combining feature work with unrelated formatting or refactoring.

## Database changes

- Generate migrations with `python manage.py makemigrations`.
- Do not edit an applied migration; add a new migration.
- Include a reversible data migration when persisted data must change.
- Verify `python manage.py makemigrations --check --dry-run` is clean.

## Security reports

Do not open a public issue for a suspected vulnerability. Follow [SECURITY.md](SECURITY.md).

## Contributor license

By submitting a contribution, you agree that it may be distributed under this repository's MIT License and that you have the right to submit it.
