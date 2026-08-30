# SafeGloss interface standard

- Status: canonical shared product standard
- Applies to: SafeGloss Core and shared behavior integrated into SafeGloss Commercial
- Accessibility target: WCAG 2.2 Level AA
- Review trigger: every new or materially changed user interface, workflow, or public accessibility claim

## Purpose

SafeGloss interfaces must be accessible, conventional, coherent, and fitted to
the user's task. Creativity belongs in selecting and composing the right proven
pattern, not in inventing unfamiliar controls or page behavior.

This standard governs product pages, navigation, forms, menus, dialogs,
drawers, tables, wizards, notifications, empty and error states, responsive
layouts, and complete user processes. It applies to public, authenticated,
student, teacher, staff, and operator interfaces that SafeGloss owns. A
conformance evaluation defines its exact product and version scope, including
whether documentation, administration, embedded content, and other surfaces
are included. Third-party provider pages are outside SafeGloss's control, but
the handoff to and recovery from them remain SafeGloss responsibilities.

The words **must**, **should**, and **may** express required, recommended, and
optional behavior. A justified exception must identify the user need, evidence,
accessibility consequences, owner, and reconsideration condition.

## Authority order

When rules appear to compete, use this order:

1. User safety, dignity, privacy, authorization, and successful task completion.
2. WCAG 2.2 Level A and AA success criteria and semantic HTML requirements.
3. The user story, workflow contract, and complete-process behavior.
4. This standard and the established SafeGloss tokens and components.
5. The repository's supported frontend framework and version-correct guidance.
6. WAI-ARIA Authoring Practices for a rich component that native HTML cannot
   express adequately.
7. Current, tested public-service patterns and direct user evidence.
8. A custom pattern, only when the preceding options cannot serve the task.

Native HTML is the default. ARIA supplements semantics and behavior; it does
not repair the wrong element or a missing interaction model. A framework
component is a starting implementation, not evidence that the finished use is
accessible or appropriate.

## Product principles

1. **Recognition over novelty.** Controls look and behave like their ordinary
   web equivalents. Labels describe the result rather than a branded metaphor.
2. **Task fit over component fashion.** A modal, drawer, wizard, table, card,
   disclosure, or toast is selected because its behavior fits the task.
3. **Consistency over page-local invention.** Reuse tokens, components,
   language, placement, and state behavior. New patterns require a demonstrated
   gap and become shared components when accepted.
4. **Accessibility before aesthetics.** Visual direction never overrides
   semantics, focus order, contrast, reflow, input alternatives, or user
   preferences.
5. **Progressive disclosure without concealment.** Show what users need now;
   defer secondary detail, but never hide requirements, errors, consequences,
   or the next action.
6. **Reversible where practical.** Preserve work, support Back and Cancel, and
   prefer undo or recovery over unnecessary interruption.
7. **Honest state.** Loading, saving, queued, completed, empty, failed,
   unavailable, and permission-limited states are explicit and actionable.
8. **Calm task surfaces.** Product pages prioritize hierarchy, legibility, and
   density over decorative spectacle. Brand character is strongest on public
   storytelling surfaces and quieter during focused work.
9. **Evidence resolves close calls.** When two conventional patterns remain
   plausible, prototype the smallest alternatives and test them with the
   intended users and states.

There is no single canonical web-app appearance. SafeGloss therefore uses a
canonical decision process: user need, native semantics, its own shared system,
established component behavior, and evidence before custom invention.

## Accessibility contract

### Target

All SafeGloss-owned web user interfaces and complete processes must be designed,
implemented, and maintained to conform to WCAG 2.2 Level AA. Level AA includes
all applicable Level A requirements. Accessibility is an acceptance criterion,
not a later visual-quality pass.

The default implementation expectations include:

- semantic landmarks, headings, lists, tables, buttons, links, labels, and
  field groups;
- complete keyboard operation with a logical order, visible focus, and no
  keyboard trap;
- focus that is not obscured by sticky content and returns sensibly after
  dialogs or temporary UI close;
