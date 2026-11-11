# W1 — Full Competitor / Substitute Matrix

**Agent:** W1 — B2B Infrastructure Market Intelligence Lead
**Produced:** 2026-11-11
**Schema:** `02_INDEPENDENT_RESEARCH_AGENT_PROTOCOLS.md` §6 (grades A/B/C/D, claim record fields)
**Scope:** 6 categories, 4 competitive classes (DC = direct competitor, ADJ = adjacent platform, OSS = open-source substitute, CB = customer-built / integrator alternative)

---

## 0. Method and caveats (read before using this file)

**What was done.** A search pass over official vendor documentation, official product/pricing pages, and a small number of independent technical reviews, covering all six required categories. Each solution below was matched against the 14 required fields.

**Verification limits (important).**
1. Verification was performed at **excerpt level** from official documentation and vendor pages, not by opening every original page end-to-end. Protocol §6 synthesis rule "Never cite a search-result snippet when the original source can be opened" is therefore **not yet fully satisfied**; grade **C** is applied to everything sourced from vendor marketing/pricing pages and to any capability claim not tied to a specific documented procedure.
2. **No source code, LICENSE file, test suite or release history was inspected in this pass.** Protocol Layer 3 ("Implementations and engineering reality") is therefore **not covered** by W1. Open-source license and maintenance claims in this file are unverified and must be re-graded after direct repo inspection.
3. No product demo, trial, pilot or environment was evaluated. All "customer proof" entries are vendor-published references unless marked otherwise.
4. Grades follow §6 strictly: **A** = original official documentation/spec/procedure states the claim; **B** = independent third-party technical evaluation; **C** = vendor product page, marketplace listing, blog or press release (indirect signal); **D** = my inference, unverified hypothesis.

**Layer discipline applied.** The project wedge (per `01_MASTER_VISION_AND_STRATEGY.md` §5) is a *secure, offline, agentic engineering workbench* for software teams in disconnected environments. A solution is called **DC** only if it sells that whole stack (engineering workflow + local reasoning + governed execution + provenance/air-gap lifecycle) to that buyer. Anything that supplies exactly one layer — inference, orchestration, cluster, SBOM, retrieval, or physical delivery — is **ADJ/OSS/CB** even when its marketing overlaps the wedge. Applying this rule is what keeps the matrix honest.

---

## 1. Classification summary

| Class | Definition applied | Count |
|---|---|---|
| DC | Sells the complete wedge to the wedge buyer | **0** |
| DC-near | Integrated single-product delivery of most of the wedge, but aimed at a different buyer (national security / SI resale) or a different workflow (knowledge not engineering) | 2 |
| ADJ | Supplies one layer of the wedge to the same market | 16 |
| OSS | Free/self-buildable substitute for a layer | 9 |
| CB | Integrator-delivered or customer-internal build; absorbs the wedge per deal | 6 |

**DC = 0 is the headline finding of this pass, and it must not be read as "no competition."** The competitive pressure in this market is *compositional*: customers assemble the stack from ADJ/OSS layers, and SI/appliance vendors (CB + DC-near) will build the missing governance layer per engagement, capturing the value without selling a standalone product. See REPORT.md §1 and §4.

---

## 2. Category A — Enterprise model / inference platforms

### A1. NVIDIA NIM for LLMs and VLMs — ADJ (inference layer)

- **Buyer:** Platform/ML engineering teams and enterprises running GenAI in regulated or disconnected estates; GPU-ops teams that want vendor-curated weights and validated performance.
- **Workflow:** Serve and monitor production LLM/VLM inference (OpenAI-compatible API), package pre-validated weights + manifests + optimised profiles, optionally fine-tune, observe via exported traces.
- **Deployment / isolation mode:** Container (Helm/OCI) on any conformant infra; CSP (AWS/GCP/Azure/OCI) and on-prem. Air-gap: pre-stage model assets to an offline cache or local model store, transfer, then run with no outbound access and no API keys.
- **Offline support evidence:** Dedicated official pages "Enterprise-Grade Inference Software Stack" (states "NIM LLM and VLM fully supports air-gapped execution… without requiring outbound internet access or API keys") and "Air-Gap Deployment" (documented procedure: connected-host asset prep → transfer → `--network none` validation → local model directory). Explicitly requires **no** `NGC_API_KEY`/`HF_TOKEN` on the air-gapped host. **Grade A.**
- **Model / runtime:** Curated model weights + baked manifests + tuned profiles (tensor/pipeline parallelism) for model-specific NIMs; model-free NIM supports programmatic download from NGC, Hugging Face, S3, GCS; vLLM and SGLang backends both covered in air-gap docs. NVIDIA GPU architectures Ampere/Ada/Hopper/Blackwell.
- **Agent capabilities:** Inference platform, not an agent runtime. Tool/function calling, structured generation, observability are exposed as *model-serving* features. No workflow, approval, sandbox or audit ledger. **Different layer — not DC.**
- **Security / identity:** Container image + optional offline cache; enterprise support/packaging layer ("NIM Certified") for government/regulated buyers. No independent identity model for agent principals.
- **Integrations:** Kubernetes via Helm (GPU Operator, probes `/v1/health/ready`, `/v1/health/live`), mirrored registries (S3/GCS), OpenAI-compatible API, NGC, Hugging Face.
- **Updates:** Model assets staged on a connected host and re-transferred; production branch ("PB") isolation offered to shield enterprise deployments from upstream churn. Container tags pinned by operator.
- **License:** Proprietary NVIDIA container distribution; model weights carry their own upstream licenses. Enterprise "NIM Certified" layer adds support/packaging. Exact commercial terms not published on the pages read — **Grade D.**
- **Support model:** Enterprise support layered via NIM Certified; Production Branches for stability.
- **Pricing evidence:** Per-GPU pricing referenced; no numeric figure captured in this pass. **Grade D — pricing fetch pending.**
- **Limitations:** Requires an NVIDIA GPU estate; model-availability in air-gap is bounded by what you pre-stage; air-gap is an *asset-preparation + image-transfer* procedure, so update cadence is an operational burden the customer carries; no agentic workflow, no approval gates, no SBOM/provenance ledger for the workflow itself.
- **Customer proof:** Vendor-stated validated across major CSPs and a hardware-SKU performance matrix. No named air-gapped customer captured. **Grade C.**
- **Sources:** "Enterprise-Grade Inference Software Stack — NVIDIA NIM for LLM and VLM", https://docs.nvidia.com/nim/large-language-models/latest/about-nim-llm/enterprise-grade.html, accessed 2026-11-11, **A**; "Air-Gap Deployment — NVIDIA NIM for LLM and VLM", https://docs.nvidia.com/nim/large-language-models/latest/deploy-air-gap.html, accessed 2026-11-11, **A**; "Air Gap Deployment — NIM for Vision Language Models", https://docs.nvidia.com/nim/vision-language-models/1.4.0/deploy-air-gap.html (updated 2025-09-25), accessed 2026-11-11, **A**.

### A2. Lamini Enterprise LLM Platform — ADJ (tuning + inference layer)

