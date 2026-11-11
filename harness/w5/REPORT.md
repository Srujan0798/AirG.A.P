# W5 — Customer Discovery Targeting Report

**Window:** W5 · **Task:** WAVE2-DISCOVERY · **Produced:** 2026-11-11 · **All sources accessed 2026-11-11**
**Schema:** `02_INDEPENDENT_RESEARCH_AGENT_PROTOCOLS.md` §6 · Grades: **A** official docs/spec · **B** independent evaluation · **C** vendor/institutional page · **D** inference
**Outputs:** [`TARGET_LIST.md`](./TARGET_LIST.md) (75 numbered rows ≈ 90 organisations; 25 evidence codes) · [`OUTREACH_KIT.md`](./OUTREACH_KIT.md) (guide + 3 messages + log template)

---

## 1. Verdict

**The list is built and interviewable, but the target list contains a finding that should worry the founder more than the list itself: the industrial/embedded segment — the one W2 re-scored *above* defence — is mostly not air-gapped.**

- **Hard isolation is real, regulated and provable** in exactly three places: **nuclear** (DAE: critical infrastructure *"isolated from Internet"*, *"restriction on removable media"* — E3, **A**), **power/OT** (CEA mandates *"physical isolation of critical OT system from Internet"* — E1, **A**), and **defence/space labs** (DRDO Trusted Desktop Platform + SAMEeKSha program-analysis backbone — E4, **A**).
- **Industrial/embedded R&D in India is connected.** Isolation there is *contract- and customer-driven on specific projects*, not site-wide. **Grade D** — no per-company isolation evidence exists in this pass.
- Therefore **W2's segment question is not settled by analysis, and cannot be.** It is settled by interview question C1 of `09` §1, and the list is built so that both segments are interviewed in parallel, as `09` §C2 instructs.

**Second finding that changes the pitch — and it is bad news.** While searching for targets, I found evidence that **the layer W1 identified as empty is less empty than W1 concluded**: Palantir's **Apollo** performs *"autonomous deployment"* across *"disconnected, air-gapped environments"* with IL6 compliance and Cross-Domain-Solution update paths; **Rubix** is hardened Kubernetes for the DoW; **PFCS Forward** (2026-02) extends IL5/IL6 authorisation; **AIP for Defense** runs *"on their network, from classified systems to devices on the tactical edge"* with *"a full audit trail"* (**E16, E17 — A/C**). **This is the closest thing yet to the "governance + lifecycle control plane" the founder planned to build, and it is already accredited, funded and deployed.** The wedge is now narrower: *not* offline deployment governance in general, but **governed offline engineering of customer software specifically**. That is a harder sell and a smaller market than W1's synthesis implied.

**Third finding, and the most useful thing in this deliverable:** **the founder's own campus is inside the national defence-innovation network.** iDEX runs 28 partner incubators including **IITG-TIC (IIT Gandhinagar Technology Innovation Council)** — E12, **A**. iDEX publishes **Procurement Contracts against the Indian Navy, IAF and Indian Army** (E13, **A**), funded ~300 startups with grants to ₹1.5 Cr and ADITI to ₹25 Cr, and **DIO was founded by HAL and BEL** (E12, **A**). That is a published, legitimate, low-approval route to ~300 defence startups and to HAL and BEL — and it costs one email.

---

## 2. Top 10 targets ranked by access × urgency

Score = (access 1–5) × (urgency 1–5). **Both are my judgements (Grade D) from published-channel availability and workflow pain — not from interviews.** They are a starting order, not a ranking of value.

