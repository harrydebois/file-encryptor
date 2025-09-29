from cryptography.fernet import Fernet
import argparse


def generate_key(path):
    key = Fernet.generate_key()
    with open(path, 'wb') as f:
        f.write(key)
    print(f"Key saved to {path}")


def encrypt(key_path, input_file, output_file):
    with open(key_path, 'rb') as f:
        key = f.read()
    fernet = Fernet(key)
    with open(input_file, 'rb') as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(output_file, 'wb') as f:
        f.write(encrypted)
    print(f"Encrypted file saved to {output_file}")


def decrypt(key_path, input_file, output_file):
    with open(key_path, 'rb') as f:
        key = f.read()
    fernet = Fernet(key)
    with open(input_file, 'rb') as f:
        data = f.read()
    decrypted = fernet.decrypt(data)
    with open(output_file, 'wb') as f:
        f.write(decrypted)
    print(f"Decrypted file saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Encrypt or decrypt files using Fernet symmetric encryption')
    subparsers = parser.add_subparsers(dest='command')
    gen_parser = subparsers.add_parser('generate-key')
    gen_parser.add_argument('key_path')
    enc_parser = subparsers.add_parser('encrypt')
    enc_parser.add_argument('key_path')
    enc_parser.add_argument('input_file')
    enc_parser.add_argument('output_file')
    dec_parser = subparsers.add_parser('decrypt')
    dec_parser.add_argument('key_path')
    dec_parser.add_argument('input_file')
    dec_parser.add_argument('output_file')
    args = parser.parse_args()
    if args.command == 'generate-key':
        generate_key(args.key_path)
    elif args.command == 'encrypt':
        encrypt(args.key_path, args.input_file, args.output_file)
    elif args.command == 'decrypt':
        decrypt(args.key_path, args.input_file, args.output_file)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
