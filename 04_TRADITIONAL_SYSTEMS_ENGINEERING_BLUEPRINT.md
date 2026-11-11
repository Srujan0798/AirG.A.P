# 04 — Traditional Systems Engineering & Product Architecture

**Purpose:** Define the engineering foundations independently of any one plugin, agent framework or vendor.  
**Product hypothesis:** Secure Offline Agentic Engineering Workbench.  
**Architecture status:** Reference design for research/prototyping; not a frozen implementation specification.

---

## 1. System requirements

### Functional requirements

- Run approved model artifacts and inference runtimes locally.
- Support customer-approved repositories, documentation and engineering artifacts.
- Perform source-grounded codebase understanding and retrieval.
- Execute bounded agent workflows with explicit state and tool permissions.
- Generate test proposals and patch proposals.
- Run tests and builds inside constrained sandboxes.
- Maintain provenance for user input, retrieved context, model, prompt, tool call, artifact, test and approval.
- Operate without public internet access after approved installation.
- Support offline update, rollback, backup and restore.
- Expose administrative controls, user authentication and audit export.

### Non-functional requirements

- Security: least privilege, strong isolation, auditable actions and safe failure.
- Reliability: durable task state, restart recovery and bounded retries.
- Performance: measured response and throughput against named workloads and hardware.
- Maintainability: modular runtime adapters, pinned dependencies and documented support matrix.
- Portability: support only hardware/OS combinations that have actually been tested.
- Reproducibility: model, code, index, config and prompt versions recorded.
- Operability: local health, logs, backup, restore and diagnostics.
- Usability: developers can inspect evidence, understand uncertainty and review changes.

Do not invent numeric service-level objectives before workload and hardware discovery. Define initial SLOs during the pilot.

## 2. Reference architecture

```text
┌──────────────────── CUSTOMER TRUST BOUNDARY ────────────────────┐
│                                                                  │
│  Users / IDE / Admin UI                                          │
│          │                                                       │
│          ▼                                                       │
│  Identity + RBAC/ABAC + Approval Service                         │
│          │                                                       │
│          ▼                                                       │
│  API Gateway / Policy Enforcement Point                          │
│          │                                                       │
│          ├──────────────► Audit Event Store (append-only)         │
│          │                                                       │
│          ▼                                                       │
│  Durable Workflow / State Machine                                │
│          │                                                       │
│          ├──────► Task Planner / Agent Coordinator               │
│          │                 │                                     │
│          │                 ▼                                     │
│          │         Tool Gateway / Capability Broker              │
│          │                 │                                     │
│          │                 ├────► Read-only Repo/Docs Tools       │
│          │                 ├────► Local Retrieval / Code Graph   │
│          │                 ├────► Build/Test Sandbox             │
│          │                 └────► Patch/Artifact Proposal         │
│          │                                                       │
│          ├──────► Model Gateway ─────► Local Inference Runtime   │
│          │                            (model adapter)            │
│          │                                                       │
│          ├──────► Evaluation Service                              │
│          │                                                       │
│          └──────► Human Review / Merge Approval                   │
│                                                                  │
│  Local Storage: relational state | object artifacts | indexes    │
│  Local Operations: metrics | logs | backups | recovery           │
└──────────────────────────────────────────────────────────────────┘

Separate connected staging zone:
model/package/image acquisition → scanning → license/provenance checks
→ signed manifest + SBOM → two-person approval → transfer bundle

Offline import gateway:
quarantine → signature/hash validation → policy check → approval
→ local registry/model store → installation/rollback evidence
```

This design is conceptual. A single-node MVP may combine some services into one deployable process. Keep logical security boundaries even when processes share a host.

## 3. Control plane versus probabilistic reasoning

Use LLMs for tasks where language understanding and synthesis are valuable: interpreting requests, retrieving context, proposing plans, generating patches, explaining failures and drafting tests.

Use deterministic software for tasks that require authority and reproducibility:

