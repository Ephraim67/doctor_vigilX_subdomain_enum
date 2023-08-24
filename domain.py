import requests

def subdmain_scanner(domain_name, sub_domains):
    print("--------Scanner Started---------")
    print("---URL after scanning subdomains---")

    for subdomain in sub_domains:
        url = f"https://{subdomain}.{domain_name}"

        try:
            requests.get(url)

            print(f'[+] {url}')

        except:
            requests.ConnectionError
            pass

if __name__ == '__main__':
    dom_name = input("Enter the Domain Name: ")

    with open('subdomains_names.txt', 'r') as file:

        name = file.read()

        sub_dom = name.splitlines()

        subdmain_scanner(dom_name, sub_dom)