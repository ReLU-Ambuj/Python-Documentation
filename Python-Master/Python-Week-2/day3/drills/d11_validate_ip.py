# Drill 11: Validate IP Address (IPv4 & IPv6)

def valid_ip_address(queryIP):
    if "." in queryIP:
        parts = queryIP.split(".")
        if len(parts) != 4: return "Neither"
        for p in parts:
            if not p.isdigit() or not 0 <= int(p) <= 255: return "Neither"
            if len(p) > 1 and p[0] == "0": return "Neither"
        return "IPv4"
        
    elif ":" in queryIP:
        parts = queryIP.split(":")
        if len(parts) != 8: return "Neither"
        hexdigits = "0123456789abcdefABCDEF"
        for p in parts:
            if not (1 <= len(p) <= 4): return "Neither"
            if not all(c in hexdigits for c in p): return "Neither"
        return "IPv6"
        
    return "Neither"

if __name__ == "__main__":
    print(valid_ip_address("172.16.254.1")) # Expected: "IPv4"
