# passive object
import random

COST_LEVEL_1 = 1
COST_LEVEL_2 = 2
COST_LEVEL_3 = 3
COST_LEVEL_4 = 4
COST_LEVEL_5 = 5

QUANTITY_LEVEL_1 = 39
QUANTITY_LEVEL_2 = 26
QUANTITY_LEVEL_3 = 21
QUANTITY_LEVEL_4 = 13
QUANTITY_LEVEL_5 = 10

TOTAL_QUANTITY_LEVEL_1 = 468
TOTAL_QUANTITY_LEVEL_2 = 312
TOTAL_QUANTITY_LEVEL_3 = 252
TOTAL_QUANTITY_LEVEL_4 = 117
TOTAL_QUANTITY_LEVEL_5 = 60

TOTAL_QUANTITY_OVERALL = TOTAL_QUANTITY_LEVEL_1 + TOTAL_QUANTITY_LEVEL_2 + TOTAL_QUANTITY_LEVEL_3 + TOTAL_QUANTITY_LEVEL_4 + TOTAL_QUANTITY_LEVEL_5  # 1209


class Pool:
    def __init__(self):
        self.total_quantity_overall = TOTAL_QUANTITY_OVERALL
        self.quantities = [
            [TOTAL_QUANTITY_LEVEL_1,
             [["Darius", COST_LEVEL_1, QUANTITY_LEVEL_1],
              ["Elise", COST_LEVEL_1, QUANTITY_LEVEL_1],
              ["Fiora", COST_LEVEL_1, QUANTITY_LEVEL_1],
              ["Garen", COST_LEVEL_1, QUANTITY_LEVEL_1],
              ["Graves", COST_LEVEL_1, QUANTITY_LEVEL_1],
              ["Kassadin", COST_LEVEL_1, QUANTITY_LEVEL_1],
              ["Kha'Zix", COST_LEVEL_1, QUANTITY_LEVEL_1],
              ["Mordekaiser", COST_LEVEL_1, QUANTITY_LEVEL_1],
              ["Nidalee", COST_LEVEL_1, QUANTITY_LEVEL_1],
              ["Tristana", COST_LEVEL_1, QUANTITY_LEVEL_1],
              ["Vayne", COST_LEVEL_1, QUANTITY_LEVEL_1],
              ["Warwick", COST_LEVEL_1, QUANTITY_LEVEL_1]]],

            [TOTAL_QUANTITY_LEVEL_2,
             [["Ahri", COST_LEVEL_2, QUANTITY_LEVEL_2],
              ["Blitzcrank", COST_LEVEL_2, QUANTITY_LEVEL_2],
              ["Braum", COST_LEVEL_2, QUANTITY_LEVEL_2],
              ["Lissandra", COST_LEVEL_2, QUANTITY_LEVEL_2],
              ["Lucian", COST_LEVEL_2, QUANTITY_LEVEL_2],
              ["Lulu", COST_LEVEL_2, QUANTITY_LEVEL_2],
              ["Pyke", COST_LEVEL_2, QUANTITY_LEVEL_2],
              ["Rek'Sai", COST_LEVEL_2, QUANTITY_LEVEL_2],
              ["Shen", COST_LEVEL_2, QUANTITY_LEVEL_2],
              ["Twisted Fate", COST_LEVEL_2, QUANTITY_LEVEL_2],
              ["Varus", COST_LEVEL_2, QUANTITY_LEVEL_2],
              ["Zed", COST_LEVEL_2, QUANTITY_LEVEL_2]]],

            [TOTAL_QUANTITY_LEVEL_3,
             [["Aatrox", COST_LEVEL_3, QUANTITY_LEVEL_3],
              ["Ashe", COST_LEVEL_3, QUANTITY_LEVEL_3],
              ["Evelynn", COST_LEVEL_3, QUANTITY_LEVEL_3],
              ["Gangplank", COST_LEVEL_3, QUANTITY_LEVEL_3],
              ["Katarina", COST_LEVEL_3, QUANTITY_LEVEL_3],
              ["Kennen", COST_LEVEL_3, QUANTITY_LEVEL_3],
              ["Morgana", COST_LEVEL_3, QUANTITY_LEVEL_3],
              ["Poppy", COST_LEVEL_3, QUANTITY_LEVEL_3],
              ["Rengar", COST_LEVEL_3, QUANTITY_LEVEL_3],
              ["Shyvana", COST_LEVEL_3, QUANTITY_LEVEL_3],
              ["Veigar", COST_LEVEL_3, QUANTITY_LEVEL_3],
              ["Volibear", COST_LEVEL_3, QUANTITY_LEVEL_3]]],

            [TOTAL_QUANTITY_LEVEL_4,
             [["Akali", COST_LEVEL_4, QUANTITY_LEVEL_4],
              ["Aurelion Sol", COST_LEVEL_4, QUANTITY_LEVEL_4],
              ["Brand", COST_LEVEL_4, QUANTITY_LEVEL_4],
              ["Cho'Gath", COST_LEVEL_4, QUANTITY_LEVEL_4],
              ["Draven", COST_LEVEL_4, QUANTITY_LEVEL_4],
              ["Gnar", COST_LEVEL_4, QUANTITY_LEVEL_4],
              ["Kindred", COST_LEVEL_4, QUANTITY_LEVEL_4],
              ["Leona", COST_LEVEL_4, QUANTITY_LEVEL_4],
              ["Sejuani", COST_LEVEL_4, QUANTITY_LEVEL_4]]],

            [TOTAL_QUANTITY_LEVEL_5,
             [["Anivia", COST_LEVEL_5, QUANTITY_LEVEL_5],
              ["Karthus", COST_LEVEL_5, QUANTITY_LEVEL_5],
              ["Kayle", COST_LEVEL_5, QUANTITY_LEVEL_5],
              ["Miss Fortune", COST_LEVEL_5, QUANTITY_LEVEL_5],
              ["Swain", COST_LEVEL_5, QUANTITY_LEVEL_5],
              ["Yasuo", COST_LEVEL_5, QUANTITY_LEVEL_5]]],
        ]
        self.probabilities = {
            2: [0, 1000],
            3: [0, 650, 950, 1000],
            4: [0, 500, 850, 1000],
            5: [0, 370, 720, 970, 1000],
            6: [0, 245, 595, 895, 995, 1000],
            7: [0, 200, 500, 830, 980, 1000],
            8: [0, 150, 400, 750, 950, 1000],
            9: [0, 100, 250, 600, 900, 1000],
        }
        self.name_to_place = {
            "Darius": [0, 0],
            "Elise": [0, 1],
            "Fiora": [0, 2],
            "Garen": [0, 3],
            "Graves": [0, 4],
            "Kassadin": [0, 5],
            "Kha'Zix": [0, 6],
            "Mordekaiser": [0, 7],
            "Nidalee": [0, 8],
            "Tristana": [0, 9],
            "Vayne": [0, 10],
            "Warwick": [0, 11],

            "Ahri": [1, 0],
            "Blitzcrank": [1, 1],
            "Braum": [1, 2],
            "Lissandra": [1, 3],
            "Lucian": [1, 4],
            "Lulu": [1, 5],
            "Pyke": [1, 6],
            "Rek'Sai": [1, 7],
            "Shen": [1, 8],
            "Twisted Fate": [1, 9],
            "Varus": [1, 10],
            "Zed": [1, 11],

            "Aatrox": [2, 0],
            "Ashe": [2, 1],
            "Evelynn": [2, 2],
            "Gangplank": [2, 3],
            "Katarina": [2, 4],
            "Kennen": [2, 5],
            "Morgana": [2, 6],
            "Poppy": [2, 7],
            "Rengar": [2, 8],
            "Shyvana": [2, 9],
            "Veigar": [2, 10],
            "Volibear": [2, 11],

            "Akali": [3, 0],
            "Aurelion Sol": [3, 1],
            "Brand": [3, 2],
            "Cho'Gath": [3, 3],
            "Draven": [3, 4],
            "Gnar": [3, 5],
            "Kindred": [3, 6],
            "Leona": [3, 7],
            "Sejuani": [3, 8],

            "Anivia": [4, 0],
            "Karthus": [4, 1],
            "Kayle": [4, 2],
            "Miss Fortune": [4, 3],
            "Swain": [4, 4],
            "Yasuo": [4, 5],
        }

    def get_shop_for_level(self, level):
        shop = ["", "", "", "", ""]
        level_probability = self.probabilities[level]

        for i in range(0, 5):
            selected_cost = random.randrange(0, 1000)
            selected_bracket = -1
            for j in range(0, len(level_probability) - 1):
                if level_probability[j] <= selected_cost < level_probability[j + 1]:
                    selected_bracket = j
                    break
            selected_champ = random.randrange(0, self.quantities[selected_bracket][0])
            for champ_record in self.quantities[selected_bracket][1]:
                if selected_champ < champ_record[2]:
                    shop[i] = champ_record[0]
                    champ_record[2] -= 1
                    self.quantities[selected_bracket][0] -= 1
                    self.total_quantity_overall -= 1
                    break
                else:
                    selected_champ -= champ_record[2]

        return shop

    def recall_old_personal_shop(self, personal_shop):
        for i in personal_shop:
            if i is not None:
                index = self.name_to_place[i]
                self.quantities[index[0]][1][index[1]][2] += 1
                self.quantities[index[0]][0] += 1
                self.total_quantity_overall += 1
