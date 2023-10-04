import dns
import dns.resolver

result = dns.resolver.resolve('hackertouch.com', 'A')
for ipval in result:
    print('IP', ipval.to_text)

"""
IP <bound method A.to_text of <DNS IN A rdata: 165.84.218.158>>
"""