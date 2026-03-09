# Drill 13: Defanging an IP Address

def defang_ip_addr(address):
    # Method 1: replace (O(N) time and space)
    return address.replace(".", "[.]")
    
    # Method 2: iterative build (O(N) time and space)
    # res = []
    # for char in address:
    #     if char == '.':
    #         res.append("[.]")
    #     else:
    #         res.append(char)
    # return "".join(res)

if __name__ == "__main__":
    print(defang_ip_addr("1.1.1.1")) # Expected: "1[.]1[.]1[.]1"
