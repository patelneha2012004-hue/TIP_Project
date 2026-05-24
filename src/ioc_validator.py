import ipaddress

def validate_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)

        if ip_obj.is_private:
            return False

        return True

    except:
        return False