| # | Target | Access | Urgency | Score | Why it's here | Warm path |
|---|---|---|---|---|---|---|
| 1 | **ISRO SAC, Ahmedabad** — Software QA / Software Development Division | 5 | 5 | **25** | Only target where isolation, a **formal SDLC standard (ISRO-SES-PD-100, IEEE 12207-based)** and a **Software Quality Assurance function** are all confirmed (E8, **A**) — and it is **40 km from the founder**. Requirements traceability and test evidence are native to their process | **Warm**: physical visit, Gujarat |
| 2 | **DRDO CAIR, Bengaluru** — Secure Software Development team | 4 | 5 | **20** | **The single most on-target org found.** Runs SAMEeKSha (centralised program analysis extended to developer desktops), a Trusted Desktop Platform, and a team doing CWE analysis in C/C++ and Java (E4, **A**). They are *already building* the governance layer — either as a customer, a partner, or the proof that the layer is occupied | **Warm**: IITGN faculty → CAIR students; DRDO YSL-AI directorate |
| 3 | **BEL Software SBU, Bengaluru** (+ SDC Visakhapatnam / Delhi / Indore) | 4 | 5 | **20** | CMMI L5, CERT-In empanelled, ISO 27001/20000-1/22301, 500+ engineers, mission software for the Armed Forces/DRDO/ADA/NSIL (E11, **C**). CMMI L5 orgs already measure QA — test-generation has a measurable metric | **Warm**: BEL co-founded DIO (E12) → iDEX ecosystem |
| 4 | **HAL** — Software / chief engineer | 4 | 5 | **20** | Co-founder of DIO (E12); iDEX procurement runs through HAL (E13); has an existing AI/ML procurement precedent | **Warm**: DIO/iDEX route |
| 5 | **Tata AutoComp TTC, Pune** — 400+ engineers across **Defence, Aero & Space, Industrial** (E23) | 4 | 4 | **16** | Highest-scoring *industrial* target. Doing defence/aerospace engineering means customer-mandated restriction on some projects — so it tests the W2 hypothesis directly while being reachable | **Warm**: Tata network; DSIR-recognised R&D unit (E18) |
| 6 | **GSAS Micro Systems, Bengaluru** — mission software, **DO-178C evidence** (E19) | 3 | 5 | **15** | DO-178C verification-evidence generation is expensive, measurable, boring and exactly the kind of thing a founder can demo on a non-production repo. Small company → fast access → good first *design partner* conversation | Cold, but small and reachable |
| 7 | **iDEX / DIO — as a channel, not a customer** | 5 | 4 | **20** | 28 partner incubators (**incl. IITG-TIC**), ~300 startups/MSMEs, published procurement contracts (E12, E13). One email reaches more defence engineers than 25 cold messages | **Warm**: IITG-TIC is on campus |
| 8 | **Manastu Space, Ahmedabad** (+ PRL Ahmedabad row 28) | 4 | 4 | **16** | Only defence-aerospace startup in the Gujarat column — combines geographic access with defence-grade software constraints | **Warm**: Gujarat + iDEX |
| 9 | **ARAI, Pune** — Digital Twin Centre + ~100-company governing council (E22, **A**) | 4 | 3 | **12** | Not a customer — a **multiplexer**. One introduction reaches ~100 industrial engineering leaders across automotive, defence, aerospace, telecom and railways. Also a natural partner/influencer | **Warm**: council membership |
| 10 | **Tata Motors Sanand, Gujarat / Cummins Ahmedabad / Adani–Torrent Ahmedabad** (rows 53, 51, 46) | 4 | 3 | **12** | The three Gujarat industrial/critical-infrastructure rows — physically reachable, and they carry the **highest-value isolation evidence outside defence** (E1, E2 for power; E18 for DSIR-recognised R&D) | **Warm**: Gujarat geography |

**Deliberately deprioritised:** DRDO labs other than CAIR (rows 3–12), ISRO centres other than SAC (22–27), BDL/MDL/GRSE/CSL (15–18), and all 11 critical-infrastructure rows (39–49) except via an institutional channel. Clearance and procurement make these slow; they are worth a *second* wave once the industrial segment question is answered.

---

## 3. The three warmest paths

**Path 1 — IITG-TIC inside the iDEX network (strongest).**
iDEX runs **28 partner incubators** and the published list includes **IITG-TIC (IIT Gandhinagar Technology Innovation Council)**, plus Maker Village (Kochi), T-Hub (Hyderabad), FORGE and PIEDS (E12, **A**). iDEX funds ~300 startups/MSMEs, publishes **Procurement Contracts** against the Indian Navy/IAF/Army (E13, **A**), and **DIO was founded by HAL and BEL** (E12, **A**). *Action this week:* one email to IITG-TIC asking for (a) the list of incubated defence software teams and (b) an introduction to the iDEX programme team. This single request opens 300 startups, HAL and BEL, and every iDEX-supported software company in the list.

