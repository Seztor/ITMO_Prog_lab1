import unittest
from src.lab1_2.caesar import encrypt_caesar,decrypt_caesar
from src.lab1_2.rsa import is_prime, gcd, multiplicative_inverse
from src.lab1_2.vigenre import encrypt_vigenere, decrypt_vigenere


class CalculatorTestCase(unittest.TestCase):

    def tests_caesar(self):
        self.assertEqual(encrypt_caesar('PYTHON'), 'SBWKRQ')
        self.assertEqual(encrypt_caesar('python'), 'sbwkrq')
        self.assertEqual(encrypt_caesar('Python3.6'), 'Sbwkrq3.6')
        self.assertEqual(encrypt_caesar('PaVeL'), 'SdYhO')
        self.assertEqual(encrypt_caesar(''),'')

        self.assertEqual(decrypt_caesar('SBWKRQ'), 'PYTHON')
        self.assertEqual(decrypt_caesar('sbwkrq'), 'python')
        self.assertEqual(decrypt_caesar('Sbwkrq3.6'), 'Python3.6')
        self.assertEqual(decrypt_caesar('xXx_GovoroV_xXx'), 'uUu_DlslolS_uUu')
        self.assertEqual(decrypt_caesar(''), '')


    def tests_vigenre(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), 'PYTHON')
        self.assertEqual(encrypt_vigenere("python", "a"), 'python')
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), 'LXFOPVEFRNHR')
        self.assertEqual(encrypt_vigenere("GOVOROV", "PAVEL"), 'VOQSCDV')

        self.assertEqual(decrypt_vigenere("PYTHON", "A"), 'PYTHON')
        self.assertEqual(decrypt_vigenere("python", "a"), 'python')
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), 'ATTACKATDAWN')
        self.assertEqual(decrypt_vigenere("LOOKATME", "PLEASE"), 'WDKKIPXT')


    def tests_rsa(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(15), False)
        self.assertEqual(is_prime(179), True)

        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)
        self.assertEqual(gcd(43442352423424, 414451344153542), 2)

        self.assertEqual(multiplicative_inverse(7, 40), 23)
        self.assertEqual(multiplicative_inverse(2143, 66435), 33202)
        self.assertEqual(multiplicative_inverse(25, 72), 49)
        self.assertEqual(multiplicative_inverse(254353464135341,365746736253443254252), 39384089349541956393)
