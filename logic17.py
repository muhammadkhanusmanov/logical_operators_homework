def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    d1 = a//10000
    d2 = (a//1000)//10
    d3 = (a%1000)//100
    d4 = (a%100)//10
    d5 = a%10
    return (d1>d2 and d2>d3 and d3>d4 and d4>d5)