- Authentication and authorization.
- Allowed tool and filesystem scope.
- Workflow state transitions.
- Retry limits, timeouts and task cancellation.
- Build/test invocation.
- Hash and signature verification.
- Artifact import approval.
- Merge/release/deployment gating.
- Audit recording and policy enforcement.
- Resource quotas and network isolation.

An LLM may propose a tool call, but a policy enforcement point must decide whether it is allowed. The agent must not decide its own permissions.

## 4. Workflow and orchestration architecture

### Recommended starting model

A durable state machine/workflow engine with an append-only event history. Represent independent subtasks as a DAG where that structure is helpful, but do not assume the entire system is a DAG.

Real agent workflows contain loops, retries, human approvals, timeouts, cancellation, partial completion and long-lived state. A DAG alone does not define their semantics.

### Minimum task state

```text
CREATED
  → SPECIFIED
  → PLANNED
  → AUTHORIZED
  → RUNNING
  → VALIDATING
  → AWAITING_REVIEW (when required)
  → ACCEPTED / REJECTED
  → MERGED (only with approval)
  → CLOSED

Failure paths: RETRYABLE_FAILURE, BLOCKED, CANCELLED, TERMINATED, ROLLED_BACK
```

Every transition must be checked by deterministic code and leave an audit event.

### Concurrency

- Parallelize read-only analysis and independent modules.
- Use isolated branches/worktrees for write tasks.
- Assign file/module ownership per task.
- Track dependency and shared-resource conflicts.
- Require integration tests and code review before merge.
- Limit concurrency by CPU/GPU, memory, I/O and review capacity.
- Avoid 30 agents editing the same repository without coordination.

### State and messaging

Do not choose Redis solely because a prior export named it. Evaluate durable workflow frameworks, PostgreSQL-backed queues, NATS JetStream, RabbitMQ, embedded stores and simpler single-process designs against actual needs.

For the MVP, a relational database as authoritative task state plus a small job runner may be enough. Introduce a broker when measured concurrency or deployment topology justifies it. Never put critical state only in volatile queue messages.

## 5. Model and inference layer

### Model policy

- Prefer open-weight models whose actual license permits the intended commercial deployment and redistribution pattern.
- “Open weights” is not equivalent to OSI-approved open-source software. Verify the model's own license, acceptable-use terms, attribution, notice, redistribution and derivative requirements.
- Pin exact model revision/commit, tokenizer, chat template, configuration and quantized artifact hash.
- Review remote model code. Disable remote code execution unless specifically reviewed and required.
- Keep model cards, evaluation reports, provenance and license records.
- Do not assume quantization preserves coding quality. Measure it on the product's task set.

### Runtime candidates

| Runtime | Candidate role | Key evaluation dimensions |
|---|---|---|
| llama.cpp | Lightweight/local and CPU/GPU hybrid inference; GGUF/quantized models. | Model compatibility, token rate, memory, batching, concurrency, hardware backend. |
| vLLM | Higher-throughput serving, batching and multi-GPU deployments. | Supported architecture, GPU requirements, scheduling, concurrency, offline model load. |
| SGLang | High-performance structured serving and multi-request inference. | Model support, structured outputs, serving stability, accelerator compatibility. |
| NVIDIA NIM / TensorRT-LLM | Vendor-optimized NVIDIA deployment and packaged enterprise serving. | License/support, hardware lock-in, air-gap cache process, profile/version compatibility. |
| Ollama | Developer workstation and fast local prototype experience. | Operational controls, concurrency, observability and suitability for target deployment. |
| Other validated runtimes | Add only if a workload or hardware profile needs them. | Same benchmark and security protocol. |

Use one primary serving runtime for the first pilot. Keep an internal adapter to prevent model-serving code from leaking throughout the product.

### Model selection benchmark

For each candidate model and hardware profile measure:

