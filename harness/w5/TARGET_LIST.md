# W5 — Target Organisation List for Customer Discovery

**Window:** W5 · **Task:** WAVE2-DISCOVERY · **Produced:** 2026-11-11 · **All sources accessed 2026-11-11**
**Schema:** `02_INDEPENDENT_RESEARCH_AGENT_PROTOCOLS.md` §6 · Grades: **A** official docs/spec · **B** independent evaluation · **C** vendor/institutional page · **D** inference
**Purpose:** give the founder a concrete, source-grounded list of organisations whose engineering plausibly runs on isolated/restricted networks, to start 15–25 interviews this week.
**Scope rule:** organisations and roles only. No personal contact details of private individuals. Government SPOC directories are cited by URL and role, not reproduced.

---

## 0. Read this before using the list

### 0.1 The single most important caveat

**Most industrial/embedded R&D in India is *restricted*, not *air-gapped*.** The founder's product hypothesis rests on "no internet" (01 §3). But:

- **Power/OT** in India is *mandated* to be physically isolated from the internet (E1, E2 — Grade A). Real air gaps, created by regulation.
- **Nuclear** critical infrastructure is *"isolated from Internet"*, with *"restriction on removable media"* (E3 — Grade A). Real air gaps, created by regulation.
- **Defence and space** labs run on classified/restricted networks with trusted-desktop and secure-software-development platforms (E4, E5 — Grade A). Real air gaps, created by classification.
- **Automotive/industrial tier-1 R&D (Tata AutoComp, Cummins, Kirloskar, Tata Motors, M&M, Bajaj, TVS, ARAI, Bosch, Continental, ZF, Harman, Mercedes-Benz R&D)** is **mostly connected**, with isolation enforced by *customer* contract and OEM information-security rules (ISO 21434, IEC 62443, TISAX-like demands) on *specific projects*, not on the whole site. **This is a Grade D inference** — no per-company isolation evidence was found in this pass.