- programmatically associated names, instructions, errors, status messages,
  and relationships;
- text contrast of at least 4.5:1 in ordinary cases, 3:1 for qualifying large
  text, and 3:1 for required non-text boundaries and state indicators;
- no reliance on color, shape, position, sound, hover, or motion alone;
- reflow and task completion at narrow CSS widths and browser zoom without
  clipped controls or two-dimensional scrolling except where the content
  genuinely requires it;
- support for text resizing, reduced motion, high-contrast or forced-color
  presentation, touch, pointer, and keyboard input;
- pointer targets that meet WCAG 2.2 Level AA sizing or spacing requirements,
  with a preferred 44-by-44 CSS-pixel comfortable target when layout permits;
- alternatives to dragging and multipoint gestures; and
- plain, specific instructions and error recovery appropriate to the user's
  language, role, and likely familiarity.

Product preferences such as larger text, contrast, or reduced animation may
improve the experience, but they must not be required to make the default
interface conformant.

### Conformance claims and statements

A policy, automated scan, code review, or accessibility statement does not by
itself prove WCAG conformance. SafeGloss may publish a full-conformance claim
only when a dated evaluation record establishes all of the following:

1. The exact product, version or commit, domains, views, states, content types,
   supported environments, and technologies relied upon are named.
2. Every WCAG 2.2 Level A and AA success criterion has been evaluated for the
   defined scope using appropriate automated and manual methods.
3. Complete processes are covered from entry through success, cancellation,
   error, and recovery; evaluating an isolated page is insufficient when it is
   one step in a process.
4. All relied-upon uses of technology are accessibility-supported in the named
   environment, and non-conforming content does not interfere with the rest of
   the page.
5. No unresolved Level A or AA failure exists within the claimed scope.
6. The report names the evaluator, method, date, limitations, assistive
   technology coverage, defects found, and remediation evidence.
7. An accountable owner approves wording that accurately reflects the report.

Use the current WCAG Evaluation Methodology (WCAG-EM) as the default structure
for defining scope, exploring the product, selecting any representative sample,
evaluating it, and reporting findings. A representative sample can support an
evaluation of a large product, but the report must still cover unique views,
components, states, content, and complete processes.

Before that gate passes, public wording must describe WCAG 2.2 AA as a **design
target** or state the accurately evaluated level of conformance. It must not say
or imply that every page is fully conformant. A published accessibility
statement must include scope, standard and level, conformance status, evaluation
method and date, known limitations, feedback and support contact, and a review
date. It must link to the underlying evaluation summary when one exists.

Any change to a claimed surface invalidates the affected portion of the claim
until proportionate regression evidence exists. Material framework, token,
navigation, shared-component, or workflow changes trigger broader review.

## Visual-system contract

### Semantic tokens

Color, typography, spacing, radius, elevation, focus, motion, and breakpoint
values must come from named shared tokens. Color tokens describe roles, not
particular hex values. At minimum the system defines:

- text, muted text, link, background, raised surface, border, and focus;
- brand primary, brand accent, and on-brand content;
- success, information, warning, danger, and their text, border, and surface
  variants; and
- interactive default, hover, active, focus, selected, disabled, and visited
  states where applicable.

Components consume semantic tokens. Templates must not introduce a new raw
color, shadow, radius, type scale, or motion duration merely to make one page
look distinctive. Brand colors are not automatically valid for every semantic
role; each pairing and state must pass its required contrast.

### Consistency is not sameness

Public marketing, product workspaces, student reading, and restricted Exam Mode
may use different density and emphasis. They must still share recognizable
typography, logo treatment, palette relationships, focus treatment, component
anatomy, language, and interaction behavior. A calm data table need not resemble
a hero section, but it must belong to the same system.

Marketing must not depict controls, states, or capabilities that the product
does not provide. A material brand-system change must update public and product
surfaces in one coordinated change or use an explicit, time-bounded migration
plan with visual-regression coverage.

## Choosing an interaction surface