- Task success on real customer-like tasks.
- Patch correctness and accepted-test rate.
- Hallucinated symbols/APIs and invalid tool calls.
- Context degradation on long repositories.
- Structured output/function-call reliability.
- Latency to first token and completion latency.
- Tokens/second and concurrent sessions.
- Peak GPU/CPU memory and KV-cache use.
- Power, storage and thermal limits where relevant.
- Quantization quality drop.
- Offline load/startup and restart behaviour.
- Model/license and supply-chain acceptability.

Do not train a model first. Start with a suitable open-weight model plus deterministic tools, local retrieval and task-specific prompting. Fine-tune or use adapters only when evaluation shows a repeatable gap that cannot be economically solved by retrieval, workflow constraints or model selection.

## 6. Retrieval, memory and code intelligence

Use separate stores with explicit authority:

- **Relational store:** users, roles, task states, permissions, approvals, configuration and metadata.
- **Object store/filesystem:** source snapshots, generated patches, test results, model artifacts and evidence bundles.
- **Vector index:** semantic retrieval over approved documentation and source chunks; rebuildable from canonical source data.
- **Code/knowledge graph:** symbols, modules, dependencies, interfaces, requirements, tests and provenance edges.
- **Event log:** immutable record of state transitions and tool actions.

Do not call a combination of relational, vector and graph storage one “database” without defining which system is authoritative. Every retrieval chunk should carry source path, revision/hash, line or symbol range, timestamp and access label.

### Memory safety

- Distinguish durable verified project facts from agent-generated summaries.
- Store decision records with author, timestamp and source.
- Treat retrieved text and previous model outputs as untrusted data.
- Avoid persisting secrets or credentials in semantic memory.
- Define retention and deletion behaviour.
- Prevent one user's or project’s memory from being exposed to another.

## 7. Execution sandbox and tool gateway

### Minimum isolation model

A generated program must not run directly on the control-plane host.

Use a disposable worker environment—container with hardened controls or a VM/microVM depending on threat model—with:

- Non-root user and dropped Linux capabilities.
- Read-only base image and read-only source snapshot.
- Separate scratch worktree/output directory.
- No host home directory, SSH agent, Docker socket or production secrets.
- Network namespace with egress denied by default.
- Explicitly allowlisted local test services only.
- CPU, memory, process, file-size and execution-time limits.
- Seccomp plus AppArmor/SELinux or equivalent host policy.
- Ephemeral credentials scoped to the task.
- Output scanning and controlled artifact export.
- Worker destruction after task completion.

For stronger threat models, test VM/microVM isolation rather than assuming containers are sufficient. The correct boundary is determined by the customer threat model and independent security review.

### AST analysis is not sufficient

An AST or static analyzer can detect some source patterns. It cannot prove that code is safe, terminate all malicious behaviour, prevent runtime exploits or stop network exfiltration by itself. Use static analysis as one signal within layered controls.

### Tool gateway

All agent actions go through a policy gateway. Define each tool with:

- Name and version.
- Input/output schema.
- Allowed identity and role.
- Read/write scope.
- Filesystem and network scope.
- Resource limits.
- Required approval class.
- Audit event type.
- Timeout, retry and failure semantics.

The default must be deny. New tools do not become authorized just because an agent discovers them.

## 8. Security and trust model

### Assets

Source code, intellectual property, engineering documents, credentials, model weights, datasets, build artifacts, test results, user identities, audit evidence and system configuration.

### Adversaries

External attackers who compromise staging media or dependencies; malicious or compromised packages/models/plugins; insiders; users with excessive privileges; prompt injection embedded in documents or repositories; compromised agent dependencies; compromised build infrastructure; and accidental operator error.

### Core controls

- Network segmentation and deny-by-default egress.
- Zone/conduit architecture where OT or separate security zones are involved.
- Strong user and service identities; short-lived task credentials.
- Least privilege and separation of duties.
- Code execution isolation and resource quotas.
- Signed model/software artifacts and version pinning.
- SBOM, provenance and license records.
- Immutable or tamper-evident audit storage.
- Secure boot/host hardening where required by deployment.
- Secrets management and controlled recovery keys.
- Prompt-injection and tool-misuse testing.
- Backup/restore and incident response runbooks.
- Human review before high-impact changes.

