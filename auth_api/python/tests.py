import unittest
from methods import Token, Restricted


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()

    def test_generate_token(self):
        self.assertEqual('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZG1pbiI6InNlY3JldCJ9.mpOWaiHGnJ-7RX9K3IhEsNFVxT3tIJUQLhEjzz4vhuo', self.convert.generate_token('admin', 'secret'))
        self.assertEqual('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJub2FkbWluIjoibm9Qb3czciJ9.NRIMXo9raefsgrJuGsAgjRIGJNVg92bvW3sXbZoTEp8', self.convert.generate_token('noadmin', 'noPow3r'))
        self.assertEqual('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJib2IiOiJ0aGlzSXNOb3RBUGFzc3dvcmRCb2IifQ.hYEbsn-66EsG7qEOUmK3tLhXc7Gj-Pv5AKnOToM2RuE', self.convert.generate_token('bob', 'thisIsNotAPasswordBob'))

    def test_access_data(self):
        self.assertEqual('You are under protected data', self.validate.access_data('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhZG1pbiI6InNlY3JldCJ9.mpOWaiHGnJ-7RX9K3IhEsNFVxT3tIJUQLhEjzz4vhuo'))
        self.assertEqual('You are under protected data', self.validate.access_data('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJub2FkbWluIjoibm9Qb3czciJ9.NRIMXo9raefsgrJuGsAgjRIGJNVg92bvW3sXbZoTEp8'))
        self.assertEqual('You are under protected data', self.validate.access_data('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJib2IiOiJ0aGlzSXNOb3RBUGFzc3dvcmRCb2IifQ.hYEbsn-66EsG7qEOUmK3tLhXc7Gj-Pv5AKnOToM2RuE'))

if __name__ == '__main__':
    unittest.main()
