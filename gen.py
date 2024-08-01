import hashlib

def generate_serial_code(date, time, seat, secret_key):
    data = date + time + seat
    hash_object = hashlib.sha256((data + secret_key).encode())
    hex_dig = hash_object.hexdigest()
    serial_code = hex_dig[:6]
    return serial_code

def validate_serial_code(date, time, seat, serial_code, secret_key):
    data = date + time + seat
    hash_object = hashlib.sha256((data + secret_key).encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig[:6] == serial_code
