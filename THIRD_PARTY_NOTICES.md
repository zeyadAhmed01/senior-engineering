# Third-Party Notices and Provenance

Senior Engineering is an original synthesis. It studies patterns from the projects below but does not combine or vendor their repositories. Where an idea influenced the design, the implementation was written anew for this project's architecture and vocabulary. This release supports OpenAI Codex only; a cited source repository name records research provenance and does not imply runtime compatibility or support.

## MIT-licensed sources studied

| Project | Pinned commit | Copyright/license noted at pin | Use in this project |
| --- | --- | --- | --- |
| `owainlewis/blueprint` | `54c952bad7dea5d40fa7951b4bd831008b567a6b` | MIT, Owain Lewis (2026) | Conceptual influence: small lifecycle, outcome/constraints/proof, independent review |
| `obra/superpowers` | `5bf4e78011075bcfc0dc295f0724994cd123ee71` | MIT, Jesse Vincent (2025) | Conceptual influence: root-cause debugging, fresh verification, pressure testing |
| `affaan-m/ECC` | `bf70150eb2df8070024e5bdf08e4aa08959e2735` | MIT, Affaan Mustafa (2026) | Conceptual influence: context budgets, iterative retrieval, specialist boundaries |
| `levnikolaevich/claude-code-skills` | `d7da390b0d4af4dba9ea2daf5c94ece06bfa14b0` | MIT, Lev Nikolaevich (2026) | Conceptual influence: mutation boundaries and evidence states |
| `kevinlin/skills` | `951dbf8f4a8ffd58036d75d47e47ca12b691c7c3` | MIT, Kevin Lin (2026) | Conceptual influence: research-plan-implement and intentional compaction |
| `msitarzewski/agency-agents` | `053ddbbf392a1688fc7043d81529f47ef2cf86c8` | MIT, AgentLand Contributors (2025) | Conceptual influence: explicit role contracts and minimal change |
| `github/awesome-copilot` | `db8d563aefebf9dd569bc72596c4ebd817847534` | MIT, GitHub, Inc. | Conceptual influence: GitHub workflow and secret-aware delivery |
| `github/github-mcp-server` | `85598ba6e1256f7ebf4867b95d63b833c4549264` | MIT, GitHub (2025) | Official GitHub capability and read-only-mode research |
| `richkuo/rk-skills` | `369cab825d81416a5a51fbdf3d774ed2fa02d23b` | MIT, Richard Kuo (2026) | Conceptual influence: claim-level validation and review reconciliation |
| `Leonxlnx/taste-skill` | `c184364c58658b2f131b4ae8bd3d206cabb3deee` | MIT, Leonxlnx (2026) | Selective visual-quality reference only; no skill text or assets copied |
| `nextlevelbuilder/ui-ux-pro-max-skill` | `dcc40ff5133ef78276117db0cc34e7b83cc8aeba` | MIT root license, Next Level Builder (2024) | Search and design-system concepts only; indexed data and assets were not copied |

No third-party source files or data corpora are vendored. No substantial verbatim text or code from these repositories is included. A root license does not establish the rights for every embedded record or asset; exact-file and exact-revision provenance must be checked before future reuse.

## Source without a located license

`thatjuan/agent-skills` was studied at commit `1a22763c98f0a37cd7dda121d48a0f5451771a28`. No root license or license notice was found in the inspected repository paths at that commit. It was used for high-level comparison only. No text or code was copied or adapted from it.

## Existing local prompt refiner

The installed user-level `%USERPROFILE%\.codex\skills\prompt-refiner` was inspected as prior local work. Senior Engineering preserves it unchanged. The new `refine` skill independently carries forward the local behavioral requirements—explicit invocation, intent preservation, ambiguity discipline, anti-inflation, and no execution—under a non-conflicting name.

## Official documentation

Codex plugin structure and current commands were checked against official OpenAI documentation. GitHub workflow and tooling guidance was checked against official GitHub documentation. Documentation describes interfaces and is not incorporated as third-party source code.