**Path 2 — The Gujarat defence-and-engineering geography (fastest and cheapest).**
**ISRO SAC** (row 21) and **PRL** (row 28) are in Ahmedabad — the same city as **Manastu Space** (row 34), **Tata Elxsi**, **Tata Motors Sanand** (row 53), **Cummins Ahmedabad** (row 51), **Adani/Torrent/Gujarat utilities** (row 46), **Zydus** and **GE Healthcare**. ISRO's own sites list **"Industry Collaboration"** and **"E-Procurement"** for SAC (E8, **A**), so there is a formal route, not just a visit. *Action this week:* one Ahmedabad trip covering 4–6 conversations; use the SAC visit to ask directly for the industry-collab contact who handles software vendors.

**Path 3 — IITGN faculty → DRDO/ISRO placement (highest-value, slower).**
DRDO's own SPOC directory (**E5, A**) and CAIR's SAMEeKSha facility (**E4, A**) are the two most relevant institutions found. IIT Gandhinagar faculty supervise DRDO/ISRO students and consult for these labs. *Action this week:* ask **2 faculty members** — one from a computer-science/embedded group, one from systems — for a 20-minute briefing on the lab's software-quality process, and for a list of students currently placed there. That list is a warm path to ~10 engineers per placement year and is **not** discoverable any other way.

**Fallback if all three stall:** the industrial/embedded block (rows 50–60) and ARAI (row 56). Lower clearance, faster reply, and a direct test of the W2 segment question.

---

## 4. Evidence log

