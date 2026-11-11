# W7 — Moat & Control-Plane Claim Stress Test

**Role:** Principal Product Architect · **Task-ID:** WAVE2-MOAT · **Produced:** 2026-11-11 · **Grades:** A=official docs/source, B=independent eval, C=vendor page, D=inference
**Addendum 1 (2026-11-11):** owner-directed incumbent check — Palantir (Apollo, Rubix, PFCS Forward, AIP for Defense, Security Forge) + India availability.

## Verdict on the pitch claim

**Claim:** "a vendor-neutral layer that governs AI coding inside the wall is still unclaimed."

**Verdict: holds with caveat — and the caveat has narrowed.** The claim **fails** if read as "no incumbent sells an air-gapped, governed, auditable AI coding assistant." It **fails harder** than W7 first assessed: Palantir has productised the control-plane thesis itself. It **holds** only in its narrowest form — *no vendor ships a vendor-neutral policy-and-ledger layer that governs replaceable, competing agents across the non-security engineering workflow (requirements → code → tests → change impact) with provenance-checked offline intake and an accreditation evidence pack.*

Ironically, Palantir **strengthens** the vendor-neutrality wedge while **destroying** the "governance is unclaimed" wedge. Governance is now claimed — by Palantir (stack-locked, cyber-scoped), Tabnine, Codeium, GitLab Duo, Cline Enterprise. The only clean ground left is **vendor-neutrality + non-security engineering scope + multi-vendor agent coverage**.

## 1. Enterprise self-hosted coding assistants W1 missed

| Solution | Air-gapped | SSO/RBAC | Audit logs | Admin policy | Agent capabilities | Models | Offline update | Pricing | Source/grade |
|---|---|---|---|---|---|---|---|---|---|
| Tabnine Enterprise | Yes (A) | Yes (C) | Yes (C) | Yes (C) | Yes — SDLC agents (C) | Anthropic/OpenAI/Google/OSS, BYOK/local (C) | Human-mediated (C) | $39/user/mo annual; Ent custom (C) | docs.tabnine.com (A), tabnine.com/pricing (C) |
| Sourcegraph Cody Ent. | Self-hosted; air-gap not explicit (C) | Yes — SAML/OAuth, repo perms (C) | Yes — event analytics (C) | Yes (C) | Yes — writes/edits, OpenCtx (C) | Claude 3.5, GPT-4o, Gemini 1.5, Mixtral; BYOK/Ollama (C) | Not documented (D) | Contact sales (D) | sourcegraph.com (C) |
| Codeium / Windsurf | Yes — zero third-party deps (C) | Yes — RBAC via AD/Okta/SCIM (C) | Yes — audit logging, AI-code trail (C) | Yes (C) | Yes — Cascade agentic IDE (C) | In-house + GPT-4o, Claude 3.5 (C) | Not documented (D) | ~$20–39/mo (C) | codeium.com/enterprise (C) |
| GitLab Duo Self-Hosted | Yes — Offline Cloud Licence, documented procedure (A) | Yes — via GitLab SSO/RBAC (A) | Yes — llm.log, usage tracking (A) | Yes — AI Catalog governance (A) | Yes — Duo Agent Platform, Code Review, RCA (A) | vLLM, Bedrock, Azure OpenAI, GitLab-managed (A) | Documented — transfer images+weights, start AI Gateway+vLLM (A) | Duo Enterprise add-on (A) | docs.gitlab.com (A) |
| JetBrains AI Enterprise | Not found (D) | Not found (D) | Not found (D) | Not found (D) | Not found (D) | Not found (D) | Not documented (D) | Not found (D) | — |
| Refact.ai | Local-first, no explicit air-gap claim (C) | Not found (D) | Not found (D) | Not found (D) | Yes — autonomous agent (C) | Any via BYOK; Ollama/LM Studio/vLLM (C) | Not documented (D) | Ent custom; cloud shut down 2026-04 (C) | refact.ai (C) |

## 2. Palantir — what it actually governs (owner Q1)

**Answer: yes, materially — for security-scoped software engineering, and it is stack-locked, not vendor-neutral.**