Relevant references: NIST SP 800-82 Rev. 4 draft for OT security; NIST SP 800-218 for secure software development; OWASP 2026 agentic and LLM risk lists; MITRE ATT&CK for ICS; ISA/IEC 62443 for industrial automation security. Standards relevance depends on the customer and jurisdiction.

## 9. Artifact and update pipeline

### Connected staging

1. Acquire source, packages, container images, model files, drivers, documentation and vulnerability feeds.
2. Pin exact versions and source revisions.
3. Verify source authenticity and license/redistribution rights.
4. Scan dependencies and files; create SBOM and provenance records.
5. Build in a controlled environment with recorded toolchain.
6. Sign a manifest with a controlled key.
7. Create a transfer bundle and record its hashes.
8. Require the designated approvers.

### Offline import

1. Receive media/bundle into quarantine.
2. Verify manifest signature, hashes, version and approval.
3. Scan and inspect content using offline tools.
4. Check for rollback/downgrade and stale vulnerability metadata.
5. Approve with separation of duties.
6. Promote into local registry/model store.
7. Install into test/staging before production.
8. Verify health and record evidence.
9. Preserve rollback path.

TUF can inform secure update metadata and rollback protections. SPDX or CycloneDX can inform inventory formats. SLSA provenance and signing approaches should be evaluated for the build pipeline. These technologies do not automatically solve the customer’s physical transfer or accreditation process.

## 10. Offline deployment profiles

Define customer profiles rather than promising universal support.

| Profile | Network | Initial support strategy |
|---|---|---|
| P0 — On-prem connected | Customer-owned network, internet permitted by policy. | Simplest development profile; not an air-gap proof. |
| P1 — Restricted egress | Outbound access allowlisted or proxied. | Explicit egress policy, logs and proxy integration. |
| P2 — Disconnected with transfer gateway | No direct internet from runtime; approved controlled imports/updates. | Staging, signed transfer bundle, offline registry. |
| P3 — Fully air-gapped | No routable connection to outside networks. | Complete local assets, offline operations, controlled media and verified maintenance. |

Product claims must specify which profile is supported and tested.

## 11. Evaluation and release gates

### Functional tests

- Local inference from local files with network disabled.
- Retrieval citation correctness.
- Tool argument/schema validation.
- State persistence after process crash/restart.
- Sandbox timeout, resource-limit and no-egress tests.
- Patch application and regression tests.
- Human approval and rejection paths.
- Audit reconstruction of a complete run.

### Security tests

- Prompt injection in source comments, README files, issue text and docs.
- Agent attempts to read secrets or unrelated directories.
- Agent attempts network egress and local network pivoting.
- Malicious package/model/artifact import.
- Downgrade/rollback attempt.
- Cross-user/project retrieval leakage.
- Sandbox escape test by qualified red-team reviewers.
- Memory poisoning and inter-agent spoofing.

### Release gates

No release if any critical/high severity issue in the defined pilot threat model is open without formal acceptance, if required outbound access exists unexpectedly, if artifact provenance is missing, or if the test environment cannot reproduce the build.

## 12. Recommended first vertical slice

Build this path before multi-agent swarm complexity:

```text
Approved source repo + local docs
          ↓
Read-only repository map and retrieval
          ↓
Engineer asks one bounded maintenance question
          ↓
Local model proposes analysis with file/line evidence
          ↓
Deterministic tool gateway checks read permissions
          ↓
Agent proposes a test or patch in isolated worktree
          ↓
Disposable no-egress sandbox runs tests
          ↓
Evaluator reports pass/fail, limitations and provenance
          ↓
Human reviews and accepts/rejects
```

Do not connect the first version to a live OT control plane. Demonstrate reliable engineering assistance on a non-production repository first.