| Surface | Use when | Do not use when | Required behavior |
|---|---|---|---|
| Full page | The task is primary, deep-linkable, lengthy, dense, or benefits from browser history | The user only needs a brief related decision without leaving context | Clear title, location, primary action, Back or destination, preserved data |
| Modal dialog | A brief, focused, blocking decision is directly related to the current task | Content is long, multi-step, reference-heavy, or should be linkable | Labelled dialog, inert background, contained focus, Escape and visible close/cancel, sensible focus return |
| Drawer or off-canvas panel | Secondary navigation, filters, or contextual controls benefit from preserving the underlying page | The task is primary, consequential, long, or needs a stable URL and browser history | Label, keyboard-equivalent open/close, focus management, non-motion alternative, responsive fallback |
| Popover or tooltip | Short supplementary explanation or a compact contextual action is useful | Information is essential, complex, persistent, or available only on hover | Keyboard and pointer access, dismissible behavior, no hidden required content |
| Disclosure or accordion | Optional or subordinate sections can be expanded independently | Sequential steps, errors, or the only route to essential instructions would be hidden | Button semantics, name and expanded state, preserved heading structure |
| Tabs | Peer views of the same object can switch without changing task order | The content is sequential, unrelated, or must all be compared at once | Correct tab semantics and keyboard behavior, clear selected state, stable content focus |
| Wizard | Ordered or conditional decisions become materially easier when separated and state can be preserved | A short form works as one page, or splitting creates repetitive waits and lost context | Named steps, meaningful progress, Back, save/resume where needed, validation at the useful boundary, review before consequential submit |
| Toast or transient status | Brief confirmation does not require a decision and loss of the message is harmless | The user must act, diagnose failure, or retain the information | Appropriate live-region behavior, enough reading time, persistent alternative for important outcomes |
| Banner or inline callout | Persistent page- or service-level context must remain visible | It substitutes for field errors or is repeated so often users ignore it | Specific scope, appropriate prominence, no duplicate competing announcements |

A mobile drawer does not justify using a drawer for the desktop task. A modal
must not become a miniature multi-page application. Tabs are not a stepper, and
a carousel is not ordinary navigation.

## Navigation and information architecture

- Global navigation contains durable destinations; local navigation contains
  the current object's or workflow's destinations.
- Current location is visible in words and programmatically exposed where the
  pattern supports it.
- Links navigate; buttons perform actions. A control's label names the outcome.
- The same destination or action uses the same name throughout the product.
- Navigation never depends on an icon alone. Decorative icons are hidden from
  assistive technology; meaningful icons have an accessible name.
- Menus contain coherent actions or destinations and follow the appropriate
  disclosure or menu-button keyboard model. Ordinary site navigation does not
  acquire desktop-application menu semantics merely because it drops down.
- Disabled actions are rare. When a prerequisite is unmet, explain it visibly
  and provide the next useful route instead of relying on a disabled control or
  tooltip.

## Forms and wizards

- Ask only for information required for the current outcome and explain why
  sensitive or surprising data is needed before collection.
- Labels remain visible. Placeholder text is an example or hint, never the only
  label. Required and optional status is stated consistently.
- Related controls use `fieldset` and `legend` or equivalent semantics.
- Choose controls by data shape: checkboxes for independent choices, radios for
  a small exclusive set, a select for a longer constrained set, and text entry
  only when the value cannot be selected more reliably.
- Validate as soon as feedback is useful without interrupting typing. On submit,
  show a concise error summary linked to each invalid field and a specific
  inline error without discarding valid answers.
- Preserve entered data across validation, Back, authentication handoff, and
  recoverable failure.
- Start with one coherent decision per step. Combine tightly related, easy
  questions; split when dependencies, cognitive load, privacy explanation, or
  error recovery materially improve. Step count alone is not a reason to split.
- Browser Back must remain safe and meaningful. Users can revisit prior answers
  without repeating unaffected later steps.
- Use a review step before a consequential or difficult-to-reverse submission.
  The final button names the actual commitment rather than “Submit.”
- Prevent duplicate submission and make queued or asynchronous work explicit.

