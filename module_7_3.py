
class WordsFinder:
    def __init__(self, *files):
        self.file_names = []
        for i in files:
            self.file_names.append(i)
    def get_all_words(self):
        pass
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                except_list = [',', '.', '=', '!', '?', ';', ':', ' - ']
                words = []
                for line in file:
                    for j in except_list:
                        if j == ' - ':
                            line = line.replace(j, ' ', -1)
                        else:
                            line = line.replace(j, '', -1)
                    a = line.replace('\n', '').lower().split(' ')
                    for x in a:
                        words.append(x)
            all_words[i] = words
        return all_words

    def find(self, word):
        pos_ = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                pos_[name] = words.index(word.lower()) + 1
        return pos_
    def count(self, word):
        counted_ = {}
        for name, words in self.get_all_words().items():
            a = 0
            for i in range(len(words)):
                if word.lower() == words[i]:
                    a += 1
            counted_[name] = a

        return counted_

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего