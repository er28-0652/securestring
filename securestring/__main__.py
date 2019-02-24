import argparse
from securestring import securestring

def main():
    p = argparse.ArgumentParser(description='SecureString wrapper by Python')
    sub_p = p.add_subparsers()

    # encrypt
    enc_p = sub_p.add_parser('encrypt', help='see `encrypt -h`')
    enc_p.add_argument(dest='plain_text', help='plain text to encrypt')
    enc_p.set_defaults(handler=securestring.encrypt)

    # decrypt
    dec_p = sub_p.add_parser('decrypt', help='see `decrypt -h`')
    dec_p.add_argument(dest='encrypted_text', help='encrypted text to decrypt')
    dec_p.set_defaults(handler=securestring.decrypt)

    args = p.parse_args()

    args.handler(args)

if __name__ == '__main__':
    main()