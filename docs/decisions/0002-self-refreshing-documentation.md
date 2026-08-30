# ADR-0002: Maintain authored and source-generated documentation together

- Status: Accepted
- Date: 2026-08-30

## Context

Product orientation existed, but a reader could not recover current routes,
model relationships, configuration names, service boundaries, or Compose
topology without scanning source. Authored diagrams also risked drifting when
structural configuration changed. Fully generated prose would have the opposite
problem: source structure cannot explain product intent, security limitations,
tradeoffs, or operational judgment.

## Decision

SafeGloss Core maintains two complementary documentation layers:

1. Canonical authored documents explain product scope, workflows,
   architecture, authorization, security, deployment, decisions, and
   limitations.
2. `scripts/generate_documentation.py` deterministically extracts installed
   apps, model fields/relations, namespaced routes, service declarations,
   management commands, environment-variable names/source locations, and
   Compose services/dependencies into committed Markdown, Mermaid, and manifest
   files under `docs/generated/`.

Generated files are never hand-edited. CI reproduces them with `--check`,
validates documentation links/ownership markers, and rejects drift. The normal
contributor/agent workflow regenerates them after relevant source changes and
still performs semantic review of authored documents.

The generator uses only Python's standard library and static repository input.
It never imports Django, reads environment values, contacts a provider, or
inspects live data. Generated topology is repository-configuration evidence,
not live-state or health evidence.

## Consequences

- Structural references and diagrams change with their source declarations.
- Readers can form a dependable architectural model before opening source.
- Pull requests expose exact structural drift and require explanatory prose
  when meaning changes.
- Generated pages can be large and describe declarations rather than runtime
  behavior, database contents, or hidden dynamic registration.
- Generator behavior itself is reviewed, formatted, versioned, and recorded in
  the manifest.
- Live deployment facts remain an operator verification responsibility.

## Reconsider when

Reconsider the static extractor when the repository adopts dynamic model/route
registration that it cannot represent, when a supported documentation platform
can consume a safer authoritative schema directly, or when generated output
becomes too large to remain useful. Preserve deterministic, secret-free,
offline generation and the authored/generated authority boundary in any
replacement.
