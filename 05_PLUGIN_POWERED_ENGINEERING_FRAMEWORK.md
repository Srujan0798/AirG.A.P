# 05 — Plugin-Powered Engineering Framework: Evaluation of the 30-Skill Collection

**Source:** Founder-provided image titled “Top 30 Claude Code Plugins,” attributed to Charlie Hills, with GitHub stars stated as read on 23 October 2026.  
**Purpose:** Evaluate these tools as development accelerators in Phase II and identify which underlying capabilities may be rebuilt as product components.  
**Important:** The image is a point-in-time curation, not an official ranking, quality audit, security review or guarantee of current compatibility.

---

## 1. Governing decision

Do not install all 30 tools into every environment. Do not make the product dependent on third-party skill prompts.

Use a three-part classification:

1. **Research accelerators:** used in the connected research environment only.
2. **Developer workflow tools:** used by the founder/engineering agents while building the product.
3. **Product capabilities:** behaviour that the product itself implements for customers. Reimplement or integrate only after checking technical fit, license, provenance, security and offline behaviour.

A single project may use a tool in more than one class, but each use requires a separate decision.

## 2. The 30 items from the supplied image

The “purpose” descriptions below preserve the intent shown in the supplied graphic. Repositories are linked where the upstream identity could be verified during this research. Where exact provenance is not verified, treat the name as a label from the image and resolve the canonical repository before installation.

### A. Code like a senior

