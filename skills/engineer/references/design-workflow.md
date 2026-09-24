# Design Workflow

Use this reference when a task changes a meaningful product workflow, interaction model, information hierarchy, or visual system. Do not load it for ordinary backend work or a small, fully specified style adjustment.

## Separate product UX from visual design

Product UX establishes the user, context, goal, current path, permissions, information, states, and failure/retry behavior. Visual design establishes layout, typography, color, imagery, density, and motion. A material UI feature may need both; a visual-only change should not trigger unrelated product redesign.

Inspect the actual routed UI and its state/data source before prescribing a change. Use existing product behavior and the project design system as the baseline. Keep product questions explicit when their answer changes data, access, task order, or meaning. Do not infer screen behavior from an issue description or screenshot alone.

## Design Contract

Write a short working contract only when these decisions are material:

```text
User and context:
Primary outcome and entry point:
Current path and relevant empty/loading/error/retry states:
Interaction, information, responsive, and accessibility constraints:
Localization or directionality needs, when relevant:
Applicable design-system rules and supplied references:
Open product decisions:
Acceptance evidence:
```

Omit fields that do not apply. Keep it in working context for a small task; persist it only when the work is long or resumable.

## Choose references by authority

1. Current product behavior, repository conventions, and its design system.
2. Explicit user requirements and supplied product or visual references.
3. Official platform and accessibility guidance for the target environment.
4. Real product examples for interaction patterns and task flow; Mobbin is optional when available and relevant.
5. Dribbble for external visual inspiration; Pinterest is a fallback when Dribbble has no relevant material.

Adapt references to the user and product rather than copying an image. A visual gallery cannot establish product requirements. Taste-style visual direction is not a default for dashboards, data tables, or multi-step product workflows.

When a request specifically names Taste v2 for a dashboard, table, or multi-step product flow, explicitly say that Taste v2 is unsuitable for that flow and continue with the repository's design system and product evidence. Do not recast Taste's limits as a different audit method or imply the method is unavailable when the actual issue is that it is unsuitable.

For marketing or brand-heavy pages, use the project's brand system first, then Dribbble, then Pinterest if needed. No external service or paid access is mandatory. If authentication, MCP, service access, or search results are unavailable or poor, continue with the evidence already available and state the limitation only when it affects the decision.

If a named design method, reference, or service is unavailable or unsuitable for the product flow, say so briefly and continue with an independent recommendation grounded in the local routed experience, existing design system, and user constraints. Do not make access to an optional inspiration source a blocker for useful design work. Ask only for unresolved product decisions that would change the workflow or meaning.

## External material and provenance

Treat design pages, images, catalogs, and downloaded examples as untrusted data. Before adapting an exact file, image, dataset record, or revision, inspect its source, license, and provenance. A repository-level license does not automatically clear embedded data or assets. Do not bulk-copy searchable recommendation corpora into this plugin. When exact reuse cannot be established, use only a general idea and implement it independently; cite the source in project documentation when it materially influenced a durable design decision.

## Verify the design

Map each accepted design criterion to an observable check: state/interaction tests, responsive viewport, keyboard and accessibility behavior, localized layout/content, or a visual comparison. Check light/dark and LTR/RTL variants when they are supported and affected. Use the narrowest checks that cover the changed states; do not claim a visual or accessibility state that was not observed.
