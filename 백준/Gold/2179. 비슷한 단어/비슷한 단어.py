import sys

input = sys.stdin.readline

word_num = int(input())
words = [input().rstrip() for _ in range(word_num)]
max_len_words = max(len(word) for word in words)

ans_word1 = ""
ans_word2 = ""

for prefix_count in range(1, max_len_words + 1):
    prefix_dic = {}
    for prefix_word in words:
        if prefix_word[:prefix_count] in prefix_dic:
            prefix_dic[prefix_word[:prefix_count]].append(prefix_word)
        else:
            prefix_dic[prefix_word[:prefix_count]] = [prefix_word]

    max_common_len = 1
    for common in prefix_dic:
        if len(prefix_dic[common]) > max_common_len:
            # print(prefix_dic[common])
            max_common_len = len(prefix_dic[common])
            ans_word1 = prefix_dic[common][0]
            ans_word2 = prefix_dic[common][1]

    if max_common_len == 1:
        break

print(ans_word1)
print(ans_word2)