**Consequence (this is the answer to W2's open segment question).** Defence/space have *hard* isolation but *hard* access. Industrial/embedded have *soft* isolation but *soft* access. The interview must therefore ask **question C1 of `09` §1 verbatim** — *"Exactly what is isolated: the whole lab, only source control, build networks, runtime networks, or classified/sensitive data?"* — because **if the answer is "only source control", the offline-governance product is a much weaker fit than the founder assumes.** Interview distribution below is deliberately weighted to disambiguate this: 22 defence/space, 15 industrial/embedded, 11 critical-infrastructure, 10 startup/MSME.

### 0.2 Workflow assignment rule

`09` §1 lists six workflows. W3 (Wave 1) recommended **Test Generation** as the strongest MVP workflow; W4 recommended a narrower read-only **codebase-understanding / change-impact** tool. The "Likely first workflow" column below follows the **narrower W4/W3-safe reading** — i.e. the workflow to *discuss*, not to sell:

- **CG** = Codebase understanding / change-impact analysis (read-only) — default; W4's narrowest pivot
- **TG** = Test generation (proposed tests, sandboxed execution) — W3's recommendation; use where the org has measurable test-coverage debt and a safety case
- **RT** = Requirements traceability — use only where the org already maintains a requirements baseline (rare; ask, don't assume)
- **DI** = Defect investigation (logs + repo → root cause) — use where they run large log estates (power/OT, aero test rigs)
- **MO** = Legacy modernization — use only to test interest; `01` §5 and `09` §C5 make it an explicit non-goal

**Do not pitch.** Per `09` §1, the first ~20 minutes cover current process only. Product discussion starts after the interviewee describes the status quo.

### 0.3 Evidence codes (full citations at the end of this file)

| Code | Claim it supports | Source | Grade |
|---|---|---|---|
| **E1** | CEA mandates *"ensure physical isolation of critical OT system from Internet"* and *"physical separation between critical OT system and enterprise IT system"* | "CEA (Cyber Security in Power Sector) Guidelines, 2021", https://cea.nic.in/whats-new/file?mode=view&path=%2Fhome%2Fcea_website%2Freports%2Fgeneral%2Fen%2FGuidelines_on_Cyber_Security_in_Power_Sector_2021-1.pdf | **A** |
| **E2** | Same isolation duties carried into draft regulations | "Draft Central Electricity Authority (Cyber Security in Power Sector) Regulations, 2024", https://cea.nic.in/wp-content/uploads/regulations_cpt/2024/08/Draft_CEA_Cyber_Security_in_Power_Sector_Regulations_2024.pdf | **A** |
| **E3** | Nuclear: *"Critical infrastructure of nuclear power plant establishment is isolated from Internet"*, *"restriction on removable media, blocking of websites & IPs"* | "Cyber Security Breach In Nuclear Plants" (PIB, Dept of Atomic Energy, 2022-03-23), https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1808677 | **A** |
| **E4** | DRDO CAIR runs a **Trusted Desktop Platform**, and **SAMEeKSha** — *"a Centralized compute infrastructure comprising of Automated Program Analysis tools extended to scientists' development desktops over the CAIR backbone network"* — plus a **Secure Software Development team** (CWE identification in C/C++ and Java, secure coding and program-analysis facility, threat modelling) | "Infrastructure Facilities — DRDO CAIR", https://www.drdo.gov.in/drdo/labs-establishment/infrastructure-facilities/centre-artificial-intelligence-robotics-cair | **A** |
| **E5** | **DRDO publishes a Single Point of Contact (SPOC) per lab in its "Industry Interaction Groups" directory** — this is the formal, published industry-engagement channel for every DRDO establishment | "DRDO Industry Interaction Groups" (SPOC directory, 2026-01-09), https://drdo.gov.in/drdo/sites/default/files/schemes_services/POC_IIG09Jan2026.pdf | **A** |
| **E6** | DRDO is *"a network of around 41 laboratories and 05 DRDO Young Scientist Laboratories"* | "About DRDO", https://www.drdo.gov.in/drdo/en/organisation/about-drdo | **A** |
| **E7** | DRDO lab inventory with locations and research areas (official PIB list) | "DRDO Laboratories and their Research Activities" (PIB, 2017-03-28), https://www.pib.gov.in/newsite/PrintRelease.aspx?relid=160059 · "Laboratories of DRDO" (PIB), https://www.pib.gov.in/newsite/PrintRelease.aspx?relid=113748 | **A** |
| **E8** | ISRO maintains an explicit **Software Quality Assurance** function. SAC's page states, **verbatim**: *"For the software development life cycle, ISRO software projects use ISRO Software Process Document (ISRO-SES-PD-100, Issue-1, October 2006) which is based on IEEE 12207 family of standards that prescribe a set of processes and related plans, procedures, guidelines and templates taking into consideration existing software practices in the centres of ISRO/DOS. It is applicable to all software activities in ISRO."* **Caution:** the document ID appears **only inside this page's body text** — it is not a separately indexed document, so a standalone document search for "ISRO-SES-PD-100" returns nothing. The **statement** is primary (Grade A); the **contents of the standard itself were not located** (Grade D) | "Software Quality Assurance — SAC Industry Portal" (live fetch 2026-11-11), https://www.sac.gov.in/SAC_Industry_Portal/rnqa_software.html | **A** (statement) / **D** (document contents) |
| **E9** | ISRO's 2025 research-area catalogue includes VSSC's **"Model-based Software Development Framework"** (Low-Code/No-Code platform for flight software), a **"Cyber Services & Information Technology"** sub-area, and a **"Systems Reliability and Safety"** sub-area | "Research Areas in Space" (DoS, 2025-05-16), https://www.isro.gov.in/media_isro/pdf/programme/Research_Areas_Space_Doc2025.pdf | **A** |
| **E10** | Official ISRO centre/units roster (VSSC, SAC, URSC, NRSC, ISTRAC, MCf, IISU, LEOS, LPSC, IPRC, SDSC-SHAR, IIRS, PRL, NARL, IIST, NE-SAC, SCL, HSFC) | "ISRO Centres & Units", https://www.isro.gov.in/isro_centre.html · "ISRO Centres", https://www.vssc.gov.in/VSSC/ISRO_Centres.html | **A** |
| **E11** | BEL's Software SBU is **CMMI Level 5**, **CERT-In empanelled**, ISO 27001/9001/20000-1/22301; 500+ engineers; SDCs in Bengaluru, Visakhapatnam, Delhi, Indore; customers include DRDO, ADA, MDL, NSIL (ISRO), Election Commission | "BEL Software SBU Centre", https://bel-india.in/bel-software-sbu-centre/ | **C** |
| **E12** | iDEX/DIO: ₹498.78 crore scheme, support for ~300 startups/MSMEs, **28 partner incubators**, DIO founded by HAL & BEL; grants up to ₹1.5 Cr, ADITI up to ₹25 Cr. Published partner list includes T-Hub (Hyderabad), Maker Village (Kochi), SINE (IIT Mumbai), TIDES (IIT Roorkee), FITT IIT Delhi, IITMIC (IIT Madras), KIIT-TBI, **IITG-TIC (IIT *Guwahati*)**, PIEDS, PSG-STEP, Incubation Centre IIT Patna, FORGE — and in **Gujarat**: **CIIE at IIM Ahmedabad** and **SASTRA** (see E26) | "iDEX Details \| DDPMoD", https://www.ddpmod.gov.in/en/offerings/schemes-and-services/idex · "iDEX Partners" (live fetch 2026-11-11), https://idex.gov.in/partners · "iDEX \| ISTI Portal", https://www.indiascienceandtechnology.gov.in/funding-opportunities/startups/idex-innovations-defence-excellence | **A** |
| **E13** | iDEX publishes a **Procurement Contract** listing winners against named procurement agencies (Indian Navy / IAF / Indian Army) — a real route from prototype to contract | "Procurement Contract", https://idex.gov.in/uploads/page/Procurement%20Contract.pdf | **A** |
| **E14** | Government of India's official **Directory of Recognised In-house R&D Units** (DSIR) — an authoritative census of Indian firms with approved in-house R&D centres | "Directory of Recognised In-house R&D Units" (IGSTC), https://www.igstc.org/html/pdfs/DSIR-recognised-Indian-industries.pdf | **A** |
| **E15** | US nuclear: 10 CFR 73.54 requires safety/security systems to be *"isolated from external communications"*, including the internet | "Cybersecurity — NRC", https://www.nrc.gov/facilities-safety/cybersecurity | **A** |
| **E16** | Defence-grade offline software delivery is already productised: Palantir **Apollo** performs IL6-compliant *"autonomous deployment"* across *"disconnected, air-gapped environments"*; **Rubix** is hardened Kubernetes for DoW; **PFCS Forward** (2026-02) extends IL5/IL6 authorisation; air-gapped updates move via **Cross Domain Solutions** | "How Palantir Meets IL6 Security Requirements with Apollo", https://blog.palantir.com/how-palantir-meets-il6-security-requirements-with-apollo-f6c3f0c51fe · "Introducing PFCS Forward", https://blog.palantir.com/introducing-pfcs-forward-d8755d34c429 · "Apollo Introduction", https://www.palantir.com/docs/apollo/core/introduction | **A** |
| **E17** | Air-gapped AI at IL scale is already productised: Palantir AIP for Defense runs *"on their network, from classified systems to devices on the tactical edge"* with *"a full audit trail"*; Anduril **Lattice** deploys on Oracle's air-gapped Isolated/National Security Regions; GDC air-gapped meets IL6/Top Secret, ISO 27001, NIST 800-53, NATO D48 | "AIP for Defense", https://www.palantir.com/platforms/aip/defense · "Anduril & Oracle Partner…", https://www.anduril.com/news/anduril-and-oracle-partner-to-deliver-ai-powered-defense-solutions-from-the-datacenter-to-the · "GDC air-gapped supportable standards", https://services.google.com/fh/files/misc/gdc_air-gapped_supportable_standards.pdf | **C** (vendor) |
| **E18** | Indian automotive/industrial R&D centres recognised under DSIR, with named R&D sites | "Directory of Recognised In-house R&D Units" (IGSTC), https://www.igstc.org/html/pdfs/DSIR-recognised-Indian-industries.pdf | **A** |
| **E19** | Private defence mission-software firms exist with DO-178C evidence and edge-AI payload work in India | "GSAS — Aerospace & Defence Engineering", https://gsasindia.com/solutions/aerospace-defense | **C** |
| **E20** | ITAR/EAR and defence-customer information-security regimes require export-controlled technical data to be handled on isolated systems; ACE/ITAR is the governing US regime. **Note:** ITAR primary text was not fetched in this pass — treat the specific obligation wording as **D** pending fetch | (not fetched — pending) | **D** |
| **E21** | CEA/CERT-In mandate periodic third-party cyber audit of IT+OT by CERT-In empanelled auditors, and the existence of CSIRT-Power and six sectoral CERTs — i.e. a **named external-auditor role the founder must not confuse with an internal approver** | "Strengthening Cybersecurity in Power Sector" (PIB, 2025-12-11), https://www.pib.gov.in/PressReleasePage.aspx?PRID=2202421 · "Energy Supply Grid" (MoP, Lok Sabha USQ 1916, 2022-07-27), https://sansad.in/getFile/loksabhaquestions/annex/179/AU1916.pdf | **A** |
| **E22** | ARAI (Pune) runs a **Digital Twin Centre for Emerging Automotive Systems** (hub at ARAI Pune, spokes Bengaluru + Guwahati) and convenes a governing council of ~100 industrial companies across automotive, defence, aerospace, telecom and railways — a concentrated, reachable industrial engineering community | "ARAI Annual Report 2024-25", https://www.araiindia.com/MediaFiles/AR_English_2024_25_150925_12335.pdf | **A** |
| **E23** | Tata AutoComp's Technical Centre (Pune) is a 400+ engineer product-engineering division covering *Automotive, Truck & Off-Highway, Defence, Aero & Space, and Industrial* — i.e. a defence/aerospace-adjacent industrial R&D centre | "Tata AutoComp Systems Technical Centre", https://www.tataautocomp.com/ttc | **C** |
| **E24** | INDSRO is a consortium of seven defence equipment firms (Pune) building an India defence & aerospace manufacturing hub under AS9100D | "INDSRO", https://www.indsro.com/index | **C** |
| **E25** | Security-graded defence-software supply chain is a *market with named incumbents* — Anchore (on-prem Feed Service, DoD IL-6 air-gap), Sonatype SAGE (offline SBOM for classified programmes), GitLab Self-Managed (offline SAST/container/secret scanning), NVIDIA NIM (documented air-gap runbook). **These are substitutes for the wedge's lifecycle layer, not customers.** | "Software Supply Chain Management Platform | Anchore Enterprise", https://anchore.com/enterprise · "Introducing Anchore Enterprise 1.1", https://anchore.com/blog/introducing-anchore-enterprise-1-1 · "Mastering software governance in air-gapped, critical mission environments", https://www.sonatype.com/blog/mastering-software-governance-in-air-gapped-critical-mission-environments · "Offline environments — GitLab Docs", https://docs.gitlab.com/user/application_security/offline_deployments/ · "Air-Gap Deployment — NVIDIA NIM", https://docs.nvidia.com/nim/large-language-models/latest/deploy-air-gap.html | **A/C** |
| **E26** | **CORRECTION (2026-11-11) — replaces the earlier IITG-TIC claim.** "IITG-TIC" on the iDEX partners page is the **IIT Guwahati Technology Incubation Centre (Assam)** — *"IITG-TIC has a Seven-member Governing Body under the Chairmanship of the Director of IIT Guwahati"* — **not** IIT Gandhinagar. The **Gujarat** iDEX partner incubators are **CIIE at IIM Ahmedabad** (*"Centre for Innovation Incubation and Entrepreneurship (CIIE) at IIM Ahmedabad"*, Gujarat) and **SASTRA** (Security and Scientific Technical Research Association, Gujarat) — both confirmed on the iDEX partners page and on iDEX's state-wise partner-incubator listing (GUJARAT section lists ciie.co and SASTRA). IIT Gandhinagar's own incubator is **IIEC — IIT Gandhinagar Innovation and Entrepreneurship Center** (IIEC, IIT Gandhinagar, Palaj-382355, Gandhinagar; a **NIDHI-TBI**, sector-agnostic), which is **not** listed as an iDEX partner incubator. iDEX's Gujarat startup/MSME list on its homepage includes Optimized Electrotech, Swadesh Fire, Ancor Labs and Robosys Automation — the authoritative list to check before citing any named Gujarat startup as iDEX-backed | "iDEX Partners" (live fetch 2026-11-11), https://idex.gov.in/partners · "iDEX — Home (state-wise Partner Incubators / Startups-MSMEs; GUJARAT section)", https://idex.gov.in/ · "Technology Business Incubators (TBIs) \| ISTI Portal" (IIEC entry, NIDHI-TBI), https://www.indiascienceandtechnology.gov.in/listingpage/tbis · "DSIR-IITGN-CRTDH for Startups" (IITGN's own domain, naming IIEC as *"the IIT Gandhinagar Innovation and Entrepreneurship Centre (IIEC), a technology business incubator located within the campus"*), https://crtdh.iitgn.ac.in/wp/wp-content/uploads/2022/07/DSIR-IITGN-CRTDH-for-Startups.pdf · "Incubators — Startup Gujarat" (IIEC and IIMA Ventures registry entries; IIMA Ventures carries the CIIE contact address), https://startup.gujarat.gov.in/page/incubators/ic-incubators?page=3 and https://startup.gujarat.gov.in/page/incubators/ic-incubators?page=2 | **A** |

---

## 1. India — Defence R&D labs (DRDO & affiliates) — 12 targets

Access channel for all rows: **DRDO Industry Interaction Groups SPOC directory (E5)**. This is the *published formal channel for industry to engage a DRDO lab*. Contact the SPOC **by role** via the directory PDF; do not publish personal contacts.

| # | Organisation (location) | Why its engineering is isolated | Likely first workflow | Role to approach | Warm path |
|---|---|---|---|---|---|
| 1 | **DRDO Centre for AI & Robotics (CAIR), Bengaluru** | **E4 (A)** — operates a Trusted Desktop Platform and **SAMEeKSha**, a centralised program-analysis compute environment extended to scientists' development desktops over the CAIR backbone; has a dedicated **Secure Software Development team** (CWE analysis in C/C++ and Java, secure-coding facility, threat modelling) | **TG** (their own SD-quality mandate makes test/defect tooling the natural conversation) | Head, Secure Software Development team / Software Quality lead | **Warm**: CAIR is the single most relevant org found — approach via IITGN faculty who supervise DRDO/CAIR students, or via the DRDO Young Scientist Laboratory–AI directorate (E6, row 12). Confirm the SAMEeKSha scope in interview |
| 2 | **DRDO Young Scientist Laboratory – AI (DYSL-AI), Bengaluru** | **E6 (A)** — one of 5 DRDO YSLs, each under a director, on a dedicated AI mandate inside DRDO's classified network | **CG** | Lab Director / project lead | **Warm**: YSL directors are reachable through the DRDO IIG/SPOC route; ask the CAIR row-1 contact for a referral (row 1 → row 12 → you) |
| 3 | **DRDO Research & Development Establishment (Engrs), Pune** | **E7 (A)** — engineering systems and weapon platforms; DRDO labs operate on classified networks with trusted platforms (E4, E5) | **CG** / **MO** | Software team lead, ground & mission software | **Warm**: IITGN alumni in Pune; also via row 1 |
| 4 | **DRDO Aeronautical Development Establishment (ADE), Bengaluru** | **E7 (A)** — aeronautics (airframe/avionics qualification) | **RT** (avionics requirement-to-code-to-test chains exist) | Head of software / avionics QA | **Warm**: via E5 SPOC; IITGN alumni at ADE |
| 5 | **DRDO Centre for Air Borne Systems (CABS), Bengaluru** | **E7 (A)** — air-borne systems; mission software | **CG** / **TG** | Mission software lead | Cold → warm after row 1 |
| 6 | **DRDO Armaments R&D Establishment (ARDE), Pune** | **E7 (A)** — armaments | **CG** | Software lead | Cold → warm via row 3 |
| 7 | **DRDO Defence Research & Development Laboratory (DRDL), Hyderabad** | **E7 (A)** — missile & strategic systems | **CG** | Software lead | Cold |
| 8 | **DRDO Defence Electronics R&D Establishment (DLRL), Hyderabad** | **E7 (A)** — defence electronics | **TG** | Software QA lead | Cold |
| 9 | **DRDO Centre for Military Airworthiness & Certification (CEMILAC), Bengaluru** | **E7 (A)** — military airworthiness & certification | **RT** | Software certification lead | Cold — **high value**: certification is the closest thing to the wedge's "evidence pack" buyer |
| 10 | **DRDO Advanced Numerical Research & Analysis Group (ANURAG), Hyderabad** | **E7 (A)** — computational systems / modelling | **CG** (scientific-computing codebases are a distinct comprehension problem) | HPC / software lead | Cold |
| 11 | **DRDO Integrated Test Range (ITR), Balasore** | **E7 (A)** — integrated test range for missiles & strategic systems | **DI** (test/telemetry logs) | Test systems lead | Cold |
| 12 | **DRDO Research & Innovation Centre (RIC), Chennai** + **DYSL-QT (DIAT, Pune)** | **E6, E7 (A)** — RIC = sensors & MEMS; DYSL-QT = quantum technologies, one of the 5 YSLs | **CG** | Lab head | **Warm**: DYSL-QT sits on the DIAT Pune campus — a dense academic-industry node the founder can enter via a seminar |

---

## 2. India — Defence PSUs, shipyards & primes — 8 targets

| # | Organisation (location) | Why its engineering is isolated | Likely first workflow | Role to approach | Warm path |
|---|---|---|---|---|---|
| 13 | **Bharat Electronics Ltd (BEL) — Software SBU, Bengaluru** (+ SDCs Visakhapatnam, Delhi, Indore) | **E11 (C)** — CMMI L5, **CERT-In empanelled**, ISO 27001, ISO 20000-1, ISO 22301; *"mission-critical software"* for Armed Forces, DRDO, ADA, NSIL (ISRO), Election Commission. CERT-In empanellment implies a formal IT-security regime | **TG** (CMMI L5 orgs already measure QA; test generation is a defensible pitch) | Head of Engineering, Software SBU / Quality Assurance head | **Warm**: BEL and HAL are the two founder members of **DIO/iDEX** (E12) — so BEL is structurally connected to the iDEX/startup ecosystem, i.e. a warm route exists via iDEX programmes and events |
| 14 | **Hindustan Aeronautics Ltd (HAL)** — HAL Software, Bengaluru; Helicopter division; Aerospace divisions | **E11, E12 (A/C)** — DIO/iDEX founder member (E12); defence OEM; software quality regime implied by airworthiness | **CG** / **TG** | Head of Software / Chief Engineer (software) | **Warm**: co-founder of DIO (E12); iDEX procurement routes run through HAL (E13) |
| 15 | **Bharat Dynamics Ltd (BDL), Hyderabad** | Defence PSU, missile systems; supplier-quality and security regimes flow down | **CG** | Software lead / Quality manager | Cold |
| 16 | **Mazagon Dock Shipbuilders (MDL), Mumbai** | Defence PSU, shipbuilding; BEL software is a supplier to MDL (E11) | **CG** | Software/IT lead | Warm-ish: via BEL (row 13) and E5 |
| 17 | **Garden Reach Shipbuilders (GRSE), Kolkata** | Defence PSU | **CG** | Software lead | Cold |
| 18 | **Cochin Shipyard Ltd (CSL), Kochi** | Defence PSU | **CG** | Software lead | Cold |
| 19 | **Larsen & Toubro — L&T Defence IC, Mumbai (Powai campus)** + **L&T Technology Services** | **E18 (A)** — L&T Defence IC has a DSIR-recognised Product & Technology Development Centre (Powai campus) and other recognised R&D units | **CG** / **MO** | Head, software/technology, Defence IC | **Warm**: L&T is a large IITGN recruiter; also on E5/IIG style industry channels |
| 20 | **Tata Advanced Systems Ltd (TAS)** + **Tata Advanced Defence Systems (TADS)**, incl. **Sanand, Gujarat** | Defence/aerospace systems integrator; customer (Indian defence services, global OEMs) mandates IT-security and export-control compliance on engineering data | **CG** | Engineering head / TADS software lead | **Warm (Gujarat)**: Tata ecosystem is dense in Gujarat (TAS Sanand, Tata Motors Sanand, Tata Elxsi Ahmedabad, GE Healthcare Ahmedabad) — a founder in Ahmedabad can reach several Tata entities through one introduction |

---

## 3. India — Space (DoS/ISRO) — 8 targets

| # | Organisation (location) | Why its engineering is isolated | Likely first workflow | Role to approach | Warm path |
|---|---|---|---|---|---|
| 21 | **ISRO Space Applications Centre (SAC), Ahmedabad** | **E8 (A/D)** — SAC runs a formal **Software Quality Assurance** function; SAC's own page states ISRO software projects use an **IEEE 12207-based** software process document *"applicable to all software activities in ISRO"* (the document ID **ISRO-SES-PD-100, Issue-1, Oct 2006** appears only inside that page's body text and the standard itself was **not located** — see E8). Develops signal/image-processing and GIS software | **RT** (SAC works to formal process + QA → requirements traceability is native) then **TG** | Software QA Manager (QASM) / Software Development Division head | **Warm (Gujarat, ~40 km)**: SAC is in Ahmedabad; the founder can visit in person. This is the highest-value non-DRDO target in India |
| 22 | **ISRO Vikram Sarabhai Space Centre (VSSC), Thiruvananthapuram** | **E9 (A)** — VSSC's **Model-based Software Development Framework** (Low-Code/No-Code platform for NGC flight software) is an explicit, named software-engineering programme; ISRO's "Cyber Services & Information Technology" research sub-area (E9) | **CG** / **TG** | Head, Software Development Division / Model-based SW framework lead | Cold → warm via ISRO row 21 (E10: SAC and VSSC both under DoS) |
| 23 | **ISRO U R Rao Satellite Centre (URSC), Bengaluru** | **E9, E10 (A)** — lead centre for satellite design/realisation; flight and ground software | **CG** | Software lead | Cold |
| 24 | **ISRO National Remote Sensing Centre (NRSC), Hyderabad** | **E10 (A)** — ground systems, data processing; ISRO process standard applies | **CG** | Software lead | Cold |
| 25 | **ISRO Telemetry Tracking and Command Network (ISTRAC), Bengaluru** | **E10 (A)** — mission control network | **DI** | Network/ops systems lead | Cold |
| 26 | **ISRO Master Control Facility (MCf), Hassan & Bhopal** | **E10 (A)** — mission control; real-time ops software | **DI** / **CG** | Software lead | Cold |
| 27 | **ISRO Liquid Propulsion Systems Centre (LPSC), Thiruvananthapuram & Bengaluru** | **E10 (A)** — propulsion systems | **CG** | Software lead | Cold |
| 28 | **Physical Research Laboratory (PRL), Ahmedabad** + **NARL, Gadanki** | **E10 (A)** — PRL is a DoS autonomous body in Ahmedabad with instrument/payload software | **CG** | Software/compute lead | **Warm (Gujarat)**: same Ahmedabad geography as SAC (row 21) — combine on one trip |

