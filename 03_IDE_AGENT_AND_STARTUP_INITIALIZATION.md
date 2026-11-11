# 03 — IDE, Agent Environment & Startup Initialization Guide

**Purpose:** Initialize the founder's separate IDE/research environment for Phase I and prepare the development workspace for Phase II.  
**Principle:** Keep online research, trusted build preparation, offline integration testing and customer deployment as separate trust zones.

---

## 1. Operating model: four environments, not one laptop session

| Environment | Connectivity | Purpose | Data allowed |
|---|---|---|---|
| R&D research environment | Internet allowed, monitored | Papers, public documentation, market research, plugin inspection and prototype development. | Public data and synthetic/sanitized code only. No customer secrets. |
| Trusted build/staging environment | Controlled network | Pin dependencies, build images, collect models, generate SBOM/provenance and prepare signed transfer bundles. | Approved source and artifacts; restricted credentials. |
| Offline integration lab | Egress blocked | Verify install, inference, agent workflows, tests, updates and recovery. | Synthetic or explicitly approved data. |
| Customer air-gapped deployment | Defined by customer | Actual production operation within customer-approved boundary. | Customer-classified data under customer policy. |

Do not let an online IDE, plugin or research agent silently become part of the customer runtime.

## 2. Workspace structure

Create a dedicated repository, for example `airgap-ai-platform/`. The name is a placeholder.

```text
airgap-ai-platform/
├── README.md
├── AGENTS.md                     # universal project instructions
├── SECURITY.md                   # security posture and reporting process
├── THREAT_MODEL.md               # assets, actors, trust boundaries, abuse cases
├── DATA_CLASSIFICATION.md        # data classes and handling rules
├── MODEL_POLICY.md               # accepted model/license/provenance rules
├── PLUGIN_POLICY.md              # skill/plugin allowlist and review process
├── CONTRIBUTING.md
├── LICENSES/                     # third-party notices; never invent permissions
├── docs/
│   ├── 00-vision-and-strategy.md
│   ├── 01-product-requirements/
│   ├── 02-customer-discovery/
│   ├── 03-research/
│   │   ├── search-log/
│   │   ├── literature-matrix/
│   │   ├── competitor-matrix/
│   │   ├── customer-evidence/
│   │   └── synthesis/
│   ├── 04-architecture/
│   │   ├── context-and-boundaries.md
│   │   ├── reference-architecture.md
│   │   └── adr/
│   ├── 05-security/
│   ├── 06-models-and-evals/
│   ├── 07-deployment-and-runbooks/
│   ├── 08-commercial/
│   └── 09-release-evidence/
├── agents/
│   ├── principal-research-director.md
│   ├── literature-scout.md
│   ├── model-runtime-architect.md
│   ├── agent-systems-architect.md
│   ├── security-red-team.md
│   ├── supply-chain-engineer.md
│   ├── market-analyst.md
│   ├── customer-discovery.md
│   ├── evaluation-lead.md
│   └── adversarial-reviewer.md
├── prompts/
│   ├── research-master.md
│   ├── specialist-protocols.md
│   ├── synthesis.md
│   └── implementation-gates.md
├── research-data/
│   ├── raw/                       # source files, metadata, source hash
│   ├── normalized/                # parsed records; preserve raw originals
│   ├── claims/                    # claim ledger with evidence grade
│   ├── graphs/                    # generated knowledge graphs
│   └── reports/
├── evals/
│   ├── tasks/
│   ├── golden-results/
│   ├── attack-cases/
│   ├── harness/
│   └── reports/
├── supply-chain/
│   ├── manifests/
│   ├── sbom/
│   ├── signatures/
│   ├── model-cards/
│   ├── licenses/
│   └── import-quarantine/
├── scripts/
├── infra/
│   ├── dev/
│   ├── offline-lab/
│   └── customer-profile-templates/
└── src/
    ├── control-plane/
    ├── model-gateway/
    ├── agent-runtime/
    ├── tool-gateway/
    ├── execution-sandbox/
    ├── retrieval/
    ├── audit/
    ├── artifact-manager/
    └── admin-ui/
```

Do not create all source modules on day one. The tree expresses intended ownership boundaries. Implement only modules required by the first validated vertical slice.

## 3. Universal project instructions (`AGENTS.md`)

Put an equivalent of the following at the repository root. Adapt syntax to the actual IDE/agent harness.

