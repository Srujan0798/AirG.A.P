# W8 — ECONOMICS.md : Cost & break-even for one offline air-gapped deployment (India)

**Task-ID:** WAVE2-GTM  
**Sources accessed:** 2026-11-11. Evidence grades: C = vendor/retailer page · D = own inference/assumption (not sourced — treat as planning figures, not facts).  
**Subject:** Single-site offline deployment of the wedge (read-only codebase understanding / change-impact, llama.cpp/vLLM on customer hardware).

---

## Hardware cost per deployment (on-prem, air-gapped — cloud rental ruled out; needs no egress)

| Component | Indicative price (INR) | Source | Grade |
|-----------|------------------------|--------|-------|
| RTX 4090 24GB GPU workstation (single-GPU build) | ₹2,50,000 – ₹5,00,000 | serverwale.com/gpu-servers-india; serverwale.com/blog/gpu-server-price-india-2026 (2026-06-27) | C |
| RTX 4090 24GB retail card (lowest India price, Nov 8 2026; noted as +254% vs typical median — inflated anomaly) | ₹5,26,999 | gpuprix.com/india/gpus/geforce-rtx-4090 | C |
| Refurbished NVIDIA V100 32GB server | ₹4,50,000 | serverwale.com/gpu-servers-india | C |
| NVIDIA A100 80GB server | ₹18,00,000 | serverwale.com/gpu-servers-india | C |
| NVIDIA RTX A6000 48GB system | ₹4,80,000 | serverwale.com/gpu-servers-india | C |

**Hardware assumption (D):** Budget **₹5,00,000** per site for a single-GPU RTX 4090 workstation-class air-gapped box (mid of indicated range, excludes GST/shipping). Exact quote required — vendor pages are indicative and prices are volatile (RTX 4090 retail observed far above median).

## Install & support effort per deployment (assumptions, D)

Air-gapped means no remote telemetry, no remote patching, physical-media/diode transfer, on-site install, per-site hardware matrix, SBOM/provenance/audit-evidence pack, human-approval workflow setup, and on-site support visits.

| Item | Person-days | Rate assumption (INR/day) | Cost (INR) | Grade |
|------|-------------|---------------------------|------------|-------|
| Staging, provenance/SBOM/signing, air-gapped bundle build | 5 | 10,000 | 50,000 | D |
| On-site install, offline config, model/runtime load | 5 | 10,000 | 50,000 | D |
| Customer baseline task suite + eval on customer code | 5 | 10,000 | 50,000 | D |
| Year-1 support (on-site visits, updates via permitted media) | 10 | 10,000 | 1,00,000 | D |
| **Subtotal install+support yr 1** | | | **2,50,000** | D |

**Fully loaded cost to serve one site, year 1 (D):** hardware ₹5,00,000 + install/support ₹2,50,000 = **₹7,50,000**.  
Year-2+ support only: **₹1,00,000/yr** (D).

## Startup fixed cost (assumptions, D)

| Item | Cost (INR/yr) | Grade |
|------|---------------|-------|
| 2 founders (₹10,00,000 each/yr) | 20,00,000 | D |
| Overhead (office, legal, compliance, travel) | 4,00,000 | D |
| **Fixed cost / yr** | **24,00,000** | D |

## Pricing models (assumptions, D — willingness-to-pay not validated; see `01` §8 / Gate A)

| Model | Price | Basis |
|-------|-------|-------|
| Paid pilot (one-time, 4–6 wk, non-production repo) | ₹2,00,000 | Covers install + eval; credited against first licence |
| Per-site annual licence | ₹4,00,000/yr | Software + updates via permitted media + support |
| Appliance bundle (one-time) | ₹12,00,000 | Hardware (₹5L) + software licence yr1 + support |

## Break-even analysis (cumulative revenue vs cumulative cost; all D assumptions)

Cumulative cost = fixed cost (24L/yr) + N × per-site variable cost (7.5L yr1, then 1L/yr support). Cumulative revenue = N × model price.

| Customers | Paid pilot ₹2L each | Per-site licence ₹4L/yr | Appliance bundle ₹12L each |
|-----------|---------------------|-------------------------|----------------------------|
| Break-even N (approx) | ~12 customers | ~6 customers | ~2 customers |
| Revenue at 20 customers | ₹40,00,000 | ₹80,00,000 | ₹2,40,00,000 |
| Cost at 20 customers (yr1) | ~₹1,74,00,000 | ~₹1,74,00,000 | ~₹1,74,00,000 |

**Read:** At pilot pricing, 20 customers (₹40L) does **not** cover year-1 cost (~₹1.74Cr) — unit economics fail at small N. At appliance-bundle pricing, 2 customers (₹24L) approaches one deployment's fully-loaded cost but still below fixed+variable at scale; per-site licence needs ~6 customers to begin covering fixed cost in year 1.

**Conclusion:** None of the three models breaks even at 1 customer. Unit economics only work if (a) hardware cost is borne by the customer (appliance model shifts capex to buyer), or (b) licence/appliance prices rise substantially above assumptions, or (c) fixed cost falls (single founder, no salary). With customer-paid hardware, per-site variable cost drops to ~₹2.5L (install+support only), making per-site licence ₹4L/yr break-even at roughly **1 customer** vs variable cost but still not vs fixed cost.

**Key open question:** actual willingness-to-pay and who pays hardware — not found; must be tested at Gate A (design-partner LOI).