| # | Image label | Role indicated by image / likely use | Phase II disposition | Cautions |
|---:|---|---|---|---|
| 1 | Superpowers | Planning, testing, debugging and verification-oriented development workflow. | **Trial as a core candidate.** | Its workflow may overlap with other process frameworks. Inspect hooks, instructions and command permissions. [Upstream](https://github.com/obra/superpowers). |
| 2 | Matt Pocock Skills | TypeScript/JavaScript engineering and type-system guidance. | **Selective.** Useful if TypeScript is in the chosen stack. | Confirm canonical upstream, authorship, license and whether it's a mirror/repackaging. |
| 3 | ECC (Everything Claude Code) | Collection of skills, agents, hooks, rules, security and memory optimizations. | **Selective toolbox, not blanket install.** | Large surface area and overlap; review individual skills and hooks. Official project identity commonly referenced as [affaan-m/ECC](https://github.com/affaan-m/ECC). |
| 4 | Karpathy Skills | Coding habits emphasizing clear thinking, simple code and deliberate verification. | **Optional.** | The skills are third-party distillations of public material, not skills authored or endorsed by Andrej Karpathy unless primary evidence says otherwise. Example repository found: [benfngu/karpathy-claude-skills](https://github.com/benfngu/karpathy-claude-skills). |
| 5 | Ponytail | Minimize unnecessary code while retaining tests and essential security/data-loss handling. | **Trial as an alternative to other coding-discipline skills.** | Avoid stacking duplicate “write less code” rules. [Upstream](https://github.com/DietrichGebert/ponytail). |
| 6 | Agent Skills | General skill packaging/format, including Anthropic's public skills repository. | **Use the format selectively; not necessarily a runtime plugin.** | A skill is instructions/scripts; it may still invoke tools or execute code. [Anthropic skills](https://github.com/anthropics/skills). |

### B. Research and understanding

| # | Image label | Role indicated by image / likely use | Phase II disposition | Cautions |
|---:|---|---|---|---|
| 7 | REA | Reverse engineering of app behaviour, web apps, Electron/.NET/native binaries with evidence. | **Specialist optional.** Useful only for authorized interoperability/research. | Legal rights, license terms and anti-circumvention rules matter. Never use it to copy proprietary internals. [Upstream](https://github.com/Eng-RSMY/REA). |
| 8 | Graphify | Convert source code, docs, papers and schemas into queryable knowledge graphs. | **High-priority trial.** | Validate edge provenance and update correctness; inferred edges are not facts. [Upstream](https://github.com/Graphify-Labs/graphify). |
| 9 | Agent Reach | Extend agent research access to public repositories, discussions, videos and selected platforms. | **Research only by default.** | Some channels need login/API credentials and may be experimental. Not for sensitive customer data or offline product runtime. [Upstream](https://github.com/Panniantong/Agent-Reach). |
| 10 | Understand Anything | Multi-agent codebase analysis and interactive code/knowledge graph. | **Compare with Graphify; choose one for MVP.** | Overlaps with Graphify. Check current canonical upstream; a repository found is [arnoldwender/understand-anything](https://github.com/arnoldwender/understand-anything). |
| 11 | Career Ops | Job-post scoring and CV matching. | **Not core to this product.** | Could be useful for the founder's separate career workflow, not the air-gap platform. |
| 12 | Last 30 Days | Recency-focused research over current online sources and communities. | **High-priority Phase I research trial.** | Discovery signal only; verify claims against papers, official docs and source repositories. Online/authenticated data sources create data-handling concerns. [Upstream](https://github.com/mvanhorn/last30days-skill). |

### C. Big projects, fewer tokens

| # | Image label | Role indicated by image / likely use | Phase II disposition | Cautions |
|---:|---|---|---|---|
| 13 | gstack | Virtual product/engineering team: product thinking, architecture, review, QA and release. | **Trial selectively.** | May overlap with Superpowers and other process tools. Browser/release hooks and external-review dependencies need review. [Upstream](https://github.com/garrytan/gstack). |
| 14 | Caveman | Shorter replies/context, fewer tokens. | **Low-priority experiment.** | Compression may discard constraints and evidence. Benchmark output quality, not token savings alone. Confirm exact canonical repo. |
| 15 | Claude-Mem | Persistent context across sessions with retrieval and compression. | **Optional after privacy review.** | Check what it stores, where it stores it, encryption, retention, secret filtering, telemetry and model dependency. [Upstream](https://github.com/thedotmack/claude-mem). |
| 16 | Headroom | File/context reduction before model reads. | **Optional.** | Confirm exact repo and compression behaviour. Never use it as the only source of truth for requirements/security policies. |
| 17 | GSD (Get Shit Done) | Lightweight meta-prompting, context engineering and spec-driven development. | **Choose instead of BMAD if a lighter process fits.** | It overlaps with other planning frameworks. Pin version and test actual task outcomes. [Upstream](https://github.com/gsd-open/get-shit-done-redux). |
| 18 | BMAD Method | Agile AI-driven product and software delivery from discovery/planning to build/verification. | **Choose instead of GSD for structured product/architecture work.** | Do not run both as simultaneous process owners. Check stable versus preview release. [Upstream](https://github.com/bmad-code-org/BMAD-METHOD). |

### D. Design and visuals

| # | Image label | Role indicated by image / likely use | Phase II disposition | Cautions |
|---:|---|---|---|---|
| 19 | UI UX Pro Max | UI/UX design system, responsive interface and visual style guidance. | **Optional when building admin UI.** | Frontend helper, not an infrastructure differentiator. [Upstream](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill). |
| 20 | Taste | Extract design decisions/tokens and critique visual design. | **Optional; compare with Impeccable/UI UX Pro Max.** | May rely on website/browser inspection; keep it outside sensitive customer environment. |
| 21 | Archify | Convert ideas, code and architecture into interactive diagrams. | **Useful for documentation.** | Validate diagram edges against source; diagram is not automatically a formal architecture model. [Upstream](https://github.com/RiantRedwood/Archify). |
| 22 | Impeccable | Interface audit, critique, accessibility and visual refinement. | **Optional; choose one UI skill.** | Review scripts/hooks and any optional network behaviour. [Upstream](https://github.com/pbakaus/impeccable). |
| 23 | PPT Master | Build/edit presentation decks. | **Useful for investor/customer material, not core engineering.** | Confirm exact upstream, license and whether output is genuinely editable. |
| 24 | Diagram Design | Generate clear architecture and editorial diagrams. | **Useful for handoff/docs.** | Confirm exact repository and ensure diagrams stay source-backed. |

### E. Writing and video

| # | Image label | Role indicated by image / likely use | Phase II disposition | Cautions |
|---:|---|---|---|---|
| 25 | Skills | Anthropic's document and productivity skills (Word, Excel, PowerPoint, PDF in image). | **Useful for project documentation and business artifacts.** | Skills/scripts may process files; review dependencies and permissions. [Upstream](https://github.com/anthropics/skills). |
| 26 | OpenMontage | AI video studio and video content workflow. | **Not core.** | Could support demos/marketing later; inspect its media and network requirements. |
| 27 | HyperFrames | Turn HTML/web scenes into video. | **Not core.** | Useful only if demo-video creation becomes a requirement. |
| 28 | Humanizer | Rewrite text to sound less generic/AI-like. | **Optional for marketing copy only.** | Do not use it to alter technical evidence, legal claims or source quotations. |
| 29 | I Have ADHD | Organize tasks/answer-first workflow and focus. | **Personal productivity only.** | Not part of product architecture. |
| 30 | Marketing Skills | Copywriting, SEO and conversion-oriented content. | **Useful later for go-to-market experiments.** | Marketing claims must remain consistent with measured product capabilities. |

---

## 3. Recommended minimal set by purpose

### Phase I — independent research

| Rank | Tool | Use | Limitation |
|---:|---|---|---|
| 1 | Last 30 Days | Find current conversations, release signals, practitioner pain and new research references. | Social signals are not technical proof. |
| 2 | Agent Reach | Access relevant public platforms, GitHub, discussion and video material. | Channel access may need credentials; some channels are experimental. |
| 3 | Graphify | Organize papers, repositories and docs into a navigable relationship graph. | Inferred edges need human verification. |

The full independent research protocol must still run without these tools.

### Phase II — product development

Start with the smallest set that covers the development process:

1. **Superpowers** — structured development, TDD, debugging and review. Trial first.
2. **BMAD or GSD** — choose one as the planning/specification system. BMAD for deeper product/architecture documentation; GSD for lighter execution. Do not use both as competing project brains.
3. **Graphify or Understand Anything** — choose one codebase/knowledge mapping tool based on accuracy, offline capability and update cost.
4. **ECC selectively** — harvest only useful, non-conflicting rules/agents after source review.
5. **One design skill** — Impeccable or UI UX Pro Max when the UI exists.
6. **REA** — only for lawful, authorized reverse engineering and only when a real need arises.

Optional: gstack for review/QA if its browser and update dependencies fit the environment; Claude-Mem only after storage/privacy testing; Ponytail as an alternative engineering style skill.

Do not activate every framework simultaneously. More prompts do not equal better engineering. Duplicated hooks, conflicting instructions and overlapping agents can make the control plane less predictable.

---

## 4. Skill/plugin security and integration rubric

Before installing or incorporating any skill, score it against these questions:

### Provenance and licensing

- Is this the canonical upstream repository?
- Who maintains it and how can the owner be verified?
- Is the exact version pinned to a commit/release?
- Is there a clearly stated license for the code and bundled content?
- Are fonts, models, datasets, templates and screenshots separately licensed?
- Does the license permit commercial use and redistribution in the intended way?

### Execution surface

- Does it install hooks, scripts, binaries or MCP servers?
- Does it read or write outside the project directory?
- Can it execute arbitrary shell commands?
- Does it access browser sessions, passwords, environment variables or credentials?
- Does it send data to a remote service?
- Does it auto-update or download assets at runtime?
- Does it create background processes or persist state?

### Offline suitability

- Does it run with DNS and outbound routing disabled?
- Are all dependencies vendorable and pinned?
- Does setup need a network registry or remote API?
- Can it be installed through a verified transfer bundle?
- Does its claimed functionality require web access?

### Product integration

- Is this merely a prompt/workflow or a genuinely reusable technical capability?
- Is there an API/CLI/module that can be isolated?
- Can the functionality be reimplemented more safely with a small deterministic component?
- Does the customer actually need it?
- What is the maintenance and vulnerability burden?

### Required record

```yaml
plugin_name: ""
upstream_repository: ""
commit_or_release: ""
license: ""
reviewed_at: "YYYY-MM-DD"
maintainer_status: ""
install_scripts_reviewed: false
hooks_reviewed: false
network_calls_reviewed: false
filesystem_scope_reviewed: false
credential_access_reviewed: false
telemetry_reviewed: false
offline_test_passed: false
commercial_redistribution_allowed: "unknown"
product_integration_candidate: false
accepted_for: [research | developer_workflow | product_component]
rejected_reasons: []
```

## 5. Do not turn plugins into the product architecture

A plugin may contribute an idea, workflow or component, but the product should expose its own stable interfaces and policy system.

Use these rules:

- Treat skills as replaceable adapters.
- Keep product logic in version-controlled, tested code.
- Do not depend on a specific IDE vendor or agent harness at runtime.
- Do not ship third-party skill prompts to customers unless the license and support model explicitly allow it and there is a product reason.
- Reimplement simple deterministic capabilities directly when this is safer and easier to maintain.
- Preserve attribution and license notices.
- Build conformance tests for any plugin adapter the platform supports.
- Make unsupported plugins fail closed; do not grant them implicit access.

## 6. Final plugin decision

**Use plugins aggressively as replaceable engineering leverage, but conservatively as trusted executable dependencies.**

The product is the secure offline workflow and its validated outcomes. The plugin ecosystem is an optional development toolset, not the foundation of the business and not the source of truth for research.