---

## 4. India — Private defence & aerospace, iDEX-backed startups & MSME — 10 targets

| # | Organisation (location) | Why its engineering is isolated | Likely first workflow | Role to approach | Warm path |
|---|---|---|---|---|---|
| 29 | **iDEX / Defence Innovation Organisation (DIO)** — **not a customer; a route** | **E12 (A)** — DIO runs iDEX with ₹498.78 Cr, ~300 startups/MSMEs, 28 partner incubators; **E13 (A)** — iDEX publishes Procurement Contracts against Indian Navy/IAF/Army; **E26 (A)** — the **Gujarat** partner incubators are **CIIE at IIM Ahmedabad** and **SASTRA** | n/a — this is the **channel**, not a target | iDEX programme team; and the Gujarat partner incubators **CIIE at IIM Ahmedabad** and **SASTRA** (E26) | **Warm (corrected 2026-11-11)**: **CIIE at IIM Ahmedabad** is a published iDEX partner incubator in Gujarat (E26, **A**) — one email there reaches the Gujarat defence-startup set and the iDEX programme team. **Correction:** IITG-TIC is **IIT Guwahati** (Assam), *not* IIT Gandhinagar. IIT Gandhinagar's own incubator is **IIEC** (a NIDHI-TBI, E26) — a genuine on-campus route for general startup access, but **not** an iDEX partner incubator |
| 30 | **GSAS Micro Systems Pvt Ltd, Bengaluru** | **E19 (C)** — mission software, **DO-178C evidence**, FPGA/board design, edge-AI payloads for aerospace/defence/space | **TG** (DO-178C verification evidence generation is the exact pain) | Founder / Head of Engineering | Cold, but **high-value**: DO-178C evidence generation is a measurable, expensive, boring workflow |
| 31 | **INDSRO (consortium of 7 defence firms), Pune** | **E24 (C)** — AS9100D aerospace QMS; Pune defence manufacturing hub | **CG** / **RT** | Consortium Director / member firms' engineering heads | **Warm**: consortium is a single door to 7 firms; also on iDEX/DRDO channels (E12, E26) |
| 32 | **Ideaforge Aerospace, Bengaluru** | iDEX-supported deep-tech drone maker; defence customer contracts impose security/export regimes on design data | **CG** / **TG** | Head of Software / Autonomy lead | **Warm**: iDEX network (E12) — Gujarat entry point **CIIE at IIM Ahmedabad** (E26) |
| 33 | **Asterion Aerospace, Bengaluru** | iDEX-supported UAV/launch systems; defence customer regimes | **CG** | Software lead | **Warm**: iDEX network (E12) — Gujarat entry point **CIIE at IIM Ahmedabad** (E26) |
| 34 | **Manastu Space, Ahmedabad** | iDEX-supported launch-vehicle maker; Ahmedabad — defence/aerospace engineering in Gujarat | **CG** | Head of Engineering | **Warm (Gujarat) + iDEX** — the only defence-aerospace startup row in the Gujarat column; Gujarat entry point **CIIE at IIM Ahmedabad** (E26). This company's own iDEX status not individually verified (D) |
| 35 | **Pixxel Space, Bengaluru** | iDEX-supported satellite imaging; space customer security regimes | **CG** | Head of Software | **Warm**: iDEX network (E12) — Gujarat entry point **CIIE at IIM Ahmedabad** (E26) |
| 36 | **Dhruva Space, Bengaluru** | iDEX-supported launch systems | **CG** | Software lead | **Warm**: iDEX network (E12) — Gujarat entry point **CIIE at IIM Ahmedabad** (E26) |
| 37 | **Paras Defence / Dynamatic Systems / Alpha Tocol** (Mumbai / Pune / Pune) | Defence component makers; customer IT-security and export-control flow-down | **CG** | Technical director | Warm-ish: via iDEX (Gujarat entry point CIIE at IIM Ahmedabad, E26) and the DRDO IIG directory (E5) |
| 38 | **Garuda Aerospace, Chennai** | iDEX-supported UAV | **CG** | Engineering head | **Warm**: iDEX network (E12) — Gujarat entry point **CIIE at IIM Ahmedabad** (E26) |