## Feedback, failure, and performance

Every asynchronous or stateful feature defines loading, empty, success, partial,
error, unavailable, permission-limited, and disabled behavior where applicable.

- A response to an ordinary action should be perceptible immediately. If work
  continues, show what is happening, whether the user may leave, and how to
  return to the result.
- Prefer a stable skeleton or reserved layout space over disruptive movement.
- Do not use an indeterminate spinner when meaningful progress or steps are
  available. Do not invent precise percentages without a real measure.
- Errors say what happened in user terms, what remains safe, and the next
  action. Preserve work and provide retry when safe.
- Empty states distinguish “nothing exists,” “no result matches,” “not yet
  available,” and “not permitted,” and provide an appropriate next step.
- Success is confirmed at the point where the user needs confidence. Important
  results remain available after a transient announcement disappears.
- Performance budgets and browser evidence govern heavy assets and layout
  stability. Animation must not conceal latency or block input.

## Destructive and consequential actions

Safeguards are proportional to consequence:

1. For low-risk reversible actions, act directly and offer Undo when practical.
2. For material but recoverable actions, explain the effect and recovery path
   in context or in a focused confirmation.
3. For irreversible, high-impact, broad, or privacy-sensitive actions, use a
   dedicated confirmation step that names the object, scope, consequences, and
   alternatives. Require typed confirmation only for exceptional risk where it
   measurably prevents the likely error.

The safe action is the default focus when confirmation appears. Destructive
actions are visually distinct but never communicated by color alone. Cancel
leaves state unchanged. Server-side authorization, idempotency, transaction
boundaries, and audit behavior remain required; a confirmation dialog is not a
security control.

## Responsive and inclusive behavior

- Design content order and semantics before arranging columns.
- Verify phone, tablet, desktop, narrow reflow, landscape, and long-content
  states. Critical actions remain reachable without hover or precision.
- Responsive changes may alter layout but must not remove the only label,
  instruction, status, or action.
- Tables preserve header relationships and gain an intentional small-screen
  strategy. Horizontal scrolling is acceptable for genuine two-dimensional
  data when the scroll region is discoverable and keyboard accessible.
- Text expansion, translation, long names, and localized number/date formats
  must not break controls or hide content.
- Motion is functional, brief, and optional. Respect system and product
  reduced-motion preferences.

## Component governance

1. Search the existing token and component inventory before creating anything.
2. Record the user story, required states, responsive behavior, semantics,
   keyboard model, content constraints, and accessibility acceptance criteria.
3. Use native HTML or an established repository component.
4. If a new component is necessary, implement all required states once and add
   a representative fixture or gallery example.
5. Document any intentional deviation from an established pattern.
6. Do not merge page-local CSS or JavaScript that silently creates a second
   version of an existing component.

Shared components must have named owners or a clear repository home. Retire or
migrate obsolete variants rather than keeping multiple accidental standards.

## Verification and release evidence

For every material UI change, collect proportionate evidence for:

- successful task completion and nearby failure/recovery branches;
- automated accessibility checks at meaningful rendered states;
- keyboard-only operation, visible focus, focus order, and dialog or menu focus
  management;
- semantics, names, descriptions, errors, and live status announcements;
- text and non-text contrast across default, hover, focus, active, selected,
  disabled, danger, and high-contrast states;
- phone, tablet, desktop, narrow reflow, 200% text sizing, and 400% browser zoom
  or equivalent 320-CSS-pixel reflow;
- reduced motion and forced-color or high-contrast behavior;
- touch target and pointer alternatives;
- loading, empty, success, error, permission, and destructive states; and
- regression comparison for shared tokens, components, and neighboring flows.

Automated tools are useful gates for detectable failures, not conformance
oracles. Manual and assistive-technology evaluation remains required. Involve
people with disabilities in significant workflow evaluation when practical,
and record what was and was not tested.

## Screenshot evidence exchange

The automated-testing and interface-design workstreams share visual evidence
without sharing authority:

