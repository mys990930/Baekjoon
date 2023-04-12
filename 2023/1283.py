import sys

class Option:
    def __init__(self, words):
        self.input_words = words
        self.shortcut_pos = -1
        self.find_shortcut()
        self.ans = self.wrap_shortcut()

    def find_shortcut(self):
        words = self.input_words.split()

        cnt = 0
        for i in range(len(words)):
            temp_word = words[i]
            if temp_word[0].upper() not in used_keys:
                used_keys.append(temp_word[0].upper())
                self.shortcut_pos = cnt
                return
            cnt += len(words[i]) + 1

        for i in range(len(self.input_words)):
            if self.input_words[i].upper() not in used_keys:
                used_keys.append(self.input_words[i].upper())
                self.shortcut_pos = i
                return

        self.shortcut_pos = -1 # if there are no shortcuts
        return

    def wrap_shortcut(self): # wrap shortcut with []
        ans = self.input_words
        if self.shortcut_pos == -1: # if there are no shortcuts
            return ans
        ans = ans[:self.shortcut_pos] + '[' + ans[self.shortcut_pos] + ']' + ans[self.shortcut_pos+1:]
        return ans

N = int(input())
options = []
used_keys = ['\n', ' '] # exceptions
for i in range(N):
    option = sys.stdin.readline()
    options.append(Option(option))

for i in range(N):
    print(options[i].ans, end='')