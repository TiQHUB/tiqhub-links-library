# M365, Intune & Security Link Library

Curated links for Microsoft 365 and Intune administration, security operations, penetration testing, and compliance (CMMC, ISO 42001). 528 links, maintained by TiQHUB Innovators.

Website: enable GitHub Pages for this repo, then browse the searchable version at `https://<owner>.github.io/<repo>/`.

Last updated: 2026-11-06

## Updating the list

1. Edit `data/links.json`.
2. Run `python3 tools/build.py` (regenerates `index.html` and this README).
3. Commit and push. GitHub Pages redeploys in about a minute.

## Contents

- [Daily](#daily)
  - [M365 Admin Portals](#m365-admin-portals)
  - [Status Pages](#status-pages)
- [Microsoft 365 & Entra](#microsoft-365--entra)
  - [Entra ID & Identity](#entra-id--identity)
  - [Email Auth (DMARC/DKIM)](#email-auth-dmarcdkim)
  - [Tenant Baselines & Drift](#tenant-baselines--drift)
  - [PowerShell & Automation](#powershell--automation)
  - [Blogs, Reference & Licensing](#blogs-reference--licensing)
- [Intune & Endpoint](#intune--endpoint)
  - [Device Management & Autopilot](#device-management--autopilot)
  - [GCC High & CMMC Intune](#gcc-high--cmmc-intune)
  - [Windows Hardening & App Removal](#windows-hardening--app-removal)
  - [macOS & Apple](#macos--apple)
  - [Troubleshooting & Error Codes](#troubleshooting--error-codes)
  - [Intune Blogs & Docs](#intune-blogs--docs)
- [Blue Team & SOC](#blue-team--soc)
  - [IP, URL & Domain Lookup](#ip-url--domain-lookup)
  - [File & Malware Analysis](#file--malware-analysis)
  - [Email & Breach Checks](#email--breach-checks)
  - [Threat Intel](#threat-intel)
  - [IoC Feeds](#ioc-feeds)
  - [Hunting & Detection](#hunting--detection)
  - [Datasets & Samples](#datasets--samples)
  - [Windows & Linux Reference](#windows--linux-reference)
- [Pentest & Offensive](#pentest--offensive)
  - [Recon & Attack Surface](#recon--attack-surface)
  - [Web App & API Testing](#web-app--api-testing)
  - [API Security Testing](#api-security-testing)
  - [Cloud Pentest: AWS](#cloud-pentest-aws)
  - [Cloud Pentest: Azure & Entra](#cloud-pentest-azure--entra)
  - [Cloud Pentest: GCP, K8s & Multi-Cloud](#cloud-pentest-gcp-k8s--multi-cloud)
  - [AI & LLM Security Testing](#ai--llm-security-testing)
  - [Exploits & Techniques](#exploits--techniques)
  - [Red Team Notes & Tools](#red-team-notes--tools)
  - [Crypto & Reverse Engineering](#crypto--reverse-engineering)
  - [Tool Directories](#tool-directories)
- [Compliance & GRC](#compliance--grc)
  - [CMMC](#cmmc)
  - [ISO 42001](#iso-42001)
  - [Frameworks & Standards](#frameworks--standards)
  - [Tabletop Exercises](#tabletop-exercises)
  - [AI Governance](#ai-governance)
- [GitHub Repos](#github-repos)
  - [M365 & Entra Config / Drift](#m365--entra-config--drift)
  - [Intune & Endpoint Repos](#intune--endpoint-repos)
  - [M365 DFIR & Assessment](#m365-dfir--assessment)
  - [Detection Engineering](#detection-engineering)
  - [Threat Hunting](#threat-hunting)
  - [Pentest & Red Team](#pentest--red-team)
  - [Web & API Pentest Repos](#web--api-pentest-repos)
  - [Cloud Pentest Repos](#cloud-pentest-repos)
  - [AI Red Team Repos](#ai-red-team-repos)
  - [Compliance & Cloud Posture](#compliance--cloud-posture)
  - [AI & Claude](#ai--claude)
  - [Datasets & References](#datasets--references)
  - [Awesome Lists](#awesome-lists)
- [Courses & Training](#courses--training)
  - [Hacking Labs & CTFs](#hacking-labs--ctfs)
  - [Cloud Security Labs](#cloud-security-labs)
  - [AI & LLM Courses](#ai--llm-courses)
  - [AI Security Labs & Reading](#ai-security-labs--reading)
  - [Compliance Training](#compliance-training)
- [Community](#community)
  - [Microsoft & Intune](#microsoft--intune)
  - [Cloudflare](#cloudflare)
  - [Cybersecurity](#cybersecurity)
  - [CMMC, NIST & GRC](#cmmc-nist--grc)
  - [Wazuh](#wazuh)
- [News](#news)
  - [IT & Security News](#it--security-news)
- [Other Useful Tools](#other-useful-tools)
  - [Dev & Data Utilities](#dev--data-utilities)
  - [Lookups & Lifecycle](#lookups--lifecycle)

## Daily

### M365 Admin Portals

- [cmd.ms](https://cmd.ms/) - Quick M365 Admin Portal Shortcuts (Merill Fernando)
- [Defender](https://security.microsoft.com/)
- [Entra ID](https://entra.microsoft.com/)
- [Exchange](https://admin.cloud.microsoft/exchange#/homepage)
- [Intune](https://intune.microsoft.com/)
- [M365](https://admin.cloud.microsoft/)
- [Purview](https://purview.microsoft.com/)
- [Sharepoint](https://admin.microsoft.com/sharepoint)

### Status Pages

- [Claude Status Page](https://status.claude.com/)
- [Cloudflare Status](https://www.cloudflarestatus.com/)
- [Microsoft 365 Roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap?filters=GCC%20High%2CGCC)
- [Microsoft service health status](https://status.cloud.microsoft/m365/referrer=serviceStatusRedirect)

[Back to top](#contents)

## Microsoft 365 & Entra

### Entra ID & Identity

- [AdminDroid](https://blog.admindroid.com/break-glass-account-for-office-365-login-during-emergency-situations/) - Break Glass Account Setup Guide
- [Entra Mind Maps](https://entra.news/p/entra-mind-maps) - by Merill Fernando
- [Graph Permissions Explorer](https://graphpermissions.merill.net/) - What Each Microsoft Graph Permission Grants (Merill Fernando)
- [idPowerToys](https://idpowertoys.merill.net/) - Conditional Access Documenter & Visualizer (Merill Fernando)
- [Microsoft First-Party App Names](https://aka.ms/AppNames) - Daily-Updated List of Microsoft App IDs (Merill Fernando)
- [Practical 365](https://practical365.com/mfa-status-user-accounts/) - Checking MFA Status for User Accounts
- [What is a Break Glass Account? Meaning, Access & Best Practices](https://www.miniorange.com/blog/what-is-a-break-glass-account/)

### Email Auth (DMARC/DKIM)

- [DMARC Wall of Shame](https://dmarcwallofshame.org/)
- [o365info](https://o365info.com/dkim-dmarc-onmicrosoft-com-domain/) - DKIM/DMARC for onmicrosoft.com

### Tenant Baselines & Drift

- [Maester](https://marketplace.microsoft.com/en-us/product/azure-applications/fortytwoio.maester?tab=Overview) - M365 Security Test Automation via Azure Marketplace (Merill Fernando et al.)
- [Maester Docs](https://maester.dev/) - Open-Source M365 Security Test Framework (Merill Fernando, Fabian Bader, Thomas Naunheim)
- [ScubaGear](https://cisagov.github.io/ScubaGear/) - Official Docs Site
- [TenantBaseline](https://www.tenantbaseline.com/) - M365 Security Baseline Monitoring (Ugur Koç)
- [UTCM: New Way to Monitor Microsoft 365 Tenant Config Changes](https://office365itpros.com/2026/02/03/utcm-beta/)

### PowerShell & Automation

- [Graph X-Ray](https://graphxray.merill.net/) - See the Graph API Calls Behind Portal Clicks (Merill Fernando)
- [IntuneAutomation](https://intuneautomation.com/) - Library of Ready-to-Run Intune PowerShell Scripts (Ugur Koç)
- [o365info](https://o365info.com/certificate-based-authentication/) - Cert-Based Auth for PowerShell Automation
- [Schedule PowerShell Scripts Using Azure Automation](https://m365scripts.com/microsoft365/how-to-schedule-powershell-scripts-using-azure-automation/)
- [Uninstall-Graph](https://uninstall-graph.merill.net/) - Cleanly Remove Graph, Entra & Az PowerShell Modules (Merill Fernando)

### Blogs, Reference & Licensing

- [AdminDroid Blog](https://blog.admindroid.com/) - M365 Reporting & Security
- [Compare All Microsoft 365 Plans](https://www.microsoft.com/en-in/microsoft-365/business/compare-all-microsoft-365-business-products)
- [Entra News](https://entra.news/) - Weekly Microsoft Entra Newsletter (Merill Fernando)
- [Jeffrey Appel](https://jeffreyappel.nl/) - MS Security Blog
- [M365 Maps](https://m365maps.com/)
- [M365 Message Center Archive](https://mc.merill.net/) - Searchable Archive of Message Center Posts (Merill Fernando)
- [Nik Charlebois](https://nik-charlebois.com/) - M365 Automation Blog
- [O365Reports](https://o365reports.com/) - M365 PowerShell Scripts & Reports
- [Sendent Help Docs](https://help.sendent.com/)
- [T-Minus365](https://docs.tminus365.com/) - M365 Docs

[Back to top](#contents)

## Intune & Endpoint

### Device Management & Autopilot

- [Autopilot Hardware Hash Upload](https://foundry-osd.github.io/docs/deploy/autopilot-hash-upload)
- [Device Offboarding Manager](https://intuneoffboarding.com/) - Bulk Offboard Devices from Intune, Autopilot & Entra (Ugur Koç)
- [Get-IntuneAssignments](https://www.powershellgallery.com/packages/Get-IntuneAssignments/1.0.15) - PowerShell Gallery module to list Intune assignments
- [Intune Assignment Checker](https://www.intuneassignments.com/) - Audit Policy & App Assignments by User, Group, or Device (Ugur Koç)
- [Intune Settings Catalog Viewer](https://intunesettings.app/)
- [IntuneGet](https://intuneget.com/) - Deploy Winget Apps to Intune Without Manual Packaging (Ugur Koç)
- [MS Eval Center](https://www.microsoft.com/en-in/evalcenter/evaluate-windows-11-microsoft-365-lab-kit) - Windows 11 + M365 Deployment Lab Kit
- [OSDeploy](https://osd.osdeploy.com/) - OS Deployment Toolkit
- [Planning guide to move to Microsoft Intune](https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/intune-planning-guide)
- [TenuVault](https://www.tenuvault.com/) - Free Intune Backup & Restore (Ugur Koç)

### GCC High & CMMC Intune

- [OIB Deployment](https://docs.mindline.com/docs/devices/device-operations/oib-deployment) - Securing GCC High (Public Preview)
- [Summit 7](https://www.summit7.us/blog/microsoft-intune) - Intune in GCC/GCC High for CMMC

### Windows Hardening & App Removal

- [Insentra](https://www.insentragroup.com/au/insights/geek-speak/secure-workplace/enable-windows-defender-application-control-with-microsoft-intune/) - WDAC Setup Guide (Intune)
- [justinverstijnen](https://justinverstijnen.nl/remove-pre-installed-windows-store-apps-with-intune/) - Remove Store Apps via Intune
- [MS Support](https://support.microsoft.com/en-us/topic/policy-based-removal-of-pre-installed-microsoft-store-apps-e1d41a92-b658-4511-95a6-0fbcc02b4e9c) - Remove Pre-Installed Store Apps
- [Patching Gaps in the CIS Windows 11 Benchmark](https://memv.ennbee.uk/posts/windows-cis-patching-gaps-part1/) - BitLocker

### macOS & Apple

- [How to Enroll macOS Devices in Intune – A Step-by-Step Guide](https://www.burgerhout.org/how-to-enroll-macos-devices-in-intune-a-step-by-step-guide/#prerequisites-for-macos-enrollment)
- [IntuneBrew](https://intunebrew.com/) - Publish & Auto-Update Homebrew macOS Apps in Intune (Ugur Koç)
- [IntuneMacAdmins](https://intunemacadmins.com/) - Community Guides & Scripts for macOS on Intune (Ugur Koç)
- [MS Learn](https://learn.microsoft.com/en-us/mem/intune-service/enrollment/tutorial-use-device-enrollment-program-enroll-ios?WT.mc_id=MVP_371911#step-1-add-mdm-server) - Enroll iOS/iPadOS via Apple Business Manager
- [MS Learn](https://learn.microsoft.com/en-us/intune/intune-service/enrollment/macos-laps) - macOS Local Admin & LAPS Setup
- [MS Learn](https://learn.microsoft.com/en-us/previous-versions/remote-desktop-client/remote-desktop-macos) - Remote Desktop to Windows from macOS
- [odds+endpoints](https://www.oddsandendpoints.co.uk/posts/macos-defender-scan-settings/) - Scheduling macOS Defender AV Scans
- [Platform SSO](https://www.intunemacadmins.com/baselinesettings/platformsso)

### Troubleshooting & Error Codes

- [Fix: Windows 11 ARM No Network on VMware Fusion](https://medium.com/@zorozeri/windows-11-arm-having-no-network-connection-on-vmware-fusion-pro-5b06e894811e)
- [Intune error codes // Tom Plant](https://tplant.com.au/blog/intune-error-codes/)
- [IntuneBrew](https://docs.intunebrew.com/docs/Troubleshooting-Common-macOS-App-Deployment-Issues-in-Intune) - macOS App Deployment Troubleshooting
- [Microsoft Login Error Code Lookup](https://login.microsoftonline.com/error)
- [MS Learn](https://learn.microsoft.com/en-us/troubleshoot/microsoft-365/admin/miscellaneous/sara-command-line-version) - SaRA Enterprise (Support & Recovery Tool)

### Intune Blogs & Docs

- [AwesomeIntune](https://awesomeintune.com/) - Directory of 187+ Free Intune Tools & Scripts (Ugur Koç)
- [Call4Cloud](https://call4cloud.nl/) - Intune & Cloud Security Blog
- [Intune Documentation](https://www.intunedocumentation.com/) - Generate Audit-Ready Intune Tenant Docs as PDF/Word (Ugur Koç)
- [odds+endpoints](https://www.oddsandendpoints.co.uk/) - Intune/macOS Blog
- [Ugur Labs](https://ugurlabs.com/) - Hub for Ugur Koç’s Free Intune & Cloud Admin Tools

[Back to top](#contents)

## Blue Team & SOC

### IP, URL & Domain Lookup

- [AbuseIPDB](https://www.abuseipdb.com/) - IP Address Abuse Reports
- [Cloudflare Radar](https://radar.cloudflare.com/scan) - URL Scanner
- [crt.sh](https://crt.sh/) - Certificate Search
- [Google Safe Browsing](https://transparencyreport.google.com/safe-browsing/search) - URL Safety Lookup
- [host.io](https://host.io/) - Domain Name Data Lookup
- [IANA](https://www.iana.org/whois) - Whois Service
- [Immuniweb](https://www.immuniweb.com/websec/) - High-Level Website Security Test
- [InQuest Labs](https://labs.inquest.net/repdb) - Domain Reputation and IOC Database
- [IPVoid](https://www.ipvoid.com/) - All-purposes IP/Domain Lookups
- [MaxMind](https://www.maxmind.com/en/geoip-demo) - IP Geolocation
- [mnemonic](https://passivedns.mnemonic.no/) - Passive DNS Lookups
- [Netlas](https://app.netlas.io/responses/) - All-purposes IP/Domain/HTTP Response/Certificate Lookups
- [Online nslookup](https://www.nslookup.io/) - NSLookup
- [Qualys SSLLabs](https://www.ssllabs.com/ssltest/) - SSL/Certificate Security Tester
- [RIPE Database](https://apps.db.ripe.net/db-web-ui/query) - Whois Database
- [Robtex](https://www.robtex.com/) - All-purposes IP/Domain Lookups
- [Symantec Sitereview](https://sitereview.bluecoat.com/#/) - URL categorization
- [urlscan.io](https://urlscan.io/) - URL Scanner
- [URLVoid](https://www.urlvoid.com/) - Website Reputation Checker
- [Whois.com](https://www.whois.com/) - Whois Lookups
- [Zelster](https://zeltser.com/lookup-malicious-websites/) - List of Website/Domain Lookup Tools

### File & Malware Analysis

- [any.run](https://app.any.run/) - Restricted automated Malware Analysis
- [AppTotal](https://apptotal.io/) - Analyze third-party OAuth apps
- [ExtensionTotal](https://www.extensiontotal.com/) - Check malicious IDE extensions
- [Hybrid Analysis](https://www.hybrid-analysis.com/) - Automated Malware Analysis
- [InQuest Labs](https://labs.inquest.net/dfi) - Automated Deep File Inspection
- [IRIS-H](https://iris-h.services/pages/dashboard) - Online Digital Forensics
- [Joe Sandbox](https://www.joesandbox.com/#windows) - Automated Malware Analysis
- [MalShare](https://www.malshare.com/) - Malware Sample Repository
- [MalwareBazaar](https://bazaar.abuse.ch/) - Malware sample exchange
- [MetaDefender](https://metadefender.opswat.com/?lang=en) - Automated File Analysis and all-purpose Scanner
- [Snyk](https://snyk.io/advisor/) - library analysis
- [socket.dev](https://socket.dev/npm) - analyse npm packages
- [VirusTotal](https://www.virustotal.com/) - Automated Malware Analysis
- [VMRay](https://threatfeed.vmray.com/) - Restricted automated Malware Analysis

### Email & Breach Checks

- [DeHashed](https://dehashed.com/) - Information Breach Checker
- [Have I Been Pwned](https://haveibeenpwned.com/) - Mail Address & Password Leak Checker
- [MXToolbox](https://mxtoolbox.com/) - Email Security Swiss Army Knife
- [PhishTank](https://www.phishtank.com/index.php) - Phishing URL tracker

### Threat Intel

- [AlienVault OTX](https://otx.alienvault.com/) - All-purposes Threat Exchange
- [CDN Finder](https://www.cdnplanet.com/tools/cdnfinder) - Comfortable find which CDNs a website uses
- [Check Sum Honeypot](https://check-the-sum.fr/) - IP and Malicious Domain Database
- [Cisco Talos](https://www.talosintelligence.com/reputation_center) - Reputation Lookups
- [Cloudflare Radar](https://radar.cloudflare.com/domains) - Domain Rankings
- [GreyNoise](https://viz.greynoise.io/) - CTI and "anti-CTI" - things not to worry about
- [IBM X-Force Exchange](https://exchange.xforce.ibmcloud.com/) - All-purposes Threat Exchange
- [ioc(.)one](https://ioc.one/) - OSINT Cyber Threat Intelligence Database
- [Microsoft](https://www.microsoft.com/en-us/wdsi/threats) - Threat Encyclopedia
- [Oasis Open](https://oasis-open.github.io/cti-stix-visualization/) - STIX Visualizer
- [ransomwatch](https://ransomwatch.telemetry.ltd/#/) - all malware group sites & posts
- [Shadowserver Foundation](https://dashboard.shadowserver.org/) - Global Sinkhole Dashboard
- [ThreatMiner](https://www.threatminer.org/) - IOC and APT Note Data Mining

### IoC Feeds

- [abuse.ch](https://abuse.ch/) - Well-curated IoC Lists
- [FireHOL](http://iplists.firehol.org/) - Collection of IoC Lists
- [I-BlockList](https://www.iblocklist.com/lists) - IoC Lists
- [InQuest Labs](https://labs.inquest.net/iocdb) - IoC Database
- [MISP](https://www.misp-project.org/feeds/) - List of default MISP Feeds
- [Proofpoint Emerging Threats](https://rules.emergingthreats.net/) - IoCs & Rules

### Hunting & Detection

- [Canarytokens](https://canarytokens.org/generate) - Tokens to alert on resource access
- [Filesec.io](https://filesec.io/) - File extensions used by attackers
- [Jai Minton](https://www.jaiminton.com/cheatsheet/DFIR/) - Extensive DFIR cheatsheet
- [JPCERT](https://jpcertcc.github.io/ToolAnalysisResultSheet/) - Mapping of Log Events to Techniques & Tools
- [KQL Search](https://www.kqlsearch.com/) - Search Engine for Community KQL Queries (Ugur Koç)
- [MaGMa](https://www.betaalvereniging.nl/en/safety/magma/) - SIEM use case Documentation & Evaluation
- [MalAPI.io](https://malapi.io/) - Windows APIs used by attackers
- [MITRE CAPEC](https://capec.mitre.org/index.html) - Attack Pattern Enumeration
- [MITRE CAR](https://car.mitre.org/analytics/) - Detections Mapped to Techniques
- [SOC Prime Threat Detection Marketplace](https://my.socprime.com/en/tdm/) - SIEM Use Cases
- [Splunk Security Content](https://research.splunk.com/detections/) - More Splunk Detection Rules
- [Splunk Security Content API](https://docs.splunkresearch.com/?version=latest) - Splunk Detection Rules
- [Stealthbits](https://attack.stealthbits.com/) - Credential Theft Attack Catalog
- [WTFBins](https://wtfbins.wtf/) - Benign binaries with malware-like behavior
- [YaraDBG](https://yaradbg.dev/) - Online Yara Rule Debugger

### Datasets & Samples

- [Malpedia](https://malpedia.caad.fkie.fraunhofer.de/library) - Malware & Threat Actor Library
- [Malware-Traffic-Analysis](https://www.malware-traffic-analysis.net/) - Malware Traffic PCAPs
- [Rapid7 Open Data](https://opendata.rapid7.com/) - Up-to-data DNS/HTTP/SSL Data
- [SecRepo](http://www.secrepo.com/) - Diverse collection of security datasets
- [vx-underground](https://www.vx-underground.org/) - Malware Samples & Threat Actor Library

### Windows & Linux Reference

- [Anomaly.io](https://anomaly.io/anomaly-detection-normal-distribution/) - Statistical anomaly detection explained
- [Checkpoint cpr](https://anti-debug.checkpoint.com/) - Anti-Debug Tricks
- [Cisco Talos](https://www.talosintelligence.com/software) - Helpful Software Collection
- [explainshell.com](https://explainshell.com/) - Unix command-line argument help
- [Microsoft Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) - Windows API Documentation
- [pinvoke.net](http://www.pinvoke.net/) - Windows API Documentation & Access Examples
- [Public Suffix List](https://publicsuffix.org/list/) - Public Domain Suffixes
- [STRONTIC xCyclopedia](https://strontic.github.io/xcyclopedia/) - Low-Level Encyclopedia for Executables
- [Syscall.sh](https://syscall.sh/) - Linux System Calls Reference
- [Ultimatewindowssecurity](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx) - Windows Event Log Documentation
- [user-agents.net](https://user-agents.net/) - Known user agents documentation
- [Wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures) - Common file headers/signatures
- [Wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) - HTTP Status Codes
- [Wikipedia](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers) - List of TCP and UDP port numbers
- [Wikipedia](https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains) - List of top-level-domains
- [Windows Sysinternals](https://learn.microsoft.com/en-us/sysinternals/downloads/) - Sysinternals Utilities

[Back to top](#contents)

## Pentest & Offensive

### Recon & Attack Surface

- [allports.exposed](http://allports.exposed/) - Network Rules Testing
- [Cali Dog Security](https://calidog.io/) - Real-Time Certificate Transparency Log
- [Censys](https://search.censys.io/) - All-purposes Internet Scanner
- [hunter.io](https://hunter.io/) - Email Address Finder
- [LeakIX](https://leakix.net/) - OSINT Information Leak Search
- [maclookup](https://maclookup.app/) - MAC Address Vendor Lookup
- [OSINT Framework](https://osintframework.com/) - Ordered List of OSINT Tools
- [Outgoing Port Tester](http://portquiz.net/) - Network Rules Testing
- [PublicWWW](https://publicwww.com/) - Website Source Code Search Engine
- [Shodan](https://www.shodan.io/) - All-purposes Internet Scanner
- [UK-OSINT](https://www.uk-osint.net/index.html) - OSINT Resource Website
- [WiGLE](https://wigle.net/) - Wireless Network Mapping

### Web App & API Testing

- [Burp Suite Community](https://portswigger.net/burp/communitydownload) - Free Web Proxy for Manual Testing
- [Caido](https://caido.io/) - Lightweight Web Security Proxy (Burp Alternative)
- [CSP Evaluator](https://csp-evaluator.withgoogle.com/) - Check Content-Security-Policy for Bypasses
- [HackerOne Hacktivity](https://hackerone.com/hacktivity) - Disclosed Bug Bounty Reports
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) - App Security Verification Standard (Test Checklist)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) - Concise Secure-Coding & Testing Cheat Sheets
- [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) - Web Security Testing Guide (Methodology)
- [PortSwigger Research](https://portswigger.net/research) - New Web Attack Techniques
- [PortSwigger XSS Cheat Sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet) - Event Handlers, Tags & Filter Bypasses
- [reqbin](https://reqbin.com/) - Online API & HTTP Request Testing Tool
- [Request Inspector](https://requestinspector.com/) - Webhook Proxy/Debugger
- [Security Headers](https://securityheaders.com/) - Scan a Site's HTTP Security Headers
- [ZAP](https://www.zaproxy.org/) - Free Open-Source Web App Scanner & Proxy

### API Security Testing

- [APIsec University](https://www.apisecuniversity.com/) - Free API Security Courses
- [GraphQL Security (HackTricks)](https://book.hacktricks.wiki/en/network-services-pentesting/pentesting-web/graphql.html) - GraphQL Introspection & Attack Techniques
- [HackTricks API Pentesting](https://book.hacktricks.wiki/en/pentesting-web/web-api-pentesting.html) - Web API Testing Methodology
- [jwt.io](https://jwt.io/) - Decode & Inspect JSON Web Tokens
- [OWASP API Security Top 10](https://owasp.org/API-Security/) - 2023 API Risk List (BOLA, BFLA, etc.)
- [Postman Public API Network](https://www.postman.com/explore) - Find API Collections & Specs to Test

### Cloud Pentest: AWS

- [AWS IAM Privilege Escalation](https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/) - 21 IAM Privesc Methods (Rhino Security Labs)
- [AWS Penetration Testing Policy](https://aws.amazon.com/security/penetration-testing/) - What You May Test Without Approval
- [AWS Security Blog](https://aws.amazon.com/blogs/security/) - Official AWS Security Guidance
- [AWS Security Maturity Model](https://maturitymodel.security.aws.dev/) - Prioritized AWS Security Roadmap
- [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html) - Multi-Account Security Design
- [pathfinding.cloud](https://pathfinding.cloud/) - AWS IAM Privilege Escalation Paths (Datadog)
- [permissions.cloud](https://aws.permissions.cloud/) - AWS IAM Actions, Managed Policies & API Mappings

### Cloud Pentest: Azure & Entra

- [AzAdvertizer](https://www.azadvertizer.net/) - Browse Azure RBAC Roles, Policies & Aliases
- [Azure Built-in Roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles) - Reference for Every Azure RBAC Role
- [Azure Threat Research Matrix](https://microsoft.github.io/Azure-Threat-Research-Matrix/) - ATT&CK-Style Matrix for Azure
- [BloodHound Docs](https://bloodhound.specterops.io/) - Attack Path Mapping for AD & Entra (AzureHound)
- [Cloudbrothers Azure Attack Paths](https://cloudbrothers.info/en/azure-attack-paths/) - Common Azure & Entra Escalation Paths
- [Dirk-jan Mollema](https://dirkjanm.io/) - Entra ID & Azure Attack Research Blog
- [Microsoft Cloud Pentest Rules of Engagement](https://www.microsoft.com/en-us/msrc/pentest-rules-of-engagement) - What You May Test in Azure & M365
- [Microsoft Cloud Security Benchmark](https://learn.microsoft.com/en-us/security/benchmark/azure/overview) - Azure Security Baseline Controls

### Cloud Pentest: GCP, K8s & Multi-Cloud

- [breaches.cloud](https://www.breaches.cloud/) - Cloud Breach Case Studies
- [Cloud Vulnerability Database](https://www.cloudvulndb.org/) - Cloud Provider Vulnerabilities & Issues
- [CloudSecDocs](https://cloudsecdocs.com/) - Cloud & Container Security Notes (Marco Lancini)
- [CloudSecList](https://cloudseclist.com/) - Weekly Cloud Security Newsletter
- [Datadog Security Labs](https://securitylabs.datadoghq.com/) - Cloud Threat Research & Attack Write-Ups
- [GCP Privilege Escalation](https://rhinosecuritylabs.com/gcp/privilege-escalation-google-cloud-platform-part-1/) - GCP IAM Privesc Methods (Rhino Security Labs)
- [Hacking The Cloud](https://hackingthe.cloud/) - AWS, Azure & GCP Attack Techniques Encyclopedia
- [HackTricks Cloud](https://cloud.hacktricks.wiki/) - Cloud, CI/CD & Kubernetes Pentest Wiki
- [Kubernetes Security Checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) - Official K8s Hardening Checklist
- [MITRE ATT&CK Cloud Matrix](https://attack.mitre.org/matrices/enterprise/cloud/) - Cloud Tactics & Techniques
- [Threat Matrix for Kubernetes](https://microsoft.github.io/Threat-Matrix-for-Kubernetes/) - ATT&CK-Style Matrix for K8s (Microsoft)

### AI & LLM Security Testing

- [0DIN](https://0din.ai/) - GenAI Bug Bounty & Jailbreak Disclosures
- [AI Incident Database](https://incidentdatabase.ai/) - Real-World AI Failures & Harms
- [AVID](https://avidml.org/) - AI Vulnerability Database
- [Embrace The Red](https://embracethered.com/blog/) - Prompt Injection & AI Agent Exploits (Johann Rehberger)
- [Google SAIF](https://saif.google/) - Secure AI Framework & Risk Map
- [huntr](https://huntr.com/) - AI/ML Open-Source Bug Bounty
- [Microsoft AI Red Team](https://learn.microsoft.com/en-us/security/ai-red-team/) - AI Red Teaming Guidance & Lessons
- [MITRE ATLAS](https://atlas.mitre.org/) - Adversarial AI Tactics & Techniques Matrix
- [OWASP AI Exchange](https://owaspai.org/) - AI Threats & Controls Reference
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) - 2025 LLM & GenAI Risk List
- [promptfoo Red Team Docs](https://www.promptfoo.dev/docs/red-team/) - LLM Red Teaming Guide & Plugins
- [Simon Willison: Prompt Injection](https://simonwillison.net/tags/prompt-injection/) - Ongoing Prompt Injection Coverage
- [Vulnerable MCP Project](https://vulnerablemcp.info/) - Known MCP Server Vulnerabilities

### Exploits & Techniques

- [ExploitDB](https://www.exploit-db.com/) - Database of Exploits
- [GTFOBins](https://gtfobins.github.io/) - Curated List of abusable Linux Binaries
- [Hijack Libs](https://hijacklibs.net/) - Known DLL Sideloading Libraries
- [LOLBAS](https://lolbas-project.github.io/) - Curated List of abusable Windows Binaries and Scripts
- [LOLDrivers](https://www.loldrivers.io/) - Living Off The Land Drivers
- [LOOBins](https://www.loobins.io/) - Curated List of abusable MacOS Binaries
- [LOTS Project](https://lots-project.com/) - Living Off Trusted Sites
- [Pentestmonkey](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet) - Reverse Shell Cheat Sheet
- [shell-storm](http://shell-storm.org/shellcode/) - Shellcode Database
- [Wietze's Blog](https://www.wietzebeukema.nl/blog/hijacking-dlls-in-windows) - More DLLs Sideloading Libraries
- [XSS Payloads](http://www.xss-payloads.com/) - XSS Payload Library

### Red Team Notes & Tools

- [AADInternals](https://aadinternals.com/) - Useful offensive Azure articles & knowledge
- [AntiScan.Me](https://antiscan.me/) - Online Malware Scanner Without Result Distribution
- [C2 Matrix](https://www.thec2matrix.com/matrix) - C2 Framework Evaluations
- [dmcxblue](https://dmcxblue.gitbook.io/red-team-notes-2-0/) - Red Team Note & Examples
- [ired.team](https://www.ired.team/) - Red Team Notes
- [obfuscator.io](https://obfuscator.io/) - JavaScript Obfuscator Tool
- [revshells](https://www.revshells.com/) - Reverse Shell Generator

### Crypto & Reverse Engineering

- [Binary Ninja Cloud](https://cloud.binary.ninja/) - Disassembler, Decompiler
- [Blockchain Explorer](https://www.blockchain.com/explorer) - Search various Blockchains
- [Compiler Explorer](https://godbolt.org/) - Live-view compiled code
- [CrackStation](https://crackstation.net/) - Online Password Hash Cracking
- [DCode](https://www.dcode.fr/tools-list) - Misc. Decoding Tools
- [factordb.com](http://factordb.com/index.php) - Known Prime Factors

### Tool Directories

- [Kali Linux](https://www.kali.org/tools/) - Tools Listing
- [Pentest Framework](http://www.vulnerabilityassessment.co.uk/Penetration%20Test.html) - Pentest Guidelines & Tools
- [SANS ISC](https://isc.sans.edu/links.html) - Useful InfoSec Links
- [SecTools](http://sectools.org/) - List of Network Security Tools
- [securitytools](https://tools.watchdawg.io/) - collection of open-source security tools

[Back to top](#contents)

## Compliance & GRC

### CMMC

- [A Small Business Guide to CMMC Compliance (2026)](https://www.totem.tech/cmmc-compliance-small-business-guide/)
- [CIO](https://dodcio.defense.gov/CMMC/Resources-Documentation/) - CMMC Resources & Documentation
- [CMMC Assessments](https://dodcio.defense.gov/CMMC/Assessments/)
- [CMMC Info Institute](https://cmmcinfo.org/800-171-self-assessments/) - 800-171 Self-Assessments & SPRS
- [CMMC Level 1](https://ndisac.org/dibscc/cyberassist/cybersecurity-maturity-model-certification/level-1/) - DIB SCC CyberAssist
- [CMMC Resources, Templates & Compliance Guides](https://www.cmmc.com/resources)
- [CMMC Toolkit Wiki](https://cmmcwiki.org/index.php/Main_Page)
- [Cybersecurity Facility-Related Control Systems (FRCS)](https://serdp-estcp.mil/resources/details/377d0819-38d9-4d1d-a7e9-d8ada43c3f70)
- [Federal Register](https://www.federalregister.gov/documents/2024/10/15/2024-22905/cybersecurity-maturity-model-certification-cmmc-program) - CMMC Program Final Rule
- [Free Tools](https://www.totem.tech/free-tools/) - Resources for your cybersecurity compliance journey
- [Microsoft CMMC Level 1 Implementation Guide](https://www.microsoft.com/cms/api/am/binary/RE54xON)
- [r/CMMC: KVM Endpoints Accessing GCC High VDI](https://www.reddit.com/r/CMMC/comments/1turrbr/treatment_of_kvm_endpoints_accessing_gcch_virtual/) - KVM Endpoints & GCCH Virtual Desktops
- [r/CMMC: We Passed Our CMMC Assessment](https://www.reddit.com/r/CMMC/comments/1owyb9a/we_passed_our_cmmc_assessment_and_heres_what_we/) - "We Passed Our Assessment" Megathread
- [RADICL CMMC Toolkit Template Library](https://radicl.com/cmmc-level-1-template-toolkit)
- [System Security Plan (SSP)](https://www.fedramp.gov/legacy/playbook/csp/authorization/ssp/#bad-control-responses) - FedRAMP Legacy Documentation
- [Totem Tech](https://www.totem.tech/processes-acting-on-behalf-of-authorized-users/#:~:text=a%20piece%20of%20software%20that,%2Fpasswd%20or%20%2Fetc%2Fshadow) - Processes Acting on Behalf of Authorized Users

### ISO 42001

- [Defining Your ISO/IEC 42001 Audit Scope](https://sensiba.com/resources/insights/iso-iec-42001-audit-scope/)
- [ISO 42001 Mandatory Documents: Complete List (All 19)](https://orbit.reconn.io/iso-42001-mandatory-documents/)
- [ISO 42001 Mandatory Documents: Complete List by Clause & Control](https://advisera.com/articles/iso-42001-mandatory-documents/)
- [ISO 42001 Template Documents + Downloads](https://cyberzoni.com/iso-42001-templates/)
- [ISO 42001 Toolkit](https://governancedocs.com/product/iso-42001-toolkit/) - Comprehensive AI Governance Templates!
- [ISO-Docs](https://iso-docs.com/products/iso-42001-ai-governance-framework) - ISO 42001 AI Governance Toolkit
- [ITSM Docs](https://www.itsm-docs.com/en-in/collections/iso-42001-ai-governance-framework-templates) - ISO 42001 AI Governance Templates

### Frameworks & Standards

- [ACSC](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight) - Essential Eight Mitigations
- [ATT&CK® Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FCloud-Architekt%2FAzureAD-Attack-Defense%2Fmain%2Fmedia%2Fmitre%2FChapter6%2FAADPB-CP6-TTPs.json&tabs=false&selecting_techniques=false)
- [BSI](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html) - IT-Grundschutz - Systemic basis for information security
- [CIS](https://www.cisecurity.org/controls/cis-controls-list) - Top 20 Security Controls
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [CISA](https://www.cisa.gov/cyber-essentials) - Cyber Essentials
- [CVE Program](https://www.cve.org/) - CVE Records (cve.org)
- [DoD Cyber Exchange](https://public.cyber.mil/stigs/) - STIGs Library
- [ENISA](https://www.enisa.europa.eu/topics/national-cyber-security-strategies/information-sharing/isacs-toolkit/view#) - Information Sharing and Analysis Centers
- [ISO 27001](https://hightable.io/iso-27001-controls/) - ISO 27001 Controls
- [MITRE CWE](http://cwe.mitre.org/) - Common Weakness Enumeration
- [MS Security Blog](https://www.microsoft.com/en-us/security/blog/2019/01/10/best-practices-for-securely-using-microsoft-365-the-cis-microsoft-365-foundations-benchmark-now-available/) - CIS M365 Foundations Benchmark
- [NIST](https://csrc.nist.gov/publications/search?viewMode-lg=brief&ipp-lg=ALL&status-lg=Final&series-lg=NISTIR) - NISTIR Standards & Frameworks
- [OWASP](https://owasp.org/www-project-security-knowledge-framework/) - Code Security Knowledge Framework
- [OWASP](https://owasp.org/www-project-top-ten/) - Top 10 Web Application Security Risks
- [PCI DSS](https://www.pcisecuritystandards.org/document_library) - PCI Standards
- [VERIS Framework](https://verisframework.org/) - Incident Taxonomy & Documentation

### Tabletop Exercises

- [CISA](https://www.cisa.gov/resources-tools/resources/ctep-package-documents) - CTEP Tabletop Exercise Package
- [Lake Ridge](https://www.lakeridge.io/how-to-run-tabletop-exercises-to-test-organizational-incident-response-capability-nist-sp-800-171-rev2-cmmc-20-level-2-control-irl2-363-template-and-checklist) - Tabletop Exercise Template (IR.L2-3.6.3)
- [NCSC](https://www.ncsc.gov.uk/section/exercise-in-a-box/tabletop-exercises) - Tabletop Exercises Guide

### AI Governance

- [LinkedIn](https://www.linkedin.com/posts/andy-ballard-cissp-273637161_microsoftdefender-defenderxdr-defenderforcloudapps-activity-7401695938496446464-AJGw) - Blocking GenAI Apps with MS Defender
- [Playbook](https://airc.nist.gov/airmf-resources/playbook/) - AIRC

[Back to top](#contents)

## GitHub Repos

### M365 & Entra Config / Drift

- [EntraExporter](https://github.com/microsoft/EntraExporter) - Entra Tenant Config Export Tool
- [IaC-UTCM](https://github.com/ElliottLW/IaC-UTCM) - Entra/Intune Config Snapshot Scripts
- [M365-Drift-Monitor](https://github.com/TiQHUB/M365-Drift-Monitor) - AI-Powered Config Drift Detection
- [Microsoft365DSC](https://github.com/microsoft/Microsoft365DSC) - M365 Tenant Config as Code
- [ScubaGear (GitHub)](https://github.com/cisagov/ScubaGear) - CISA M365 Baseline Scanner
- [TenantBaseline (GitHub)](https://github.com/ugurkocde/TenantBaseline) - M365 Drift Prevention Tool (Ugur Koç)
- [UTCM-tooling](https://github.com/jussiroine/UTCM-tooling) - M365 Tenant Config Management

### Intune & Endpoint Repos

- [blawalt/WinPEAP](https://github.com/blawalt/WinPEAP)
- [De-Bloat](https://github.com/andrew-s-taylor/public/tree/main/De-Bloat) - Windows Debloat Script
- [Harden-Windows-Security](https://github.com/HotCakeX/Harden-Windows-Security) - Community Windows hardening module (HotCakeX, not Microsoft)
- [IntuneManagement](https://github.com/Micke-K/IntuneManagement) - Intune/Azure Policy Export-Import Tool
- [IntuneOneDataCollector](https://github.com/markstan/IntuneOneDataCollector) - Intune Support Data Tool
- [IntuneQL](https://github.com/ugurkocde/IntuneQL) - Terminal UI to Query & Act on Intune via Graph (Ugur Koç)
- [mdatp-xplat](https://github.com/microsoft/mdatp-xplat/tree/master/macos/mobileconfig/profiles) - macOS Defender Config Profiles
- [MSEndpointMgr/Intune](https://github.com/MSEndpointMgr/Intune) - Script Collection
- [OpenIntuneBaseline: macOS Settings Guidance](https://github.com/SkipToTheEndpoint/OpenIntuneBaseline/wiki/macos-settingsguidance) - macOS Settings Guidance
- [OpenIntuneBaseline: Windows Settings Output](https://github.com/SkipToTheEndpoint/OpenIntuneBaseline/blob/main/WINDOWS/SETTINGSOUTPUT.md#section-46) - Windows Settings Reference

### M365 DFIR & Assessment

- [CRT](https://github.com/CrowdStrike/CRT) - CrowdStrike Reporting Tool for Azure/M365
- [CSET](https://github.com/cisagov/cset) - CISA Cybersecurity Evaluation Tool
- [DFIR-O365RC](https://github.com/anssi-fr/dfir-o365rc) - ANSSI M365/Azure Log Collection
- [Hawk](https://github.com/T0pCyber/hawk) - M365 Compromise Investigation
- [Microsoft-Extractor-Suite](https://github.com/invictus-ir/Microsoft-Extractor-Suite) - M365/Azure Log Acquisition
- [Monkey365](https://github.com/silverhack/monkey365) - M365/Azure Security Assessment
- [Sparrow](https://github.com/cisagov/Sparrow) - CISA M365 Incident Triage (check status; see Untitled Goose Tool)
- [Velociraptor](https://github.com/velocidex/velociraptor) - Endpoint DFIR & Hunting
- [Zero Trust Assessment](https://github.com/microsoft/zerotrustassessment) - Microsoft’s Automated Entra & Intune Posture Check

### Detection Engineering

- [awesome-lists](https://github.com/mthcht/awesome-lists) - Security Lists for SOC Detections
- [Azure-Sentinel](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions) - KQL Detection Rules
- [Bulk-IOC-CSVs](https://github.com/jkerai1/SoftwareCertificates/tree/main/Bulk-IOC-CSVs/MDA) - MDA IOC Import Templates
- [detection-rules](https://github.com/elastic/detection-rules) - Elastic Security Detection Rules
- [Sigma](https://github.com/SigmaHQ/sigma) - Generic SIEM Signature Format & Rules
- [sigma-rules](https://github.com/joesecurity/sigma-rules) - Sigma Rules (Joe Security)

### Threat Hunting

- [CyberThreatHunting](https://github.com/A3sal0n/CyberThreatHunting) - Threat Hunter Resource Collection
- [EDR-Telemetry](https://github.com/tsale/EDR-Telemetry) - Compare EDR Capabilities
- [Mitigating-Web-Shells](https://github.com/nsacyber/Mitigating-Web-Shells) - NSA Web Shell Guidance
- [red_team_tool_countermeasures](https://github.com/fireeye/red_team_tool_countermeasures) - Red Team Tool Signatures
- [ThreatHunter-Playbook (now OTRF)](https://github.com/hunters-forge/ThreatHunter-Playbook) - Hunting Ideas
- [ThreatHunting](https://github.com/ThreatHuntingProject/ThreatHunting) - General Threat Hunting Info

### Pentest & Red Team

- [adversary_emulation_library](https://github.com/center-for-threat-informed-defense/adversary_emulation_library) - Adversary Emulation Plans
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) - Adversary Emulation Tests
- [Github](https://github.com/wisec/domxsswiki/wiki/Sinks) - wisec/domxsswiki - Code execution sinks in web apps
- [Hack-Tools](https://github.com/LasCC/Hack-Tools) - All-in-One Web Pentest Browser Extension
- [HackTricks](https://github.com/carlospolop/hacktricks) - Pentest Techniques Wiki
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) - Payloads & Bypasses for Web Apps
- [Red-Team-Infrastructure-Wiki](https://github.com/bluscreenofjeff/Red-Team-Infrastructure-Wiki) - Red Team Infra Setup
- [webshell](https://github.com/tennc/webshell) - Webshell Collection

### Web & API Pentest Repos

- [Arjun](https://github.com/s0md3v/Arjun) - HTTP Parameter Discovery
- [crAPI](https://github.com/OWASP/crAPI) - Completely Ridiculous API (Vulnerable API Lab)
- [Dalfox](https://github.com/hahwul/dalfox) - XSS Scanner & Parameter Analyzer
- [DVGA](https://github.com/dolevf/Damn-Vulnerable-GraphQL-Application) - Damn Vulnerable GraphQL App
- [ffuf](https://github.com/ffuf/ffuf) - Fast Web Fuzzer
- [graphql-cop](https://github.com/dolevf/graphql-cop) - GraphQL Security Auditor
- [httpx](https://github.com/projectdiscovery/httpx) - Fast HTTP Probing Toolkit
- [InQL](https://github.com/doyensec/inql) - GraphQL Testing Burp Extension
- [jwt_tool](https://github.com/ticarpi/jwt_tool) - JWT Testing & Exploitation
- [katana](https://github.com/projectdiscovery/katana) - Web Crawler & Spider
- [Kiterunner](https://github.com/assetnote/kiterunner) - API Endpoint & Route Discovery
- [nuclei](https://github.com/projectdiscovery/nuclei) - Template-Based Vulnerability Scanner
- [SecLists](https://github.com/danielmiessler/SecLists) - Wordlists for Fuzzing & Discovery
- [sqlmap](https://github.com/sqlmapproject/sqlmap) - Automatic SQL Injection Tool
- [VAmPI](https://github.com/erev0s/VAmPI) - Vulnerable REST API Lab

### Cloud Pentest Repos

- [AWSGoat](https://github.com/ine-labs/AWSGoat) - Vulnerable-by-Design AWS Lab
- [AzureAD-Attack-Defense](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense) - Entra Attack Scenarios & Detections
- [AzureGoat](https://github.com/ine-labs/AzureGoat) - Vulnerable-by-Design Azure Lab
- [AzureHound](https://github.com/SpecterOps/AzureHound) - Entra & Azure Data Collector for BloodHound
- [Checkov](https://github.com/bridgecrewio/checkov) - IaC Static Analysis (Terraform, Bicep, K8s)
- [CloudFox](https://github.com/BishopFox/cloudfox) - Find Exploitable Attack Paths in Cloud
- [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) - Vulnerable-by-Design AWS Scenarios
- [GraphRunner](https://github.com/dafthack/GraphRunner) - Post-Exploitation via Microsoft Graph
- [Kubescape](https://github.com/kubescape/kubescape) - Kubernetes Security Scanner
- [MicroBurst](https://github.com/NetSPI/MicroBurst) - Azure Security Assessment Scripts
- [Pacu](https://github.com/RhinoSecurityLabs/pacu) - AWS Exploitation Framework
- [Peirates](https://github.com/inguardians/peirates) - Kubernetes Penetration Testing Tool
- [PurpleCloud](https://github.com/iknowjason/PurpleCloud) - Azure & Entra Cyber Range Builder
- [ROADtools](https://github.com/dirkjanm/ROADtools) - Entra ID Recon & Token Toolkit
- [ScoutSuite](https://github.com/nccgroup/ScoutSuite) - Multi-Cloud Security Auditing
- [Stratus Red Team](https://github.com/DataDog/stratus-red-team) - Cloud Attack Technique Emulation
- [TeamFiltration](https://github.com/Flangvik/TeamFiltration) - M365 Enumeration, Spraying & Exfil
- [TokenTacticsV2](https://github.com/f-bader/TokenTacticsV2) - Entra Token Manipulation Toolkit
- [Trivy](https://github.com/aquasecurity/trivy) - Container, IaC & Cloud Misconfig Scanner
- [TruffleHog](https://github.com/trufflesecurity/trufflehog) - Find & Verify Leaked Secrets

### AI Red Team Repos

- [Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox) - ML Evasion, Poisoning & Extraction Attacks
- [agent-scan (formerly mcp-scan)](https://github.com/snyk/agent-scan) - Scan MCP Servers & Agents for Tool Poisoning
- [AI Goat](https://github.com/orcasecurity-research/AIGoat) - Vulnerable AI Infrastructure Lab
- [Damn Vulnerable LLM Agent](https://github.com/ReversecLabs/damn-vulnerable-llm-agent) - Vulnerable ReAct Agent Lab
- [garak](https://github.com/NVIDIA/garak) - LLM Vulnerability Scanner
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - Programmable LLM Guardrails
- [promptfoo](https://github.com/promptfoo/promptfoo) - LLM Evals & Red Teaming CLI
- [PyRIT](https://github.com/microsoft/PyRIT) - Microsoft's AI Red Teaming Framework

### Compliance & Cloud Posture

- [cmmc-advisor](https://github.com/LV-262/cmmc-advisor) - CMMC 2.0 Advisor (Claude Code Skill)
- [cmmc-level-1-compliance](https://github.com/TEKIMAX/cmmc-level-1-compliance) - Open-Source CMMC L1 Platform
- [cmmc-tracker](https://github.com/jonathancaruso/cmmc-tracker) - CMMC Artifact & Evidence Tracker
- [JAKTOOL/cmmc](https://github.com/JAKTOOL/cmmc) - NIST 800-171 Compliance Manager
- [Prowler](https://github.com/prowler-cloud/prowler) - Open-Source Multi-Cloud Security Scanner

### AI & Claude

- [ai-sec-resources](https://github.com/Arcanum-Sec/ai-sec-resources) - Arcanum AI Security Resources
- [auto-parts-ctf](https://github.com/arcanum-ai/auto-parts-ctf) - Arcanum AI Security CTF
- [Claude Code](https://github.com/anthropics/claude-code/issues/27801) - Cowork Workspace Bug (#27801)
- [Everything Claude Code](https://github.com/affaan-m/everything-claude-code)
- [Lokka](https://github.com/merill/lokka) - MCP Server for Microsoft Graph & Azure (Merill Fernando)
- [Microsoft Graph Skill](https://github.com/merill/msgraph) - Graph API Skill for AI Agents (Merill Fernando)
- [Stanford CME295 VIP Cheatsheet (afshinea)](https://github.com/afshinea/stanford-cme-295-transformers-large-language-models)

### Datasets & References

- [11Syscalls](https://github.com/ikermit/11Syscalls) - Windows 11 Syscall Table
- [brawl-public-game-001](https://github.com/mitre/brawl-public-game-001) - Adversary Emulation Log Data
- [domain_generation_algorithms](https://github.com/baderj/domain_generation_algorithms) - Known DGA List
- [Event-Forwarding-Guidance](https://github.com/nsacyber/Event-Forwarding-Guidance) - Windows Event Log Collection
- [MBC](https://github.com/MBCProject/mbc-markdown/blob/main/anti-behavioral-analysis/sandbox-detection.md) - Anti-Behavioral Analysis: Sandbox Detection
- [mordor (now OTRF Security-Datasets)](https://github.com/hunters-forge/mordor) - Attack Replay Logs
- [proxylist](https://github.com/fate0/proxylist) - Free Open Proxy Server List
- [RMM-Catalogue](https://github.com/0x706972686f/RMM-Catalogue) - Known Remote Management Tools
- [rung/threat-matrix-cicd](https://github.com/rung/threat-matrix-cicd) - Threat matrix for CI/CD Pipeline
- [windows-syscalls](https://github.com/j00ru/windows-syscalls) - Windows Syscall Tables

### Awesome Lists

- [awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) - AI Security Resource List
- [awesome-cloud-security](https://github.com/4ndersonLin/awesome-cloud-security) - Cloud Security Resource List
- [awesome-entra](https://github.com/merill/awesome-entra) - Microsoft Entra Resource List (Merill Fernando)
- [awesome-graphps](https://github.com/merill/awesome-graphps) - Microsoft Graph PowerShell Resource List (Merill Fernando)
- [Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) - Repo List for Security Researchers
- [awesome-llm-security](https://github.com/corca-ai/awesome-llm-security) - LLM Security Tools & Papers
- [awesome-pentest](https://github.com/0sm0s1z/awesome-pentest) - Pentesting Resource Collection
- [awesome-security](https://github.com/sbilly/awesome-security) - Security Software & Resource List
- [awesome-sysadmin](https://github.com/kahun/awesome-sysadmin) - Open Source Sysadmin Resources
- [awesome-threat-detection](https://github.com/0x4D31/awesome-threat-detection) - Threat Detection & Hunting List
- [awesome-web-security](https://github.com/qazbnm456/awesome-web-security) - Web Security Learning Resources
- [detection-and-response-pipeline](https://github.com/0x4D31/detection-and-response-pipeline) - Suggested D&R Tools
- [InfoSec-Black-Friday](https://github.com/0x90n/InfoSec-Black-Friday) - InfoSec Tool Deals List

[Back to top](#contents)

## Courses & Training

### Hacking Labs & CTFs

- [CTFtime.org](https://ctftime.org/) - CTF Stats, Calendar & Writeups
- [Gandalf by Lakera](https://gandalf.lakera.ai/) - Prompt Injection Game
- [Hack The Box](https://www.hackthebox.com/) - Penetration Testing Labs
- [Hacker101](https://www.hacker101.com/) - CTF
- [OverTheWire](https://overthewire.org/wargames/) - Simple, progressive CTF challenges
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) - Intentionally Insecure Web App
- [PentesterLab](https://pentesterlab.com/) - Web Pentest Exercises
- [PortSwigger](https://portswigger.net/web-security/all-topics) - Web Security Academy (All Topics)
- [pwn.college](https://pwn.college/) - Hacking Courses
- [pwnable.kr](https://pwnable.kr/#) - War Games
- [Root Me](https://www.root-me.org/?lang=en) - Hacking and Information Security learning platform
- [TryHackMe](https://tryhackme.com/) - Guided Hacking Labs
- [VulnHub](https://www.vulnhub.com/) - VMs vulnerable by Design

### Cloud Security Labs

- [Altered Security Azure Labs](https://www.alteredsecurity.com/azureadlab) - Azure AD/Entra Red Team Bootcamp (CARTP)
- [Cloud Security Championship](https://cloudsecuritychampionship.com/) - Monthly Cloud CTF Challenges (Wiz)
- [CloudFoxable](https://cloudfoxable.bishopfox.com/) - AWS Attack-Path CTF (Bishop Fox)
- [Cybr](https://cybr.com/) - Cloud Security Courses & Labs
- [flAWS](http://flaws.cloud/) - AWS Misconfiguration Challenges
- [flAWS2](http://flaws2.cloud/) - AWS Attacker & Defender Paths
- [Kubernetes Goat](https://madhuakula.com/kubernetes-goat/) - Vulnerable-by-Design K8s Cluster
- [Pwned Labs](https://pwnedlabs.io/) - AWS, Azure & GCP Hands-On Labs
- [Thunder CTF](https://thunder-ctf.cloud/) - GCP Security Challenges

### AI & LLM Courses

- [AI Red Teaming Roadmap](https://roadmap.sh/ai-red-teaming)
- [Anthropic Courses](https://anthropic.skilljar.com/)
- [Chain-of-Thought Prompting](https://www.promptingguide.ai/techniques/cot)
- [DeepLearning.AI Pro: Become an AI Builder](https://learn.deeplearning.ai/membership)
- [Generative AI with LLMs Certification](https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-associate/?ncid=ref-inpa-200949)
- [OWASP Top 10 LLM and GenAI](https://learn.snyk.io/learning-paths/owasp-top-10-llm/)
- [TCM Security Academy](https://academy.tcm-sec.com/) - AI 100: Fundamentals course

### AI Security Labs & Reading

- [AI Security Lab Hub](https://arcanum-sec.github.io/ai-sec-resources/) - Training Environment
- [Crucible](https://crucible.dreadnode.io/) - AI Red Teaming CTF Challenges (Dreadnode)
- [Executive Offense #11](https://executiveoffense.beehiiv.com/p/executive-offense-issue-10-start-hacking-llms) - Start Hacking LLMs
- [Gray Swan Arena](https://app.grayswan.ai/arena) - AI Jailbreak Competitions
- [HackAPrompt](https://www.hackaprompt.com/) - Prompt Hacking Competition & Challenges
- [Immersive Labs Prompt Injection](https://prompting.ai.immersivelabs.com/) - Progressive Prompt Injection Levels
- [LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) - OWASP Gen AI Security Project
- [PortSwigger LLM Attacks](https://portswigger.net/web-security/llm-attacks) - Free Web LLM Attack Labs
- [Prompt Airlines](https://promptairlines.com/) - Jailbreak an AI Customer Service Bot (Wiz)
- [Sec-Context](https://arcanum-sec.github.io/sec-context/) - AI Code Security Anti-Patterns

### Compliance Training

- [Securiti](https://education.securiti.ai/certifications/ai-governance/introduction-ai-governance/overview-introduction-to-ai-governance-certification/) - AI Governance Certification Overview

[Back to top](#contents)

## Community

### Microsoft & Intune

- [Entra Tech Community](https://techcommunity.microsoft.com/category/microsoft-entra) - Microsoft Entra blog and discussion space
- [Intune Tech Community](https://techcommunity.microsoft.com/category/microsoft-intune) - Microsoft Intune blog and discussion space
- [MacAdmins](https://www.macadmins.org/) - Apple admin community (Slack)
- [Microsoft Q&A](https://learn.microsoft.com/en-us/answers/) - Microsoft technical Q&A answered by staff and MVPs
- [Microsoft Tech Community](https://techcommunity.microsoft.com/) - Official Microsoft forums, blogs and events
- [r/AZURE](https://www.reddit.com/r/AZURE/) - Azure and Entra subreddit
- [r/Intune](https://www.reddit.com/r/Intune/) - Intune and Autopilot subreddit
- [r/macsysadmin](https://www.reddit.com/r/macsysadmin/) - Mac admin subreddit
- [r/msp](https://www.reddit.com/r/msp/) - Managed service provider subreddit
- [r/Office365](https://www.reddit.com/r/Office365/) - Microsoft 365 admin subreddit
- [r/sysadmin](https://www.reddit.com/r/sysadmin/) - Systems administration subreddit
- [Security Tech Community](https://techcommunity.microsoft.com/category/microsoft-security) - Microsoft Defender, Sentinel and Purview discussions
- [Spiceworks Community](https://community.spiceworks.com/) - IT pro forums
- [WinAdmins](https://winadmins.io/) - Windows and Intune admin community (Discord)

### Cloudflare

- [Cloudflare Community](https://community.cloudflare.com/) - Official Cloudflare forum
- [Cloudflare Discord](https://discord.cloudflare.com/) - Cloudflare developers Discord
- [r/CloudFlare](https://www.reddit.com/r/CloudFlare/) - Cloudflare subreddit

### Cybersecurity

- [r/AskNetsec](https://www.reddit.com/r/AskNetsec/) - Security Q&A subreddit
- [r/blueteamsec](https://www.reddit.com/r/blueteamsec/) - Defensive security and threat intel
- [r/cybersecurity](https://www.reddit.com/r/cybersecurity/) - General cybersecurity subreddit
- [r/netsec](https://www.reddit.com/r/netsec/) - Technical security news and research
- [r/purpleteamsec](https://www.reddit.com/r/purpleteamsec/) - Purple team, detection and emulation
- [r/redteamsec](https://www.reddit.com/r/redteamsec/) - Offensive security and red teaming

### CMMC, NIST & GRC

- [r/CMMC](https://www.reddit.com/r/CMMC/) - CMMC and DFARS compliance subreddit
- [r/GRC](https://www.reddit.com/r/GRC/) - Governance, risk and compliance subreddit
- [r/NISTControls](https://www.reddit.com/r/NISTControls/) - NIST 800-171, 800-53 and CSF subreddit

### Wazuh

- [r/Wazuh](https://www.reddit.com/r/Wazuh/) - Wazuh subreddit
- [Wazuh Community](https://wazuh.com/community/) - Official Wazuh community hub
- [Wazuh GitHub Discussions](https://github.com/wazuh/wazuh/discussions) - Q&A on the Wazuh GitHub repo
- [Wazuh Google Group](https://groups.google.com/g/wazuh) - Wazuh mailing list
- [Wazuh Slack](https://wazuh.com/community/join-us-on-slack/) - Join the Wazuh community Slack

[Back to top](#contents)

## News

### IT & Security News

- [BleepingComputer](https://www.bleepingcomputer.com/)
- [EFF](https://www.eff.org/) - Electronic Frontier Foundation
- [Federal News Network](https://federalnewsnetwork.com/)
- [Packet Storm](https://packetstormsecurity.com/)
- [The Hacker News](https://thehackernews.com/) - Cybersecurity News
- [The Register](https://www.theregister.com/) - Tech & Security News
- [Toms Hardware](https://www.tomshardware.com/)
- [Windows Central](https://www.windowscentral.com/)
- [ZDNet Security](https://www.zdnet.com/topic/security/) - Cybersecurity News

[Back to top](#contents)

## Other Useful Tools

### Dev & Data Utilities

- [CyberChef](https://gchq.github.io/CyberChef/) - Cyber Swiss Army Knife
- [grep.app](https://grep.app/) - Source Code Search Engine
- [JSFiddle](https://jsfiddle.net/) - Online Web IDE & Code Playground
- [JSON Crack](https://jsoncrack.com/editor) - JSON Visualizer
- [MDN Web Docs](https://developer.mozilla.org/en-US/)
- [searchcode](https://searchcode.com/) - Source Code Search Engine
- [Stack Overflow](https://stackoverflow.com/)
- [WolframAlpha](https://www.wolframalpha.com/) - Math Swiss Army Knife

### Lookups & Lifecycle

- [Downdetector](https://downdetector.com/) - Service Outage Stats
- [endoflife.date](https://endoflife.date/) - List of EOL software versions
- [Open Source Security Index](https://opensourcesecurityindex.io/) - Top OSS Security Projects

[Back to top](#contents)
