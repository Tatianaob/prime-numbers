import unittest

from primes import get_primes_up_to_250

class TestGetPrimes(unittest.TestCase):
    # test if all primes up to 250 are in the list
    def test_prime_lists(self):
        expected_primes =  [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 
            61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 
            137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 
            199, 211, 223, 227, 229, 233, 239, 241
        ]
        self.assertEqual(get_primes_up_to_250(), expected_primes)
    
    #Tests if certain primes are in the list
    def test_prime_membership(self):
        primes = get_primes_up_to_250()
        self.assertIn(2, primes)
        self.assertIn(3, primes)
        self.assertIn(7, primes)
        self.assertIn(241, primes)

    #test if no prime numbers are not in the list
    def test_non_primes(self):
        primes = get_primes_up_to_250()
        self.assertNotIn(4, primes)
        self.assertNotIn(9, primes)
        self.assertNotIn(10, primes)
        self.assertNotIn(240, primes)

    # test a total of 53 prime nums up from 2 -250
    def test_length_of_list(self):
        primes = get_primes_up_to_250()
        self.assertEqual(len(primes), 53)
    

if __name__ == "__main__":
    unittest.main()