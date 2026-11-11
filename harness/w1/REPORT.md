# W1 — Competitor / Substitute Map: Air-Gapped AI & Secure Engineering Automation

**Agent:** W1 — B2B Infrastructure Market Intelligence Lead · **Produced:** 2026-11-11 · **Schema:** `02_INDEPENDENT_RESEARCH_AGENT_PROTOCOLS.md` §6
**Full matrix (27 solutions, 14 fields each):** [`harness/w1/COMPETITOR_MATRIX.md`](./COMPETITOR_MATRIX.md)

---

## 1. Verdict

**No product in the surveyed set is a direct competitor of the wedge** (secure, offline, agentic *engineering* workbench for enterprise software teams). Two products come close; neither addresses the same buyer or the same workflow.

The competitive reality is **compositional, not head-to-head**. Four findings, in order of importance:

1. **The market is already fully supplied at every layer except the governance/lifecycle layer.** Inference (NVIDIA NIM, vLLM, SGLang, llama.cpp, Ollama), disconnected Kubernetes (OpenShift, RKE2, K3s, GDC), SBOM/artifact governance (Anchore, Sonatype SAGE, GitLab), offline RAG (deepset, Elastic+Jina, ONES), local coding agents (Cline, Continue, LocalPilot, Sovereign, LocalCode, DeskAI, llm-local-assistant, offgrid) — every layer has a credible, sometimes accredited, sometimes documented-air-gap product. **The wedge cannot win on any of these layers and must not try.**
2. **The genuinely underserved layer is governance + lifecycle + evidence.** Across five independently-built local coding agents, *none* publishes an enterprise identity model, RBAC, scoped agent principals, an immutable action/approval ledger, SBOM/provenance intake, signed asset verification, an air-gap update path, or accreditation evidence packs. The agent *capability* layer is commodity and free. **The wedge's product must be the control plane around a replaceable agent**, not a better agent. *(Grade C — five marketplace listings, 2026-11-11.)*
3. **Disconnected update lifecycle is the market's unsolved common problem — the wedge's strongest wedge-in.** Seven vendors each hand-rolled a different mechanism (OpenShift's mirroring cadence, Testkube's offline licence, Anchore's on-prem Feed Service, Legion's rollback-capable model updates, Vault-OS's signed USB payloads, SpaceGrade's encrypted USB, Salian's in-boundary updates). Nobody has standardised it. *(Grade A — official docs across seven sources.)*
4. **The dominant threat is substitution, not competition.** An SI (Forge, Salian, Intumit) or an appliance chassis (Element 31, SpaceGrade, Vault-OS, GDC appliance) can assemble the same function per deal and absorb the wedge's value without any of it appearing as a competitor. Element 31's model is explicit: the ISV's software becomes the image, the chassis vendor owns delivery. *(Grade C/D.)*

**Consequence for positioning.** The defensible claim is not "we work offline" (NIM, GDC, Testkube, Legion, Vault-OS all do) and not "we do agentic coding" (Cline does, free). It is: *a governed, auditable, provenance-checked engineering workflow that can be installed, updated and evidenced with no outbound path* — assembled on replaceable OSS layers, sold with an accreditation-evidence pack. This claim is **not yet proven**; it is a hypothesis (D) that the Layer 3 and Layer 6 passes must test.

**Two unverified findings that change the picture if confirmed:** (a) Continue is reportedly unmaintained post-Cursor acquisition (B — verify the repo); (b) Legion Centurion is an accredited IL2–IL6 air-gapped agentic platform with SBOM/HBOM and rollback-capable model updates (C — verify accreditations). If (b) adds engineering workflows, the direct-competitor count becomes 1.

---

## 2. Competitor matrix (27 solutions — full detail in COMPETITOR_MATRIX.md)

**Class:** DC = direct competitor · DC-near = integrated, different buyer/workflow · ADJ = adjacent layer · OSS = open-source substitute · CB = customer-built/integrator.

| # | Solution | Class | Layer | Offline evidence (grade) | License | Pricing evidence | Key limitation |
|---|---|---|---|---|---|---|---|
| A1 | NVIDIA NIM LLM/VLM | ADJ | Inference | Documented air-gap runbook: pre-stage → transfer → `--network none`, no API keys (**A**) | Proprietary | Per-GPU, no figure captured (D) | NVIDIA-only; asset prep is customer labour |
| A2 | Lamini | ADJ | Tuning+inference | "air-gapped" self-managed asserted; **no runbook** (C) | Proprietary | Starter $250/yr; self-managed per-GPU, Custom (C) | Narrow models; air-gap unproven; no provenance |
| A3 | Red Hat AI Inference Server | ADJ | Inference on K8s | "air-gapped out of the box" on disconnected OpenShift, `oc-mirror` (A) | Subscription | Not captured (D) | Heavy; disconnected upgrade tax |
| A4 | vLLM | OSS | Inference | Documented offline-inference mode (A); **no air-gap lifecycle** | Not verified (D) | Free + GPU (C) | DIY: identity, audit, upgrades all yours |
| A5 | llama.cpp | OSS | Inference | Self-contained GGUF, transferable (A) | Not verified (D) | Free (C) | Quantisation quality ceiling; agentic weak at small sizes |
| A6 | SGLang | OSS | Inference | NIM backend incl. air-gap (A) | Not verified (D) | Free (C) | Documented backend failure on Grace Hopper/ARM |
| B1 | OpenShift Container Platform | ADJ | Cluster | Disconnected/air-gap/restricted docs + `oc-mirror` (A) | Subscription | Not captured (D) | Expensive; recurring disconnected-upgrade burden |
| B2 | OKD | OSS | Cluster | Maintained disconnected docs (4.17/4.18/4.21) (A) | Open | Free (C) | No commercial support for accredited programmes |
| B3 | RKE2 / K3s | OSS | Cluster | Dedicated air-gap install docs (A) | RKE2 subscription / OSS | Not captured (D) | **RKE2's hardened-by-default posture is the strongest open substrate fit** |
| B4 | Google Distributed Cloud | ADJ+CB | Managed K8s + appliance | "Fully disconnected: Yes"; IL5 appliance (A) | Proprietary | Not captured (D) | Total Google stack dependency; ~45 kg; not operable in transit |
| B5 | Testkube On-Prem | ADJ | Test execution | Complete disconnected install + per-release manifest + **offline licence** (A) | Open-core + licence | Not captured (D) | Different layer; but best-documented offline lifecycle found |
| B6 | IBM Cloud Pak / Content Cortex / BAW | ADJ | App platform | CASE + `ibm-pak` air-gap install, 3 product lines (A) | Proprietary | Not captured (D) | "Tanzu does not support offline deployment" |
| C1 | Cline (+Ollama) | OSS | Coding agent | Local-Ollama path; **telemetry must be separately disabled** (B) | Not verified (D) | Free (C) | Model-tier bound (≥13–30B); no governance layer |
| C2 | Continue | OSS | Coding agent | Offline via local models (B) | Not verified (D) | Free (C) | **Reportedly unmaintained post-Cursor acquisition (B — verify repo)** |
| C3 | LocalPilot Agent | OSS | Coding agent | "Unplug the network: it keeps editing, running tests" (C) | MIT (C) | $0/mo; cites cloud at $8–200/dev (C) | **261 installs, 0 ratings**; no governance |
| C4 | Sovereign Agent | OSS | Coding agent | Loopback guard; remote endpoints hard-blocked (C) | **GPL-3.0-or-later** (C) | Free (C) | **18 installs**; GPL-3.0 reciprocal-licensing question |
| C5 | LocalCode | OSS | Coding agent | "Offline-capable once models are downloaded" (C) | MIT (C) | Free (C) | v0.1.0; no identity/audit/provenance |
| C6 | DeskAI | OSS | Coding agent | "100% offline", bundles llama-server (C) | Not stated (D) | Free (C) | **159 installs**; 12 GB+ RAM floor; first-launch model download |
| C7 | llm-local-assistant | OSS | Coding agent | "No internet required" (C) | MIT (C) | Free (C) | Author-documented "Cross-File Contract Drift" limitation |
| C8 | offgrid | OSS | Coding agent | One-time download then local (C); **SHA-256 verified models** | MIT (C) | Free (C) | **14 installs**; completion-only triggers |
| C9 | Coder | ADJ | Remote dev env | "All features supported air-gapped"; offline licence + air-gapped images/docs (A) | Proprietary | Not captured (D) | **VS Code Remote-SSH needs outbound HTTPS to 3 MS hosts — IDE must be pre-staged** |
| D1 | Anchore Enterprise | ADJ | SBOM/supply chain | Air-gapped IL6 on-prem; on-prem Feed Service (A/C) | Open-core + Ent | Pricing page unfetched (D) | Provenance layer, no agentic workflow |
| D2 | Sonatype SAGE | ADJ | Supply chain | "fully disconnected" Lifecycle + offline SBOM (C) | Proprietary | Not captured (D) | Supply-chain layer only |
| D3 | GitLab Self-Managed | ADJ | DevSecOps | Per-scanner offline directions, metadata DB load (A) | Free + paid tiers | Not captured (D) | **More a wedge integration target than a competitor** |
| D4 | SBOM Central (t2data) | ADJ | SBOM mgmt | Explicit air-gapped mode (C) | Proprietary | Not captured (D) | Smaller vendor; SBOM layer only |
| E1 | deepset Haystack Ent. Platform | ADJ | RAG/agent platform | Air-gapped deployment + documented degradations (A) | Proprietary (on Apache-2.0 Haystack) | Contact sales (C) | Not an engineering workbench; external services must be self-hosted |
| E2 | Elastic + Jina On-Prem | ADJ | Search/retrieval | ELSER air-gapped deploy guide (A); Jina On-Prem (C) | Elastic tiers + Jina | Not captured (D) | ELSER is English/out-of-domain; no fine-tuning on your data |
| E3 | Varuni Systems | CB | Vertical AI/RAG | Air-gapped, "nothing calls out" (C) | Services | Engagement (C) | Capability statement, not a product |
| E4 | ONES / Danswer / AnythingLLM | ADJ+OSS | Knowledge | Air-gapped reviews; self-hosted (C) | Mixed | Confirmed w/ vendor (C) | Knowledge layer; OSS tools **not audit-ready out of the box** |
| F1 | **Legion Intelligence — Centurion** | **DC-near** | Integrated agentic platform | Fully air-gapped, IL2–IL6, offline-first, rollback model updates (A) | Proprietary | Demo only (C) | **National-security buyer via SIs; ~350-user ceiling; no engineering workflow** |
| F2 | **Element 31 — Czar/Substrate** | **DC-near** | Appliance delivery | Sealed air-gapped units for ISVs (C) | Per-deal | Deal-specific (C) | **ISV owns the customer — displaces standalone software** |
| F3 | Vault-OS | DC-near | Appliance | 0 packet egress, TPM 2.0 binding, signed USB updates (C) | Proprietary | Pricing page + sizing calc (C) | Knowledge/HR workflows, not engineering |
| F4 | GDC air-gapped appliance | ADJ+CB | Hardware+cloud | Physically isolated, IL5, managed Harbor (A) | Proprietary | Not captured (D) | Update mechanics for a handed-over sealed unit = **Grade D gap** |
| F5 | SpaceGrade OS | CB | Appliance | Fully air-gapped SG-3; encrypted-USB updates (C) | Proprietary + per-seat | **$35,000+ hardware; $24,000/yr + $89–149/seat** (C) | PLM domain — **best pricing anchor found** |
| F6 | Strike48 | ADJ | SecOps appliance | Air-gapped on-prem, local GPU via PCI passthrough (C) | Proprietary | Demo only (C) | Cybersec domain; but proves the appliance shape is productised |
| F7 | Salian Defense | CB | Defence integrator | Fully offline; in-boundary updates required (C) | Services | Engagement (C) | Programme model; **digital-twin validation method is transferable** |
| F8 | Forge AI Deployment | CB | Systems integrator | Offline install/update paths; enumerated egress (C) | Services over webAI | None published (C) | **"Systems integrator, not a software reseller" — owns the whole path** |
| F9 | Intumit | CB | A&D AI platform | Air-gapped / offline-capable agents (C) | Proprietary | Not captured (D) | Defence workflows, not engineering; sells into the SI channel |

**Customer-built / integrator-assembled substitutes (the real alternative):** CB-1 DIY stack (local model + Cline + OpenShift + Anchore) · CB-2 integrator assembly (Forge, Salian, Intumit) · CB-3 appliance chassis (Element 31, SpaceGrade, Vault-OS, GDC) · **CB-4 do nothing / existing internal tooling** · CB-5 accredited incumbent (Legion Centurion) · CB-6 rebuild on GDC appliance. **CB-4 is the least-evidenced and most consequential entry** (D, no source) and is the priority gap for customer discovery.

---

## 3. Evidence log

**Grades:** A = official docs/spec/procedure states it · B = independent technical evaluation · C = vendor page/marketplace/blog (indirect) · D = my inference.
**Method limits (material):** verification was at **excerpt level** from official documentation and vendor pages. **No source code, LICENSE file, test suite or release history was inspected** — protocol Layer 3 is *not covered* by this pass. No demo/trial/pilot was evaluated. Marketing-derived claims (accreditations, customer logos, "first to market") are capped at C.

| Claim | Summary | Grade | Key sources (all accessed 2026-11-11) |
|---|---|---|---|
| C-0101 | No surveyed product supplies the complete wedge to enterprise software teams | **D** | Aggregate S1–S55; counter: F1 |
| C-0102 | Local coding-agent layer: strong for individuals, empty at the enterprise/accredited end (261/18/159/14 installs, 0 ratings; no identity/audit/provenance/update-lifecycle published) | **C** | S24–S29 |
| C-0103 | Disconnected update lifecycle is the binding cross-market constraint — 7 vendors each hand-rolled a mechanism | **A** | S8, S18, S34, S47, S50, S51, S54 |
| C-0104 | The IDE itself needs internet (VS Code Remote-SSH → 3 MS hosts; JetBrains/code-server exceptions) — offline workbenches must pre-stage the IDE | **A** | S30 |
| C-0105 | An ISV/appliance chassis can displace a standalone product without competing with it (ISV's nameplate + support line on a sealed unit) | **D** | S49 |
| C-0106 | "Do nothing" is the least-evidenced, most consequential alternative | **D** | none — gap |
| C-0107 | NIM's air-gap is an *asset-preparation* procedure, not an offline *lifecycle* (no API keys needed on the air-gapped host) | **A** | S2, S3 |
| C-0108 | Two vendors (Legion, Vault-OS) already ship signed/rollback-capable offline update mechanisms — the wedge's proposed differentiator is partially claimed | **C** | S47, S50 |
| C-0109 | GitLab Self-Managed is more a wedge integration target than a competitor — the estate already owns it | **A** | S38 |
| C-0110 | Air-gap cost anchor: $35,000+ hardware / $24,000 per year / $89–149 per seat for an accredited-class appliance bundle | **C** | S51 |

**Source register:** all 55 sources (titles, URLs, publish dates, grades) are listed in `COMPETITOR_MATRIX.md` §9. Principal primary sources: NVIDIA NIM air-gap (S2), OpenShift disconnected ops (S8), Coder air-gap (S30), GitLab offline (S38), deepset deployment options (S40), Elastic ELSER air-gap (S43), GDC appliance (S17), Testkube air-gapped (S18).

---

## 4. Open questions (ranked by decision impact)

1. **Is the "governance + lifecycle" gap real at the enterprise end, or is it just unpublished by small maintainers?** *Check:* inspect the five local coding agents' source and docs for identity/audit/update features; hunt for any enterprise-grade local coding agent not surfaced by search. **If the gap is only "unpublished", the wedge has no product.** *(Gate: W1→W3)*
2. **Does Legion Centurion or any national-security vendor move into engineering workflows?** *Check:* IL2–IL6 vendor procurement records, GSA/DoD schedules, archived Centurion release notes. **If yes → DC count becomes 1 and the wedge must either partner or pivot.** *(Gate: differentiation)*
3. **What does the "do nothing" baseline actually cost?** *Check:* customer interviews — current workflow, engineer-hours, defect/escape rate, what is already automated. **Unmeasured baseline = unmeasurable value.** *(Gate: Gate D)*
4. **Can the wedge be sold as software into an appliance-chassis deal, or must it become the image?** *Check:* SI interviews on Element 31-style engagements; who owns the software selection. *(Gate: commercial)*
5. **Do the local agent models clear a useful quality bar on realistic multi-file engineering tasks at customer-class hardware?** *Check:* run the local models on a real repo; tier-constraint is already documented (C1: ≥13–30B for credible multi-step; B-grade).
6. **What is the actual accreditation burden and who pays it?** *Check:* which accreditation (IL4/IL5/IL6, FedRAMP, CMMC, NIST 800-171) is required by the target buyer, and whether the wedge can produce evidence vs. merely support a customer in producing it.
7. **Open-source licence and maintenance audit** (protocol Layer 3): Continue's real status (B-grade claim); LICENSE files for vLLM, llama.cpp, SGLang, Cline, Continue, LocalCode, LocalPilot, Sovereign (GPL-3.0), llm-local-assistant, offgrid, Syft/Grype.
8. **Pricing reality** — the weakest-evidenced field: Anchore, Sonatype, Red Hat OpenShift AI, GitLab, deepset, Elastic. Only NIM, Lamini, SpaceGrade, Vault-OS currently have any pricing signal.
9. **Air-gap update mechanics for GDC appliance (S17) and deepset (S40)** — both Grade D, both plausible wedge targets.
10. **Vendor update-cadence reality** — does any platform support *unsupervised* offline update, or is every "update" a human-run media transfer? (Evidence so far: every one is human-run.)

---

## 5. Handoff

**Do not build** a model runtime, a cluster manager, a coding agent, an SBOM tool or an appliance — all five layers are occupied and each is a credible standalone product. **Do not build** a generic "offline AI platform"; three already exist as accredited products (Legion, GDC appliance, Vault-OS).
**Build, if the Gate D value is real:** the governed engineering control plane — deterministic policy over replaceable agents, provenance-checked asset intake, sandboxed execution with an immutable approval ledger, in-boundary updates, and an accreditation evidence pack.
**Immediate next actions:** (1) verify the five local coding agents' source and docs; (2) start customer discovery with CB-4 as the baseline; (3) brief the adversarial committee (Agent 12) on C-0101, C-0105 and C-0106, which are the three claims most likely to be wrong.
