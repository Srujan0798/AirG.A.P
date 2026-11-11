# 01 — Master Vision, Opportunity & Strategic Direction

**Project:** AI for the Air-Gapped Economy  
**Status:** Strategic hypothesis and handoff baseline — 30 October 2026  
**Owner:** Founder / product architect  
**Purpose:** Carry the original intent, independent strategy and initial product recommendation into a separate IDE and research environment.

---

## 1. Executive decision

### The selected opportunity

Build for **AI for the Air-Gapped Economy**, the tenth idea in Y Combinator's Winter 2027 Requests for Startups. YC describes customers that want frontier AI running entirely inside their own buildings without an internet connection. Its stated opportunity areas include on-premises models, deployment tooling, security accreditation and hardware. YC separately lists **Own Your Intelligence** as idea #11: help companies control and improve models using their own data. Treat #11 as an adjacent capability and potential expansion, not as a replacement for the chosen #10 opportunity.

Primary source: [YC Requests for Startups — Winter 2027](https://www.ycombinator.com/rfs).

### Recommended first product hypothesis

Build a **secure, offline, agentic engineering workbench** for software teams operating inside disconnected or tightly restricted engineering environments. The first version should help teams understand, maintain, test and modernize software without sending code, requirements, logs or proprietary data to external AI services.

This is a wedge into the air-gapped economy, not the whole company vision. The wider platform can later provide reusable offline model serving, controlled artifact intake and updates, policy enforcement, secure agent execution, audit evidence, customer-owned model adaptation and other vertical workflows.

The working description is preferable to locking in “Air-Gapped Engineering Matrix (AGEM)” as a permanent name. AGEM appeared in a prior AI-generated export; it is not a user-confirmed brand or a validated product definition.

### Why this wedge

1. It turns a broad infrastructure opportunity into a bounded workflow with observable inputs and outputs.
2. It offers a path to measurable customer value: reduced engineering cycle time, faster codebase comprehension, more test coverage, improved traceability and less manual effort on legacy systems.
3. It can be piloted on a non-production repository and an isolated engineering lab. That avoids making the first product responsible for controlling safety-critical live systems.
4. It uses multi-agent orchestration where parallel work is useful, while deterministic systems control permissions, execution and acceptance.
5. It creates a foundation for adjacent capabilities: disconnected deployment, model lifecycle, customer-owned intelligence and secure knowledge systems.

**This recommendation must be challenged by customer discovery and competitive research before the company commits to it.**

---

## 2. Reconstructed founder intent

The following points are extracted from the founder's own statements in the Gemini export and the current conversation. They describe intent, not externally verified facts.

### 2.1 Build in the real economy

The founder does not want to build another shallow AI layer or a conventional application that merely wraps a hosted model API. The target is an important, difficult, real-world problem where AI must operate within economic and technical constraints that ordinary cloud-first products do not address.

### 2.2 Pursue a high-leverage opportunity

The founder initially asked for three different kinds of recommendations:

- A conventional, high-volume idea that a generic AI recommendation might produce.
- An unusual or overlooked niche opportunity.
- The strongest opportunity based on the founder's technical interests, multi-agent engineering approach and potential to execute.

The founder later selected YC idea #10, AI for the Air-Gapped Economy, as the direction to pursue. The ambition is to build a serious startup whether or not YC selects it.

### 2.3 Operate above ordinary agentic coding

The founder describes working with advanced coding agents, multi-agent workflows and a collection of roughly 30 Claude Code skills/plugins. The founder wants a fast-forward engineering approach, but not uncontrolled “vibe coding.” They want to design systems and orchestrate agent capabilities rather than simply prompt an agent to write files.

This is a self-described capability and intended operating style. The receiving agent must still verify what the founder can execute, what hardware and team are available, and which tools are actually installed. Do not treat self-description as evidence of a finished product or proven customer traction.

### 2.4 Reject three false choices

The founder rejects each of these as a complete approach:

- Traditional engineering alone, if it ignores the leverage available from capable agents and tools.
- Plugin dependence alone, because branded skills can be brittle, overlapping, internet-dependent, insecure or poorly suited to a customer environment.
- A superficial combination that simply installs tools and calls it a hybrid architecture.

The preferred philosophy is a **customized hybrid**: foundational engineering for correctness and control; agentic systems for leverage; research for discovery; plugins as replaceable accelerators; custom integrations where a real gap exists; and independent validation throughout.

### 2.5 Separate research tools from product tools

The founder has two intended uses for the Claude Code skills/plugin collection:

1. Use a small, suitable subset of research-oriented skills to help research the air-gapped AI opportunity, recent developments, papers, repositories and market evidence.
2. Evaluate the wider 30-skill collection as potential tools for developing the product in the IDE. Some underlying capabilities may later be re-engineered as customer-facing product capabilities, but a developer plugin is not automatically a product component.

The founder specifically does not want research to be biased toward the named plugins. The agents must discover the best general approaches, even when those approaches do not use any of the supplied plugins.

### 2.6 The expected handoff

The founder wants to leave this ChatGPT environment with an independent local IDE and advanced research agents. The handoff must therefore be complete, structured and actionable. It must carry the vision, research protocol, IDE setup, engineering foundation, plugin strategy and hybrid delivery method without depending on this chat remaining available.

---

## 3. Opportunity framing: what “air-gapped AI” actually means

Do not collapse several deployment modes into one vague term.

| Mode | Meaning | Typical implications |
|---|---|---|
| Cloud AI | Inference or data processing is performed by a remote service. | External trust, connectivity, data-transfer and vendor-dependency questions. |
| Private/on-prem AI | AI runs on infrastructure controlled by the customer, but may still have internet access. | Customer control, private networking, local data; not necessarily disconnected. |
| Restricted-connectivity AI | The system has tightly controlled outbound/inbound connectivity, gateways or allowlists. | Explicit network boundaries and monitoring. |
| Disconnected AI | The deployment does not rely on continuous internet access; controlled imports/updates may be possible. | Staged assets, offline registries, controlled transfer and maintenance procedures. |
| Fully air-gapped AI | The target environment has no direct network path to the public internet or other untrusted networks. | Offline installation, verified transfer, local operations, local observability and planned update mechanisms. |

A customer may use “air-gapped” loosely. The product must first learn the customer's actual isolation model, threat model, data classification, transfer policy, operational constraints and accreditation requirements.

An air gap is a network property, not proof that the system is secure. Removable media, supply-chain compromise, privileged insiders, compromised build machines, malicious dependencies, contaminated model weights, prompt injection and excessive agent privileges remain relevant.

### The lifecycle problem

Air-gapped AI is not just “download a model and run it locally.” It includes:

1. Selecting hardware, operating system, drivers, runtime and models.
2. Acquiring software, model weights, containers, packages and documentation in a connected staging environment.
3. Checking provenance, licenses, signatures, checksums, SBOMs and policy.
4. Approving and transferring a complete, versioned bundle through the customer's permitted path.
5. Installing and running locally without hidden internet dependencies.
6. Managing users, roles, secrets, data, tools, memory and audit records.
7. Evaluating model and agent behaviour on the customer's own tasks.
8. Updating, rolling back, patching and supporting the system while disconnected.
9. Producing evidence for security review, procurement, audits and accreditation.

NVIDIA's documented NIM air-gap workflow itself separates a network-connected asset-preparation phase from an air-gapped execution phase. That is evidence that the lifecycle matters; it is not evidence that NVIDIA has solved every customer workflow. See [NVIDIA NIM air-gap deployment](https://docs.nvidia.com/nim/large-language-models/latest/deploy-air-gap.html).

---

## 4. Strategic opportunity map

Investigate all of these layers. Do not assume the first product must build every layer.

### Layer A — Offline AI infrastructure and deployment

- Model and inference runtime packaging.
- Hardware discovery and compatibility.
- Offline container and package registries.
- Disconnected cluster installation and upgrade.
- Model and adapter lifecycle management.
- Observability and diagnosis without cloud services.
- Backup, restore and rollback.

**Strategic reading:** Important but already served in parts by major vendors and open-source infrastructure. A generic launcher or model registry is unlikely to be enough by itself.

### Layer B — Secure agent runtime

- Agent identities and scoped permissions.
- Policy-enforced tool gateway.
- Sandboxed command execution.
- Isolated workspaces and per-task credentials.
- Network egress control.
- Immutable action and approval records.
- Agent-to-agent trust and message validation.
- Bounded retries, resource limits, kill switches and recovery.

**Strategic reading:** Strong candidate for differentiation when attached to a valuable customer workflow. “A swarm of agents” is not a moat; safe, predictable and auditable work completion may be.

### Layer C — Engineering workflows

- Repository and dependency understanding.
- Requirements-to-code and test traceability.
- Legacy code modernization and migration planning.
- Test generation and regression triage.
- Defect investigation and repair proposals.
- Documentation and configuration analysis.
- Firmware/embedded software workflows, subject to customer and safety constraints.

**Strategic reading:** Best initial wedge to test because the outputs can be reviewed and measured without giving an agent control of live infrastructure.

### Layer D — Customer-owned intelligence

- Customer-controlled knowledge stores and retrieval.
- Domain-specific evaluation sets.
- Prompt, tool and model version control.
- Fine-tuning/adapter support only where it provides measurable benefit.
- Local model routing and task specialization.
- Customer-controlled model artifacts and update policies.

**Strategic reading:** This maps to YC's adjacent “Own Your Intelligence” idea. Begin with data ownership, retrieval, evaluations and model portability. Do not assume that training a foundation model is the first task.

### Layer E — Trust, supply chain and accreditation evidence

- Artifact provenance, signature and checksum verification.
- Model/data/software inventories and SBOMs.
- License and export-control checks.
- Vulnerability intelligence bundles with provenance and freshness metadata.
- Policy configuration and audit trails.
- Deployment hardening and customer evidence packs.
- Security tests and incident response procedures.

**Strategic reading:** This is essential to customer adoption, but “we are compliant” cannot be claimed without a defined scope, assessment and evidence. The product can help produce evidence; it cannot guarantee certification.

---

## 5. Initial product hypothesis: Offline Agentic Engineering Workbench

### One-sentence definition

A customer-controlled engineering environment that runs local models and policy-governed agents to understand, test, modernize and propose changes to software repositories without sending source code or operational data outside the customer's approved boundary.

### First users

- Software engineering teams in defense/aerospace/industrial suppliers with isolated engineering labs.
- Product teams maintaining embedded, firmware, infrastructure or long-lived codebases.
- Regulated organizations with restricted development networks and a clear backlog of code comprehension, test, migration or maintenance work.

These are candidate profiles, not confirmed customer segments. The first buyer and workflow must be selected through interviews.

### First workflow candidates

1. **Codebase understanding:** map modules, dependencies, entry points, data flows and test coverage; let engineers query the repo with source references.
2. **Requirements traceability:** connect requirements, code units, tests and change history; identify missing links and inconsistencies.
3. **Change-impact analysis:** explain which files, interfaces, tests and dependent components a proposed change may affect.
4. **Test generation:** propose tests for a bounded issue or function, execute them in a sandbox and show what was not tested.
5. **Legacy modernization:** propose a migration plan and small, reviewable patches; never silently replace an entire subsystem.
6. **Defect investigation:** inspect logs and repository context, identify candidate root causes and produce a reproducible test or patch proposal.

### MVP boundary

The MVP should:

- Run on a documented, bounded hardware configuration.
- Work with one local model-serving path and one fallback path.
- Support one source-control/codebase integration.
- Index a customer-approved repository and local documentation.
- Offer read-only analysis by default.
- Generate patch proposals in an isolated worktree.
- Run selected tests in a disposable sandbox with no external network access.
- Require human approval before changes are merged or exported.
- Keep a local audit record of inputs, model/runtime version, tool calls, test results and approvals.
- Be demonstrably functional when outbound internet access is blocked.

### Explicit non-goals for the first release

- Building a frontier foundation model from scratch.
- Supporting every model, GPU, operating system, IDE, customer vertical and deployment topology.
- Autonomous changes to live power-grid, nuclear, medical or industrial control systems.
- Claiming full regulatory compliance or “zero data leakage.”
- Replacing all human software engineers.
- Shipping 30 third-party skills as a runtime dependency.
- Creating custom hardware before customers demonstrate a requirement that cannot be met by supported standard servers.

---

## 6. Positioning and competitive logic

The product must not position itself as “another local LLM chat interface.” Local coding assistants and enterprise AI platforms already exist. Examples include self-hosted code completion, coding agents that support local model endpoints, general on-prem inference, and enterprise disconnected deployment stacks.

The hypothesis to test is that buyers need a **complete, policy-controlled engineering workflow** that combines repository context, local reasoning, isolated execution, acceptance tests, update provenance and auditable approval under their specific disconnected constraints.

Potential differentiation:

- Reproducible offline install/upgrade/update lifecycle.
- Auditable agent action and approval control.
- Secure, reusable task sandboxes.
- Domain-specific code/requirements/test context.
- Evaluation on customer tasks rather than generic leaderboard scores.
- A validated hardware/runtime support matrix.
- Evidence packs for security teams and procurement.
- Integrations with the customer's source control, identity, ticketing and engineering systems, all operable locally.

Do not claim these capabilities are unique until competitors and open-source projects have been exhaustively mapped.

### Adjacent competitor classes to benchmark

1. Model and inference platforms: NVIDIA NIM, vLLM, llama.cpp, SGLang and other local serving stacks.
2. Enterprise AI platforms: Red Hat OpenShift AI, enterprise private AI infrastructure and vendor-specific on-prem systems.
3. Self-hosted coding assistants/agents: Tabby, Cline, Roo Code and other local-model coding tools.
4. Agent frameworks and workflow systems: agent SDKs, coding agents, orchestration frameworks and evaluation harnesses.
5. Secure software development and supply-chain products: SBOM, signing, artifact promotion, vulnerability and policy tools.

The competitor analysis must compare actual product limits, supported deployment modes, licenses, offline operations and customer evidence—not only marketing pages.

---

## 7. Product architecture principles

1. **Offline by construction:** The isolated runtime must not need internet access for inference, retrieval, workflow control, logging, tool execution or updates.
2. **Deterministic control plane:** Models can recommend actions; deterministic policy and workflow code decides which actions are allowed and when a workflow changes state.
3. **Agents are untrusted principals:** An agent is not a trusted administrator. It receives narrowly scoped credentials, tools and filesystem permissions.
4. **Human approval for consequential actions:** Especially repository writes, dependency changes, builds, artifact export, privilege changes and any connection to operational systems.
5. **Sandbox every execution:** Generated code runs in a disposable, constrained environment. A prompt instruction or AST scan is not a security boundary.
6. **Reproducibility:** Pin software, model, tokenizer, configuration, dataset, prompt/skill and runtime versions.
7. **Portable model layer:** Keep model-serving APIs behind an internal adapter so runtimes can be replaced.
8. **Evidence over claims:** Every important result should link to sources, code locations, tests, model versions and decisions.
9. **Fail closed:** If policy, model assets, audit storage or required dependencies are unavailable, disable the relevant action rather than silently falling back to an unsafe mode.
10. **Least complexity:** Start with a single-node deployment and expand to distributed nodes only when measured requirements justify it.

---

## 8. Startup strategy and commercial hypotheses

### Initial buyer hypothesis

A technical leader responsible for a secure software engineering environment who has a measurable backlog of maintenance, testing, code comprehension or modernization work and cannot send the relevant repository to public AI services.

### Discovery questions

- What exactly is isolated: the whole lab, only source control, build systems, runtime networks, or classified data?
- What AI tools have been rejected, and why?
- How are developers currently allowed to move code, packages, model weights and updates into the environment?
- Which engineering tasks are costly enough to justify a new product?
- Who owns security approval, procurement, infrastructure and engineering outcomes?
- What hardware is already available?
- What would constitute a failed pilot?
- Which systems must the product integrate with?
- What would a customer pay for: software, deployment, support, appliance, or an outcome-based engagement?

### Candidate business model

Start with enterprise software plus deployment and support, priced by site, deployment profile, capacity or engineering team after customer discovery. A validated appliance bundle may follow. Avoid pricing around cloud token consumption because the target may have no cloud connection.

Potential revenue components:

- Annual platform license per deployment/site.
- Initial deployment and integration fee.
- Premium support and controlled update service.
- Additional model/runtime or workflow modules.
- Optional pre-validated hardware bundle through partners.

These are pricing hypotheses, not known willingness-to-pay.

### Distribution

- Founder-led technical discovery and pilots.
- Partnerships with defense, aerospace, industrial software and secure-infrastructure integrators.
- Reference deployments and evidence-led technical workshops.
- Procurement/security documentation prepared early.
- Start with one repeatable vertical workflow; expand after proof.

### Defensibility hypothesis

The moat is unlikely to be a single model, prompt, generic agent framework or collection of plugins. More credible sources of defensibility could become:

- Deep integration into regulated engineering workflows.
- Reliable offline deployment and update operations.
- Security policy and audit evidence accepted by buyers.
- Customer-specific evaluations and workflow knowledge.
- Trust earned through successful installations and support.
- Domain-specific connectors and migration/test assets.
- A validated operational footprint across hardware and software combinations.

---

## 9. Validation gates and kill criteria

Do not confuse building a technically impressive demo with proving a business.

### Gate A — Problem validation

Pass when multiple target customers independently confirm the same expensive workflow problem, explain current workarounds and identify a buyer and deployment boundary.

Fail or pivot if customers mainly want generic chat, cannot host a local runtime, have no budget owner, or already solve the problem adequately with existing tools.

### Gate B — Technical feasibility

Pass when the team can install and run the prototype with outbound network blocked; process a real but non-sensitive codebase; generate useful source-grounded findings; and produce a patch/test proposal inside a constrained sandbox.

Fail or narrow if supported local models cannot meet a useful quality/latency/cost threshold on actual customer hardware.

### Gate C — Trust and security

Pass when a documented threat model, identity model, no-egress controls, sandbox, artifact verification and audit evidence withstand an independent review appropriate to the pilot scope.

Fail if the product requires unrestricted agent permissions, untracked dependencies, hidden external services or unverifiable updates.

### Gate D — Measurable value

Compare against a baseline on real tasks. Measure:

- Task completion with accepted tests.
- Engineer time to complete each task.
- Human review and correction effort.
- Regression and escape rate.
- Test coverage and quality, not just count.
- Evidence traceability.
- Runtime/compute footprint.
- Offline reliability and time to recover.
- Security-policy violations and denied action attempts.

### Gate E — Commercial proof

Pass with a design partner willing to provide a real workflow, a defined security boundary, a named buyer and a paid or otherwise concrete pilot commitment.

---

## 10. Initial execution sequence

### First 2 weeks: discovery and evidence

- Interview 15–25 carefully selected engineers, security leads, engineering directors and system integrators. The count is a planning target, not a market statistic.
- Map 3–5 concrete workflows and select one.
- Build competitor and open-source feature matrices.
- Identify one pilot repository and one target hardware profile.
- Establish baseline task set and security requirements.

### Weeks 3–4: feasibility vertical slice

- Stage one local model and one serving runtime.
- Install offline with egress blocked.
- Index one approved repository and documentation corpus.
- Run a read-only codebase Q&A/impact analysis workflow.
- Add one sandboxed test-generation or patch-proposal loop.
- Capture every tool call and evaluation result.

### Weeks 5–8: controlled pilot system

- Add identity, permissions, policy engine and audit log.
- Add deterministic workflow state, retries and task recovery.
- Add update/artifact import verification.
- Add the customer-defined baseline task suite.
- Run security and prompt-injection tests.

### Weeks 9–12: design-partner pilot decision

- Deploy in a permitted test environment.
- Compare against baseline and collect user acceptance data.
- Fix the largest operational/security blocker.
- Produce installation, rollback, admin and security documentation.
- Decide to expand, narrow or abandon based on actual evidence.

---

## 11. Important facts and caveats

- YC's Requests for Startups is a statement of interests and an invitation, not a guarantee of funding or validation for an individual company.
- YC says Winter 2027 on-time applications are due **2 November 2026 at 8pm Pacific Time**. If applying, verify the live deadline and submit only claims that are true. [YC Apply](https://www.ycombinator.com/apply).
- NIST SP 800-82 Rev. 4 is an **initial public draft** published 21 September 2026, with comments due 30 November 2026. It is relevant to OT security; it is not a certification checklist for this product. [NIST SP 800-82 Rev. 4 IPD](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd).
- “No internet” does not mean “no risk.” Air-gapped deployments still need supply-chain, removable-media, identity, insider, vulnerability and physical-security controls.
- This document is a strategic baseline, not legal, certification, export-control or security-accreditation advice.

---

## 12. Source register

### Primary source and standards

- [YC Requests for Startups — Winter 2027](https://www.ycombinator.com/rfs)
- [YC Apply](https://www.ycombinator.com/apply)
- [NIST SP 800-82 Rev. 4 Initial Public Draft](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd)
- [NIST SP 800-218 Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
- [NIST AI RMF Generative AI Profile, NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [OWASP GenAI / LLM Top 10 2026](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10)
- [MITRE ATT&CK for ICS — Network Segmentation M0930](https://attack.mitre.org/mitigations/M0930/)
- [The Update Framework specification](https://github.com/theupdateframework/specification/blob/master/tuf-spec.md)
- [SPDX specification](https://spdx.github.io/spdx-spec/)

### Deployment and runtime references

- [NVIDIA NIM air-gap deployment](https://docs.nvidia.com/nim/large-language-models/latest/deploy-air-gap.html)
- [vLLM offline inference](https://docs.vllm.ai/en/latest/serving/offline_inference/)
- [llama.cpp](https://github.com/ggml-org/llama.cpp)
- [RKE2 air-gap install](https://docs.rke2.io/install/airgap)
- [K3s air-gap install](https://docs.k3s.io/installation/airgap)

### Agent and software-engineering evaluation

- [A Comprehensive Survey on Benchmarks and Solutions in Software Engineering of LLM-Empowered Agentic Systems](https://arxiv.org/abs/2510.09721)
- [Survey on Evaluation of LLM-based Agents](https://arxiv.org/abs/2503.16416)
- [SWE-Bench Pro, ICML 2026](https://proceedings.mlr.press/v306/deng26f.html)
- [SWE-rebench, NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/21bec6ace947b1b58967b945c8ac0f10-Abstract-Datasets_and_Benchmarks_Track.html)
- [InjecAgent](https://arxiv.org/abs/2403.02691)
- [AgentDojo](https://arxiv.org/abs/2406.13352)
- [Why SWE-bench Verified no longer measures frontier coding capabilities](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)

---

**Handoff rule:** The local research team may change this strategy. It must record the evidence and customer observations that justify each change. Do not preserve a recommendation merely because it appears in this document.