---

## 5. India — Critical infrastructure (nuclear, power, transport) — 11 targets

These have the **hardest isolation evidence** (E1, E2, E3, E15) and the **worst access**. Use them to test whether the "regulated isolation" hypothesis survives contact with a security officer, not to build a pipeline.

| # | Organisation (location) | Why its engineering is isolated | Likely first workflow | Role to approach | Warm path |
|---|---|---|---|---|---|
| 39 | **NPCIL — Nuclear Power Corporation of India Ltd**, Mumbai + all plants (Rajasthan, Gujarat **Kakrapara/Kudankulam**, Tamil Nadu, Andhra) | **E3 (A)** — DAE states nuclear critical infrastructure is *"isolated from Internet"*, with *"hardening of internet and administrative intranet connectivity, restriction on removable media, blocking of websites & IPs"* | **DI** / **CG** (plant software, analyser/instrumentation code) | Head of Computer/IT division (CISAG/TAFICS interface) | **Warm-ish (Gujarat)**: **Kudankulam & Kakrapara are in Gujarat**; DAE's own specialist groups (CISAG, TAFICS) are the named internal security owners (E3) — ask the security group, not the plant |
| 40 | **Bhabha Atomic Research Centre (BARC), Mumbai** | **E3 (A)** — DAE unit; *"safety and security critical systems are designed and developed in-house using custom built hardware and software which are subjected to regulatory verification and validation"* | **CG** / **TG** | Computer Division / Software Technology Division head | Cold |
| 41 | **Indira Gandhi Centre for Atomic Research (IGCAR), Kalpakkam** | **E3 (A)** | **CG** | Software lead | Cold |
| 42 | **Nuclear Fuel Complex (NFC), Hyderabad** + **Uranium Corporation of India (UCIL), Jaduguda** | **E3 (A)** — DAE-regulated; classified material handling | **CG** | IT/software lead | Cold |
| 43 | **POWERGRID Corp of India Ltd**, Gurugram + CTUs | **E1, E2 (A)** — CEA mandates physical isolation of critical OT from the internet and physical separation of critical OT from enterprise IT | **CG** | Head of IT / Grid Management systems | Cold |
| 44 | **NTPC Ltd**, New Delhi + plants | **E1, E2 (A)** — CEA Responsible Entity; mandated audits by CERT-In empanelled auditors (E21) | **CG** | Head of IT / Engineering | Cold |
| 45 | **Indian Oil Corp / GAIL / Petronet** (pipeline/aviation-fuel OT) | **E1, E2 (A)** — CEA-recognised critical infrastructure | **CG** | IT/Ot engineering | Cold |
| 46 | **Tata Power / Torrent Power / Gujarat State Electricity Corp / Adani (Ahmedabad)** | **E1, E2 (A)**; Gujarat utilities are CEA Responsible Entities | **CG** | Head of IT/OT | **Warm (Gujarat)** — Torrent & Adani Ahmedabad; Gujarat utility procurement offices are physically reachable |
| 47 | **Indian Railways — RDSO / CRIS / RailTel; DMRC, BMRCL, Namma Metro** | Rail signalling and control systems run under safety-critical standards with restricted networks; **specific per-organisation isolation evidence not found — Grade D** | **CG** / **DI** | Head of IT / signalling systems | Cold (but a very large engineering population — worth one interview to test the hypothesis) |
| 48 | **Airports Authority of India — Air Navigation Services** | CNS/ATM software is safety-critical; **per-org isolation evidence not found — Grade D** | **CG** | Head of IT / CNS engineering | Cold |
| 49 | **Tata Steel / JSW Steel / Indian Metals (Chhattisgarh, Odisha)** | Process-control OT in steel plants falls under CEA-style OT isolation for power/industrial critical infrastructure; **Grade D** | **CG** | OT/IT engineering | Cold |

