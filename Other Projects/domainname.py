import whois

domain = input("Enter a domain name: ")
domain_info = whois.whois(domain)
for key, value in domain_info.items():
    if value:
        print(f"{key}: {value}")