- the testing workstream owns reproducible scenario execution, deterministic
  data, browser capture, artifact storage, metadata, comparison mechanics, and
  the functional pass or failure of the tested workflow;
- the interface-design workstream owns visual interpretation, comparison with
  this standard and approved references, design findings, severity, proposed
  corrections, and any resulting token, component, or interaction decision;
  and
- neither workstream treats an image-only judgment as evidence for source
  correctness, authorization, DOM semantics, accessible names, focus order,
  keyboard behavior, announcements, or complete WCAG conformance.

### Minimum screenshot artifact contract

Every screenshot offered for design analysis must be traceable to:

- a stable scenario and step or state identifier;
- product and repository commit or build identifier;
- Core or Commercial scope, route, user role or persona, and fixture identity
  that contains no real personal data;
- browser and version, operating system or rendering platform, viewport width
  and height, device-pixel ratio, zoom or text-size condition, theme or contrast
  mode, locale, and reduced-motion state;
- the intended state, such as initial, loading, empty, validation error,
  permission failure, partial, success, destructive confirmation, or recovery;
- capture time, expected result, actual workflow result, and any masked or
  intentionally unstable region; and
- links to the related DOM/accessibility snapshot, automated check results,
  trace, console/network evidence, or reference image when those artifacts
  exist.

Dynamic data must be deterministic or explicitly masked. Masking must not hide
the layout, status, content-length, overflow, focus, contrast, or error behavior
being evaluated. Images containing customer, student, credential, provider, or
production data are not valid design-review artifacts.

### Capture selection

Do not capture every transition merely because automation can. Capture the
smallest set that represents the user's visual experience and the design risks:

- entry and stable success;
- each materially distinct loading, empty, partial, error, permission, or
  recovery state;
- destructive or consequential review and confirmation;
- phone, tablet, desktop, and narrow-reflow layouts where the composition
  changes;
- long text, translated text, long names, dense data, and other overflow-prone
  fixtures; and
- before, approved reference, and after states for an intentional design
  change.

A functional test can pass while its screenshot exposes weak hierarchy,
clipping, visual drift, misleading state, poor density, or a missing next
action. Conversely, a pixel difference is not automatically a defect; expected
content, rendering, or responsive differences must be interpreted against the
user story and standard.

### Design-analysis output

Each material visual finding records:

1. screenshot artifact and scenario/state identifiers;
2. viewport, role, locale, and other relevant capture conditions;
3. direct observation, kept separate from inference and product judgment;
4. affected standard rule, token, component, workflow, or approved reference;
5. impact on task clarity, consistency, responsiveness, accessibility, state
   completeness, content, interaction, performance stability, or regression
   risk;
6. severity, affected scope, recommended smallest correction, and owner; and
7. whether the test workstream needs a new state, fixture, viewport, metadata
   field, or regression assertion.

Accepted design findings feed requirements back to the testing workstream. The
testing workstream then preserves the relevant screenshot or structural
assertion as regression evidence. This loop turns screenshots into durable
design evidence rather than an unreviewed image archive.

## Change checklist

A change is ready only when the reviewer can answer yes to the applicable
questions:

- Does the chosen pattern fit the user story better than the conventional
  alternatives?
- Does it reuse the shared visual and interaction system?
- Are all meaningful states and complete-process branches represented?
- Does it meet the accessibility contract with recorded evidence?
- Is the action reversible or proportionately safeguarded?
- Does it remain understandable and operable responsively and with assistive
  technology?
- Are public descriptions and screenshots truthful to the product?
- Have affected standards, component references, workflows, tests, and
  accessibility evaluation records been updated?

## External references

- [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/)
- [WCAG Evaluation Methodology (WCAG-EM) 2.0](https://www.w3.org/TR/wcag-em-2/)
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [W3C guidance for accessibility statements](https://www.w3.org/WAI/planning/statements/)
- [GOV.UK Design System patterns](https://design-system.service.gov.uk/patterns/)

These references inform the standard. WCAG is normative for the stated
conformance target; the other references are implementation and evaluation
guidance and do not replace task-specific evidence.
