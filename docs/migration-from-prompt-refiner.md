# Migration from the Existing Prompt Refiner

The installed user-level `%USERPROFILE%\.codex\skills\prompt-refiner` remains unchanged and usable as `$prompt-refiner`. Senior Engineering does not install another skill with that name.

Use `refine` when working through this plugin. It preserves the same essential contract:

- explicit invocation only;
- intent and scope preservation;
- proportional ambiguity handling;
- no prompt inflation;
- no execution of the refined task;
- output only the refined prompt.

No destructive migration is needed. Existing prompts that explicitly name `$prompt-refiner` can continue to use it. New cross-runtime documentation should prefer the plugin's namespaced `refine` skill. Remove the old skill only if the user later chooses to consolidate and has verified all callers.
