# SafeGloss security model

## Trust boundaries

SafeGloss assumes the hosting operator controls the server, database, domain, backups, and administrator accounts. Teachers control their courses and glossaries. Students may access only courses in which they have an active enrollment.

Every mutating browser request uses Django CSRF protection. Course and glossary views perform server-side ownership or enrollment checks; hiding a link is never treated as authorization.

## Exam Mode

Exam Mode changes the server-rendered response for enrolled students:

- unapproved terms are omitted;
- definitions and examples are omitted; and
- pronunciation links are omitted.

Teachers retain their authoring view. Manual Exam Mode may have an expiry, and scheduled windows are evaluated using server time.

Exam Mode does not:

- lock the student's device or browser;
- block other websites, files, applications, screenshots, or prior downloads;
- provide identity verification or proctoring;
- prevent a student from remembering or independently obtaining information; or
- certify compliance with a particular examination authority.

Schools must combine SafeGloss with their own assessment controls and confirm that bilingual glossary use is permitted.

## Data minimization

The public core stores account email addresses, display names, language preferences, course enrollment, and authored glossary content. It does not include behavioral telemetry, advertising analytics, payments, OAuth access tokens, employee-ID images, AI prompts, or provider payloads.

Fixtures and tests must use synthetic data. Production database and media exports must never enter the repository.
