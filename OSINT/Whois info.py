import whois

whois_info = whois.whois("hackertouch.com")

print(whois_info)

print("Creation date")

print(whois_info["creation_date"])


"""
{
  "domain_name": "HACKERTOUCH.COM",
  "registrar": "PDR Ltd. d/b/a PublicDomainRegistry.com",
  "whois_server": "whois.publicdomainregistry.com",
  "referral_url": null,
  "updated_date": [
    "2023-09-22 07:47:11",
    "2023-09-22 07:47:12"
  ],
  "creation_date": "2020-04-18 14:09:04",
  "expiration_date": "2024-04-18 14:09:04",
  "name_servers": [
    "NS1.NEXCESS.NET",
    "NS2.NEXCESS.NET",
    "NS3.NEXCESS.NET",
    "NS4.NEXCESS.NET",
    "ns1.nexcess.net",
    "ns2.nexcess.net",
    "ns3.nexcess.net",
    "ns4.nexcess.net"
  ],
  "status": "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",      
  "emails": [
    "abuse-contact@publicdomainregistry.com",
    "amitarora5423@gmail.com"
  ],
  "dnssec": [
    "unsigned",
    "Unsigned"
  ],
  "name": "AMIT ARORA",
  "org": "BRIGHT GUJARAT",
  "address": "201/A, UPASNA APRTMENT, NEAR GATTU SCHOOL GIDC COLONY",
  "city": "ANKLESHWAR",
  "state": "GUJARAT",
  "registrant_postal_code": "393002",
  "country": "IN"
}
Creation date
2020-04-18 14:09:04
"""