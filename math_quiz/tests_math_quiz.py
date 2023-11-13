import unittest
from math_quiz import gen_rand_int, get_operator, calculate


class TestMathGame(unittest.TestCase):

    def test_gen_rand_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for x in range(1000):  # Test a large number of random values
            rand_num = gen_rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_operator(self):
        #Test if the operator returned is random. test for randomness for '+' operand.
        #start counter for how many times the operand was generated
        s = 0
        for x in range(1000): #generate the random operand for a large range
            rand_op = get_operator()
            #inc s whenever the operand generated by the func is '+'.
            if rand_op=='+':
                s += 1
        #by law of randomness, prob of s must be less than or equal to 1000/3
        self.assertTrue((s/1000) <= (1000/3))

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (-1, -2, '+', '-1-2', -3),
                (-1, 6, '+', '-1+6', 5),
                (6, -2, '-', '6-(-2)', 8),
                (-1, -2, '-', '-1-(-2)', 1),
                (6.6, -6, '-', '6.6-6', 12.6),
                (6.1, -2.2, '*', '6.1*-2.2', -13.42),
                (-3.3, 2, '*', '-3.3*2', -6.6)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                actual_problem,actual_answer = calculate(num1,num2,operator)
                self.assertTrue(actual_answer==expected_answer)

if __name__ == "__main__":
    unittest.main()