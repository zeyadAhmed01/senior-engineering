# Feature Workflow

## Discover the product seam

Translate the requested outcome into observable acceptance criteria. Identify the user, entry point, permissions, primary path, failure path, data lifecycle, and existing neighboring behavior. Inspect current UI/API and repository conventions before choosing a component structure.

## Design the smallest complete slice

Prefer a vertical slice through real behavior over speculative layers. Reuse existing services, components, policies, schemas, and design patterns when they fit. Add an abstraction only when it owns a real invariant or removes demonstrated duplication.

For each acceptance criterion, name:

- public seam;
- state and validation;
- authorization or trust boundary;
- persistence and compatibility effect;
- loading, error, empty, and retry behavior where relevant;
- evidence that will prove it.

## Implement and verify

Build one observable slice at a time. Keep business rules outside UI/controller glue when the repository already uses that separation or reuse requires it. Test at the lowest level that does not bypass the risk, then run the real user/API boundary when practical.

Avoid unrelated polish, premature API layers, and generic frameworks that are not required by the feature.