- **Security Forge** (official product page): model-agnostic AI reviewer platform. "Chained AI agents inspect code, deployments, and security boundaries"; "Ontology-grounded Triage" evaluates findings against source, ownership, dependencies, prior incidents; engineers get findings with "remediation paths" and "the same tooling can be handed to agents for automated downstream fixes"; "Apollo-powered Rollout" recalls affected package versions fleet-wide and rolls forward to patched releases; **"Every agent log, severity score, and remediation step is captured in the Ontology"**; "Security review pipelines are not locked to a single model family." [A]
- **Palantir blog (2026-08-20)**: "operating capabilities for multi-agent source-code review, analyst-directed vulnerability hunting, product-team triage, and runtime validation… we have also productionized our model-agnostic AI reviewer platform — called Security Forge — for customers to use." "AIP's orchestration and control mechanisms ensure that agents operate within approved boundaries while preserving the evidence behind every finding." "Apollo eliminates this gap, providing a single, auditable control plane that spans the full lifecycle from alert generation to confirmed remediation without requiring manual intervention." "Security Forge includes the Foundry, AIP, and Apollo platforms… an integrated solution that customers can use in their own environments." [A]
- **Foundry Code Repositories AIP features** (docs): AIP Assist for code comprehension, Code explanation, Find bugs, Translate (Python/SQL/Mesa/Java), **"AI error enhancer" = "proposed code changes"**, Python-only autocomplete. [A]
- **Apollo** (FedRAMP marketplace package doc): "real-time vulnerability scanning with SBOM and CVE visibility into deployed services"; Air-gapped/Highside; "Apollo-powered" rollout. [A]
- **PFCS Forward (2026-02-12)**: DISA IL5/IL6 authorisation extended to on-prem + edge; "authorize once, use everywhere"; Apollo "supports both opportunistic and air-gapped update workflows" in DDIL. [A]
- **Not found for Palantir:** requirements traceability; functional unit-test generation for customer software (AIP Evals generates tests/evaluators for *LLM-backed functions*, not customer code); change-impact analysis; general (non-security) defect investigation; legacy modernization. [D]

**Consequence:** the "immutable approval ledger + sandboxed agent execution + auditable control plane" moat element is **no longer unclaimed** — Security Forge claims it for cyber workflows, and it is a full-platform attach sale (Foundry + AIP + Apollo required), i.e. the **opposite of vendor-neutral**.

## 3. Palantir — availability to Indian buyers (owner Q2)

**Answer: not found.**
- PFCS Forward blog is scoped "For US Government Customers" and "For Industry Partners: Software Vendors"; accreditation is DISA/eMASS/FedRAMP — US bodies only. [A]
- FedRAMP marketplace package lists AIP, Apollo, Apollo Agent, Foundry, Gotham — all US accredited services. [A]
- No Indian subsidiary, office, contract, or regional certification for Apollo/Rubix/PFCS Forward/AIP for Defense found in any official source. "India" appears only as an entry in Palantir's website country-selector dropdown — marketing localisation, **not** availability evidence. [D]
- Palantir localises product docs into en/jp/kr/zh — Japan/Korea/China, **not** India. [D]

