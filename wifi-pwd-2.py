import subprocess

data = (
    subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    .decode("utf-8")
    .split("\n")
)
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

with open('wifi-passwords.txt', 'w') as f:

    for i in profiles:
        results = (
            subprocess
            .check_output(["netsh", "wlan", "show", "profile", i, "key=clear"])
            .decode("utf-8")
            .split("\n")
        )
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        f.write("{:<30}|  {:<}".format(i, results[0]))
        f.write('\n')
        try:
            print("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}|  {:<}".format(i, ""))
        
