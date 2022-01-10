import pygame
import random
import copy


class Game2048(object):
    def __init__(self, matrix_size=(4, 4), max_score_filepath=None):
        self.matrix_size = matrix_size
        self.max_score_filepath = max_score_filepath

        self.initialize()

    def initialize(self):
        self.game_matrix = [['null' for _ in range(self.matrix_size[1])] for _ in range(self.matrix_size[0])]

        self.score = 0
        self.max_score = self.readMaxScore()

        self.randomGenerateNumber()
        self.randomGenerateNumber()

        print(self.game_matrix)

        self.move_direction = None

    def update(self):
        self.game_matrix_before = copy.deepcopy(self.game_matrix)
        self.move()
        if self.game_matrix != self.game_matrix_before:
            self.randomGenerateNumber()

        if self.score > self.max_score:
            self.max_score = self.score

    def randomGenerateNumber(self):

        empty_pos = []
        for i in range(self.matrix_size[0]):
            for j in range(self.matrix_size[1]):
                if self.game_matrix[i][j] == 'null':
                    empty_pos.append([i, j])

        i, j = random.choice(empty_pos)

        self.game_matrix[i][j] = 2 if random.random() > 0.1 else 4

        print('позиция[{0}][{1}] = значение{2}'.format(i, j, self.game_matrix[i][j]))

    def readMaxScore(self):
        try:
            f = open(self.max_score_filepath, 'r', encoding='utf-8')
            score = int(f.read().strip())
            f.close()
            return score
        except:
            return 0

    def setDirection(self, direction):
        assert direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']
        self.move_direction = direction
        print(self.move_direction)

    def move(self):

        def extract(array):
            new_array = []
            for arr in array:
                if arr != 'null':
                    new_array.append(arr)
            return new_array

        def merge(array):
            score = 0
            if len(array) < 2:
                return array, score
            for i in range(len(array) - 1):
                if array[i] == 'null':
                    break
                if array[i] == array[i + 1]:
                    array[i] += array[i + 1]
                    score += array[i]
                    array.pop(i + 1)
                    array.append('null')
            return extract(array), score

        if self.move_direction is None:
            return

        if self.move_direction == 'UP':

            for j in range(self.matrix_size[1]):

                col = []
                for i in range(self.matrix_size[0]):
                    col.append(self.game_matrix[i][j])

                new_col = extract(col)

                new_col, score = merge(new_col)
                self.score += score

                new_col.extend('null' for _ in range(self.matrix_size[0] - len(new_col)))

                for i in range(self.matrix_size[0]):
                    self.game_matrix[i][j] = new_col[i]


        elif self.move_direction == 'DOWN':

            for j in range(self.matrix_size[1]):

                col = []
                for i in range(self.matrix_size[0]):
                    col.append(self.game_matrix[i][j])

                col.reverse()

                new_col = extract(col)

                new_col, score = merge(new_col)
                self.score += score

                new_col.extend('null' for _ in range(self.matrix_size[0] - len(new_col)))

                new_col.reverse()

                for i in range(self.matrix_size[0]):
                    self.game_matrix[i][j] = new_col[i]


        elif self.move_direction == 'LEFT':

            for i in range(self.matrix_size[0]):

                row = []
                for j in range(self.matrix_size[1]):
                    row.append(self.game_matrix[i][j])

                new_row = extract(row)

                new_row, score = merge(new_row)
                self.score += score

                new_row.extend('null' for _ in range(self.matrix_size[1] - len(new_row)))

                for j in range(self.matrix_size[1]):
                    self.game_matrix[i][j] = new_row[j]


        elif self.move_direction == 'RIGHT':

            for i in range(self.matrix_size[0]):

                row = []
                for j in range(self.matrix_size[1]):
                    row.append(self.game_matrix[i][j])

                row.reverse()

                new_row = extract(row)

                new_row, score = merge(new_row)
                self.score += score

                new_row.extend('null' for _ in range(self.matrix_size[1] - len(new_row)))

                new_row.reverse()

                for j in range(self.matrix_size[1]):
                    self.game_matrix[i][j] = new_row[j]

        self.move_direction = None

    def saveMaxScore(self):

        f = open(self.max_score_filepath, 'w', encoding='utf-8')
        f.write(str(self.max_score))
        f.close()

    @property
    def isGameOver(self):

        for i in range(self.matrix_size[0]):
            for j in range(self.matrix_size[1]):
                if self.game_matrix[i][j] == 'null':
                    return False
                elif (j + 1 <= self.matrix_size[1] - 1) and (self.game_matrix[i][j] == self.game_matrix[i][j + 1]):
                    return False
                elif (i + 1 <= self.matrix_size[0] - 1) and (self.game_matrix[i][j] == self.game_matrix[i + 1][j]):
                    return False
        return True


if __name__ == "__main__":
    game_2048 = Game2048(matrix_size=(4, 4), max_score_filepath='../score')