**India-specific incumbent found (bigger threat to the India wedge than Palantir):** **Innefu Labs** (New Delhi; founded 2010; Series B USD 30M, 2026-06-05; revenue > ₹100 crore; 100+ critical deployments; empanelled by India's National e-Governance Division as an AI solutions provider for government ministries). Product **Sarvagata AI — "Air-Gapped Sovereign Agentic AI in a Box"** with autonomous agent workflows and a private knowledge base; 100+ installations across the Indian subcontinent, Middle East and SE Asia; describes building an LLM "designed specifically for defence and intelligence use, trained, deployed, and run entirely within air-gapped infrastructure." [A for company/product statements on innefu.com; B/C for the third-party market analysis]
- **Not found:** that Sarvagata AI governs *software engineering* (code comprehension, test generation, patch proposals). Its published workflows are intelligence fusion, OSINT, forensics, fraud detection, predictive policing. [D]
- **Inference:** local-content and government-empanelment rules make a foreign vendor-neutral layer harder to sell in Indian public defence than a domestic incumbent — the single most decision-relevant new fact for the India beachhead. [D]

## 4. Re-check: Legion, NVIDIA NIM / AI Enterprise, Red Hat OpenShift AI

- **Legion Centurion:** governed agentic platform, IL2–IL6, air-gapped, FedRAMP High, human-in-the-loop, attribution/audit, rollback updates, model-agnostic. National-security buyer via SIs (~350-user ceiling); workflows = intelligence/operational reporting, **not software engineering**. Remains DC-near. [A/C]
- **NVIDIA NIM / AI Enterprise:** inference platform only; documented air-gap execution (pre-stage → transfer → `--network none`). No agent runtime, no approval gates, no workflow SBOM/provenance ledger. Not a governed coding agent. [A]
- **Red Hat OpenShift AI:** disconnected/air-gapped support, Private AI on-prem/disconnected mode, MCP servers, AgentOps governance, Dev Spaces isolated execution for AI coding agents. Platform layer moving toward governed coding agents; no engineering approval ledger or SDLC accreditation evidence pack. [A/C]

## 5. Cline, Continue, LocalPilot, Sovereign — identity/audit/update (W1 open question 1)

- **Cline:** Apache 2.0 OSS + Cline Enterprise — SSO (SAML/OIDC), RBAC, central policy, OpenTelemetry audit trails, model/tool controls, remote config, self-hosted/on-prem/VPC; offline-capable with local models. **Has identity/audit at enterprise tier.** [B/C]
- **Continue:** reportedly unmaintained post-Cursor acquisition (final 2.0.0). No enterprise control plane in docs; treat as open foundation you own operationally. [B; needs direct repo verification for A]
- **LocalPilot:** 261 installs, 0 ratings, MIT. No identity/audit/RBAC/update-lifecycle published. [C]
- **Sovereign Agent:** loopback guard, remote endpoints blocked. GPL-3.0. 18 installs. No identity/audit/RBAC/update-lifecycle published. [C]

**Conclusion:** the identity/audit gap at the enterprise end is **not real** — Tabnine, Codeium, GitLab Duo and Cline Enterprise all publish SSO/RBAC/audit. The remaining gap is engineering-workflow governance, and Palantir has now closed part of that too.

## Control-plane claim map (detail in MOAT.md)

| Element | Status | Claimed by |
|---|---|---|
| Air-gapped deployment | TAKEN | Tabnine, Codeium, GitLab Duo, NIM, OpenShift AI, Legion, Palantir Apollo, Vault-OS |
| SSO/RBAC identity | PARTLY CLAIMED | Tabnine, Codeium, GitLab Duo, Cline Enterprise, Legion, Palantir AIP |
| Audit logs / observability | PARTLY CLAIMED | Tabnine, Codeium, GitLab Duo, Cline Enterprise, Palantir (Ontology-captured agent logs) |
| Admin policy / model & tool controls | PARTLY CLAIMED | Tabnine, Cline Enterprise, Codeium, GitLab AI Catalog, Palantir AIP |
| IDE coding agent | TAKEN | Cline, Continue, Tabnine, Codeium Cascade, GitLab Duo Agent Platform, Palantir Code Repositories AIP |
| Model-agnostic multi-agent orchestration w/ boundaries + preserved evidence | **TAKEN (cyber-scoped)** | **Palantir Security Forge (Foundry+AIP+Apollo)** |
| Governed **non-security** engineering workflow (requirements→code→tests→change-impact) | **UNCLAIMED** | — |
| Provenance-checked asset intake + SBOM | PARTLY CLAIMED | Anchore, Sonatype, GitLab, Legion HBOM, **Palantir Apollo (SBOM+CVE on deployed services)** |
| Sandboxed execution + immutable approval ledger over eng. changes | **PARTLY CLAIMED (security workflows)** | **Palantir Security Forge / Apollo**; Cline Plan/Act is per-developer only |
| In-boundary / offline update lifecycle | PARTLY CLAIMED | GitLab Duo (documented), Testkube (offline licence), Legion (rollback), **Palantir Apollo (air-gapped update workflows, CDS, PFCS Forward)** |
| Accreditation evidence pack for eng. workflow | **UNCLAIMED** | — (Palantir's PFCS Forward is a deployment-accreditation package, not an engineering-workflow evidence pack) |
| **Vendor-neutral policy/ledger layer governing competing agents** | **UNCLAIMED** | — (Palantir is stack-locked; every coding assistant requires its own IDE/agent) |

## 3 most defensible features to build first

1. **Vendor-neutral approval + attribution ledger** over *replaceable, competing* agents and engineering artifacts (diffable, rejectable, exportable evidence pack). The only element no incumbent can ship without cannibalising itself.
2. **Provenance-checked, in-boundary asset/model intake with signed offline updates** (TUF-style). Partially claimed in supply-chain and deployment layers, unclaimed as an integrated engineering-workflow control point; still the strongest wedge-in per W1 finding #3.
3. **Deterministic policy engine over replaceable agents** (scoped principals, tool allowlists, kill switches, fail-closed) — the control plane, not the agent. Vendor-neutrality is the feature, not a side effect.

## Recommended pitch wording

**Do not say:** "a vendor-neutral layer that governs AI coding inside the wall is still unclaimed." Palantir Security Forge, Tabnine, Codeium, GitLab Duo and Cline Enterprise all govern AI coding inside the wall.

**Say instead:** "Palantir's Security Forge proved the model — model-agnostic agents, an auditable control plane, evidence preserved behind every finding, rollout through a disconnected control plane. But it is locked to the Palantir stack and scoped to cyber defence. Tabnine, Codeium, GitLab Duo and Cline Enterprise each govern the *developer*, inside their own product. Nobody ships a vendor-neutral layer that governs *competing* agents across the full non-security engineering workflow — requirements, code, tests, change impact — with provenance-checked offline intake and an accreditation evidence pack. That is the layer we own."

## Open questions

1. Does Palantir Security Forge's scope expand beyond cyber into requirements traceability, functional test generation, change-impact analysis, or general defect investigation? (Determines whether the remaining engineering-workflow moat is real or already timed-limited.) [D]
2. Does Innefu Labs' Sarvagata AI extend to software-engineering workflows, or is it purely intelligence/operational? And can a vendor-neutral foreign layer clear Indian government empanelment/local-content rules? (Largest India-specific threat — Gate A/C.) [D]
3. Will air-gapped buyers pay a premium for an accreditation evidence pack, or treat governance as satisfied by Tabnine/GitLab Duo/Palantir? [D]
4. Is Cline Enterprise's on-prem/air-gapped offering genuinely sold and deployed, or only documented? (Grade B/C — needs customer reference.) [D]
5. Should the wedge interoperate with GitLab Duo Self-Hosted and Palantir (already inside target estates) rather than displace them? (Integration target vs competitor per W1 C-0109.) [D]

## Evidence log

| Claim | Summary | Grade | Source |
|---|---|---|---|
| Palantir Security Forge is a shipped customer product | Model-agnostic AI reviewer; chained agents; Ontology-grounded triage; agent logs/severity/remediation captured in Ontology; not model-family-locked | A | palantir.com/security-forge (2026-11-11) |
| Palantir governs AI coding/engineering work | "multi-agent source-code review… patch development… productionized… Security Forge"; AIP "preserving the evidence behind every finding"; Apollo "single, auditable control plane" | A | blog.palantir.com/securing-software-at-the-speed-of-ai (2026-08-20) |
| Palantir code comprehension + patch proposals | AIP Assist, Code explanation, Find bugs, Translate, "AI error enhancer… proposed code changes" | A | palantir.com/docs/foundry/code-repositories/aip-features (2026-11-11) |
| Palantir requirements traceability / functional test gen | Not found; AIP Evals targets LLM-backed functions | D | palantir.com/docs/foundry/aip-evals/overview (2026-11-11) |
| Palantir air-gapped updates + IL5/IL6 | DISA authorisation of PFCS Forward; Apollo opportunistic + air-gapped update workflows; SBOM/CVE scanning | A | businesswire.com PFCS release (2026-02-12); blog.palantir.com/introducing-pfcs-forward; github.com/palantir/palantir-fedramp-marketplace |
| Palantir India availability | Not found; PFCS Forward scoped "For US Government Customers"; no India subsidiary/contract/certification located | D | blog.palantir.com/introducing-pfcs-forward (2026-11-11) |
| Innefu Labs is the India incumbent | Sarvagata AI air-gapped sovereign agentic AI in a box; USD 30M Series B; >₹100 cr revenue; 100+ deployments; NeGD empanelled | A/B/C | innefu.com; innefu.com/press-release Series B (2026-06-05); sacra.com/c/innefu-labs; businessreporter.in (2026-08-10) |
| Tabnine air-gapped + SSO/RBAC/audit/agents | Private installation air-gapped; SSO, RBAC, usage metrics, provenance, SDLC agents | A/C | docs.tabnine.com; tabnine.com/pricing; tabnine.com/platform (2026-11-11) |
| Codeium self-hosted air-gapped + RBAC + audit | "air-gapped deployments with zero third party dependencies"; RBAC via SCIM; audit logging | C | codeium.com/enterprise; windsurf.com blog (2026-11-11) |
| GitLab Duo Self-Hosted air-gapped documented | Offline Cloud Licence; deploy: transfer images+weights, start AI Gateway+vLLM | A | docs.gitlab.com/.../offline_deployment/; support.gitlab.com (2026-11-11) |
| Cline Enterprise SSO/RBAC/audit/offline | SSO SAML/OIDC, RBAC, OpenTelemetry audit trails, local models offline | B/C | cline.bot/teams; docs.cline.bot/enterprise-solutions (2026-11-11) |
| Continue unmaintained | Final 2.0.0 post-Cursor acquisition; migrate to Cline | B | fast.io/resources/cline-vs-continue/ (2026-07-16) |
| LocalPilot/Sovereign no governance | 261/18 installs; no identity/audit/RBAC published | C | VS Marketplace (2026-11-11) |
| Legion governed but not engineering | IL2-IL6, air-gapped, human-in-the-loop; operational workflows only | A/C | legionintel.com/platform; /centurion (2026-11-11) |
| Red Hat OpenShift AI disconnected + agent governance | Private AI disconnected mode; MCP servers; AgentOps; Dev Spaces isolated execution | A/C | redhat.com/en/products/ai/openshift-ai; developers.redhat.com (2026-11-11) |
