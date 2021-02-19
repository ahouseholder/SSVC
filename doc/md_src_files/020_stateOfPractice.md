

# Current state of practice

**Vulnerability management** is a term of art for security practitioners, used to include “the discovery, analysis, and handling of new or reported security vulnerabilities in information systems \[and\] the detection of and response to known vulnerabilities in order to prevent them from being exploited” [@csirtservices_v2]. Prioritization of organizational and analyst resources is an important precursor to vulnerability analysis, handling, and response. The general problem is: given limited resources, which vulnerabilities should be processed and which can be ignored for now. We approach this problem from a pragmatic, practitioner-centered angle.

The de facto standard prioritization language is CVSS [@spring2018litrev]. CVSS avoids discussing decisions and, instead, takes **technical severity** as its fundamental concept. We understand severity’s role as informing decision making about vulnerability management. The CVSS standard indicates vulnerability management decisions, and only those decisions, as what they expect CVSS scores to inform -- “CVSS provides a way to capture the principal characteristics of a vulnerability … reflecting its severity … to help organizations  properly assess and prioritize their vulnerability management processes” [@cvss_sig]. However, the standard does not provide clear advice about how CVSS scores might inform decisions.

How CVSS is used matters. Using just the base scores, which are “the intrinsic characteristics of a
vulnerability that are constant over time and across user environments,” as a stand-alone prioritization method is not recommended [@cvss_v3-1]. However, as two examples, the U.S. government [see @nist800-115, p. 7-4; @nist800-40r3, p. 4; and @bod15-01] and the global payment card industry [@pcidss_v3] both have defined such misuse as expected practice in their vulnerability management requirements. CVSS has struggled to adapt to other stakeholder contexts; various stakeholder groups have expressed dissatisfaction by making new versions of CVSS, such as medical devices [@mitre2019medical], robotics [@vilches2018towards], and industrial systems [@figueroa2020survey]. In these three examples, the modifications tend to add complexity to CVSS by adding metrics. Product vendors have varying degrees of adaptation of CVSS for development prioritization, including but not limited to [Red Hat](https://access.redhat.com/security/updates/classification), [Microsoft](https://www.microsoft.com/en-us/msrc/security-update-severity-rating-system), and [Cisco](https://tools.cisco.com/security/center/resources/security_vulnerability_policy.html#asr). The vendors codify CVSS’s recommended qualitative severity rankings in different ways, and Red Hat and Microsoft make the user interaction base metric more important. The various stakeholder re-adaptations of CVSS suggest a stakeholder-specific prioritization is important.

Unfortunately, all such re-adaptation of the basic CVSS mindset inherit its deeper issues. For example, the CVSS scoring algorithm has not been argued for transparently, and the standardization group has not justified the use of the formula either formally or empirically [@spring2018cvss]. In addition, severity should only be a part of vulnerability response prioritization [See, e.g., @farris2018vulcon]. One complaint is that a high CVSS score is not predictive of which vulnerabilities will be commonly exploited or have exploits publicly released [@allodi2012preliminary]. Studies of CVSS scoring consistency indicate that analysts do not consistently interpret the elements of a CVSSv3.0 score [@allodi2018effect], and as many adaptations of CVSS simply add additional metrics we expect they inherit such inconsistency. Analyst usability has so far been an afterthought, but we know from other areas of information security that usability is not well-served as an afterthought [@garfinkel2014usable].

Surveys of security metrics [@pendleton2016survey] and information sharing in cybersecurity [@laube2017survey] do not indicate any major efforts to conduct a wholesale rethinking of vulnerability prioritization. The surveys indicate some options for available measurements a prioritization method might consider, such as exploit availability or system attack surface.  Section 3 describes our design goals for a pragmatic prioritization methodology that can improve and build on the state of current practice.  

The target audience for SSVC is vulnerability managers of any kind.
SSVC assumes that the vulnerability manager has identified that there is a vulnerability.  
We take our definition of **vulnerability** from [@householder2020cvd]: "a set of conditions or behaviors that allows the violation of an explicit or implicit security policy."
There are a variety of problems or issues with computer systems that are important that are not vulnerabilities.
SSVC presents a risk prioritization method that might be useful or at least allied to other risk management methods for these other kinds of issues.
However, for this work we focus on decisions in the situation where there is a vulnerability and the vulnerability management team wants to decide what to do about it.