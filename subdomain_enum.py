import requests
import json
import socket
import concurrent.futures

#API call from crt.sh for subdomain enum
def get_subdomain_from_crtsh(domain_name):
    url = f"https://crt.sh/?q=%25.{domain_name}&output=json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            subdomains = set()
            for entry in json_data:
                common_name = entry['name_value']
                subdomains.update(common_name.split('\n'))
            return list(subdomains)
        else:
            print(f"Failed to get subdomains from crt.sh (status code: {response.status_code})")
            return []

    except Exception as e:
        print(f"Error occured while fetching subdomains: {e}")
        return []


# Perform DNS Lookup to check if subdomain exists
def check_subdomain_dns(subdomain):
    try:
        socket.gethostbyname(subdomain)
        return True

    except socket.gaierror:
        return False

# Perform a single single domain scan
def scan_subdomain(subdomain):
    url = f"https://{subdomain}"
    try:
        # Making HTTP request with timeout
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f'[+] {url} is reachable'
        else:
            return f'[-] {url} returned {response.status_code}'
    except requests.ConnectionError:
        return f'[-] {url} - Connection Failed'
    except Exception as e:
        return f'[-] {url} - Error: {str(e)}'
    

# Main function to handle scanning of subdomains
def subdomain_scanner(domain_name, sub_domains):
    print("--------- Scanner started ----------")

    # Filter out only valid subdomains by checking DNS
    valid_subdomains = [sub for sub in sub_domains if check_subdomain_dns(sub)]

    print(f"Found {len(valid_subdomains)} valid subdomains with DNS.")

    # ThreadPoolExecutor to speed up the scanning process
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(scan_subdomain, subdomain) for subdomain in valid_subdomains]

        for future in concurrent.futures.as_completed(futures):
            print(future.result())


# Output result to a file
def save_result_file(domain_name, results):
    with open(f'{domain_name}_subdomains_scan.txt', 'w') as file:
        for result in results:
            file.write(result + '\n')

if __name__ == '__main__':
    dom_name = input("Enter the Domain Name: ")

    #Fetch subdomains from crt.sh
    sub_domains = get_subdomain_from_crtsh(dom_name)
     
    if sub_domains:
        print(f"Found {len(sub_domains)} subdomains.")
        subdomain_scanner(dom_name, sub_domains)

    else:
        print("No subdomains found.")