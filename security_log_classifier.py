filename = input("Enter log filename (or press Enter for 'logins.txt'): ").strip()
if not filename:
    filename = "logins.txt"

with open(filename) as f:
    lines = f.readlines()

print(f"Loaded {len(lines)} login records.\n")

users = []
ips = []
results = []

for line in lines:
    parts = line.strip().split()
    if len(parts) == 3:
        users.append(parts[0])
        ips.append(parts[1])
        results.append(parts[2])

successful_logins = 0
failed_logins = 0

for result in results:
    if result == "SUCCESS":
        successful_logins += 1
    else:
        failed_logins += 1

internal_ips = 0
external_ips = 0

for ip in ips:
    if ip.startswith("10.") or ip.startswith("192.168."):
        internal_ips += 1
    else:
        external_ips += 1

failed_attempts = {}

for i in range(len(users)):
    if results[i] == "FAILURE":
        user_ip_combo = (users[i], ips[i])
        if user_ip_combo in failed_attempts:
            failed_attempts[user_ip_combo] += 1
        else:
            failed_attempts[user_ip_combo] = 1

output_lines = []
output_lines.append("=" * 40)
output_lines.append("SECURITY LOG SUMMARY REPORT")
output_lines.append("=" * 40)
output_lines.append(f"Total login attempts: {len(lines)}")
output_lines.append(f"Successful logins: {successful_logins}")
output_lines.append(f"Failed logins: {failed_logins}")
output_lines.append(f"Internal IPs: {internal_ips}")
output_lines.append(f"External IPs: {external_ips}")
output_lines.append("=" * 40)

brute_force_found = False

for (user, ip), count in failed_attempts.items():
    if count >= 3:
        if not brute_force_found:
            output_lines.append("\nPossible brute-force alert:")
            brute_force_found = True
        output_lines.append(f"User '{user}' had {count} failed logins from IP {ip}")

if not brute_force_found:
    output_lines.append("\nNo brute-force patterns detected.")

output_lines.append("=" * 40)
output_lines.append("Analysis complete.")

for line in output_lines:
    print(line)

with open("summary.txt", "w") as f:
    for line in output_lines:
        f.write(line + "\n")

print(f"\nReport also saved to 'summary.txt'")