| Claim | Grade | Sources (all accessed 2026-11-11) |
|---|---|---|
| CEA mandates physical isolation of critical OT from the internet, and physical separation of critical OT from enterprise IT | **A** | "CEA (Cyber Security in Power Sector) Guidelines, 2021", https://cea.nic.in/whats-new/file?mode=view&path=%2Fhome%2Fcea_website%2Freports%2Fgeneral%2Fen%2FGuidelines_on_Cyber_Security_in_Power_Sector_2021-1.pdf · "Draft CEA (Cyber Security in Power Sector) Regulations, 2024", https://cea.nic.in/wp-content/uploads/regulations_cpt/2024/08/Draft_CEA_Cyber_Security_in_Power_Sector_Regulations_2024.pdf |
| Nuclear critical infrastructure is isolated from the internet, with removable media restricted | **A** | "Cyber Security Breach In Nuclear Plants" (PIB, DAE, 2022-03-23), https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1808677 |
| DRDO CAIR operates a Trusted Desktop Platform and SAMEeKSha centralised program analysis over the CAIR backbone, with a dedicated secure-software-development team | **A** | "Infrastructure Facilities — DRDO CAIR", https://www.drdo.gov.in/drdo/labs-establishment/infrastructure-facilities/centre-artificial-intelligence-robotics-cair |
| DRDO publishes a SPOC directory for every establishment via Industry Interaction Groups | **A** | "DRDO Industry Interaction Groups" (2026-01-09), https://drdo.gov.in/drdo/sites/default/files/schemes_services/POC_IIG09Jan2026.pdf |
| DRDO operates ~41 labs and 5 DYSLs; official lab inventory with locations | **A** | "About DRDO", https://www.drdo.gov.in/drdo/en/organisation/about-drdo · PIB lab lists, https://www.pib.gov.in/newsite/PrintRelease.aspx?relid=160059 and /relid=113748 |
| ISRO runs a Software Quality Assurance function and the IEEE-12207-based ISRO-SES-PD-100 software process document for all ISRO software | **A** | "Software Quality Assurance — SAC Industry Portal", https://www.sac.gov.in/SAC_Industry_Portal/rnqa_software.html |
| ISRO's 2025 research catalogue names VSSC's Model-based Software Development Framework and a "Cyber Services & Information Technology" sub-area | **A** | "Research Areas in Space" (DoS, 2025-05-16), https://www.isro.gov.in/media_isro/pdf/programme/Research_Areas_Space_Doc2025.pdf |
| Official ISRO centre/units roster (19 units incl. SAC, VSSC, PRL, IIRS) | **A** | https://www.isro.gov.in/isro_centre.html · https://www.vssc.gov.in/VSSC/ISRO_Centres.html |
| BEL Software SBU is CMMI L5 + CERT-In empanelled + ISO 27001/20000-1/22301, 500+ engineers, SDCs in Bengaluru/Visakhapatnam/Delhi/Indore; customers include DRDO, ADA, MDL, NSIL | **C** | "BEL Software SBU Centre", https://bel-india.in/bel-software-sbu-centre/ |
| iDEX: ₹498.78 Cr, ~300 startups/MSMEs, 28 partner incubators incl. **IITG-TIC**, DIO founded by HAL & BEL; grants up to ₹1.5 Cr, ADITI up to ₹25 Cr | **A** | "iDEX Details \| DDPMoD", https://www.ddpmod.gov.in/en/offerings/schemes-and-services/idex · "iDEX Partners", https://idex.gov.in/partners · "iDEX \| ISTI Portal", https://www.indiascienceandtechnology.gov.in/funding-opportunities/startups/idex-innovations-defence-excellence |
| iDEX publishes Procurement Contracts against Indian Navy / IAF / Indian Army | **A** | "Procurement Contract", https://idex.gov.in/uploads/page/Procurement%20Contract.pdf |
| Government of India Directory of Recognised In-house R&D Units (DSIR) — authoritative census incl. Tata AutoComp, Tata Motors, Cummins, Kirloskar, Kalyani, Kinetic, Vanaz, TTK | **A** | "Directory of Recognised In-house R&D Units" (IGSTC), https://www.igstc.org/html/pdfs/DSIR-recognised-Indian-industries.pdf |
| ARAI runs a Digital Twin Centre (hub Pune, spokes Bengaluru/Guwahati) and convenes a governing council of ~100 companies across automotive, defence, aerospace, telecom, railways | **A** | "ARAI Annual Report 2024-25", https://www.araiindia.com/MediaFiles/AR_English_2024_25_150925_12335.pdf |
| Power sector has named external auditors (CERT-In empanelled, periodic) and CSIRT-Power + six sectoral CERTs — a role the founder must not confuse with an internal approver | **A** | "Strengthening Cybersecurity in Power Sector" (PIB, 2025-12-11), https://www.pib.gov.in/PressReleasePage.aspx?PRID=2202421 · MoP Lok Sabha USQ 1916, https://sansad.in/getFile/loksabhaquestions/annex/179/AU1916.pdf |
| US nuclear: 10 CFR 73.54 requires safety/security systems isolated from external communications incl. internet | **A** | "Cybersecurity — NRC", https://www.nrc.gov/facilities-safety/cybersecurity |
| **Offline software-delivery governance is already productised**: Palantir Apollo does IL6-compliant autonomous deployment across disconnected/air-gapped environments; Rubix is hardened DoW Kubernetes; PFCS Forward (2026-02) extends IL5/IL6 authorisation; air-gapped updates use Cross Domain Solutions | **A** | "How Palantir Meets IL6 Security Requirements with Apollo", https://blog.palantir.com/how-palantir-meets-il6-security-requirements-with-apollo-f6c3f0c51fe · "Introducing PFCS Forward", https://blog.palantir.com/introducing-pfcs-forward-d8755d34c429 · "Apollo Introduction", https://www.palantir.com/docs/apollo/core/introduction |
| Air-gapped AI at classification scale is productised: AIP for Defense runs on classified networks with a full audit trail; Anduril Lattice deploys on Oracle air-gapped Isolated Regions; GDC air-gapped meets IL6/Top Secret, ISO 27001, NIST 800-53, NATO D48 | **C** (vendor) | "AIP for Defense", https://www.palantir.com/platforms/aip/defense · "Anduril & Oracle Partner…", https://www.anduril.com/news/anduril-and-oracle-partner-to-deliver-ai-powered-defense-solutions-from-the-datacenter-to-the · "GDC air-gapped supportable standards", https://services.google.com/fh/files/misc/gdc_air-gapped_supportable_standards.pdf |
| Defence supply-chain/offline substitutes already exist and compete with the lifecycle layer: Anchore (on-prem Feed Service, DoD IL-6 air-gap), Sonatype SAGE (offline SBOM), GitLab Self-Managed (offline SAST/container/secret scanning), NVIDIA NIM (documented air-gap runbook) | **A/C** | https://anchore.com/enterprise · https://anchore.com/blog/introducing-anchore-enterprise-1-1 · https://www.sonatype.com/blog/mastering-software-governance-in-air-gapped-critical-mission-environments · https://docs.gitlab.com/user/application_security/offline_deployments/ · https://docs.nvidia.com/nim/large-language-models/latest/deploy-air-gap.html |
| Tata AutoComp TTC: 400+ engineers, product engineering across Automotive, Defence, Aero & Space, Industrial | **C** | "Tata AutoComp Systems Technical Centre", https://www.tataautocomp.com/ttc |
| GSAS: mission software, DO-178C evidence, edge-AI payloads | **C** | "GSAS — Aerospace & Defence Engineering", https://gsasindia.com/solutions/aerospace-defense |
| INDSRO: consortium of 7 defence firms, Pune hub, AS9100D | **C** | "INDSRO", https://www.indsro.com/index |
| ITAR/EAR primary text — **not fetched**; the specific obligation wording on isolation is therefore unverified | **D** | (pending) |

