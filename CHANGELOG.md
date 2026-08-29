# Changelog

All notable changes to SafeGloss Core will be recorded here.

The project follows semantic versioning after the first stable release. During alpha, minor releases may contain schema or interface changes documented in release notes.

## Unreleased

### Changed

- Made documentation review and updates part of completion for every implementation,
  behavior, interface, test, script, dependency, configuration, security, deployment,
  operations, architecture, and user-visible change.
- Added a lightweight documentation handoff check. It verifies that implementation
  diffs include a durable documentation path while leaving semantic accuracy to the
  required implementation-to-document comparison.
- Established a standing cadence to commit and push task-owned, verified Core changes
  at cohesive green checkpoints and task completion. Production delivery remains a
  separate reviewed Core-to-Hosted integration step.
- Clarified that protected `main` changes use scoped task branches, pull requests, and
  required checks; administrator bypass is not part of the standing cadence.

## 0.1.0 - 2026-08-15

### Added

- Clean public-core Django application.
- Email-based teacher and student accounts.
- Courses, rosters, enrollment, and join codes.
- Multilingual glossary, term, and translation models.
- Study Mode, manual Exam Mode, and scheduled Exam Mode.
- CSV import/export and print-friendly student views.
- Public contributor, security, support, and architecture documentation.
