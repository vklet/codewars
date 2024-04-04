


def count_ips():

    def ip_to_list(ip:str) -> list[int]:
        return list(map(int, ip.split('.')))

    ip1 = "122.201.114.207"
    ip2 = "124.235.84.228"

    #35774997 
    
    x1 = ip_to_list(ip1)
    x2 = ip_to_list(ip2)

    diff = [b - a for a, b in zip(x1, x2)]
    
    out = [256**i*x for i, x in enumerate(diff[::-1])]


    print(sum(out))

count_ips()