---

## 5. Open questions

1. **Is the industrial/embedded segment actually air-gapped?** The single most decision-relevant question. If C1 comes back "only source control" for industrial rows, **the "air-gapped" positioning is wrong for that segment** and the founder should pivot the wedge to "isolated/restricted engineering environments" rather than "air-gapped". *Resolve:* ≥3 industrial interviews (rows 50–60) + ≥3 defence interviews.
2. **Does Palantir Apollo/Rubix close the gap W1 identified?** Evidence says it substantially does, at the deployment-governance layer, for defence buyers. If so, the wedge must be narrowed to *engineering-workflow* governance (code comprehension, test generation, traceability) rather than general offline software delivery. *Resolve:* read Apollo's IL6 documentation and PFCS Forward in detail; ask two defence interviewees what they use today.
3. **Who is the buyer at DRDO CAIR — and are they a customer, a partner, or proof the layer is occupied?** SAMEeKSha suggests they have already built in-house. *Resolve:* the row-1 interview itself; the answer may redirect the product entirely.
4. **What does an accredited defence software buyer actually pay for — software, deployment, support, or an appliance?** No pricing evidence exists for this buyer class in any pass. *Resolve:* B2/B3 questions in 2–3 interviews.
5. **Is the iDEX route exploitable within 2 weeks, and does it reach engineers or only founders?** iDEX's network is procurement-and-grant shaped; engineers inside those startups may not be the same population the founder needs. *Resolve:* the IITG-TIC email + one iDEX intro.
6. **Are the ISRO and DRDO institutional channels (SAC "Industry Collaboration", DRDO IIG SPOC directory) open to a single student with no company?** Not verified — this determines whether rows 1–12 and 21–28 are reachable this month. *Resolve:* two emails this week; the answer changes the whole schedule.
7. **Which specific iDEX startups actually do *software* engineering (rather than hardware)?** iDEX's published portfolio skews hardware; the software subset is not enumerated. *Resolve:* read the published Procurement Contract list (E13) for AI/ML/software items.
8. **What is the minimum pilot that satisfies a defence security approver?** `01` §5 and `09` §C3 warn this could blow up the MVP. *Resolve:* C5 question in the first two security-approver interviews, before writing any code.
9. **Is there an alternative to the defence segment with the same isolation evidence but better access — e.g. nuclear?** Nuclear has the strongest isolation evidence (E3, **A**) and the worst access. *Resolve:* one institutional enquiry only; do not invest more until access is proven.
10. **Does the founder's own inbound tooling (local coding agents, offline inference) already satisfy a niche of this need — i.e. is the interview revealing "we already have something"?** A6/D1 questions exist for this. Any such reply is a signal to narrow, not to widen.
