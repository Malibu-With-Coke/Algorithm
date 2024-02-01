import sys

input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

t_a_count = t.count("A")
t_b_count = t.count("B")
t_len = len(t)

s_a_count = s.count("A")
s_b_count = s.count("B")
s_len = len(s)


def add_char(word, word_a_count, word_b_count):
    # print(word)
    if word == t:
        print(1)
        exit(0)

    if len(word) >= t_len or word_a_count > t_a_count or word_b_count > t_b_count:
        return

    add_char(word + "A", word_a_count + 1, word_b_count)
    reverse_word = word[::-1]
    add_char("B" + reverse_word, word_a_count, word_b_count + 1)
    return


def delete_char(word, word_a_count, word_b_count):
    if word == s:
        print(1)
        exit(0)

    if len(word) <= s_len or word_a_count < s_a_count or word_b_count < s_b_count:
        return

    if word[-1] == "A":
        delete_char(word[:-1], word_a_count - 1, word_b_count)
    if word[0] == "B":
        delete_char(word[:0:-1], word_a_count, word_b_count - 1)
    return


# add_char(s, s_a_count, s_b_count)
delete_char(t, t_a_count, t_b_count)
print(0)
