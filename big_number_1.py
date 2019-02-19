class Sum_array():
    def sum_add(self,array1, array2):
        len1 = len(array1)
        len2 = len(array2)
        # 两种情况，第一种：数组1的长度小于数组2的长度，交换数组。
        if len1 <= len2:
            # 较大和较小的数组长度
            minlen = len1
            maxlen = len2
        else:
            minlen = len2
            maxlen = len1
            array1, array2 = array2, array1

        ans = [0 for i in range(maxlen)]
        # 数组的后一部分保存较短数组的值
        ans[-minlen:] = array1
        # print ans
        for i in range(1, maxlen + 1):
            i = -i  # 从数组尾部开始算
            temp = ans[i] + array2[i]
            # 如果和大于10，则保留个位数值，并进位
            if temp >= 10:
                temp = temp - 10
                ans[i] = temp

                # 数组的第一位，进位后超出数组范围，用python的insert函数，在数组前插入数值
                if i == -maxlen:
                    ans.insert(0, 1)

                # 如果没有超出数组范围，则直接在新建的数组的前一位加1
                else:
                    ans[i - 1] = ans[i - 1] + 1
            else:
                ans[i] = temp
        return ans

if __name__ == "__main__":
    # 测试用例
    array1 = [1, 2, 3]
    array2 = [4, 5, 5, 9, 6, 6]
    # print(Sumab(array2, array1))
    array1 = [1, 2, 3, 9, 6, 5, 3, 1, 5, 9, 8, 4, 1, 0, 2, 3, 6, 9, 8, 5, 6, 4, 1, 5, 6, 3, 2, 5, 6, 8, 5, 4, 8, 2, 3, 6, 9,
          6, 9, 5, 1, 0, 3, 9, 8, 7, 9, 6, 5, 6, 2, 3, 6, 9, 8]

    array2 = [4, 5, 5, 9, 6, 6, 6, 2, 9, 8, 4, 2, 3, 1, 6, 9, 0, 8, 6, 0, 4, 1, 5, 9, 7, 8, 4, 1, 1, 9, 6, 5, 8, 4, 3, 6, 5,
          9, 1, 4, 6, 9, 8, 7, 1, 5, 3, 3]