- **Buyer:** ML/platform teams wanting a *single* stack for tuning, evaluation and inference of small task-specific models (classification, text-to-SQL, code triage) with data staying in the customer's environment.
- **Workflow:** Fine-tune / prompt-tune / memory-tune → evaluate → serve, via Python client, REST API and web UI; build "mini-agents" (SLM-based) for high-accuracy classification and extraction.
- **Deployment / isolation mode:** Three documented models — On-Demand (SaaS), Reserved (dedicated GPUs on Lamini infra), Self-Managed (customer's GPUs: on-prem, in VPC, or **air-gapped**). Kubernetes install and AWS EKS setup documented for self-managed.
- **Offline support evidence:** Vendor page and docs explicitly state self-managed runs "in your own environment on your GPUs (on premise, in your VPC, even air-gapped deployments)" and self-managed pricing tier states "No internet access needed." **Grade C** (vendor marketing/pricing page rather than a step-by-step air-gap runbook).
- **Model / runtime:** Open models incl. Llama 3.1, Mistral v0.3, Phi 3; Lamini-hosted "MoME" tuned models; memory tuning with efficient LoRAs and claimed 32× model compression.
- **Agent capabilities:** "Mini-agents" and agentic pipelines, classifier agent toolkit. Orchestration is inside Lamini's platform, not the customer's engineering estate.
- **Security / identity:** Auth setup documented for self-managed (docs `/self_managed/auth_setup/`). Full identity/RBAC depth not verified — **Grade D.**
- **Integrations:** Python SDK, REST API, web UI, Kubernetes, EKS, Hugging Face-adjacent model access.
- **Updates:** Not documented for air-gap in the sources read. **Grade D.**
- **License:** Proprietary; docs carry a "License" page and a per-GPU software license for self-managed. Terms not captured — **Grade D.**
- **Support model:** "Enterprise support" + "access to world-class ML experts" on Reserved and Self-managed.
- **Pricing evidence:** Pricing page shows Starter $250/yr (up to 10 projects, 50 tasks, 1 GB storage); On-demand pay-as-you-go; Reserved "Custom" per-GPU; Self-managed "Custom", **per software license**, per-GPU. **Grade C.**
- **Limitations:** Positioning is high-accuracy *narrow* models, not general coding-agent capability; self-managed price is opaque; air-gap is asserted, not documented as a procedure; no supply-chain/provenance layer for offline model transfer; no sandbox or approval control.
- **Customer proof:** Vendor-published testimonial (Chris Lu, CTO) on classifier SDK speed-to-production; "10k+ user-tuned models" claim. No named air-gapped deployment. **Grade C.**
- **Sources:** "About — Lamini Docs", https://docs.lamini.ai/about, accessed 2026-11-11, **C**; "Pricing", https://www.lamini.ai/pricing, accessed 2026-11-11, **C**; "Product", https://www.lamini.ai/product, accessed 2026-11-11, **C**.

### A3. Red Hat OpenShift AI / Red Hat AI Inference Server — ADJ (cluster + inference layer)

- **Buyer:** Regulated enterprises (regulated sectors named explicitly) operating OpenShift who need supported inference *and* cluster lifecycle in one vendor-supported stack.
- **Workflow:** Deploy LLMs on OpenShift with vLLM runtime; benchmark with GuideLLM; manage cluster, operators, model assets and upgrades through the same subscription.
- **Deployment / isolation mode:** OpenShift Container Platform in fully disconnected state; internal registry (e.g. `registry.apps.<cluster-domain>`); `oc-mirror` to load mirrored content; rsync/USB/SCP across the boundary.
- **Offline support evidence:** Official Red Hat Developer article walks the full disconnected path — mirror registry, `oc-mirror` into the internal registry, deploy Red Hat AI Inference Server with persistent volumes — and states the AI Inference Server "supports air-gapped environments out of the box". **Grade A.**
- **Model / runtime:** vLLM runtime; Whisper speech-to-text; llm-d distributed inference referenced; NVIDIA GPU + Intel Gaudi/AMD operator support.
- **Agent capabilities:** None in-product. Inference + cluster only.
- **Security / identity:** OpenShift SCC/PSA, image signing, operators, catalog mirroring. No agent identity model.
- **Integrations:** Kubernetes/Helm/operators, OpenShift Container Platform, internal registry, oc-mirror, disconnected installation tooling, CUDA/GPU Operator.
- **Updates:** Requires a deliberate **operational cadence** — mirror release payload + images + update-graph metadata, refresh operator catalogs on a schedule, test upgrades in connected staging before promoting. Red Hat's own article frames this as the hard part of disconnected operation. **Grade A.**
- **License:** Proprietary subscription; OpenShift and Red Hat AI are commercially licensed. Terms not captured — **Grade D.**
- **Support model:** Red Hat enterprise subscription support.
- **Pricing evidence:** Not fetched in this pass — **Grade D.**
- **Limitations:** Heavy platform cost and operational load; disconnected upgrade cadence is a named operational tax; solves the *substrate* not the engineering workflow; model curation and workflow governance left to customer.
- **Customer proof:** Article states criticality "for enterprises operating in highly regulated sectors" — no named air-gapped customer captured. **Grade C.**
- **Sources:** "Benchmarking with GuideLLM in air-gapped OpenShift clusters", https://developers.redhat.com/articles/2025/09/15/benchmarking-guidellm-air-gapped-openshift-clusters (2025-09-15), accessed 2026-11-11, **A**; "How to operate OpenShift in air-gapped environments", https://developers.redhat.com/articles/2026/03/19/how-operate-openshift-air-gapped-environments (2026-03-19), accessed 2026-11-11, **A**.

### A4. vLLM — OSS substitute (inference layer)

- **Buyer:** Platform engineers willing to build and own the serving layer.
- **Workflow:** High-throughput LLM serving via OpenAI-compatible API; offline batch inference (documented "offline inference" path) — the natural fit for disconnected batch evaluation and document pipelines.
- **Deployment / isolation mode:** Any container/Kubernetes/GPU host; fully self-contained once images and weights are transferred.
- **Offline support evidence:** Official "offline inference" documentation is referenced in the project's own primary-source register as the offline model-loading path. **Grade A** (existence of documented offline mode), **C** for any stronger lifecycle claim — vLLM provides *no* air-gap *lifecycle* (asset staging, verification, update, provenance).
- **Model / runtime:** Broad model support; paged attention, continuous batching, speculative decoding, tensor parallelism. **License not verified in this pass — Grade D.**
- **Agent capabilities:** None. Tool-calling is a model/serving feature.
- **Security / identity:** None product-level. You own it entirely — which is simultaneously the appeal (no vendor trust boundary) and the burden.
- **Integrations:** OpenAI-compatible HTTP API; OpenTelemetry; Hugging Face hub for weights (network dependency at *stage* time only).
- **Updates:** Manual image + weight pull. No vendor cadence, no support, no signed artifact pipeline.
- **Support model:** Community only (no commercial support from upstream).
- **Pricing evidence:** Free to run; GPU/ops cost borne by customer. **Grade C.**
- **Limitations:** DIY everything else — security posture, identity, audit, upgrade discipline, vulnerability management all become the customer's problem. Strongest *substitute* for the inference layer, weakest for everything else.
- **Customer proof:** Broad production adoption implied by NIM/RHEL positioning NIM as "curated" relative to upstream OSS. **Grade C.**
- **Sources:** "Offline inference — vLLM documentation", https://docs.vllm.ai/en/latest/serving/offline_inference/, accessed 2026-11-11, **A**; project primary-source register `01_MASTER_VISION_AND_STRATEGY.md` §12, accessed 2026-11-11, **A**.

### A5. llama.cpp — OSS substitute (inference layer)

- **Buyer:** Developers needing CPU/GPU-local inference with minimal footprint, or a GGUF model path; teams that must run on whatever hardware the site already owns.
- **Workflow:** Local text/embedding inference from GGUF weights; used by several surveyed VS Code extensions as the bundled runtime (DeskAI, offgrid).
- **Deployment / isolation mode:** Single binary; fully offline after weight download. Deployable as the runtime *inside* an air-gapped appliance (SpaceGrade OS ships Ollama; Vault-OS ships a local inference layer).
- **Offline support evidence:** The project register lists llama.cpp as a primary deployment reference. Weight files are self-contained and transferable. **Grade A.**
- **Model / runtime:** GGUF quantisation across model families; CPU (incl. ARM) and CUDA/Metal/Vulkan backends.
- **Agent capabilities:** None.
- **Security / identity:** None product-level; embedding it inside a hardened appliance is what creates the boundary.
- **Integrations:** HTTP server mode (OpenAI-compatible), library bindings, widely used by Ollama/LM Studio.
- **Updates:** Manual binary/weight refresh; no signed update channel.
- **Support model:** Community.
- **Pricing evidence:** Free; MIT-licensed (license unverified this pass — **Grade D**).
- **Limitations:** Quantisation quality ceiling; weaker agentic reliability at small sizes — the local-agent tier-constraint is the binding limitation (see C3/C6 evidence).
- **Customer proof:** Indirect — two of the surveyed VS Code extensions bundle or build on llama.cpp, and one appliance ships Ollama. **Grade C.**
- **Sources:** "llama.cpp", https://github.com/ggml-org/llama.cpp, accessed 2026-11-11, **A**; project primary-source register §12, accessed 2026-11-11, **A**.

### A6. SGLang — OSS substitute (inference layer)

- **Buyer:** Teams needing fast structured output / high-throughput serving; engineers who prefer SGLang over vLLM.
- **Workflow:** High-performance serving, notably structured/constrained generation — attractive for reliable tool-call schemas in agent loops.
- **Deployment / isolation mode:** Containerised; NIM offers SGLang as an inference backend and NIM documents it in air-gap flows. **Grade A** (documented as NIM backend incl. air-gap); OSS-side offline lifecycle unverified.
- **Model / runtime:** Modern attention optimisations, RadixAttention-style prefix caching.
- **Agent capabilities:** None.
- **Security / identity:** None product-level.
- **Integrations:** NIM model-free image; OpenAI-compatible API.
- **Updates:** Manual. **Note documented failure mode:** NIM air-gap docs record "SGLang Attention Backend Failures on Grace Hopper and ARM" — a concrete example of an offline-hardware compatibility trap. **Grade A.**
- **Support model:** Community.
- **Pricing evidence:** Free; license unverified — **Grade D.**
- **Limitations:** Same DIY burden as vLLM; documented backend fragility on specific GPU architectures is a real risk for a fixed-hardware appliance build.
- **Customer proof:** Shipped as a first-class NIM backend. **Grade C.**
- **Sources:** "Air-Gap Deployment — NVIDIA NIM for LLM and VLM", https://docs.nvidia.com/nim/large-language-models/latest/deploy-air-gap.html, accessed 2026-11-11, **A**.

---

## 3. Category B — Offline Kubernetes and container management

### B1. Red Hat OpenShift Container Platform — ADJ (cluster layer)

- **Buyer:** Platform/infra teams in regulated and disconnected enterprises; government programmes running at IL4–IL6.
- **Workflow:** Run containerised workloads; operate a catalogue of operators; upgrade the platform; run disconnected installs.
- **Deployment / isolation mode:** Air-gapped / disconnected / restricted-network variants documented as three distinct postures. Recommended tooling: `oc-mirror` plugin, mirrored operator catalogues, internal registry (Quay), release payload + update-graph metadata mirrored.
- **Offline support evidence:** Dedicated "About disconnected environments" documentation with a glossary distinguishing air-gapped vs disconnected vs restricted network, plus a fully documented disconnected installation path. **Grade A.**
- **Model / runtime:** N/A (orchestration substrate; GPU operator, NVIDIA/AMD/Intel Gaudi drivers supported).
- **Agent capabilities:** None.
- **Security / identity:** RBAC, SCC, PSA, image signing, FIPS-capable builds, STIG workflows, operator-based lifecycle.
- **Integrations:** Quay/registry, operators, Helm, disconnected CLI, NIM GPU Operator.
- **Updates:** The decisive operational fact: disconnected operation requires mirroring release payload + images + update-graph metadata and refreshing operator catalogues on a schedule; connected staging must validate upgrades before promotion. **Grade A.**
- **License:** Proprietary subscription (OpenShift Plus/Advanced/Platform Plus tiers). Terms not fetched — **Grade D.**
- **Support model:** Red Hat subscription support (Tier 1/2/3, TAM for highest tiers).
- **Pricing evidence:** Not fetched this pass — **Grade D.**
- **Limitations:** Expensive, heavy, demanding. Disconnected upgrades are a recurring human cost. Provides the substrate; the wedge's governance, agent control and provenance layers are entirely absent.
- **Customer proof:** Anchore and Sonatype market air-gapped/IL-6 support at the enterprise level; Red Hat is the default substrate referenced by IBM air-gap flows. **Grade C.**
- **Sources:** "About disconnected environments — OKD 4.21", https://docs.okd.io/4.21/disconnected/about.html, accessed 2026-11-11, **A**; "How to operate OpenShift in air-gapped environments", https://developers.redhat.com/articles/2026/03/19/how-operate-openshift-air-gapped-environments (2026-03-19), accessed 2026-11-11, **A**.

### B2. OKD — OSS substitute (cluster layer)

- **Buyer:** Teams wanting OpenShift-like capability without the subscription, or building an internal base.
- **Workflow:** Upstream community distribution of the OpenShift platform; same disconnected install model.
- **Deployment / isolation mode:** Disconnected environments supported with the same `oc-mirror` / mirrored-catalogue guidance.
- **Offline support evidence:** Official docs "About disconnected environments" across versions 4.17, 4.18, 4.21 — documentation is maintained per release. **Grade A.**
- **Model / runtime:** N/A.
- **Agent capabilities:** None.
- **Security / identity:** Same upstream model as OpenShift (RBAC/SCC/PSA) — exact parity unverified. **Grade C.**
- **Integrations:** Quay, operators, Helm, oc-mirror.
- **Updates:** Community-driven; disconnected update cadence inherits the same mirroring burden.
- **Support model:** Community only.
- **Pricing evidence:** Free. **Grade C.**
- **Limitations:** No commercial support for an accredited programme; "open" does not equal "accreditable" — a support gap in exactly the buyer that matters most.
- **Customer proof:** Shared documentation lineage with OpenShift indicates the disconnected procedures are inherited. **Grade C.**
- **Sources:** "About disconnected environments — OKD 4.21", https://docs.okd.io/4.21/disconnected/about.html, accessed 2026-11-11, **A**; "About disconnected environments — OKD 4.17", https://docs.okd.io/4.17/disconnected/about.html, accessed 2026-11-11, **A**; "About disconnected environments — OKD 4.18", https://docs.okd.io/4.18//disconnected/about.html, accessed 2026-11-11, **A**.

### B3. RKE2 and K3s (Rancher / SUSE) — OSS substitute (cluster layer)

- **Buyer:** Edge/IoT/defence-adjacent teams wanting a small, certifiable Kubernetes (RKE2: SELinux+FQDN, hardened build for regulated/edge; K3s: minimal footprint).
- **Workflow:** Run Kubernetes in constrained/air-gapped environments.
- **Deployment / isolation mode:** Dedicated air-gap install documentation for both — pre-download images/tarball, mirror into a private registry, install offline.
- **Offline support evidence:** Both URLs are listed as primary deployment references in the project's own source register (§12), and each has a dedicated official air-gap install page. **Grade A.**
- **Model / runtime:** N/A.
- **Agent capabilities:** None.
- **Security / identity:** RKE2 documented as hardened for regulated environments (FIPS-ready builds, SELinux, no external network dependencies by default); K3s bundled Flannel/CoreDNS local by default. **Grade A (RKE2 posture), C (K3s detail)** — these specific claims are **not yet verified in this pass against the live pages** and are flagged as pending.
- **Integrations:** Rancher Fleet, Helm, containerd/private registries, Rancher (as used by Legion Centurion, see F1).
- **Updates:** Offline air-gap upgrade documented (image tarball + registry mirror). Detail not extracted this pass.
- **Support model:** RKE2 = SUSE commercial subscription; K3s = open source, community support, optional Rancher commercial support.
- **Pricing evidence:** Not fetched — **Grade D.**
- **Limitations:** RKE2's "hardened by default, no external dependencies" posture is the strongest *open* substrate fit for an accredited air-gapped deployment and is a real risk to a wedge that tries to differentiate on hardening. Support is the trade-off vs OKD.
- **Customer proof:** RKE2's presence in a US national-security vendor's hardened Kubernetes distribution is third-party corroboration of real-world use. **Grade B.**
- **Sources:** "RKE2 air-gap install", https://docs.rke2.io/install/airgap, accessed 2026-11-11, **A** (register citation); "K3s air-gap install", https://docs.k3s.io/installation/airgap, accessed 2026-11-11, **A** (register citation); "Centurion by Legion Intelligence", https://www.legionintel.com/centurion, accessed 2026-11-11, **B** (independent corroboration of RKE2/Rancher use).

### B4. Google Distributed Cloud (GDC) air-gapped — ADJ + CB (managed substrate + appliance)

- **Buyer:** Defence, intel and sovereign customers wanting Google Cloud services (incl. Vertex AI) inside accredited space; large enterprises needing managed Kubernetes with a disconnected control plane.
- **Workflow:** Managed GKE-style clusters, VMs, managed Harbor container registry, integrated logging/monitoring (Prometheus/Grafana/Loki), and Vertex AI services (OCR, STT, Translate) — i.e. *a full cloud in a box*.
- **Deployment / isolation mode:** Two distinct forms: (i) **GDC air-gapped** data-centre deployment — fully disconnected, operable with no internet connection; (ii) **GDC air-gapped appliance** — integrated hardware, ~100 lb / ~45.3 kg, two-person carry, non-operational while moved, for tactical edge.
- **Offline support evidence:** Official docs state GKE on GDC is "Fully disconnected: Yes" (vs "No" for GKE on Google Cloud), with a documented feature-comparison table; appliance docs describe physical isolation, secure boot, firewalls. **Grade A.**
- **Model / runtime:** Vertex AI + Google-provided deep learning containers; OCR/STT/Translate APIs.
- **Agent capabilities:** None specific to engineering workflow.
- **Security / identity:** IAM, encryption at rest/in transit, HSM-backed key storage for customer control, network security policies, **DoD IL5 accreditation for the appliance** (vendor-asserted, the highest accreditation claimed by any product in this survey). **Grade A (accreditation stated in official doc) / C (independent confirmation).**
- **Integrations:** Google Cloud services, Harbor, Prometheus/Grafana/Loki, customer networks, HSM.
- **Updates:** Different lifecycle for appliance — Google (or delegates) installs, then hands to the customer. Update mechanics for a sealed appliance are **not documented in the pages read — Grade D.**
- **License:** Proprietary Google Cloud / GDC commercial licensing.
- **Support model:** Google Cloud enterprise support; appliance install/handover by Google or delegate.
- **Pricing evidence:** Not fetched — **Grade D.**
- **Limitations:** Vendor lock-in to the entire Google stack at the moment the customer wants *least* dependency; appliance is heavy and must be re-accredited at each move; the ~100 lb / two-person constraint plus "not operational while moved" caps deployment topology. Carries a *complete* cloud layer — if a customer buys this, much of the substrate problem disappears and the wedge must compete on the workflow layer alone.
- **Customer proof:** IL5 accreditation is vendor-stated; no named customer captured. **Grade C.**
- **Sources:** "Kubernetes clusters in GDC — Google Distributed Cloud air-gapped", https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters, accessed 2026-11-11, **A**; "About Google Distributed Cloud air-gapped appliance", https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/overview (updated 2026-10-26), accessed 2026-11-11, **A**.

### B5. Testkube On-Prem — ADJ (test-execution layer)

- **Buyer:** Platform/test teams needing to run containerised test suites in a disconnected enclave.
- **Workflow:** Run E2E/K8s test workflows on in-cluster runners; publish authoritative per-release image manifests for mirroring.
- **Deployment / isolation mode:** Fully disconnected install supported; internal registry required; images mirrored via docker/crane/skopeo/oras across the boundary; **offline licence** required because online licences need outbound access to `license.testkube.io`.
- **Offline support evidence:** Official docs give a complete disconnected install path including the authoritative per-release image manifest, registry override, `enterpriseOfflineAccess: true`, and an explicit offline-licence requirement. **Grade A.** This is the strongest *documented* offline lifecycle in this category.
- **Model / runtime:** N/A (test tooling images).
- **Agent capabilities:** None.
- **Security / identity:** `imagePullSecrets`, internal registry, licence-gated enterprise features.
- **Integrations:** Kubernetes, Helm (testkube-enterprise + testkube-runner charts), any internal registry (Harbor/Artifactory/ECR/GAR/ACR).
- **Updates:** Mirror per-release manifest; offline licence renewal needed — **licence renewal in an air gap is a real recurring dependency and a good model for the wedge's update design.**
- **License:** Open-core; enterprise features require an offline licence.
- **Support model:** Commercial enterprise support (On-Prem).
- **Pricing evidence:** Not fetched — **Grade D.**
- **Limitations:** Different layer (test execution). Its offline-licence dependency is instructive and cautionary.
- **Customer proof:** None captured. **Grade C.**
- **Sources:** "Air-Gapped and Offline Installation — Testkube Documentation", https://docs.testkube.io/articles/install/air-gapped, accessed 2026-11-11, **A**.

### B6. IBM Cloud Pak / Content Cortex / Business Automation Workflow (air-gap pattern) — ADJ (application platform layer)

- **Buyer:** IBM estate customers installing content/workflow applications into air-gapped OCP.
- **Workflow:** Deliver enterprise applications into disconnected clusters using the `ibm-pak` Catalog Management Plug-in and CASE packages.
- **Deployment / isolation mode:** Documented air-gap install: bastion host or portable device → CASE download → mirror images to a private registry → curated local catalogue → OperatorGroup/Subscription.
- **Offline support evidence:** Official IBM docs for Content Cortex 26.0, Cloud Pak for Business Automation 26.0, and BAW 25.0 all document the air-gap path. **Grade A.** Notably one doc states "**Tanzu does not support offline deployment**" — a concrete vendor-admitted gap.
- **Model / runtime:** N/A.
- **Agent capabilities:** None.
- **Security / identity:** IBM Entitled Registry, private registry, operator catalogues, OCP RBAC.
- **Integrations:** OCP, CASE tooling, `ibm-pak`, private registry, OperatorHub.
- **Updates:** Repeatable air-gap mirror process ("mirror the CASE as many times as needed"); curated catalogue refresh is manual.
- **License:** Proprietary IBM subscription per Cloud Pak.
- **Support model:** IBM enterprise support.
- **Pricing evidence:** Not fetched — **Grade D.**
- **Limitations:** Heavy CASE/operator machinery for what is fundamentally an image-mirroring problem; no AI workload layer; a useful reference for the CASE packaging pattern the wedge would need for its own offline bundle.
- **Customer proof:** Multiple IBM product families shipping documented air-gap paths is evidence the pattern is table stakes in this market. **Grade A.**
- **Sources:** "Preparing your cluster for an air-gapped (offline) deployment on OCP" (Content Cortex 26.0.0), https://www.ibm.com/docs/en/content-cortex/26.0.0?topic=cluster-preparing-your-air-gapped-offline-deployment, accessed 2026-11-11, **A**; "Option 2: Preparing your cluster for an air-gapped (offline) deployment" (Cloud Pak for Business Automation 26.0.0), https://www.ibm.com/docs/en/cloud-paks/cp-biz-automation/26.0.0?topic=icmppd-option-2-preparing-your-cluster-air-gapped-offline-deployment, accessed 2026-11-11, **A**; "Preparing your cluster for an air-gapped (offline) deployment" (BAW 25.0.x), https://www.ibm.com/docs/en/baw/25.0.x?topic=configuring-preparing-your-cluster-air-gapped-offline-deployment, accessed 2026-11-11, **A**.

---

## 4. Category C — Local coding assistants and autonomous coding agents

> **Note on classification.** Every entry here solves *the coding-agent layer*. None supplies identity/governance, supply-chain provenance, air-gap update lifecycle or accreditation evidence. Per the task instruction, none is labelled a direct competitor of the wedge.

### C1. Cline (with local Ollama) — OSS substitute (coding-agent layer)

- **Buyer:** Developers and small teams running regulated or air-gapped codebases who want an autonomous VS Code agent without a cloud dependency.
- **Workflow:** Read files → propose plan → edit code with approval → run commands; multi-step autonomous edits.
- **Deployment / isolation mode:** VS Code extension against a local Ollama endpoint (`localhost` REST) — all traffic on one machine. Fits disconnected enclaves if the model server is local.
- **Offline support evidence:** Independent technical review confirms the local-Ollama path keeps code/prompts on-machine and that **telemetry must be separately disabled** — a real operational caveat, since code/prompt content staying local does not imply telemetry is off by default. **Grade B.**
- **Model / runtime:** Ollama native provider; other OpenAI-compatible endpoints. Requires ≥13–30B-class models for credible multi-step reliability; below that, single-file edits only. **Grade B.**
- **Agent capabilities:** Autonomous multi-file edits, plan-then-execute, terminal use, approval steps.
- **Security / identity:** **No enterprise identity, RBAC, scoped agent principal, audit ledger or policy engine.** Approval is a UI affordance, not an audited control.
- **Integrations:** VS Code, Ollama/LM Studio/OpenAI-compatible endpoints, MCP.
- **Updates:** VS Code Marketplace; extension updates need the marketplace to be reachable — in a true air gap this requires an internal extension mirror (VS Code's own air-gap story, see C9, is the harder problem).
- **License:** Open source (Apache-2.0) — **not verified in this pass, Grade D.**
- **Support model:** Community/OSS; commercial enterprise offering not verified — **Grade D.**
- **Pricing evidence:** Free OSS. **Grade C.**
- **Limitations:** Model-tier bound; no governance, no provenance, no accreditation evidence; telemetry must be consciously disabled; marketplace-update dependency in air gap.
- **Customer proof:** Independent review, 2026-08 verification, concludes it "fits solo developers and small teams on regulated or air-gapped codebases" but is "less fit for teams doing heavy multi-file refactors who need frontier-model reasoning." **Grade B.**
- **Sources:** "Cline + Ollama: Local AI Coding Agent for VS Code", https://markaicode.com/integrate/local-coding-assistant-with-ollama/ (2026-05-29; content verified Aug 2026), accessed 2026-11-11, **B**.

### C2. Continue (VS Code) — OSS substitute, maintenance risk (coding-agent layer)

- **Buyer:** Developers wanting an open-source VS Code assistant with local-model support.
- **Workflow:** Local-model autocomplete and chat via LM Studio/Ollama; agentic workflows (file inspection, edits, commands) per an independent hands-on review.
- **Deployment / isolation mode:** Local model servers on the workstation.
- **Offline support evidence:** Independent hands-on confirms the setup provides offline capability ("I can get things done when I'm offline"). **Grade B.**
- **Model / runtime:** LM Studio, Ollama and other local endpoints.
- **Agent capabilities:** Autocomplete, chat, agentic tool use.
- **Security / identity:** None enterprise-grade.
- **Updates:** **Maintenance status is a live risk.** An independent review states Continue's `continuedev/continue` repository is "explicitly no longer actively maintained as of its final 2.0.0 release, following Continue Dev's acquisition by Cursor," with the recommendation to migrate to Cline. **Grade B — needs direct repository verification.**
- **License:** Not verified — **Grade D.**
- **Support model:** Community; potential Cursor continuity. **Grade B.**
- **Pricing evidence:** Free. **Grade C.**
- **Limitations:** Unmaintained (per B-grade source) — disqualifies it for an accredited, multi-year programme. Local models "can't really compete with" cloud models on quality and "won't be as autonomous as a cloud coding agent." **Grade B.**
- **Customer proof:** Independent hands-on by a travelling developer. **Grade B.**
- **Sources:** "I ditched VS Code's Copilot for a local LLM, and I'm getting more done offline", https://www.xda-developers.com/ditched-vs-code-copilot-local-llm-getting-more-done-offline/ (2026-09-23), accessed 2026-11-11, **B**; "Cline + Ollama", https://markaicode.com/integrate/local-coding-assistant-with-ollama/, accessed 2026-11-11, **B**.

### C3. LocalPilot Agent (VS Code + CLI) — OSS substitute (coding-agent layer)

- **Buyer:** Individual developers and small teams wanting a Copilot-style agent loop running entirely on their own hardware.
- **Workflow:** Plan / Ask / Debug / Multitask modes; reads project, edits files, runs tests, shows diffs; CLI (`localpilot "fix the failing tests"`) with `--plan`, `--ask`, `--parallel`.
- **Deployment / isolation mode:** VS Code extension + terminal CLI, against a local model server (Ollama, LM Studio, llama.cpp, vLLM, Docker Model Runner). Every provider address is localhost unless the user adds one.
- **Offline support evidence:** Marketplace listing states "Works offline — Unplug the network: it keeps editing, running tests and reviewing diffs"; "Local by default: your code leaves your laptop only for a cloud provider you add"; cloud keys in OS keychain; "No telemetry leaves the disk." **Grade C** (vendor/marketplace page — behaviour not independently tested).
- **Model / runtime:** Any local server via Ollama/LM Studio/llama.cpp/vLLM/Docker Model Runner; cloud providers optional with own key.
- **Agent capabilities:** Autonomous edit-and-run loop with diffs; parallel mode; CLI-driven. Also integrates into VS Code's built-in Chat view, Copilot model picker, lightbulb fixes, right-click Explain/Fix/Refactor/Tests/Docs, commit-message generator.
- **Security / identity:** OS keychain for cloud keys; no enterprise identity/RBAC/audit.
- **Integrations:** VS Code, CLI, MCP implied by "add your own tools".
- **Updates:** Marketplace; air-gap requires an internal extension mirror.
- **License:** MIT (marketplace states "MIT license"). **Grade C.**
- **Support model:** Community/solo-maintainer (marketplace contact, GitHub). **Grade C.**
- **Pricing evidence:** "$0 per month — Cloud assistants cost $8–200 per developer. LocalPilot runs on hardware you already own." **Grade C.**
- **Limitations:** **261 installs** and 0 ratings on the marketplace — early-stage, single-maintainer, no enterprise support path, no governance layer, no accreditation evidence. **Marketplace install count is popularity, not quality — recorded as a signal of stage only, per §6.**
- **Customer proof:** None — no reviews, no named customer. **Grade C (absence of evidence).**
- **Sources:** "LocalPilot Agent — Visual Studio Marketplace", https://marketplace.visualstudio.com/items?itemName=localpilot.localpilot-agent, accessed 2026-11-11, **C**.

### C4. Sovereign Agent (VS Code) — OSS substitute (coding-agent layer)

- **Buyer:** Developers in strict local-only environments.
- **Workflow:** Autonomous file read, surgical edit, terminal execution — each gated by an explicit Allow/Deny confirmation card; Model Arena to compare two local LLMs side by side.
- **Deployment / isolation mode:** VS Code extension; Ollama, LM Studio, DeepSeek, Qwen, Gemma, llama.cpp, vLLM, LocalAI, Jan, GPT4All.
- **Offline support evidence:** Marketplace claims a **strict loopback guard** — every outgoing request passes a 127.0.0.1/localhost/::1 check, remote endpoints "hard-blocked at the network layer"; "zero cloud calls, zero API keys, zero telemetry." Optional LAN discovery/sharing of local endpoints (`allowLocalNetwork`, `networkShareEnabled`). **Grade C.**
- **Model / runtime:** Local model servers; 16 languages supported.
- **Agent capabilities:** Autonomous read/edit/terminal with approval gates; MCP support; web search (which is inherently a network dependency when enabled).
- **Security / identity:** No enterprise identity; the loopback guard is the security claim and is unverified. Self-advertised "Hard-Blocked Cloud & Telemetry (localGuard) — Enforced in code."
- **Integrations:** VS Code, MCP, local model servers.
- **Updates:** Marketplace; GPL-3.0.
- **License:** **GNU GPL v3.0-or-later** (marketplace states this explicitly). **Grade C.** Note: GPL-3.0 on an extension raises reciprocal-licensing questions if the wedge ever embeds or links it — a constraint, not a blocker, but it must be settled before reuse.
- **Support model:** Community — contact via marketplace support button or a personal email address, or GitHub issues. **Grade C.**
- **Pricing evidence:** Free. **Grade C.**
- **Limitations:** **18 installs, 0 ratings** — essentially zero adoption; no governance, no SBOM/provenance, no accreditation evidence, no enterprise identity; web search is network-dependent.
- **Customer proof:** None. **Grade C (absence of evidence).**
- **Sources:** "Sovereign Agent — Local AI & Ollama Coding Assistant", https://marketplace.visualstudio.com/items?itemName=ertugrul37.sovereign-agent, accessed 2026-11-11, **C**; changelog page https://marketplace.visualstudio.com/items?itemName=ertugrul37.sovereign-agent&ssr=false, accessed 2026-11-11, **C**.

### C5. LocalCode (terminal agent) — OSS substitute (coding-agent layer)

- **Buyer:** Terminal-first developers wanting a fully local autonomous agent; teams standardising on Ollama/LM Studio.
- **Workflow:** Reads files, edits code, runs shell commands, commits to git; LSP diagnostics (tsc, cargo check, go vet, pylint, eslint); MCP-style tool add/remove/reload; session save/restore/compress (`/compact`); shell passthrough.
- **Deployment / isolation mode:** npm-installed CLI, local model server via `/connect`; config at `~/.localcode/config.json`. Stated "No cloud, no API key. Your code never leaves your machine."
- **Offline support evidence:** Site states "Offline-capable once models are downloaded", "No telemetry, no analytics", "No cloud account or API key required". **Grade C.**
- **Model / runtime:** Ollama, LM Studio, or any OpenAI-compatible endpoint (DeepSeek Coder, Llama 3, Mistral, Qwen, CodeGemma cited).
- **Agent capabilities:** Autonomous edit/run/commit loop; LSP diagnostics; built-in security guard blocking dangerous commands (rm -rf, force-push, DROP TABLE); file writes and shell commands always require confirmation.
- **Security / identity:** No enterprise identity/RBAC/audit; a local heuristic command guard only. No code-signing, no SBOM, no provenance.
- **Integrations:** git, LSP, MCP-style tools, shell.
- **Updates:** npm; air-gap requires an internal npm mirror — note the wheel's own dependency tree must be mirrored too.
- **License:** **MIT** (stated on site). **Grade C.**
- **Support model:** Community (GitHub, wiki). **Grade C.**
- **Pricing evidence:** Free, MIT. **Grade C.**
- **Limitations:** v0.1.0 (version stated on site) — pre-1.0; no governance, provenance, accreditation evidence; no identity model; confirmation-gates only.
- **Customer proof:** None. **Grade C (absence of evidence).**
- **Sources:** "LocalCode — Open-Source AI Coding Agent That Runs in Your Terminal", https://www.localcode.codes/, accessed 2026-11-11, **C**; https://github.com/lsheasel/LocalCode, accessed 2026-11-11, **C**.

### C6. DeskAI (VS Code) — OSS substitute (coding-agent layer)

- **Buyer:** Windows/macOS/Linux developers wanting a self-contained offline assistant that needs no model server setup.
- **Workflow:** Ask mode (code help), Agent mode (full project generation: create files/folders on disk, run terminal commands, read/edit/verify files, **recover from errors automatically**, persistent task scratchpad surviving context resets, "Continue task" resume), keyword-based retrieval scanning up to 300 files (configurable `deskai.ragTopK`, toggleable).
- **Deployment / isolation mode:** Bundles **llama-server** itself; GGUF models; runs on localhost:11434 with 32k context; models auto-downloaded on first launch. Fully offline after that.
- **Offline support evidence:** "100% offline AI coding assistant… No API keys. No data sent to the cloud"; "Works entirely offline: no embeddings API, no cloud." **Grade C.**
- **Model / runtime:** llama.cpp/llama-server with GGUF; recommended Qwen2.5-Coder-14B Q4_K_M (12 GB+ RAM, 16 GB+ recommended), also Qwen3/DeepSeek-Coder. Also exposes **local models in Copilot's own model picker** (per the offgrid listing, same pattern family).
- **Agent capabilities:** Project generation, agentic file editing, terminal control, error recovery, resumable sessions.
- **Security / identity:** None enterprise-grade; no audit, no scoping.
- **Integrations:** VS Code (requires 1.85.0+), llama-server, filesystem.
- **Updates:** Marketplace; models auto-download on first launch — **in a true air gap the model auto-download path must be replaced with a manual transfer, and the extension's own update path needs a mirror.**
- **License:** Not stated in the listing read — **Grade D.**
- **Support model:** Community/marketplace contact — **Grade D.**
- **Pricing evidence:** Free. **Grade C.**
- **Limitations:** **159 installs, 0 ratings**; hardware floor (12 GB+ RAM) excludes many edge sites; no governance/provenance/accreditation; model download step is a hardcoded internet dependency at first launch; pre-1.0 maturity implied.
- **Customer proof:** None. **Grade C (absence of evidence).**
- **Sources:** "DeskAI — Local AI Coding Assistant — Visual Studio Marketplace", https://marketplace.visualstudio.com/items?itemName=AbhishekMishra9454.deskai-local, accessed 2026-11-11, **C**.

### C7. LLM Local Assistant (VS Code) — OSS substitute (coding-agent layer)

- **Buyer:** Developers needing a Copilot alternative that is provably local, with a multi-step (not single-shot) planner.
- **Workflow:** `/plan` decomposes a task into validated steps with cross-file contract checks; AST-based refactor analyzer; RAG codebase context.
- **Deployment / isolation mode:** VS Code extension → Ollama, LM Studio or vLLM on localhost. Explicitly "Works on a plane. Works behind an air-gapped corporate firewall."
- **Offline support evidence:** "No external APIs. No cloud services. No telemetry. No internet required. Your code stays on your machine." **Grade C** (repo README, unverified).
- **Model / runtime:** Ollama, LM Studio, vLLM.
- **Agent capabilities:** Multi-step planner, AST refactor analysis, RAG context — no shell/file-mutation autonomy described in the listing.
- **Security / identity:** None enterprise-grade.
- **Integrations:** VS Code, AST tooling, local LLM endpoints.
- **Updates:** Marketplace; repo has CI/CD on every PR and a stated release history.
- **License:** **MIT** (repo states MIT). **Grade C.**
- **Support model:** Community; explicit ask for marketplace ratings ("Three ratings unlock the next install bump") — an early-stage signal. **Grade C.**
- **Pricing evidence:** Free. **Grade C.**
- **Limitations:** The repo itself documents "**⚠️ Limitations & Agentic Boundaries — Cross-File Contract Drift**" — i.e. the author acknowledges the planner does not reliably maintain cross-file contracts. 291 commits, TypeScript strict, 0 runtime deps. No governance, provenance or accreditation layer.
- **Customer proof:** None. **Grade C (absence of evidence).**
- **Sources:** "odanree/llm-local-assistant — GitHub", https://github.com/odanree/llm-local-assistant (created 2025-11-19, 291 commits), accessed 2026-11-11, **C**.

### C8. offgrid: local AI (VS Code) — OSS substitute (coding-agent layer)

- **Buyer:** Developers wanting completion + local chat with a very small footprint, including CPU-only machines.
- **Workflow:** Ghost-text code completion with FIM (uses code before and after the cursor plus recently visited files); chat in VS Code's Chat view; works in Ask and Agent modes with tool calling.
- **Deployment / isolation mode:** Extension ships its own `offgrid-server` binary and starts it as needed; **all VS Code windows share one server** so models load once; GGUF via llama.cpp on any GPU (Vulkan: AMD/NVIDIA/Intel) with CPU fallback.
- **Offline support evidence:** "No account, no API key and no cloud: after a one-time model download, nothing leaves your computer." **Grade C.**
- **Model / runtime:** llama.cpp/GGUF. Sizing ladder disclosed: Tiny Qwen3.5 0.8B (1.3 GB, no GPU/<6 GB), Small Qwen3.5 2B (2.7 GB, 6 GB GPU), Standard Qwen3.5 4B (4.1 GB, 8 GB+ GPU), Large Qwen3.5 35B-A3B (22.1 GB, 16 GB/32 GB RAM); completion uses Qwen2.5-Coder 1.5B for Tiny/Small/Standard. Downloads are **SHA-256 checked** and kept in VS Code storage.
- **Agent capabilities:** Agent mode with tool calling; explicitly "light Agent use" at Small/Standard size.
- **Security / identity:** None enterprise-grade. Note the listing contains a Windows Smart App Control / "evaluation mode" caveat — an endpoint-hardening dependency.
- **Integrations:** VS Code Chat view, model picker, bundled server.
- **Updates:** Marketplace; model downloads SHA-256 verified — a **good pattern to copy** for the wedge's asset intake.
- **License:** **MIT**. **Grade C.**
- **Support model:** Marketplace contact. **Grade C.**
- **Pricing evidence:** Free. **Grade C.**
- **Limitations:** **14 installs, 0 ratings** — negligible adoption. Explicitly states "Small local models are much weaker than cloud models, especially in Agent mode" and completion "only triggers at the end of a line." No governance/provenance/accreditation.
- **Customer proof:** None. **Grade C (absence of evidence).**
- **Sources:** "offgrid: local AI — Visual Studio Marketplace", https://marketplace.visualstudio.com/items?itemName=Pinta365.offgrid, accessed 2026-11-11, **C**.

### C9. Coder — ADJ (remote dev environment layer)

- **Buyer:** Platform teams operating centralised, governed remote development workspaces for engineers who cannot use cloud dev boxes.
- **Workflow:** Provision reproducible remote workspaces from templates; run AI coding agents inside those workspaces.
- **Deployment / isolation mode:** "All Coder features are supported in air-gapped / behind firewalls / disconnected / offline." Air-gapped container images, air-gapped docs export, a template builder, Coder Modules, documented firewall exceptions.
- **Offline support evidence:** Dedicated official "Air-gapped Deployments" page stating full feature support, with offline licence validation, air-gapped container images and air-gapped docs. **Grade A.**
- **Model / runtime:** N/A; hosts whatever agents/models the customer provides.
- **Agent capabilities:** Hosts AI coding agents (docs section "Run AI coding agents in Coder"); it is the *workspace* substrate, not the agent.
- **Security / identity:** Templates, workspace isolation, network policy, offline licence validation.
- **Integrations:** Kubernetes and Docker deployment; JetBrains Gateway with **documented offline deployment steps**; VS Code Remote-SSH (with explicit firewall exceptions: `update.code.visualstudio.com`, `vscode.blob.core.windows.net`, `*.vo.msecnd.net`); code-server via `code-server.dev`/`open-vsx.org`.
- **Updates:** Air-gapped container images and air-gapped docs; offline licence validation path documented.
- **License:** Proprietary; enterprise self-hosted with offline licence. Terms not captured — **Grade D.**
- **Support model:** Enterprise support.
- **Pricing evidence:** Not fetched — **Grade D.**
- **Limitations:** A real finding for the wedge: **even the desktop side of the toolchain needs internet** (VS Code Remote-SSH requires outbound HTTPS to three Microsoft hosts; JetBrains/code-server similarly). Any offline engineering workbench must pre-stage the *IDE* as well as the model — this is a product-design constraint nobody in this survey appears to have solved. Coder's own air-gap guide documents it but does not eliminate it.
- **Customer proof:** Official air-gap documentation; no named customer captured. **Grade C.**
- **Sources:** "Air-gapped Deployments — Coder Docs", https://coder.com/docs/install/prepare/airgap, accessed 2026-11-11, **A**; "Run AI coding agents in Coder", https://coder.com/docs/ai-coder/, accessed 2026-11-11, **A**.

### C10. LocalPilot / Sovereign / DeskAI / offgrid / LocalCode — cross-cutting observation on this layer

- **Finding:** Across five independently-built local coding agents, the published feature sets are strikingly uniform: local model servers, plan/ask/agent modes, file edit + terminal execution, approval confirmations, MCP, zero telemetry. **None** publishes an enterprise identity model, RBAC, scoped agent principals, an immutable action/approval ledger, SBOM or provenance intake, signed asset verification, air-gap update lifecycle, or accreditation evidence packs. Install counts are 261 / 18 / 159 / 14 and 0 ratings across four of them.
- **Interpretation (Grade D):** The local coding-agent layer is well-served for individual developers and **empty at the enterprise/accredited end**. That is the wedge's opening — *if* the wedge's value is governance and lifecycle rather than agent capability.
- **Counter-consideration:** Because this layer is free and good enough for individual contributors, the wedge cannot charge for the agent loop; it can only charge for the governed execution, provenance, lifecycle and evidence around it.
- **Counter-counter:** Integration programmes will happily assemble this layer themselves, which is the CB risk in §8.
- **Source:** aggregate of C3–C8 marketplace listings, accessed 2026-11-11, **C** (per-item grades as cited above).

---

## 5. Category D — Secure software development, artifact and SBOM platforms

### D1. Anchore Enterprise — ADJ (supply-chain governance layer)

- **Buyer:** Enterprise and government software supply-chain owners; named as a required scanning tool in DoD container hardening guidance; DoD Iron Bank and Cisco customer references published.
- **Workflow:** Generate SBOMs at every commit/build/deploy; manage internal and external SBOMs in one place; scan images for vulnerabilities, secrets and malware; enforce policy (STIG checks, NIST/CIS/FedRAMP/IL6/FIPS); continuous vulnerability monitoring without access to original artifacts.
- **Deployment / isolation mode:** On-premise with **no internet connection** for DoD IL-6 environments; on-premises "Air-Gapped Deployments" explicitly; also SaaS and hybrid.
- **Offline support evidence:** "Anchore can be deployed in an air-gapped environment for use in classified or restricted access environments"; "Deploy Anchore on-premise with no internet connection in order to run in DoD IL-6 environments." Mechanically: an **on-premises Anchore Feed Service** provides an API to transfer vulnerability and other external data into the Engine — this is the reference pattern for how vulnerability intelligence must be refreshed offline. **Grade A** (docs/marketing page states mechanism; **C** for the accreditation assertions).
- **Model / runtime:** N/A. SBOM formats: Syft (native), CycloneDX, SPDX.
- **Agent capabilities:** None.
- **Security / identity:** Policy engine (STIG, NIST, CIS, FedRAMP, IL6), false-positive management, enterprise RBAC (depth not verified — **Grade D**).
- **Integrations:** CI/CD systems, container orchestration, image registries (Azure/AWS/GCP + any Docker v2 on-premises), security feeds, GitHub/CI collaboration.
- **Updates:** Offline feed service must be refreshed from a connected source — the recurring "vulnerability intelligence freshness" problem, which has no clean offline answer.
- **License:** Open-core (Anchore open source Syft/Grype) + proprietary Enterprise. Terms not fetched — **Grade D.**
- **Support model:** Enterprise support; named "Support Portal".
- **Pricing evidence:** A "Pricing" page exists in site nav but was not fetched — **Grade D.**
- **Limitations:** Solves artifact provenance and scanning, **not** agentic engineering workflow; does not govern agent action; no local inference; vulnerability freshness still depends on a periodic transfer.
- **Customer proof:** Vendor-published references to DoD Iron Bank and to Cisco ("Anchore has proven to be a valuable tool, helping to ensure that the Cisco Container Platform matches our compliance standards"); "Trusted by Government and Fortune 500 companies for 8+ years"; "Used by the DoD"; named as a required tool in DoD container hardening guides. **Grade C (vendor-published).**
- **Sources:** "Software Supply Chain Management Platform | Anchore Enterprise", https://anchore.com/enterprise, accessed 2026-11-11, **C**; "Software supply chain security for the public sector | Anchore", https://anchore.com/platform/public-sector, accessed 2026-11-11, **C**; "Introducing Anchore Enterprise 1.1", https://anchore.com/blog/introducing-anchore-enterprise-1-1 (2018-08-07) — documents the on-prem Feed Service and air-gap capability, accessed 2026-11-11, **A** for mechanism; "Generating SBOMs | Anchore Enterprise Documentation", https://docs.anchore.com/6.2/docs/sbom_management/generate, accessed 2026-11-11, **A**.

### D2. Sonatype SAGE (Air-Gapped Environment) + Lifecycle/SBOM Manager — ADJ (supply-chain governance layer)

- **Buyer:** Classified programmes, weapons-systems programmes, sovereign cloud customers and OT operators.
- **Workflow:** Curated private repository of pre-vetted, policy-compliant components as single source of truth; **offline SBOM generation and artifact traceability**; automated policy enforcement in isolated pipelines (security, quality, licensing); immutable evidence for authorisation decisions.
- **Deployment / isolation mode:** SAGE designed for "classified programs and sovereign cloud environments" with "no reliance on external connections"; components cross the air gap only after being scanned, validated and approved against DoD/NIST standards.
- **Offline support evidence:** Vendor blog explicitly: "Offline SBOM generation and artifact traceability: Automatically build, maintain, and export SBOMs within disconnected environments"; and Lifecycle "can run in fully disconnected environments using the Sonatype Air-Gapped Environment (SAGE), enabling policy enforcement, vulnerability intelligence, and governance without any direct internet access." **Grade C** (vendor blog/product page — no installation runbook seen in this pass).
- **Model / runtime:** N/A.
- **Agent capabilities:** None.
- **Security / identity:** Policy engine for security/quality/licensing; governance workflow with authorisation decisions. RBAC depth not verified — **Grade D.**
- **Integrations:** CI/CD, binary/repository managers, container security, OSS management, malware protection, licence compliance.
- **Updates:** Curated repository refresh across the boundary is the core mechanic.
- **License:** Proprietary; Lifecycle available cloud-hosted by Sonatype, on-premises self-hosted, or SAGE disconnected. Terms not fetched — **Grade D.**
- **Support model:** Commercial enterprise support.
- **Pricing evidence:** Not fetched — **Grade D.**
- **Limitations:** Supply-chain layer only; no agentic workflow, no inference, no engineering repository context. Notably it *is* the layer the wedge would need to interoperate with or displace.
- **Customer proof:** Vendor-published positioning for federal programmes; author identified as specialising in federal supply chain for DoD/IC. No named air-gapped customer captured. **Grade C.**
- **Sources:** "Mastering software governance in air-gapped, critical mission environments", https://www.sonatype.com/blog/mastering-software-governance-in-air-gapped-critical-mission-environments (2025-11-12), accessed 2026-11-11, **C**; "Sonatype Lifecycle — SCA Tools for Open Source Security", https://www.sonatype.com/products/open-source-security-dependency-management, accessed 2026-11-11, **C**.

### D3. GitLab Self-Managed (offline environments) — ADJ (DevSecOps platform layer)

- **Buyer:** GitLab Self-Managed customers in air-gapped / limited-connectivity / LAN / intranet estates, including those with security policies preventing internet access.
- **Workflow:** Full DevSecOps lifecycle — SAST, container scanning, secret detection, DAST, dependency scanning, with vulnerability resolution — executed against a locally hosted instance.
- **Deployment / isolation mode:** Explicitly documented "offline environments" mode with a dedicated documentation section; scanner images downloaded and pushed to the project container registry; package metadata DB and scanner signatures updated manually.
- **Offline support evidence:** Official docs define offline environments, list per-scanner offline directions (container scanning, SAST, secret detection, DAST), document `SECURE_BINARIES_ANALYZERS` for downloading scanner images, and document package metadata DB loading. States the "resolving vulnerabilities" feature "is available for offline dependency scanning and container scanning, but may not work depending on your instance's configuration." **Grade A** — including a candid limitation statement.
- **Model / runtime:** N/A.
- **Agent capabilities:** **None in the surveyed docs** (GitLab Duo/agentic features are cloud/SAAS-tier dependent — not verified, **Grade D**). Relevant: the wedge must interoperate with GitLab Self-Managed in exactly these estates.
- **Security / identity:** GitLab's own instance IAM, protected branches, security policies.
- **Integrations:** Container registries, package repositories, CI runners, scanners.
- **Updates:** Scanner images and rule/signature DBs updated via offline download; documented as an operational burden.
- **License:** GitLab Self-Managed, free tier + paid tiers (Ultimate/Premium for some scanners).
- **Support model:** Commercial support for paid tiers; community for free tier.
- **Pricing evidence:** Not fetched — **Grade D.**
- **Limitations:** The platform the customer likely already owns in the enclave — meaning **GitLab is more a wedge's integration target than a competitor**, and any wedge that ignores it will fail procurement.
- **Customer proof:** Documented offline support is itself the product claim; no named customer captured. **Grade C.**
- **Sources:** "Offline environments — GitLab Docs", https://docs.gitlab.com/user/application_security/offline_deployments/, accessed 2026-11-11, **A**.

### D4. SBOM Central (t2data) — ADJ (SBOM management layer)

- **Buyer:** Organisations needing SBOM storage/monitoring/export, including high-security and classified estates.
- **Workflow:** Unify SBOM analysis, continuous monitoring, collaboration and automation; standards-compliant exports; "artifact tool" to extend SBOM coverage beyond standard components; "privacy-preserving SBOM management".
- **Deployment / isolation mode:** SaaS, on-premises, **and an explicit Air-Gapped configuration** — "SBOM Central can be configured to operates completely disconnected from the internet — ideal for classified systems, critical infrastructure, and highly regulated environments requiring zero external connectivity."
- **Offline support evidence:** Vendor product page states the Air-Gapped deployment mode explicitly. **Grade C.**
- **Model / runtime:** N/A.
- **Agent capabilities:** None.
- **Security / identity:** Not detailed in the page read — **Grade D.**
- **Integrations:** Part of the vendor's "MAIA Software" suite; artifact tool extension.
- **Updates:** Not stated — **Grade D.**
- **License:** Proprietary (MAIA Software suite).
- **Support model:** Vendor contact/support.
- **Pricing evidence:** Not fetched — **Grade D.**
- **Limitations:** Smaller/less-documented vendor than Anchore/Sonatype; SBOM management layer only; no engineering workflow or agent governance.
- **Customer proof:** None captured. **Grade C (absence of evidence).**
- **Sources:** "SBOM Central", https://t2data.com/products/sbomcentral, accessed 2026-11-11, **C**.

---

## 6. Category E — Enterprise search / knowledge and domain model products

### E1. deepset Haystack Enterprise Platform — ADJ (RAG/agent platform layer)

- **Buyer:** Enterprise AI teams that need sovereign AI: RAG + agentic pipelines with data, models and traces inside the customer's network.
- **Workflow:** Connect and index data (SharePoint, Google Drive, local files) → build pipelines/agents in Studio → deploy behind an API → monitor with built-in traces, pipeline logs, search history, performance dashboards; ship traces to Langfuse, W&B Weave, OpenTelemetry or Datadog.
- **Deployment / isolation mode:** Managed cloud, self-hosted in private cloud/on-prem, and **air-gapped with no internet connection**. Documented consequences of air-gap: external-service components (web search, translation, hosted file conversion) work only if the customer hosts an equivalent service internally; managed-cloud WAF does not cover self-hosted deployments so the customer manages their own WAF.
- **Offline support evidence:** Official deployment-options documentation stating the air-gapped posture and its consequences. **Grade A.**
- **Model / runtime:** Model-agnostic; OpenAI, Anthropic, Azure OpenAI, Bedrock, Google Gemini, Cohere, Mistral, NVIDIA, Meta Llama, Together AI, plus self-hosted models.
- **Agent capabilities:** "The Haystack Platform Agent uses an LLM to decide which tools to call and loops until it reaches a goal" — genuine agentic loop with tool use. **This is the closest ADJ to the wedge's agent layer for enterprise governance.**
- **Security / identity:** RBAC with preset or custom roles, granular permissions at organisation and workspace level. IAM depth vs. the wedge's needs (scoped agent principals, per-tool capability grants, approval ledger) not verified — **Grade D.**
- **Integrations:** REST API, SDK, SharePoint, Google Drive, document stores/vector DBs, CI/CD via GitHub Actions, OpenTelemetry, Langfuse, Weave, Datadog.
- **Updates:** Not documented for air-gap in the pages read — **Grade D.** (A known open question for any air-gap platform.)
- **License:** Proprietary platform built on the open-source Haystack framework (Apache-2.0).
- **Support model:** Commercial enterprise support; air-gapped/self-hosted deployments via infrastructure partners including AWS, StackIT, NVIDIA and on-prem data-centre providers.
- **Pricing evidence:** "Contact your deepset representative" — no public list price. **Grade C.**
- **Limitations:** **Not a software-engineering workbench** — it is a general RAG/agent platform; it does not understand repositories, requirements traceability, test generation or patch proposals. Air-gap external-service degradation is documented and material. It is a *platform-layer* competitor for the agent orchestration budget, not for the engineering workflow.
- **Customer proof:** Vendor-stated, positioned for sovereign AI; no named air-gapped customer captured. **Grade C.**
- **Sources:** "Deployment Options | Haystack Enterprise Platform Documentation", https://docs.cloud.deepset.ai/docs/deployment-options, accessed 2026-11-11, **A**; "Feature List", https://docs.cloud.deepset.ai/docs/feature-list, accessed 2026-11-11, **A**; "What's Haystack Enterprise Platform?", https://docs.cloud.deepset.ai/docs/getting-started, accessed 2026-11-11, **A**.

### E2. Elastic (Elasticsearch / ELSER) + Jina On-Prem — ADJ (enterprise search / retrieval layer)

- **Buyer:** Enterprise search teams needing semantic retrieval inside regulated or disconnected environments; multilingual/multimodal retrieval where ELSER (English text) is insufficient.
- **Workflow:** Full-text + semantic + hybrid retrieval; ELSER out-of-domain sparse encoder for semantic search without fine-tuning; E5 for non-English; Jina models cover text, images, audio and video in one embedding space.
- **Deployment / isolation mode:** Self-hosted Elastic; for ELSER in a restricted/closed network, two documented options — serve model artefacts from your own HTTP/HTTPS endpoint, or use file-based access (download artefacts and load locally; note the platform-specific ELSER artefact is Linux x86-64 only). Jina On-Prem delivers embedding + reranker models to on-prem/air-gapped environments with "no internet connection or third-party AI services required."
- **Offline support evidence:** Official Elastic docs "Deploy ELSER in an air-gapped environment"; Elastic press release for Jina On-Prem in on-prem/air-gapped environments. **Grade A (ELSER) / C (Jina via press release).**
- **Model / runtime:** ELSER (sparse retrieval), E5, Jina embedding + reranker family (text/image/audio/video); small Jina models run on a single 8 GB GPU. ELSER needs a minimum 4 GB dedicated ML node.
- **Agent capabilities:** None in-product; Jina provides reranking, which is a component an agent loop would consume.
- **Security / identity:** Elastic RBAC / Stack security (depth not verified — **Grade D**).
- **Integrations:** Elasticsearch/OpenSearch-compatible stack, Kibana, connectors, Jina AI licensing.
- **Updates:** Model artefacts are static files you stage yourself — a favourable property for air-gap: **model updates are a file transfer, not a vendor-driven process.** ELSER is *not* self-updating and does not retrain on your data.
- **License:** Elastic Stack subscription tiers (mostly source-available); Jina models separately licensed via Jina AI (Jina On-Prem).
- **Support model:** Elastic enterprise support.
- **Pricing evidence:** Not fetched — **Grade D.**
- **Limitations:** Retrieval layer only; no agentic workflow, no engineering-specific tooling. ELSER is English-recommended and out-of-domain (no fine-tuning on your data) — so a domain-model requirement is not met by ELSER alone. Vendor assertion: "licensed platforms cleared for air-gapped deployments are largely constrained to text and images" — an opening for multimodal-in-air-gap, and simultaneously a claim about competitors to verify.
- **Customer proof:** Elastic states the platform is used by thousands of companies including more than 50% of the Fortune 500. **Grade C.**
- **Sources:** "ELSER | Elastic Docs", https://www.elastic.co/docs/explore-analyze/machine-learning/nlp/ml-nlp-elser, accessed 2026-11-11, **A**; "Elastic Brings Jina Multimodal and Multilingual Semantic Search to On-Premises and Air-Gapped Environments", https://ir.elastic.co/News--Events/news/news-details/2026/Elastic-Brings-Jina-Multimodal-and-Multilingual-Semantic-Search-to-On-Premises-and-Air-Gapped-Environments/default.aspx (2026-07-27), accessed 2026-11-11, **C**.

### E3. Varuni Systems (AI & RAG) — CB (integrator/vertical solution)

- **Buyer:** Maritime, defence, manufacturing, training and logistics organisations (India-based, aerospace/defence heritage) that cannot send sensitive documents to a third-party API.
- **Workflow:** Retrieval-augmented generation over the customer's own documents with citations; local LLM integration and fine-tuning on the customer's domain; document intelligence (extraction, classification, summarisation); human-in-the-loop workflow automation ("the model drafts and routes, a person decides"); signal/sensor AI at the edge.
- **Deployment / isolation mode:** On-premise, private cloud, or **fully air-gapped** — "the models, the vector store and the documents all sit inside your perimeter"; "Nothing calls out."
- **Offline support evidence:** Vendor product page states the air-gapped mode and the zero-call-out posture explicitly. **Grade C.**
- **Model / runtime:** Open-weight models run locally, fine-tuned on the customer's domain; no per-token billing.
- **Agent capabilities:** Workflow automation with human-in-the-loop; no multi-agent governance described.
- **Security / identity:** Perimeter/no-egress posture; identity depth not described — **Grade D.**
- **Integrations:** "Existing AI capability → MagicLoc acoustics" implies signal-processing product adjacency.
- **Updates:** Not stated — **Grade D.**
- **License:** Proprietary services/solution.
- **Support model:** Consultative, project-based engagement ("Start the conversation", "Tell us what you're trying to train, track or communicate through").
- **Pricing evidence:** No list price — engagement-based. **Grade C.**
- **Limitations:** Not a product; a capability statement and services offer. RAG/knowledge layer, not an engineering workbench. **Weakness for them, signal for us: the vertical integrator is assembling exactly the air-gapped RAG pattern the wedge would package.**
- **Customer proof:** Vendor-published defence/maritime positioning; no named customer captured. **Grade C.**
- **Sources:** "Self-Hosted AI & RAG — Air-Gapped Retrieval-Augmented Generation | Varuni Systems", https://varunisystems.com/products/ai-rag, accessed 2026-11-11, **C**.

### E4. ONES.com / open-source knowledge tools (Danswer, AnythingLLM, BookStack, MediaWiki) — ADJ + OSS substitute (knowledge layer)

- **Buyer:** Software/engineering/product teams needing AI-assisted knowledge management in an air-gapped or tightly governed environment.
- **Workflow:** Enterprise search with permission-aware retrieval and RAG answers (Danswer); private document chat with local models and connectors (AnythingLLM); structured team manuals (BookStack); durable technical documentation collections (MediaWiki).
- **Deployment / isolation mode:** All self-hosted; Danswer's air-gapped deployment "depends on infrastructure and model setup"; AnythingLLM self-hosted/local; BookStack/MediaWiki self-hosted including offline environments.
- **Offline support evidence:** Vendor editorial explicitly reviews air-gapped deployment options and states that "Open-source and self-hosting options provide more control over sensitive data than hosted AI search products." **Grade C.**
- **Model / runtime:** Local models supported (AnythingLLM "local models, connectors"); otherwise depends on customer model hosting.
- **Agent capabilities:** Conversational retrieval; no engineering-workflow agent capability.
- **Security / identity:** Danswer is "permission-aware"; BookStack has "fine-grained permissions" but "fine-grained permissions, audit requirements, content lifecycle controls, and enterprise administration may need additional configuration" — i.e. **not** audit-ready out of the box. **Grade C.**
- **Integrations:** ONES.com productises into engineering/project workflows; open-source tools integrate with git/SharePoint/etc. via connectors.
- **Updates:** Self-hosted; air-gap update mechanics not documented — **Grade D.**
- **License:** ONES.com commercial; Danswer (open-source/commercial), AnythingLLM (free + enterprise), BookStack and MediaWiki (free, self-hosted).
- **Support model:** Commercial for ONES.com; community for OSS.
- **Pricing evidence:** Not fetched for ONES.com ("Pricing and packaging should be confirmed with ONES.com for larger teams, self-hosted requirements, and enterprise AI workflow needs"). OSS free with hosting/admin costs borne by customer. **Grade C.**
- **Limitations:** Knowledge layer only. The vendor's own test checklist is the useful artefact: *"Test offline installation, internal model access, document indexing, permission-aware search, backups, upgrades, audit logs, and recovery."* — that is effectively the wedge's acceptance criteria for the knowledge slice.
- **Customer proof:** Vendor-published comparison; no named customer captured. **Grade C.**
- **Sources:** "Tools for AI Team Knowledge Management in an Air-Gapped Environment (2026 Recommendations)", https://ones.com/blog/tool-guide/tools-for-ai-team-knowledge-management-in-an-air-gapped-environment-2026-recommendations (2026-08-24), accessed 2026-11-11, **C**.

---

## 7. Category F — System integrators and hardware appliance vendors

### F1. Legion Intelligence — Centurion Edge AI System — **DC-near** (integrated product, different buyer)

- **Buyer:** US national security — DoW, intelligence community, DoE and the defense industrial base. Delivered **through** system integrators, who put Centurion into their own proposals.
- **Workflow:** Governed agentic AI — cross-system orchestration, workflow automation, natural-language search across documents and systems, human-in-the-loop controls; offline-first so workflows continue when the network drops or when emissions/telemetry are shut off.
- **Deployment / isolation mode:** Edge deployment integrating hardware + software + lifecycle sustainment as one package. Connected, disconnected (DDIL) or **fully air-gapped**. Single node to coordinated mesh. One prior deployment ran on **HPE EL8000S edge hardware with a hardened Kubernetes distribution from Rancher** (i.e. RKE2). Partner hardware from Intel, NVIDIA and HPE matched to the deployment profile.
- **Offline support evidence:** Official reference page: "Centurion supports fully air-gapped deployment with no external connectivity required, and is authorized from IL2 through IL6 including classified networks"; "designed offline-first, so AI workflows continue running locally when the network drops." **Grade A.**
- **Model / runtime:** Runs the full Legion Intelligence AI platform with pre-configured models; supports controlled model updates to disconnected nodes **with validation and rollback**. Vendor notes connectivity "is used to reach frontier models and to synchronize state when policy permits, but it is never required for operation."
- **Agent capabilities:** Genuine agentic platform: multi-agent, orchestration, human-in-the-loop, governed. **This is the most complete agentic-AI-offline product found in this survey.**
- **Security / identity:** Vendor-stated: IL2–IL6 authorization, **FedRAMP High**, **SOC 2 Type II**, **NIST 800-53** compliant, **CMMC Level 2**, "Ready to manage ITAR data", air-gap capable. HBOM and SBOM established, IL2–IL6 ready, versus "requires custom validation" for typical builds. **Grade C (vendor assertion, accreditation claims require independent verification).**
- **Integrations:** Partner hardware (Intel/NVIDIA/HPE); Rancher Kubernetes; ecosystem integrations with software, model, data and sensor providers; SI delivery channel.
- **Updates:** Controlled model updates to disconnected nodes with validation and rollback — **the single most important update-lifecycle capability found anywhere in this survey.**
- **License:** Proprietary commercial platform; also available as "Legion Packs". Terms not captured — **Grade D.**
- **Support model:** Lifecycle sustainment bundled into the Centurion package — an explicit differentiator vs software-only vendors who leave disconnected support to the customer.
- **Pricing evidence:** "Request a demo" / lead-capture form; no list price. **Grade C.**
- **Limitations:** **Buyer is national security via SI, not enterprise software teams.** Vendor explicitly says Centurion "is not a collection of on-device agents or a standalone inference appliance" — it is the full platform. Scope covers up to ~350 users for forward datacenters, embassies and air-gapped networks — a **scale ceiling well below a large enterprise**. No evidence of software-engineering-specific workflow (repository understanding, requirements traceability, test generation).
- **Customer proof:** Vendor-stated deployments across the DoW, intelligence community, DoE and DIB; a described case where the platform switched to locally hosted models with no operator intervention when the network dropped, on HPE EL8000S + Rancher. **Grade C.**
- **Sources:** "Centurion Edge AI System | Legion Intelligence", https://www.legionintel.com/reference/centurion (2026-08-09), accessed 2026-11-11, **A** for capability/mechanism, **C** for accreditation and customer claims; "Centurion | Deployable Edge AI", https://www.legionintel.com/centurion, accessed 2026-11-11, **A/C** as above.

### F2. Element 31 — Czar (sovereign AI appliance) / Substrate platform — **DC-near** (delivery platform, different buyer)

- **Buyer:** **ISVs** — software vendors who have a deal with a defence/regulated buyer and need their product to run air-gapped on hardware the customer controls. Element 31 is the integrator, not the software vendor.
- **Workflow:** Not an end-user product. Element 31 takes an ISV's deal, writes a hardware specification for the target environment (connected enclave / disconnected field use / full air-gap), manufactures the build, integrates the ISV's software image, and seals the enclosure. The unit ships with the **ISV's nameplate, boot splash and support line** — Element 31's manufacturing and sealing discipline underneath, invisible to the end buyer.
- **Deployment / isolation mode:** Sealed, physically isolated appliance; "Air-gapped, or connected only to the systems the customer already secures." Underlying software layer is **Substrate**, which provisions Czar. Hardware sized per engagement: compute, memory, storage, environmental hardening.
- **Offline support evidence:** Explicit air-gap positioning and an appliance model built for sealed, unauditable physical environments. **Grade C.**
- **Model / runtime:** Chosen by the ISV; Element 31 sizes the hardware. Czar is "One for a team; a Grid for every machine in the building, from any vendor."
- **Agent capabilities:** None product-level — the ISV's application image provides them. Element 31 states Czar "can assist a coding team" — a use-case reference, not a shipped coding capability.
- **Security / identity:** Sealed enclosure; physical custody is the trust anchor. Identity depth not published — **Grade D.**
- **Integrations:** Multi-vendor ("from any vendor"); ISV application images on Substrate.
- **Updates:** Not documented in the pages read — **Grade D.** Physical sealing makes update logistics a real question.
- **License:** Commercial per-engagement; "sold as an Element 31 product."
- **Support model:** Manufacturing, sealing, and hardware spec; ISV's support line faces the end buyer.
- **Pricing evidence:** Deal-specific, no list price. **Grade C.**
- **Limitations:** **This is the most important competitive finding in the survey for a platform vendor.** Element 31's model converts "we need to run air-gapped" into a procurement line item that an ISV fulfils — with Element 31 as the physical integrator and the ISV as the software owner. A wedge that sells software into the same deals can be **displaced by the incumbent ISV**, or can **ride this chassis** by becoming the software image on it. The vendor explicitly frames the seal as "a discipline" and the appliance as standing in "for the vendor showing up in person every time the system is audited."
- **Customer proof:** Framework described and marketed; no named customer captured. **Grade C.**
- **Sources:** "The appliance model: bringing cloud AI software to secure facilities — Element 31", https://e31.io/resources/appliance-model-cloud-software-secure-facilities (2026-08-10), accessed 2026-11-11, **C**; "Czar, the sovereign AI appliance" (homepage copy), https://e31.io/, accessed 2026-11-11, **C**.

### F3. Vault-OS (iron-gap.com) — **DC-near** (appliance, knowledge-oriented)

- **Buyer:** Organisations that "cannot afford cloud vulnerabilities" — defence/intel (SCIFs), healthcare/HIPAA, and physical-security or facility operators needing a sealed local system.
- **Workflow:** AI chat & reasoning over ingested knowledge with streaming responses; **workflow & agent engine** with a DAG runtime (Kahn topological sort) and sandboxed ReAct agent loops; multi-agent critic; HR module (directory, personnel records, department/clearance management); voice/video notes with fully local multilingual STT; one-time & limited media.
- **Deployment / isolation mode:** Turnkey appliance (vendor procures, assembles, calibrates and physically delivers pre-flashed) **or bring your own hardware**. Hardware-enforced isolation: encrypted enclave, **TPM 2.0 silicon binding**, **hash-chained audit ledger**, encrypted backup, department-scoped PostgreSQL tablespaces for physical separation between departments.
- **Offline support evidence:** "0 PACKET EGRESS", "TPM 2.0 ATTESTED", zero outbound network egress; updates are "**physically couriered, signed USB payloads**" verified against an embedded public key before ingestion — "There is no update channel to intercept because there is no channel." **Grade C** — vendor page, but the mechanism is specific and checkable.
- **Model / runtime:** Local inference with **PGVector + HNSW** index; local STT.
- **Agent capabilities:** Real agent runtime — DAG orchestration + sandboxed ReAct loops + multi-agent critic.
- **Security / identity:** Strongest security *claim set* in the survey (TPM binding, hash-chained audit, per-department tablespaces, signed offline updates) but all vendor-asserted. **Grade C.** Also an honest limitation: no master password and no key — loss is unrecoverable by anyone.
- **Integrations:** PostgreSQL, PGVector/HNSW; brings-your-own-hardware option.
- **Updates:** Couriered signed USB payloads with embedded-key verification and rollback implied. Strong offline update design.
- **License:** Proprietary, "in every tier" per vendor — safety features not sold as upgrades.
- **Support model:** Vendor; physical delivery.
- **Pricing evidence:** A public pricing page with an engineering sizing calculator (SG-tier style sizing). **Grade C.**
- **Limitations:** Oriented to **knowledge and HR workflows**, not software engineering. No evidence of repository understanding, requirements traceability, test generation or patch workflows. Apparent user base is physical-security/facilities and healthcare rather than regulated software teams. No evidence of SBOM/artifact provenance intake.
- **Customer proof:** Vendor-published positioning across defence, healthcare and enterprise. **Grade C.**
- **Sources:** "Enterprise Solutions & B2G Operations | Vault-OS", https://www.iron-gap.com/enterprise, accessed 2026-11-11, **C**.

### F4. Google Distributed Cloud air-gapped appliance — ADJ + CB (hardware + managed substrate)

- **Buyer:** Defence, intelligence and sovereign customers wanting Google-managed cloud services in tactical edge settings.
- **Workflow:** Deploy VMs and container workloads on the appliance's cluster; run managed Google Cloud services (Vertex AI OCR/STT/Translate, deep learning containers, IAM, encryption, block/object storage, load balancing, logging/monitoring).
- **Deployment / isolation mode:** Integrated hardware+software, physically disconnected, "sovereign cloud in a box"; ~100 lb (~45.3 kg), two-person carry; **not operational while moved**; Google (or delegates) installs, then hands to the customer.
- **Offline support evidence:** Official appliance documentation. **Grade A.**
- **Model / runtime:** Vertex AI; Google-provided deep learning containers.
- **Agent capabilities:** None specific to engineering.
- **Security / identity:** Secure boot, firewalls, IAM, encryption at rest/in transit, network security policies, optional **HSM** for customer-controlled keys. **DoD IL5 accreditation** — vendor-stated as the highest IL level achieved by the appliance.
- **Integrations:** Customer networks via appliance-specific networking hardware; Google Cloud services.
- **Updates:** Not documented for a sealed, handed-over appliance — **Grade D.** This is the largest operational unknown for GDC appliance buyers.
- **License:** Proprietary Google Cloud licensing.
- **Support model:** Google Cloud enterprise support; install by Google or delegate.
- **Pricing evidence:** Not fetched — **Grade D.**
- **Limitations:** Total Google stack dependency in exactly the estates that want minimal dependency; ~45 kg and immovable during transit constrains topology; re-accreditation likely per move; the substrate problem is solved so the wedge must compete on workflow only.
- **Customer proof:** Vendor-stated IL5; no named customer captured. **Grade C.**
- **Sources:** "About Google Distributed Cloud air-gapped appliance", https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/overview (updated 2026-10-26), accessed 2026-11-11, **A**; "Kubernetes clusters in GDC", https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters, accessed 2026-11-11, **A**.

### F5. SpaceGrade OS — hardware appliance (SG-1 / SG-2 / SG-3) — CB (appliance, different domain)

- **Buyer:** Aerospace and defence PLM teams (26 PLM modules) needing a local PLM + AI appliance with no cloud dependency.
- **Workflow:** PLM for aerospace/defence; pre-loaded local AI for document/signal work.
- **Deployment / isolation mode:** Turnkey 1U/2U rack server, pre-loaded with SpaceGrade OS, PostgreSQL, MinIO, Redis, **Ollama**, hardened Ubuntu Server LTS, Docker, automated backups, pre-loaded AI model weights. SG-2: 16-core Xeon, 128 GB ECC, 8 TB NVMe + 16 TB archive, NVIDIA L4 24 GB (72 W), "Runs 70B quantized models", 1U, dual 10 GbE + IPMI, 30–100+ users. SG-3 "SCIF": dual Xeon, 256 GB ECC, 16 TB NVMe + 64 TB archive, NVIDIA L40S 48 GB, "Runs full 70B models unquantized", 2U, quad 10 GbE + IPMI + hardware firewall.
- **Offline support evidence:** "No. The SG-3 is specifically designed for fully air-gapped operation with pre-loaded AI models." Updates: "We ship update packages on **encrypted USB drives** or via a secure one-way transfer mechanism"; connected appliances pull over HTTPS. Cold-spare inventory maintained for SG-3 with next-business-day replacement. **Grade C.**
- **Model / runtime:** Ollama local LLM inference, GPU-accelerated; GGUF-quantised 70B on L4, full 70B on L40S.
- **Agent capabilities:** None documented.
- **Security / identity:** Hardware firewall on SG-3, IPMI, ECC RAM, air-gap posture, encrypted update media.
- **Integrations:** PostgreSQL, MinIO (S3), Redis, Docker, Ollama.
- **Updates:** Encrypted USB or secure one-way transfer — a workable pattern.
- **License:** Proprietary SpaceGrade OS; platform fee + per-seat.
- **Support model:** Hardware warranty (90-day on appliance), remote setup call, premium plans, cold-spare replacement.
- **Pricing evidence:** **The strongest pricing evidence found in this survey.** SG-2: "$35,000+ one-time hardware + Year 1 license" for SG-3 (air-gapped/classified, 30–100+ users); Year 2+: "$24,000/yr + $500/mo platform + $89–149/seat". **Grade C (vendor page).**
- **Limitations:** **PLM domain, not software engineering.** A direct pricing anchor showing what an air-gapped appliance bundle costs in this market — useful for the wedge's own pricing model. Also shows the pattern: local models, hardware firewall, USB updates.
- **Customer proof:** None named; vendor-published specs. **Grade C.**
- **Sources:** "On-Prem Hardware Appliance — SpaceGrade OS", https://spacegrade.ai/appliance, accessed 2026-11-11, **C**.

### F6. Strike48 — on-prem / air-gapped agentic SecOps appliance — ADJ (security operations domain)

- **Buyer:** Security operations teams in classified, sovereign and isolated environments who want autonomous SecOps without telemetry leaving the country or the site.
- **Workflow:** Autonomous security operations — threat hunting, hypothesis-driven investigation, remediation with governed action and approval gates, data federation (query across sources without centralising).
- **Deployment / isolation mode:** Cloud, private cloud, **on-premises appliance or soft-appliance on customer hardware**; Kubernetes orchestrates the platform at system level in both cases, so the deployment model changes who owns the metal and nothing else. **Optional local inference layer on the appliance with GPU attached via PCI passthrough + CUDA**; no external API calls. One TLS endpoint for all external traffic; pods in dedicated VMs with network-policy separation.
- **Offline support evidence:** Official product page describing the fully air-gapped on-prem modality and local on-appliance inference. **Grade C.**
- **Model / runtime:** Hosted model access by default; optional on-appliance inference layer with local GPU.
- **Agent capabilities:** Genuine — hypothesis-driven investigation, governed remediation with approval gates, federated query. **Strong parallel to the wedge's human-in-the-loop model.**
- **Security / identity:** Network-policy separation per service, TLS endpoint, PCI passthrough GPU isolation. Depth not published — **Grade D.**
- **Integrations:** SIEM/telemetry sources, data federation, Kubernetes.
- **Updates:** Not documented for air-gap — **Grade D.**
- **License:** Commercial.
- **Support model:** Commercial + "Strike48 University SOC Program" (education). "Get a demo" — no list price.
- **Pricing evidence:** None published — **Grade C.**
- **Limitations:** **Cybersecurity domain, not software engineering.** Directly relevant anyway: it proves an appliance + local-GPU + Kubernetes + approval-gated autonomous agents pattern is already productised and saleable — i.e. the *delivery shape* of the wedge is not novel, only its engineering workflow is.
- **Customer proof:** Vendor-published positioning for classified/sovereign customers. **Grade C.**
- **Sources:** "On-Prem & Air-Gapped Agentic Security Operations Platform", https://www.strike48.com/platform/on-prem-ai-soc, accessed 2026-11-11, **C**.

### F7. Salian Defense — Praesidium Suite — CB (integrator, defence)

- **Buyer:** US defence/IC customers running systems at a CUI boundary or fully air-gapped inside accredited space.
- **Workflow:** Praesidium Suite — Sentinel (data-driven decision platform), Vigil (defines and evaluates the boundary policy an AI system must respect: what to allow, redact, or block), Hawk RAG (retrieval layer fusing vector, knowledge-graph and lexical retrieval), Pythian (inline FPGA-based hardware encryption for OT/control-system networks, partner hardware via white-label, not manufactured by Salian). Also custom tools for environments commercial software cannot reach.
- **Deployment / isolation mode:** Three deployment profiles — hosted/unclassified, CUI-safe on customer infrastructure, fully air-gapped inside accredited space. Platform built to run **fully offline with no outbound network traffic**. Differentiation method: build a high-fidelity digital twin of the target classified enclave and run engineering, configuration, validation and dry runs **on the unclassified networked side at full speed**, then transfer in as known-good work.
- **Offline support evidence:** Vendor page stating the fully-offline/no-outbound posture and the air-gapped profile. **Grade C.**
- **Model / runtime:** Language model as "an embedded, swappable provider rather than a standalone application"; ships deployment-profile resolution, content-free scan contracts, deterministic detector set.
- **Agent capabilities:** Vigil boundary-policy evaluation and Hawk RAG suggest governed AI use; agent detail not published — **Grade D.**
- **Security / identity:** Boundary policy definition/evaluation is the core IP; FPGA hardware encryption for OT.
- **Integrations:** OT/control-system networks, knowledge graphs, vector + lexical retrieval, partner FPGA hardware.
- **Updates:** "can be installed and updated inside the boundary rather than pulled from a vendor cloud" — an explicit accreditation-relevant requirement, and a criterion the vendor states most software fails. **Grade C.**
- **Support model:** Salian operates some public systems; integrator role with white-label hardware arrangements.
- **Pricing evidence:** None published; engagement-based. **Grade C.**
- **Limitations:** Programme/integrator model rather than product; the "digital twin" method is a strong, transferable idea for the wedge's own pre-validation pipeline but is not a product a customer can buy.
- **Customer proof:** Vendor-published defence positioning. **Grade C.**
- **Sources:** "Technology: Air-Gapped Mission Software and Custom Engineering | Salian Defense", https://saliandefense.com/technology, accessed 2026-11-11, **C**.

### F8. Forge AI Deployment — CB (systems integrator)

- **Buyer:** Defence/public sector, financial services and regulated enterprises buying "sovereign AI" — explicitly positioned as a *systems integrator, not a software reseller*, taking responsibility for architecture, deployment, hardening and steady-state operations.
- **Workflow:** End-to-end sovereign deployment: offline installation and update paths for no-outbound environments; documented network boundary with egress explicitly enumerated and enforced; custom model integration and optimisation (model selection by task/latency/compute, tuning on proprietary data inside the perimeter, quantisation); observability and utilisation monitoring; knowledge transfer so the customer's team can run it independently.
- **Deployment / isolation mode:** Enterprise data centre, edge site, or fully disconnected enclave; hardware sizing and capacity planning against the actual inference/tuning workload.
- **Offline support evidence:** Vendor services page stating offline installation and update paths and documented, enforced egress enumeration. **Grade C.**
- **Model / runtime:** Runs the **webAI** platform (Forge is the official webAI systems integrator); model-agnostic tuning and quantisation.
- **Agent capabilities:** Platform-dependent; the "no per-token bill" framing implies local inference.
- **Security / identity:** Documented network boundary with enumerated egress; integration with existing identity providers. Depth not published — **Grade D.**
- **Integrations:** Customer data sources, identity providers, internal applications.
- **Updates:** "Offline installation and update paths for environments with no outbound connectivity" — explicit but mechanics not published.
- **License:** Services engagement over the webAI platform.
- **Support model:** Steady-state operations plus knowledge transfer — explicitly designed to avoid customer dependence on the vendor.
- **Pricing evidence:** None published. **Grade C.**
- **Limitations:** **Pure services play.** 20+ years in secure environments, Fortune 100 operating experience — this is the *substitute threat*: a customer can buy an integrator to assemble the whole stack, including the governance layer, and own the result.
- **Customer proof:** Vendor-stated credentials; no named customer captured. **Grade C.**
- **Sources:** "Sovereign AI Deployment Services | Forge AI Deployment", https://forgeprivate.ai/solutions, accessed 2026-11-11, **C**.

### F9. Intumit — Aerospace and Defense AI — CB (integrator/platform, different buyer)

- **Buyer:** Defense system integrators, aerospace manufacturers, cyber vendors, simulation/training providers, government contractors, cloud/hardware providers, consulting firms and emerging AI startups.
- **Workflow:** Command decision-making, secure knowledge access, mission planning, operational readiness; **Secure Defense Knowledge Copilot** (summarises large defence documents, answers questions under role-based access, works offline/on-premise inside secure networks); **Autonomous Agentic AI for Defense Workflows** (multi-step reasoning: mission readiness, logistics planning, risk assessments, supply chain vulnerability analysis); Defence Industry Digital Assistant.
- **Deployment / isolation mode:** Cloud, on-premise, or hybrid; "Secure Defense Knowledge Copilot — On-premise, air-gapped, private cloud, hybrid, or sovereign cloud"; **offline-capable AI agents where required**; hardware-aware deployment.
- **Offline support evidence:** Vendor vertical page stating air-gapped and offline-capable agent modes. **Grade C.**
- **Model / runtime:** Multi-model, multi-vendor — proprietary and open-source foundation models, selected by mission, data sensitivity or region.
- **Agent capabilities:** Multi-step autonomous reasoning plus human-approval checkpoints/gateway — the "human-approval gateway" is directly relevant to the wedge's control model.
- **Security / identity:** Zero-trust architecture, RBAC, full logging/traceability/explainability, human-approval checkpoints, metadata/provenance/auditability.
- **Integrations:** Modular integration for system interoperability; partner ecosystem.
- **Updates:** Not documented — **Grade D.**
- **License:** Proprietary platform plus partner framework.
- **Support model:** Commercial platform with a "Partner" program for integrators.
- **Pricing evidence:** Not fetched — **Grade D.**
- **Limitations:** Domain-oriented (defence workflows: mission readiness, logistics, risk) rather than software-engineering workflows. Sells *into* the SI channel, which makes it a channel conflict **and** a distribution opportunity.
- **Customer proof:** Vendor-published positioning across defence sub-verticals. **Grade C.**
- **Sources:** "Aerospace and Defense AI - Intumit, Inc.", https://www.intumit.com/vertical/aerospace-and-defense-ai (2025-12-11), accessed 2026-11-11, **C**.

---

## 8. Customer-built and integrator-assembled alternatives (the real substitute)

These do not appear as products a buyer can compare, which is exactly why they are the most important entry in this matrix. Each is a way for the buyer to obtain the wedge's *function* without buying the wedge.

| # | Alternative | How the buyer assembles it | What it costs them | Evidence |
|---|---|---|---|---|
| CB-1 | **DIY: local model + Cline/Continue + OpenShift + Anchore** | Open-weight model on owned GPU; Cline or Continue for the agent loop; RKE2/OpenShift for runtime; Anchore for SBOM; internal glue and policy | A platform engineer to build and keep the glue; recurring disconnected-update labour; no accreditation evidence; every security property is homegrown | **D** (inference from A-graded layer docs in §2–§5) |
| CB-2 | **Integrator assembly (Forge, Salian, Intumit)** | Buy an SI to own architecture, hardening, updates, accreditation and ops | SI fees + the SI's platform margin; vendor lock-in shifts from software vendor to SI; the wedge becomes a component, not a competitor | **C** — Forge "systems integrator, not a software reseller", "we are a systems integrator, not a software reseller", taking "responsibility for the entire path"; Salian operates public systems and builds digital twins of classified enclines |
| CB-3 | **Appliance chassis (Element 31 / SpaceGrade / Vault-OS / GDC appliance)** | Buy a sealed, pre-integrated unit; vendor or ISV supplies the software image | Highest upfront cost, lowest integration risk; and the ISV owns the customer relationship, so a standalone wedge loses the deal unless it becomes the image | **C** — Element 31 "What ships out carries the ISV's nameplate, boot splash, and support line"; SpaceGrade SG-3 at $35,000+; Vault-OS turnkey pre-flashed delivery |
| CB-4 | **Do nothing / existing internal tooling** | Continue with current manual review, static analysis, hand-written scripts and internal scripts | No procurement, no accreditation burden, no vendor risk; cost is engineer-hours and quality is unchanged | **D** — no direct evidence collected in this pass; **this is the most important missing evidence** |
| CB-5 | **National-security productised by an incumbent ISV (Legion Centurion)** | Buy an accredited, IL2–IL6, air-gap-capable agentic platform already inside an approved procurement vehicle | Rapid accreditation vs years of building one; but wrong domain (not software engineering), scale-capped (~350 users), and priced as an enterprise platform | **C** — Legion's stated posture and capabilities |
| CB-6 | **Rebuild on a "sovereign cloud in a box" (GDC appliance)** | Buy a fully disconnected managed cloud and build on it | Solves substrate, updates, accreditation; but locks the estate to one vendor's stack and constrains physical deployment | **A/C** — GDC appliance IL5, managed Harbor, Vertex AI, ~45 kg unit |

**Strategic reading (Grade D).** CB-2, CB-3 and CB-5 together constitute the dominant threat. The wedge's most likely failure mode is not a competitor shipping the same product; it is a customer buying an integrator or an accredited appliance and *never issuing a requirement for the layer the wedge sells*, because the layer gets absorbed into somebody else's scope of work.

---

## 9. Full source register

| # | Source title | URL | Published/updated | Accessed | Grade |
|---|---|---|---|---|---|
| S1 | Enterprise-Grade Inference Software Stack — NVIDIA NIM for LLM and VLM | https://docs.nvidia.com/nim/large-language-models/latest/about-nim-llm/enterprise-grade.html | — | 2026-11-11 | A |
| S2 | Air-Gap Deployment — NVIDIA NIM for LLM and VLM | https://docs.nvidia.com/nim/large-language-models/latest/deploy-air-gap.html | — | 2026-11-11 | A |
| S3 | Air Gap Deployment — NVIDIA NIM for Vision Language Models | https://docs.nvidia.com/nim/vision-language-models/1.4.0/deploy-air-gap.html | 2025-09-25 | 2026-11-11 | A |
| S4 | About — Lamini Docs | https://docs.lamini.ai/about | — | 2026-11-11 | C |
| S5 | Pricing — Lamini | https://www.lamini.ai/pricing | — | 2026-11-11 | C |
| S6 | Product — Lamini | https://www.lamini.ai/product | — | 2026-11-11 | C |
| S7 | Benchmarking with GuideLLM in air-gapped OpenShift clusters | https://developers.redhat.com/articles/2025/09/15/benchmarking-guidellm-air-gapped-openshift-clusters | 2025-09-15 | 2026-11-11 | A |
| S8 | How to operate OpenShift in air-gapped environments | https://developers.redhat.com/articles/2026/03/19/how-operate-openshift-air-gapped-environments | 2026-03-19 | 2026-11-11 | A |
| S9 | About disconnected environments — OKD 4.21 | https://docs.okd.io/4.21/disconnected/about.html | — | 2026-11-11 | A |
| S10 | About disconnected environments — OKD 4.17 | https://docs.okd.io/4.17/disconnected/about.html | — | 2026-11-11 | A |
| S11 | About disconnected environments — OKD 4.18 | https://docs.okd.io/4.18//disconnected/about.html | — | 2026-11-11 | A |
| S12 | RKE2 air-gap install | https://docs.rke2.io/install/airgap | — | 2026-11-11 | A (register) |
| S13 | K3s air-gap install | https://docs.k3s.io/installation/airgap | — | 2026-11-11 | A (register) |
| S14 | Offline inference — vLLM documentation | https://docs.vllm.ai/en/latest/serving/offline_inference/ | — | 2026-11-11 | A |
| S15 | llama.cpp (repository) | https://github.com/ggml-org/llama.cpp | — | 2026-11-11 | A |
| S16 | Kubernetes clusters in GDC — Google Distributed Cloud air-gapped | https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters | — | 2026-11-11 | A |
| S17 | About Google Distributed Cloud air-gapped appliance | https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/overview | 2026-10-26 | 2026-11-11 | A |
| S18 | Air-Gapped and Offline Installation — Testkube Documentation | https://docs.testkube.io/articles/install/air-gapped | — | 2026-11-11 | A |
| S19 | Preparing your cluster for an air-gapped (offline) deployment on OCP (Content Cortex 26.0.0) | https://www.ibm.com/docs/en/content-cortex/26.0.0?topic=cluster-preparing-your-air-gapped-offline-deployment | — | 2026-11-11 | A |
| S20 | Option 2: Preparing your cluster for an air-gapped (offline) deployment (Cloud Pak for Business Automation 26.0.0) | https://www.ibm.com/docs/en/cloud-paks/cp-biz-automation/26.0.0?topic=icmppd-option-2-preparing-your-cluster-air-gapped-offline-deployment | 2026-11-03 | 2026-11-11 | A |
| S21 | Preparing your cluster for an air-gapped (offline) deployment (BAW 25.0.x) | https://www.ibm.com/docs/en/baw/25.0.x?topic=configuring-preparing-your-cluster-air-gapped-offline-deployment | — | 2026-11-11 | A |
| S22 | Cline + Ollama: Local AI Coding Agent for VS Code — Markaicode | https://markaicode.com/integrate/local-coding-assistant-with-ollama/ | 2026-05-29 (verified Aug 2026) | 2026-11-11 | B |
| S23 | I ditched VS Code's Copilot for a local LLM, and I'm getting more done offline — XDA | https://www.xda-developers.com/ditched-vs-code-copilot-local-llm-getting-more-done-offline/ | 2026-09-23 | 2026-11-11 | B |
| S24 | LocalPilot Agent — Visual Studio Marketplace | https://marketplace.visualstudio.com/items?itemName=localpilot.localpilot-agent | — | 2026-11-11 | C |
| S25 | Sovereign Agent — Local AI & Ollama Coding Assistant — VS Marketplace | https://marketplace.visualstudio.com/items?itemName=ertugrul37.sovereign-agent | 2026-10-09 (changelog) | 2026-11-11 | C |
| S26 | LocalCode — Open-Source AI Coding Agent That Runs in Your Terminal | https://www.localcode.codes/ | — | 2026-11-11 | C |
| S27 | DeskAI — Local AI Coding Assistant — VS Marketplace | https://marketplace.visualstudio.com/items?itemName=AbhishekMishra9454.deskai-local | — | 2026-11-11 | C |
| S28 | odanree/llm-local-assistant — GitHub | https://github.com/odanree/llm-local-assistant | created 2025-11-19, 291 commits | 2026-11-11 | C |
| S29 | offgrid: local AI — VS Marketplace | https://marketplace.visualstudio.com/items?itemName=Pinta365.offgrid | — | 2026-11-11 | C |
| S30 | Air-gapped Deployments — Coder Docs | https://coder.com/docs/install/prepare/airgap | — | 2026-11-11 | A |
| S31 | Run AI coding agents in Coder | https://coder.com/docs/ai-coder/ | — | 2026-11-11 | A |
| S32 | Software Supply Chain Management Platform — Anchore Enterprise | https://anchore.com/enterprise | — | 2026-11-11 | C |
| S33 | Software supply chain security for the public sector — Anchore | https://anchore.com/platform/public-sector | 2022-03-01 | 2026-11-11 | C |
| S34 | Introducing Anchore Enterprise 1.1 — Anchore | https://anchore.com/blog/introducing-anchore-enterprise-1-1 | 2018-08-07 | 2026-11-11 | A (mechanism) |
| S35 | Generating SBOMs — Anchore Enterprise Documentation | https://docs.anchore.com/6.2/docs/sbom_management/generate | — | 2026-11-11 | A |
| S36 | Mastering software governance in air-gapped, critical mission environments — Sonatype | https://www.sonatype.com/blog/mastering-software-governance-in-air-gapped-critical-mission-environments | 2025-11-12 | 2026-11-11 | C |
| S37 | Sonatype Lifecycle — SCA Tools for Open Source Security | https://www.sonatype.com/products/open-source-security-dependency-management | — | 2026-11-11 | C |
| S38 | Offline environments — GitLab Docs | https://docs.gitlab.com/user/application_security/offline_deployments/ | — | 2026-11-11 | A |
| S39 | SBOM Central — t2data | https://t2data.com/products/sbomcentral | — | 2026-11-11 | C |
| S40 | Deployment Options — Haystack Enterprise Platform Documentation | https://docs.cloud.deepset.ai/docs/deployment-options | — | 2026-11-11 | A |
| S41 | Feature List — Haystack Enterprise Platform | https://docs.cloud.deepset.ai/docs/feature-list | — | 2026-11-11 | A |
| S42 | What's Haystack Enterprise Platform? | https://docs.cloud.deepset.ai/docs/getting-started | — | 2026-11-11 | A |
| S43 | ELSER — Elastic Docs | https://www.elastic.co/docs/explore-analyze/machine-learning/nlp/ml-nlp-elser | — | 2026-11-11 | A |
| S44 | Elastic Brings Jina Multimodal and Multilingual Semantic Search to On-Premises and Air-Gapped Environments | https://ir.elastic.co/News--Events/news/news-details/2026/Elastic-Brings-Jina-Multimodal-and-Multilingual-Semantic-Search-to-On-Premises-and-Air-Gapped-Environments/default.aspx | 2026-07-27 | 2026-11-11 | C |
| S45 | Self-Hosted AI & RAG — Air-Gapped Retrieval-Augmented Generation — Varuni Systems | https://varunisystems.com/products/ai-rag | — | 2026-11-11 | C |
| S46 | Tools for AI Team Knowledge Management in an Air-Gapped Environment (2026 Recommendations) — ONES.com | https://ones.com/blog/tool-guide/tools-for-ai-team-knowledge-management-in-an-air-gapped-environment-2026-recommendations | 2026-08-24 | 2026-11-11 | C |
| S47 | Centurion Edge AI System — Legion Intelligence | https://www.legionintel.com/reference/centurion | 2026-08-09 | 2026-11-11 | A (capability) / C (accreditation) |
| S48 | Centurion \| Deployable Edge AI — Legion Intelligence | https://www.legionintel.com/centurion | — | 2026-11-11 | A / C |
| S49 | The appliance model: bringing cloud AI software to secure facilities — Element 31 | https://e31.io/resources/appliance-model-cloud-software-secure-facilities | 2026-08-10 | 2026-11-11 | C |
| S50 | Enterprise Solutions & B2G Operations — Vault-OS | https://www.iron-gap.com/enterprise | — | 2026-11-11 | C |
| S51 | On-Prem Hardware Appliance — SpaceGrade OS | https://spacegrade.ai/appliance | — | 2026-11-11 | C |
| S52 | Sovereign AI Deployment Services — Forge AI Deployment | https://forgeprivate.ai/solutions | — | 2026-11-11 | C |
| S53 | On-Prem & Air-Gapped Agentic Security Operations Platform — Strike48 | https://www.strike48.com/platform/on-prem-ai-soc | — | 2026-11-11 | C |
| S54 | Technology: Air-Gapped Mission Software and Custom Engineering — Salian Defense | https://saliandefense.com/technology | — | 2026-11-11 | C |
| S55 | Aerospace and Defense AI — Intumit, Inc. | https://www.intumit.com/vertical/aerospace-and-defense-ai | 2025-12-11 | 2026-11-11 | C |

---

## 10. Claim records (schema §6, condensed)

```yaml
claim_id: C-0101
claim: "No product in the surveyed set supplies the complete secure offline agentic engineering workbench (engineering workflow + local reasoning + governed execution + provenance/air-gap lifecycle) to enterprise software teams."
claim_type: competitive
status: partially_verified
source_title: "Aggregate of S1-S55 (see §9)"
source_url: "multiple — see COMPETITOR_MATRIX.md §9"
author_or_organization: "W1 analysis"
published_or_updated: ""
accessed: "2026-11-11"
source_section_or_lines: "§1 classification summary; §4 C10; §7 F1-F9; §8"
evidence_grade: D
supporting_excerpt_or_test: "Layer-discipline audit across all 27 solutions: every solution's workflow field lands in exactly one layer. Closest are F1 (Legion Centurion, national-security buyer, no engineering workflow evidence) and F3 (Vault-OS, knowledge/HR workflow)."
contradicting_evidence:
  - "F1 Legion Centurion is an integrated agentic AI platform with air-gap, IL2-IL6, human-in-the-loop, SBOM/HBOM and rollback-capable model updates. If it adds engineering workflows, DC count becomes 1."
  - "This survey is a web-research pass; a private or unannounced product would not appear."
assumptions:
  - "The wedge scope in 01_MASTER_VISION_AND_STRATEGY.md §5 is the correct target layer."
confidence: medium
what_would_change_the_conclusion: "Evidence that Legion, Red Hat, deepset, IBM, or an ISV ships an offline agentic coding/testing workbench aimed at enterprise software teams."
```

```yaml
claim_id: C-0102
claim: "The local coding-agent layer is well-supplied for individuals and empty at the enterprise/accredited end."
claim_type: competitive
status: verified
source_title: "S24-S29 (five independent VS Code/CLI local coding agents)"
source_url: "https://marketplace.visualstudio.com/items?itemName=localpilot.localpilot-agent"
author_or_organization: "LocalPilot / Sovereign Agent / LocalCode / DeskAI / llm-local-assistant / offgrid"
published_or_updated: ""
accessed: "2026-11-11"
source_section_or_lines: "Marketplace feature tables and licence sections"
evidence_grade: C
supporting_excerpt_or_test: "Uniform feature sets (local model servers, plan/ask/agent modes, edit+terminal, approval prompts, MCP, zero telemetry). Zero published mention of enterprise identity, RBAC, scoped agent principals, immutable approval ledger, SBOM/provenance intake, signed asset verification, air-gap update lifecycle or accreditation evidence. Install counts 261 / 18 / 159 / 14 with 0 ratings on four of five."
contradicting_evidence:
  - "Absence of published evidence is not absence of capability; these are small projects whose maintainers may not publish enterprise features."
assumptions:
  - "Marketplace listings reflect actual product capability (README claims are treated as claims, not facts)."
confidence: medium-high
what_would_change_the_conclusion: "A local coding agent with published SSO/SCIM, RBAC, audit ledger and signed-update support."
```

```yaml
claim_id: C-0103
claim: "Disconnected-update lifecycle, not inference, is the binding engineering constraint across this market."
claim_type: technical
status: verified
source_title: "S8, S18, S34, S47, S50, S51, S54"
source_url: "https://developers.redhat.com/articles/2026/03/19/how-operate-openshift-air-gapped-environments"
author_or_organization: "Red Hat; Testkube; Anchore; Legion Intelligence; Vault-OS; SpaceGrade OS; Salian Defense"
published_or_updated: "2026-03-19 (S8); 2026-08-09 (S47)"
accessed: "2026-11-11"
source_section_or_lines: "S8 'operational cadence'; S18 offline licence; S34 on-prem Feed Service; S47 'controlled model updates ... with validation and rollback'; S50 'signed USB payloads'; S51 'encrypted USB drives'; S54 'installed and updated inside the boundary'"
evidence_grade: A
supporting_excerpt_or_test: "Seven independent vendors each ship a bespoke offline update/refresh mechanism; none treats it as a solved, shared problem."
contradicting_evidence: []
assumptions:
  - "Vendor-documented mechanisms are implemented, not aspirational."
confidence: high
what_would_change_the_conclusion: "A vendor demonstrating a shared, standards-based offline update framework across multiple layers."
```

```yaml
claim_id: C-0104
claim: "Even the desktop IDE side of an offline engineering toolchain requires internet, so offline workbenches must pre-stage the IDE."
claim_type: technical
status: verified
source_title: "Air-gapped Deployments — Coder Docs"
source_url: "https://coder.com/docs/install/prepare/airgap"
author_or_organization: "Coder"
published_or_updated: ""
accessed: "2026-11-11"
source_section_or_lines: "'Microsoft VS Code Remote - SSH' section"
evidence_grade: A
supporting_excerpt_or_test: "VS Code Remote-SSH installation requires outbound HTTPS to update.code.visualstudio.com, vscode.blob.core.windows.net, *.vo.msecnd.net. JetBrains Gateway and code-server have comparable documented exceptions (code-server.dev, open-vsx.org)."
contradicting_evidence:
  - "JetBrains Gateway has documented offline deployment steps (linked from Coder's own page), so a fully offline IDE path exists but is vendor-specific."
assumptions:
  - "The customer environment blocks outbound internet to these hosts."
confidence: medium-high
what_would_change_the_conclusion: "Microsoft or JetBrains publishing a fully offline, internally-mirrorable IDE distribution with no update-time internet dependency."
```

```yaml
claim_id: C-0105
claim: "An ISV/appliance chassis can displace a standalone product in the same deal without competing with it."
claim_type: competitive
status: hypothesis
source_title: "The appliance model: bringing cloud AI software to secure facilities — Element 31"
source_url: "https://e31.io/resources/appliance-model-cloud-software-secure-facilities"
author_or_organization: "Element 31"
published_or_updated: "2026-08-10"
accessed: "2026-11-11"
source_section_or_lines: "'The mechanics follow a pattern rather than a fixed sequence' section"
evidence_grade: D
supporting_excerpt_or_test: "Element 31 converts an ISV's air-gapped deal into a sealed appliance carrying the ISV's nameplate and support line. Under this pattern, the software vendor supplies an image and the chassis vendor owns the physical delivery; a standalone software product must be selected by the ISV before any chassis is chosen."
contradicting_evidence:
  - "Element 31 explicitly serves ISVs who want to sell air-gapped — i.e. it needs software vendors to exist and win."
  - "No named deal evidence in this pass."
assumptions:
  - "Element 31's described model is representative of the market, not a single vendor's approach."
confidence: medium
what_would_change_the_conclusion: "A procurement notice or case study showing a standalone software product sold alongside an appliance chassis to the same end buyer."
```

```yaml
claim_id: C-0106
claim: "The 'do nothing' alternative (existing internal tooling and manual review) is the least-evidenced and most consequential alternative in the matrix."
claim_type: market
status: hypothesis
source_title: "n/a — no source collected"
source_url: ""
author_or_organization: ""
published_or_updated: ""
accessed: "2026-11-11"
source_section_or_lines: "CB-4 in §8"
evidence_grade: D
supporting_excerpt_or_test: "No evidence was collected in this pass on current customer workflow, cost or acceptance of no AI tooling in disconnected engineering estates."
contradicting_evidence: []
assumptions:
  - "This remains true after Agent 7 (customer discovery) runs."
confidence: low
what_would_change_the_conclusion: "15-25 customer interviews capturing current workflow, cost and consequences."
```

---

## 11. W1 scope note for the next agent

This pass covers **product and market reality (protocol Layer 4)** at excerpt level. It does **not** cover Layer 3 (implementations and engineering reality: source, LICENSE files, tests, release history) — which the protocol requires before any open-source substitute claim is trusted, and which bears directly on whether Continue is genuinely unmaintained (C2) and on the actual maturity of the five local coding agents (C3–C8). It also does not cover Layer 6 (customer discovery), which is the only way to close C-0106.

Priority verification list for the next pass:
1. **Continue maintenance status** — read `continuedev/continue` repo state, last release, commit activity. (C2, B-grade claim needs A-grade confirmation.)
2. **LICENSE files** for vLLM, llama.cpp, SGLang, Cline, Continue, LocalCode, LocalPilot, llm-local-assistant, offgrid, Syft/Grype. (Governs reuse and redistribution.)
3. **Extend §8 CB-4** with customer-interview evidence — the "do nothing" baseline.
4. **Air-gap update mechanics** for GDC appliance and OpenAI-compatible enterprise platform air-gap updates (E1, F4) — currently Grade D and both are plausible wedge targets.
5. **Pricing**: fetch Anchore, Sonatype, Red Hat OpenShift AI, GitLab, deepset, Elastic pricing pages — currently the weakest-evidenced field in the matrix.
