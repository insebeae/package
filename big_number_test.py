import unittest
from allow.zt.big_number_1 import Sum_array


class TestSumConfigInterface(unittest.TestCase):
    def setUp(self):
        self.array1 = [1, 2, 3, 9, 6, 5, 3, 1, 5, 9, 8, 4, 1, 0, 2, 3, 6, 9, 8, 5, 6, 4, 1, 5, 6, 3, 2, 5, 6, 8, 5, 4,
                       8, 2, 3, 6, 9,
                       6, 9, 5, 1, 0, 3, 9, 8, 7, 9, 6, 5, 6, 2, 3, 6, 9, 8]
        self.array2 = [4, 5, 5, 9, 6, 6, 6, 2, 9, 8, 4, 2, 3, 1, 6, 9, 0, 8, 6, 0, 4, 1, 5, 9, 7, 8, 4, 1, 1, 9, 6, 5,
                       8, 4, 3, 6, 5,
                       9, 1, 4, 6, 9, 8, 7, 1, 5, 3, 3]
        self.array3 = [1, 2, 3, 9, 6, 5, 3, 6, 1, 5, 8, 0, 7, 6, 5, 3, 5, 4, 0, 8, 8, 1, 0, 6, 4, 9, 2, 9, 8, 4, 5, 2,
                       6, 6, 4, 8, 9, 3, 5, 3, 5, 4, 0, 5, 7, 9, 4, 3, 5, 4, 9, 5, 2, 3, 1]

    def test_sum_add(self):
        fsm_instance = Sum_array()
        res = fsm_instance.sum_add(self.array1, self.array2)
        self.assertEqual(res, self.array3)

def suite():
    suite = unittest.TestSuite()
    # 往此添加需要测试的方法testgetSize()
    suite.addTest(TestSumConfigInterface("test_add"))
    return suite


if __name__ == "__main__":
    # 在主函数中调用全局方法suite.
    unittest.main(defaultTest='suite')
