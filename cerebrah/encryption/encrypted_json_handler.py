import encryptor
import json

class json_handler:

    def __init__(self, key_dir=''):
        self.encryptor = encryptor.Encryptor(key_dir)

    def read(self, file_path):
        json_data = self.parse_json(file_path)
        decrypted_json = self.decrypt_json(json_data)
        return decrypted_json

    def write(self, file_path, json_data):
        encrypted_json = self.encrypt_json(json_data)
        self.write_json(encrypted_json, file_path)

    def parse_json(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    def encrypt_json(self, json_data):
        json_data = str(json_data)
        encrypted_data = self.encryptor.encrypt(json_data, self.encryptor.key)
        return encrypted_data

    def decrypt_json(self, json_data):
        decrypted_data = self.encryptor.decrypt(json_data, self.encryptor.key)
        return decrypted_data

    def convert_to_json(self, file):
        return json.dumps(file)

    def convert_to_dict(self, file):
        conv_json = json.loads(file)
        return conv_json

    def write_json(self, data, file_path='./data.json'):
        with open(output, 'w') as json_file:
            json.dump(data, json_file, indent=2)
