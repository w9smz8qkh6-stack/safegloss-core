# Security policy

## Supported versions

Security updates are provided for the latest tagged release and the current `main` branch while the project is in alpha.

## Reporting a vulnerability

Use GitHub's private vulnerability reporting feature for this repository. Do not include exploit details, credentials, personal information, or student data in a public issue.

Include:

- affected version or commit;
- deployment assumptions;
- reproduction steps using synthetic data;
- likely impact; and
- any suggested mitigation.

Maintainers will acknowledge a complete report as soon as practical, coordinate remediation, and publish an advisory when users need to act.

## Secrets

SafeGloss does not require provider credentials in its public core. Production secrets must be supplied by the deployment environment. Never place secrets in source files, Docker images, fixtures, screenshots, logs, issue comments, or CI artifacts.

If a secret is committed, revoke or rotate it immediately. Removing the current file is not sufficient because the value remains in git history.

## Exam Mode

Exam Mode is application-level content restriction, not a secure kiosk or proctoring system. Its threat model and limitations are documented in [docs/development/SECURITY_MODEL.md](docs/development/SECURITY_MODEL.md).
