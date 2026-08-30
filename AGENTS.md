# Repository guidance

SafeGloss Core is the vendor-neutral open-source glossary and exam-access application.

- Keep dissertation research, hosted billing, provider credentials, production deployment state, and customer data outside this repository.
- Use PostgreSQL for development and CI.
- Keep authorization checks server-side and cover them with tests.
- Treat Exam Mode as content restriction, not secure-browser enforcement.
- Do not add curriculum PDFs, copied webpages, assessment content, provider payloads, or real user data.
- Add migrations and tests for model changes.
- Treat documentation as part of completion for every change to source code,
  behavior, interfaces, tests, scripts, dependencies, configuration, security,
  deployment, operations, architecture, or user-visible output. Follow
  `docs/development/DOCUMENTATION_MAINTENANCE.md` and update every affected
  durable record in the same task.
- Compare explanatory documentation semantically with the finished
  implementation. Generated freshness and path checks are evidence only.
- Complete related documentation changes in Hosted or another canonical
  SafeGloss repository in the same task. If accurate documentation cannot be
  updated, report the task incomplete with the exact repository, document,
  missing fact, and blocker.
- Run Django checks, migration checks, pytest, Ruff, dependency audit, and secret scanning before handoff.
- Run `python scripts/check_documentation_updates.py` before handoff.
- Run `python scripts/generate_documentation.py` after changing models, routes,
  settings, services, commands, environment-variable use, or Compose topology.
  Commit every resulting `docs/generated/` change and run the same command with
  `--check` before handoff. Generated files are source-derived facts and must
  never be edited by hand.
- Start every repository orientation at `docs/README.md`, then read
  `docs/CURRENT_STATE.md` before detailed architecture or implementation work.
  Verify volatile branch, pull-request, CI, and environment facts live. Keep
  the reading order, current-state summary, authored system, workflow, and
  authorization documents, generated references, public/Commercial boundary,
  and decision records semantically aligned. Automation does not replace the
  required human explanation of intent, invariants, limitations, security, or
  operational consequences.
- Read `docs/product/ROADMAP.md` for Core product-planning work. Broad or
  potentially private SafeGloss ideas are captured first in Commercial's
  private strategy system; copy an initiative into Core only after its complete
  public, vendor-neutral scope and disclosure boundary are reviewed. Never add
  Commercial, provider, customer, research, analytics, billing, or private
  operational context to make the public roadmap more complete. A proposal is
  not a roadmap commitment.
- Update `docs/CURRENT_STATE.md` when product maturity, supported runtime or
  database posture, repository ownership, Core/Commercial boundaries, delivery
  or deployment posture, important limitations, durable active work, or the
  next integration checkpoint materially changes. Do not churn it when its
  claims remain accurate.
- Update the public roadmap when an approved Core initiative changes horizon,
  outcome, dependencies, success signal, or delivery status. Keep shared work
  Core-first and update Commercial's private strategy record separately.
- Run `python scripts/check_strategy_records.py` after every public roadmap
  edit.
- After checks pass, commit task-owned changes and push the current branch to
  its existing configured upstream at a cohesive green checkpoint and task
  completion. Verify branch, remote, divergence, diff, and secret safety;
  never force-push, rewrite history, bypass branch protection, or include
  unrelated work. Core has no production deployment target; integrate reviewed
  Core changes into Hosted through the documented downstream flow.
- Core `main` requires a scoped task branch and pull request. Wait for all
  required checks and merge only when repository gates pass and no required
  human approval remains; administrator bypass is not part of the cadence.
