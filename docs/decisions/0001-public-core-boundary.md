# ADR-0001: Establish a separate public SafeGloss core

- Status: Accepted
- Date: 2026-08-14

## Context

The hosted SafeGloss codebase combined glossary management with a legacy reading application, dissertation instrumentation, commercial billing, behavioral analytics, provider integrations, and Render-specific operations. Those concerns created a large migration graph and made safe publication difficult.

The hosted product now presents its primary purpose as multilingual glossary accommodation and restricted glossary access during exams.

## Decision

SafeGloss Core is a new, vendor-neutral Django application with clean history and clean initial migrations. Its first boundary includes:

- accounts and teacher/student roles;
- languages and subjects;
- courses, rosters, enrollment, and join codes;
- multilingual glossaries, terms, and translations;
- Study Mode and Exam Mode; and
- CSV and print delivery.

The first public release excludes:

- dissertation experiments and research exports;
- stories, lessons, quizzes, and reading telemetry;
- subscriptions, payments, coupons, and commercial entitlements;
- PostHog, Sentry, and hosted operational configuration;
- Google Classroom, Clever, OneRoster, LTI, and other provider integrations;
- gamification and blog features; and
- curriculum PDFs, copied source material, and catalogs without verified redistribution terms.

Provider integrations may later return as optional Django apps with independent security and maintenance ownership.

## Consequences

- The public schema is intentionally not migration-compatible with the hosted monolith.
- Hosted deployments need an explicit export/import bridge or a private downstream overlay.
- Core development and tests require no paid provider account.
- Features enter the public core only when they fit its mission, have a sustainable maintenance owner, and meet privacy and licensing requirements.
