import requests

url = input("[+] ENTER THE URL ! : ").rstrip('/')
wordlist = open("/home/radon/Downloads/common.txt", "r").read().splitlines()
print("[+] WAIT A MOMENT..........")
print("-" * 60)

for word in wordlist:
	full_url = url + "/" + word
	try:
		r = requests.get(full_url, timeout=5)
		if r.status_code != 404:
	   	   print(f"[FOUND] [{r.status_code}] :  {full_url}")
		with open("result.txt", "a") as f:
			f.write(full_url + "\n")
	except requests.exceptions.RequestException:
            print("[-] THERE IS AN ISSUE, SKIP IT !")
            continue