---

## 6. India — Industrial / embedded R&D centres (the "soft isolation" test group) — 14 targets

**Purpose of this block:** this is the group that decides whether W2's Industrial/embedded hypothesis (rubric score 15 vs Defence 13) is right. Their isolation is **usually contract/customer-driven, not site-wide**. Interview question **C1** decides the row.

| # | Organisation (location) | Why its engineering is isolated | Likely first workflow | Role to approach | Warm path |
|---|---|---|---|---|---|
| 50 | **Tata AutoComp Systems — Technical Centre (TTC), Pune** (+ Chennai) | **E23 (C)** — 400+ engineer product-engineering division spanning *Automotive, Truck & Off-Highway, **Defence, Aero & Space**, Industrial & Consumer Products*; embedded systems for automotive/aerospace/medical/industrial. **Defence/aerospace customer contracts** drive restricted handling on those projects | **TG** (embedded test generation) | Head of Engineering, TTC | **Warm**: Tata network; also E18 (DSIR-recognised R&D unit) |
| 51 | **Cummins India Ltd**, Pune (Kothrud R&D) + **Ahmedabad** | **E18 (A)** — DSIR-recognised in-house R&D units (TU/IV-RD/255, R&D Labs 1 & 2, Kothrud); engine software for global OEM programmes with customer security regimes | **TG** | R&D head / Powertrain software lead | **Warm (Gujarat)** — Cummins has an Ahmedabad presence; Pune R&D via IITGN alumni |
| 52 | **Kirloskar Brothers Ltd** (Pune / Sangli / Dewas) + **Kirloskar Oil Engines** | **E18 (A)** — DSIR-recognised R&D units (TU/IV-RD/325) incl. Corporate Research & Engineering Division | **CG** | R&D head | Cold |
| 53 | **Tata Motors Ltd** (Pimpri Pune; **Sanand, Gujarat**) | **E18 (A)** — DSIR-recognised R&D unit; vehicle software, ADAS | **CG** / **TG** | Vehicle-software head | **Warm (Gujarat)** — Sanand plant; Tata ecosystem |
| 54 | **Kalyani Group (Kalyani PSM / Kalyani Steels), Pithampur, MP** | **E18 (A)** — DSIR-recognised R&D units; heavy-vehicle and powertrain software | **CG** | R&D head | Cold (Pithampur is ~1 day from Ahmedabad) |
| 55 | **Kinetic Engineering / Kinetic Green**, Pune (Chinchwad) | **E18 (A)** — DSIR-recognised R&D unit (TU/IV-RD/512) | **CG** | R&D head | Cold |
| 56 | **ARAI — Automotive Research Association of India, Pune** | **E22 (A)** — operates a **Digital Twin Centre for Emerging Automotive Systems** and convenes a governing council of ~100 companies across automotive, **defence, aerospace, telecom, railways**; also runs certification/testing labs | **RT** / **CG** (a standards/eval org — a natural *partner* and *influencer*, not just a customer) | Director / head of Digital Twin Centre | **Warm**: a single door to ~100 industrial engineering leaders — use it as a **multiplexer**, not a customer |
| 57 | **Bosch India — Bosch Technology Centre / R&D** (Bengaluru, Coimbatore) | Global OEM security regimes (ISO 21434) on connected-vehicle and safety software; **per-entity isolation evidence not found — Grade D** | **TG** | Head of engineering | Warm: via ARAI council (row 56) |
| 58 | **Mercedes-Benz R&D India, Bengaluru** | Vehicle software; global OEM security regimes; **Grade D** | **CG** / **TG** | Head of software engineering | Warm: via ARAI |
| 59 | **Continental India / ZF India / Visteon Technical Centre / Harman India** (Bengaluru, Pune) | Tier-1 safety-software (ISO 26262) with customer-isolated development environments (restricted IT, controlled data exchange) — a real and common industry practice; **Grade D** | **TG** | Head of software engineering / process owner | Warm: via ARAI |
| 60 | **Hero MotoCorp (Dharuhera, Rajasthan)**, **TVS Motor (Hosur)**, **Bajaj Auto (Pune)**, **Eicher/Royal Enfield (Pithampur)**, **Maruti Suzuki (Gurgaon & Gujarat)**, **Tube Investments of India** | **E18 (A)** where DSIR-recognised; vehicle/embedded software with customer-restricted development for connected/telematics and ADAS programmes; **Grade D** for per-company isolation | **CG** | R&D / embedded software head | Cold → warm via ARAI (row 56). Note: Hero (Dharuhera) and Maruti (Hansalpur, Gujarat) are closest to Gujarat |

