# ADR-0003: Publish only reviewed Core roadmap projections

- Status: Accepted
- Date: 2026-08-30

## Context

SafeGloss-wide planning can include private Commercial, provider, customer,
research, billing, analytics, and operational context that cannot enter the
public Core repository. Core still benefits from a transparent view of
reviewed public direction, and future contributors need to distinguish
proposals from actual maintainer priorities.

## Decision

Core maintains `docs/product/ROADMAP.md` as a filtered public roadmap. It uses
Now, Next, Later, and Exploring horizons without implying delivery dates.

An initiative is copied into Core only after its complete public scope,
vendor-neutral ownership, self-hosting implications, privacy/data boundary,
dependencies, and success or learning signal are reviewed. Commercial-only
context is omitted rather than paraphrased. Shared work follows Core-first
delivery and receives public Core specifications before downstream
integration.

The private Commercial strategy system remains the authoritative SafeGloss-wide
idea register and prioritization record. Public issues and contributions may
propose additions but do not become roadmap commitments without explicit
maintainer approval.

Repository guidance and CI keep the public roadmap linked from Core's
orientation chain.

## Consequences

- Contributors can see genuine public direction without exposing private
  strategy or creating accidental commitments.
- Core and Commercial roadmap views can differ deliberately.
- Promotion requires human disclosure and ownership judgment.
- Empty horizons are preferable to invented work or leaked private context.

## Reconsider when

Reconsider when SafeGloss adopts a public planning system that can enforce the
same disclosure boundary, outcome/horizon semantics, and Core-first ownership
rules without duplicating or leaking the private source of truth.
