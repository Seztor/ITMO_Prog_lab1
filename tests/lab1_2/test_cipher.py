import unittest
from src.lab1_2.caesar import encrypt_caesar,decrypt_caesar
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


    def tests_rsa(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), 'PYTHON')
        self.assertEqual(encrypt_vigenere("python", "a"), 'python')
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), 'LXFOPVEFRNHR')
        self.assertEqual(encrypt_vigenere("GOVOROV", "PAVEL"), 'VOQSCDV')

        self.assertEqual(decrypt_vigenere("PYTHON", "A"), 'PYTHON')
        self.assertEqual(decrypt_vigenere("python", "a"), 'python')
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), 'ATTACKATDAWN')
        self.assertEqual(decrypt_vigenere("LOOKATME", "PLEASE"), 'WDKKIPXT')

