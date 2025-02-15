from prime_utils import is_prime, generate_primes

def test_is_prime_true():
    assert is_prime(2) is True
    assert is_prime(17) is True

def test_is_prime_false():
    assert is_prime(4) is False
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False

def test_generate_primes():
    assert generate_primes(10) == [2, 3, 5, 7]
    assert generate_primes(0) == []
    assert generate_primes(1) == []
    assert generate_primes(2) == [2]
    assert generate_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
