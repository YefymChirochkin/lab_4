class WChain:
    def __init__(self, file):
        """
        constructor to initialize input file
        :param file: name of file to get data from
        """
        self.file = file

    def count_chains(self):

        """
        finds the longest possible length of a word chain taken from file
        :return: the longest possible length of a word chain
        """
        # creating dict with keys as words and start values as 1 (we always have at least one word chain)
        words = sorted(self._read_words_from_file(), key=len)
        word_chains = {word: 1 for word in words}
        for word in word_chains.keys():
            if len(word) == 1:
                continue
            for iterator in range(len(word)):
                # getting all possible variations of word without i-th character
                word_to_check = word.replace(word[iterator], '', 1)
                if word_to_check in word_chains:
                    word_chains[word] = max(word_chains[word_to_check] + 1, word_chains[word])
        result_word_chain = max(word_chains.values())
        WChain._write_answer_to_file(result_word_chain)
        return result_word_chain

    def _read_words_from_file(self):
        """
        puts all words from file .in into array and sort it
        :return: list of words in file
        """
        words = []
        with open(self.file, "r") as file:
            number_of_words = int(file.readline())
            for line in range(number_of_words):
                words.append(file.readline().strip())
        return words

    @staticmethod
    def _write_answer_to_file(answer):
        with open("../output.out", "w") as file:
            file.write(str(answer))