---

## 7. Global — 15 targets

Access is cold for all of these; treat them as **benchmark/validation-of-hypothesis** targets, not pipeline. Use them for the **pricing and procurement reality** data that India cannot give (E15, E16, E17).

| # | Organisation | Why its engineering is isolated | Likely first workflow | Role to approach | Warm path |
|---|---|---|---|---|---|
| 61 | **Lockheed Martin — Rotary & Mission Systems / Aeronautics** | **E20 (D)** — ITAR-governed technical data requires isolated systems; **E16 (A)** — the offline software-delivery pattern (Apollo, Rubix, CDS-based air-gapped updates) exists to serve exactly this class of buyer | **CG** / **TG** | Director, Software Engineering / DevSecOps | Cold |
| 62 | **Northrop Grumman — Software & Mission Systems** | **E20 (D)** | **CG** | Engineering leadership | Cold |
| 63 | **RTX (Raytheon & Collins Aerospace)** | **E20 (D)** | **CG** | Software/IT leadership | Cold |
| 64 | **Boeing — BDS/BCI software** | **E20 (D)** | **CG** | Software engineering leadership | Cold |
| 65 | **SpaceX — Software Engineering (Starlink/vehicle software)** | **E20 (D)**; also commercial-customer launch-security regimes | **CG** | Software engineering manager | Cold |
| 66 | **BAE Systems — Engineering & IT** (UK) | **E20 (D)** | **CG** | Head of software engineering | Cold |
| 67 | **Thales — Engineering / Air Defence software** (FR/UK) | **E20 (D)** | **CG** | Software/secure engineering lead | Cold |
| 68 | **Airbus — Software / Satellite** (FR/DE/ES/UK) | **E20 (D)** | **CG** | Software quality/engineering lead | Cold |
| 69 | **Saab — Software (Grip, Barracuda, Anduril-adjacent ecosystems)** (SE) | **E20 (D)** | **CG** | Software engineering lead | Cold |
| 70 | **Leonardo — Engineering** (IT) | **E20 (D)** | **CG** | Software lead | Cold |
| 71 | **Rheinmetall — Digital/software** (DE) | **E20 (D)** | **CG** | Software lead | Cold |
| 72 | **General Dynamics — GDIT (Electric / Mission Systems)** | **E20 (D)** | **CG** | Software/IT leadership | Cold |
| 73 | **Leidos / SAIC / CACI / Jacobs / Booz Allen** — defence IT & mission software | **E20 (D)**; **also the SI route** (Forge/Salian analogue) | **CG** | Software/AI practice lead | Cold |
| 74 | **Siemens Energy / Hitachi Energy / ABB — Grid & OT software** | **E1/E2 analogue: IEC 62443 zones-and-conduits (E25-context) and regulator-driven OT isolation** | **CG** / **DI** | OT software engineering leadership | Cold |
| 75 | **Emerson / Rockwell Automation / Yokogawa** | OT/software for safety-critical control; regulatory isolation | **CG** / **TG** | Software engineering lead | Cold |

