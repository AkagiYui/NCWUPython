# 键盘密码 解密

# 反转数字
secret = [52, 91, 91, 32, 92, 71, 33, 82]
for i in range(len(secret)):
    secret[i] = int(str(secret[i])[::-1])
print(secret)

# 键盘密码
keymap = {
    11: 'A', 12: 'B', 13: 'C', 14: 'D', 15: 'E', 16: 'F', 17: 'G', 18: 'H', 19: 'I', 110: 'J',
    21: 'K', 22: 'L', 23: 'M', 24: 'N', 25: 'O', 26: 'P', 27: 'Q', 28: 'R', 29: 'S',
    31: 'T', 32: 'U', 33: 'V', 34: 'W', 35: 'X', 36: 'Y', 37: 'Z',
}
keymap_qwerty = {
    11: 'Q', 12: 'W', 13: 'E', 14: 'R', 15: 'T', 16: 'Y', 17: 'U', 18: 'I', 19: 'O', 110: 'P',
    21: 'A', 22: 'S', 23: 'D', 24: 'F', 25: 'G', 26: 'H', 27: 'J', 28: 'K', 29: 'L',
    31: 'Z', 32: 'X', 33: 'C', 34: 'V', 35: 'B', 36: 'N', 37: 'M',
}
plain = ''
for s in secret:
    plain += keymap_qwerty[s]
print(plain)
