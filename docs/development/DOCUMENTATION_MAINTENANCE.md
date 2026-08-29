# Documentation maintenance

Documentation is part of the SafeGloss Core definition of done. Every task that
changes source code, behavior, interfaces, tests, scripts, dependencies,
configuration, security, deployment, operations, architecture, or
user-visible output must review and update the relevant durable documentation
in that same task. Contributors do not wait for a separate documentation
request.

## Documentation map

Identify the records that govern the changed area before editing:

- `README.md` for public scope, features, setup, supported environments, data
  formats, and primary quality gates;
- `CONTRIBUTING.md` and `AGENTS.md` for contributor and agent workflow;
- `.env.example` and `docs/development/DEPLOYMENT.md` for configuration and
  operator setup;
- `SECURITY.md` and `docs/development/SECURITY_MODEL.md` for security, privacy,
  trust boundaries, and Exam Mode limitations;
- public UI help and documented CSV or other interfaces for user-visible
  contracts;
- `docs/decisions/` for durable architectural and repository-boundary
  decisions; and
- `CHANGELOG.md`, plus any active project-state, capability, or workstream
  record added later, for externally meaningful changes and current status.

## Completion procedure

1. Inspect the finished implementation, tests, configuration, and observed
   behavior, then compare every governing document by meaning rather than by
   timestamp, filename, or keyword.
2. Update affected setup instructions, architecture, operational runbooks,
   public contracts and data formats, security and privacy guidance, user
   documentation, and changelog entries.
3. Update project-state, capability, workstream, and decision records whenever
   their claims or status change. Add or amend an ADR for a durable
   architectural decision.
4. If repository-owned tooling can safely regenerate facts, schemas,
   inventories, or indexes, use it and review the generated diff. Passing
   freshness, generation, link, or path checks is evidence only; it does not
   prove that explanatory documentation is accurate.
5. Run the documentation handoff check and all affected repository quality
   gates. Report changed documents and verification results explicitly.

Run `python scripts/check_documentation_updates.py` locally. CI runs the same
diff-based check. It fails when implementation paths change without a durable
documentation path, but semantic completeness remains the contributor's and
reviewer's responsibility.

## Cross-repository and incomplete work

Core is the public, vendor-neutral upstream of the private SafeGloss Hosted
application. When a Core change affects Hosted integration, deployment,
operations, architecture, or user-facing behavior, update Hosted's canonical
documentation in the original task. The converse applies when Hosted work
changes a public Core contract. Keep repository edits and verification
separate and report the Core-to-Hosted integration order.

If an affected repository is unavailable, overlapping work prevents a safe
edit, or a required fact cannot be verified, the task is incomplete. Name the
repository, exact missing or inaccurate document, unresolved fact, and blocker
in the handoff.

Documentation completion is a prerequisite for Core's standing delivery
cadence. After relevant checks pass, commit task-owned changes and push the
current branch to its existing configured upstream at a cohesive green
checkpoint and task completion. Local edits, commits, pushes, and Hosted
integration remain distinct checked steps. Never include unrelated dirty work,
force-push, rewrite history, bypass branch protection, expose secrets, or
proceed past failed checks. Core itself has no production deployment target;
reviewed Core changes reach production only through the documented Hosted
integration flow.
