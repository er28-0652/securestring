import unittest
from securestring import securestring

TESTS = [
    'tesuya',
    'testtest'
]

class TestSecureString(unittest.TestCase):
    def test_encrypt_and_decrypt(self):
        for test in TESTS:
            enc_test = securestring.encrypt(test)
            dec_test = securestring.decrypt(enc_test)
            self.assertEqual(dec_test, test)