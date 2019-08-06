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