```text
PROJECT: Air-Gapped AI Platform

MISSION
Build a secure, customer-controlled AI system for disconnected environments. The initial product hypothesis is an offline agentic engineering workbench. This is a hypothesis to validate, not a fixed architecture.

ENGINEERING RULES
- Read docs/00-vision-and-strategy.md, THREAT_MODEL.md and the relevant ADRs before making architectural changes.
- Do not invent customer requirements, test results, source citations, compliance status or benchmark results.
- Requirements and claims must be traceable to a source or be labelled as hypotheses.
- Architecture before implementation for non-trivial changes.
- Prefer the smallest design that satisfies a verified requirement.
- Preserve stable interfaces and document breaking changes.
- No network access in offline-lab test runs unless a test explicitly proves that a network dependency is intentionally allowed.
- Never put credentials, customer source, production logs or regulated data into external research tools, plugins, telemetry or public model APIs.
- All tool use is least-privilege. Agents are untrusted principals.
- Generated code must execute only in a disposable sandbox with no host secrets and denied network egress.
- A model's statement that an action is safe is not a security control.
- No automatic merge, release, deployment, permission grant or artifact import without the defined approval gate.
- Every implementation task must define acceptance tests before code is considered complete.
- Record significant design choices in an ADR.
- Pin dependencies and model artifacts; never use floating latest versions in reproducible builds.

IMPLEMENTATION LOOP
1. Inspect existing code and requirements.
2. Write a bounded spec and test plan.
3. Identify affected modules and trust boundaries.
4. Create an isolated branch/worktree.
5. Implement the minimum change.
6. Run unit, integration, regression and security tests.
7. Review diff and artifact provenance.
8. Request human approval where policy requires.
9. Record evidence and update docs.

OUTPUT DISCIPLINE
Report changed files, commands run, results, limitations, risks, evidence and skipped checks. Never say “verified” unless the test was actually executed and its output inspected.
```

## 4. Agent topology

Start with specialist prompts and one orchestrator. Do not start by running 30 agents concurrently.

| Agent | Responsibility | Permissions |
|---|---|---|
| Principal orchestrator | Owns workflow state, task assignment, deadlines, dependency checks and merge gates. | Task metadata and control-plane APIs; no direct unrestricted shell. |
| Product/research analyst | Maintains evidence, requirements and customer workflow hypotheses. | Read research corpus; write research artifacts. |
| Repository analyst | Maps code and identifies affected components. | Read-only repo access. |
| Architect | Proposes design and ADRs. | Read code/docs; propose, not merge. |
| Implementer | Makes a bounded code change. | One isolated worktree and task-scoped files. |
| Test engineer | Builds and runs test plans. | Test sandbox and fixtures; no production credentials. |
| Security reviewer | Threat-models and reviews changes. | Read-only source, tests and policy; can block. |
| Evaluator | Runs task suite and captures metrics. | Evaluation harness; no ability to change golden results. |
| Release/supply-chain agent | Prepares manifests, SBOM and evidence. | Staging only; release signature requires authorized human/key process. |
| Adversarial reviewer | Looks for counterexamples, bypasses and unsupported claims. | Read-only; can create findings. |

### Concurrency policy

- Parallelize independent literature searches and independent code modules.
- Do not parallelize multiple agents editing the same files in the same worktree.
- Give each implementer an isolated Git worktree/branch and explicit file/module ownership.
- Merge through a deterministic integration step with tests and conflict review.
- Shared memory is a source of recorded facts and decisions, not a writable free-for-all. Use immutable events or versioned records for important decisions.

## 5. Research-tool setup: use two or three, selectively

### Recommended research candidates

