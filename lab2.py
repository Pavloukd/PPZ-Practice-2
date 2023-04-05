import platform


def main():
    print(palindrome('око дід крамниця'))
    print(validate_ip('192.0.100.0'))
    print(get_os())


def palindrome(text):
    words = text.split()
    palindromes = [word for word in words if word == word[::-1]]

    return palindromes


def validate_ip(ip_address):
    chunks = ip_address.split('.')
    if len(chunks) > 4:
        return False

    for chunk in chunks:
        try:
            if int(chunk) > 255:
                return False
        except:
            return False

    return True


def get_os():
    return platform.system()


if __name__ == '__main__':
    main()
