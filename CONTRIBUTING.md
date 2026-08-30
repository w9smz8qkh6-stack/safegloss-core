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

Start at `docs/README.md`, read `docs/CURRENT_STATE.md`, and use live Git/PR/CI
evidence for volatile status before identifying the remaining canonical
records. When a change
affects models, relations, routes, settings, services, commands,
environment-variable use, or Compose topology, refresh and commit the
source-derived references:

```bash
python scripts/generate_documentation.py
python scripts/generate_documentation.py --check
```

Do not edit `docs/generated/` by hand. CI reproduces those files and rejects
drift. Generated inventories and diagrams cover structural facts only;
contributors must still update authored architecture, workflow, security,
deployment, decision, and changelog explanations when their meaning changes.
Update `docs/CURRENT_STATE.md` only when its lifecycle, ownership, integration,
delivery, limitations, durable active-work, or next-checkpoint claims change.

## Database changes

- Generate migrations with `python manage.py makemigrations`.
- Do not edit an applied migration; add a new migration.
- Include a reversible data migration when persisted data must change.
- Verify `python manage.py makemigrations --check --dry-run` is clean.

## Security reports

Do not open a public issue for a suspected vulnerability. Follow [SECURITY.md](SECURITY.md).

## Contributor license

By submitting a contribution, you agree that it may be distributed under this repository's MIT License and that you have the right to submit it.