| Candidate | Use | Do not use for |
|---|---|---|
| [Last 30 Days](https://github.com/mvanhorn/last30days-skill) | Recent community, GitHub, news and arXiv discovery; track current pain and changes. | Peer-review verification, legal conclusions or final market-size evidence. |
| [Agent Reach](https://github.com/Panniantong/Agent-Reach) | Reach specific public platforms/repositories and retrieve social/video/discussion material. | Sensitive customer research, unrestricted personal accounts or air-gapped customer runtime. |
| [Graphify](https://github.com/Graphify-Labs/graphify) | Structure paper/code/document relationships and navigate large corpora. | Treating inferred graph edges as facts. |

### Safe installation procedure

Perform this on the R&D machine, not the target offline lab:

1. Confirm the exact upstream repository and maintainer. Do not install a similarly named fork just because it appears in a chart.
2. Inspect `README`, `LICENSE`, `SECURITY`, install scripts, hooks, MCP servers, dependencies and update mechanism.
3. Record repository URL, commit SHA, release/version, license and review date.
4. Search for shell execution, network calls, browser/profile/session access, secret reads, file writes and telemetry.
5. Install into a disposable test environment with no valuable credentials.
6. Monitor filesystem and network activity during a test run.
7. Test whether it still works with network disabled if local operation is claimed.
8. Pin the reviewed commit. Do not auto-update the version used for reproducible research.
9. Store the source, license and review notes in `PLUGIN_POLICY.md`.
10. Re-review before using it on proprietary code.

### Research-only caution

The current Last 30 Days README describes connections across public and sometimes authenticated sources and optional setup for arXiv, X, YouTube and other platforms. Agent Reach's README describes optional login-based platform access and experimental channels. Those capabilities are useful for public research but create account, terms-of-service and data-handling risks. Use dedicated low-privilege accounts. Never place customer secrets in these tools.

## 6. The 30-skill collection: installation strategy

The supplied image is a snapshot labelled “Top 30 Claude Code Plugins,” with GitHub stars read on 23 October 2026. It is not a security audit, quality ranking or current compatibility guarantee.

Do not install all 30 globally. Begin with a small, measured allowlist. The separate `05_PLUGIN_POWERED_ENGINEERING_FRAMEWORK.md` contains the complete inventory and disposition.

Suggested initial engineering evaluation set:

- **Superpowers** — structured development, debugging, testing and review workflows.
- **One planning framework only:** BMAD *or* GSD. Do not run two competing process owners on the same task.
- **Graphify** — repository/paper relationship mapping.
- **ECC selectively** — reuse specific useful rules or agents only after checking overlap and security.
- **One UI skill later** — Impeccable or UI UX Pro Max, only when there is an actual UI task.

Optional, task-dependent: REA for authorized reverse engineering; gstack for product/review/QA workflows; Claude-Mem after privacy and retention checks; Ponytail as an alternative coding-discipline skill. Avoid using every workflow framework simultaneously.

## 7. Local memory and knowledge management

Keep project truth in version-controlled files. Do not rely only on an agent vendor's hidden memory.

Use four distinct stores:

1. **Source archive:** original papers, docs, snapshots and hashes.
2. **Claim ledger:** atomic claims with sources, dates, evidence grade and counterevidence.
3. **Decision log:** ADRs with status, owner, options, decision, rationale and consequences.
4. **Operational state:** agent task state, current plan, artifacts, test outputs and approvals.

A vector database or graph database may help retrieval, but neither should replace canonical records. Use relational storage for authoritative workflow state and permissions; use object storage for immutable artifacts; use vector/graph indexes as derived, rebuildable views.

## 8. First-time IDE startup prompt

Paste after the repository and files exist:

```text
You are the Principal Engineering Orchestrator for this project.

First, read AGENTS.md, docs/00-vision-and-strategy.md, docs/02-customer-discovery, THREAT_MODEL.md, DATA_CLASSIFICATION.md and the existing ADRs. Do not write implementation code yet.

Produce:
1. A concise map of the current repository and missing documents.
2. A requirements register distinguishing founder intent, evidence, hypotheses and unknowns.
3. A research backlog mapped to the 12 specialist roles in the research protocol.
4. A dependency graph and proposed parallel execution groups.
5. A threat-boundary map for the current development environment.
6. A list of tools/plugins that need security/license review before installation.
7. A proposed first customer-discovery sprint and first technical proof-of-feasibility experiment.

Do not choose a final model, hardware platform, orchestration framework or customer vertical without evidence. Do not install plugins automatically. Ask for approval before any command that changes system-level configuration or downloads executable software.

End with a prioritized decision log and a list of the five most important unknowns.
```

## 9. First-week operating cadence

**Day 1:** Initialize repository, security policy, source ledger and decision log.  
**Day 2:** Install/inspect only the research tools; create source-search templates.  
**Day 3:** Run literature, platform and competitor scouts in parallel.  
**Day 4:** Run customer discovery and adversarial product review.  
**Day 5:** Synthesize three product hypotheses and identify one experiment per hypothesis.  
**Day 6:** Select one non-sensitive repository and hardware profile for an offline feasibility test.  
**Day 7:** Review evidence, update the product decision and decide whether a build sprint is justified.

The schedule is a suggested cadence, not a claim that the work will finish in a week.

## 10. IDE/environment acceptance checklist

- [ ] Project vision and requirements are stored in version control.
- [ ] Agents have distinct roles and least-privilege access.
- [ ] No agent has unrestricted access to home directories, SSH keys or production credentials.
- [ ] Customer or sensitive data is excluded from online research tools.
- [ ] All third-party plugins have exact upstream source, license and pinned version recorded.
- [ ] Hooks and scripts are inspected before installation.
- [ ] Offline lab network egress is denied by infrastructure, not merely by prompt.
- [ ] Test workspaces are disposable and have no host secrets mounted.
- [ ] Task, approval and audit records survive process restart.
- [ ] The same installation can be rebuilt from pinned artifacts.
- [ ] A human can stop agents and revoke their permissions.
- [ ] There is a documented backup, restore and rollback path.