---

## 8. Counts and coverage

| Segment | Rows | Row numbers | Country |
|---|---|---|---|
| Defence R&D labs (DRDO & affiliates) | 12 | 1–12 | India |
| Defence PSUs, shipyards, primes | 8 | 13–20 | India |
| Space (DoS/ISRO) | 8 | 21–28 | India |
| Private defence/aerospace + iDEX channel + startups | 10 | 29–38 | India |
| Critical infrastructure (nuclear, power, transport) | 11 | 39–49 | India |
| Industrial / embedded R&D centres | 11 | 50–60 | India |
| Global primes, OT vendors, SIs | 15 | 61–75 | US/UK/FR/DE/SE/IT |
| **Total numbered rows** | **75** | — | — |

**Distinct organisations ≈ 90.** 61 rows name a single organisation; 9 rows bundle multiple (row 19 → 2, row 20 → 2, row 28 → 2, row 37 → 3, row 45 → 3, row 46 → 4, row 49 → 3, row 59 → 4, row 60 → 6), adding 29 more.
**Row 29 (iDEX/DIO) is a channel, not a customer** — it is listed because it is the access route to ~300 defence startups and to HAL and BEL (E12, E13).
**Counted geography:** India 60 rows / ≈ 72 organisations · Global 15 rows / 15 organisations.

---

## 9. Honest limitations of this list

1. **Isolation evidence is uneven.** Defence/space/power/nuclear rows have Grade A regulatory or institutional evidence (E1–E10, E15). Industrial rows (50–60) mostly carry **Grade D** — inferred from OEM security regimes, not from per-company evidence. Do not present industrial isolation as established.
2. **DRDO/ISRO entry is institutional, not interpersonal.** A student approaching a classified lab needs a published channel (E5 IIG directory, E8/E9 ISRO industry collaboration, E13 iDEX procurement) plus a sponsor. Cold email alone will not work; budget 2–3 weeks per org.
3. **Six startup names (Ideaforge, Pixxel, Dhruva Space, Garuda, Asterion, Manastu) were not individually verified as iDEX winners** in this pass — the iDEX scheme page (E12) confirms the *programme* and *incubator network*, not each company. *(Grade D on individual company iDEX status; A on programme.)* **Correction (2026-11-11):** iDEX's homepage publishes a **state-wise list of iDEX startups/MSMEs**; the **GUJARAT** section names **Optimized Electrotech, Swadesh Fire, Ancor Labs and Robosys Automation** (E26, **A**) — check that list first for Gujarat targets, rather than assuming any named company is iDEX-backed.
4. **No personal contact details are included.** For DRDO, use the SPOC role named in the IIG directory (E5). For all others, use published role-based channels (vendor/industry portals, ISRO Industry Collaboration, iDEX, ARAI membership).
5. **No market size, budget figure, or willingness-to-pay number appears here**, consistent with `09` §9.
6. **Segment ranking is not settled.** `09` §5 ranks Defence #1; W2 re-scored Industrial/embedded above Defence using `09`'s own rubric (15 vs 13). This list is deliberately built to **interview both in parallel**, which is also `09` §C2's instruction ("Pair one defense interview set with one industrial interview set in parallel").
