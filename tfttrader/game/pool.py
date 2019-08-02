# passive object


cost_level_1 = 1
cost_level_2 = 2
cost_level_3 = 3
cost_level_4 = 4
cost_level_5 = 5

quantity_level_1 = 39
quantity_level_2 = 26
quantity_level_3 = 21
quantity_level_4 = 13
quantity_level_5 = 10


class Pool:
    def __init__(self):
        self.quantities = {
            "Darius": (cost_level_1, quantity_level_1),
            "Elise": (cost_level_1, quantity_level_1),
            "Fiora": (cost_level_1, quantity_level_1),
            "Garen": (cost_level_1, quantity_level_1),
            "Graves": (cost_level_1, quantity_level_1),
            "Kassadin": (cost_level_1, quantity_level_1),
            "Kha'Zix": (cost_level_1, quantity_level_1),
            "Mordekaiser": (cost_level_1, quantity_level_1),
            "Nidalee": (cost_level_1, quantity_level_1),
            "Tristana": (cost_level_1, quantity_level_1),
            "Vayne": (cost_level_1, quantity_level_1),
            "Warwick": (cost_level_1, quantity_level_1),

            "Ahri": (cost_level_2, quantity_level_2),
            "Blitzcrank": (cost_level_2, quantity_level_2),
            "Braum": (cost_level_2, quantity_level_2),
            "Lissandra": (cost_level_2, quantity_level_2),
            "Lucian": (cost_level_2, quantity_level_2),
            "Lulu": (cost_level_2, quantity_level_2),
            "Pyke": (cost_level_2, quantity_level_2),
            "Rek'Sai": (cost_level_2, quantity_level_2),
            "Shen": (cost_level_2, quantity_level_2),
            "Twisted Fate": (cost_level_2, quantity_level_2),
            "Varus": (cost_level_2, quantity_level_2),
            "Zed": (cost_level_2, quantity_level_2),

            "Aatrox": (cost_level_3, quantity_level_3),
            "Ashe": (cost_level_3, quantity_level_3),
            "Evelynn": (cost_level_3, quantity_level_3),
            "Gangplank": (cost_level_3, quantity_level_3),
            "Katarina": (cost_level_3, quantity_level_3),
            "Kennen": (cost_level_3, quantity_level_3),
            "Morgana": (cost_level_3, quantity_level_3),
            "Poppy": (cost_level_3, quantity_level_3),
            "Rengar": (cost_level_3, quantity_level_3),
            "Shyvana": (cost_level_3, quantity_level_3),
            "Veigar": (cost_level_3, quantity_level_3),
            "Volibear": (cost_level_3, quantity_level_3),

            "Akali": (cost_level_4, quantity_level_4),
            "Aurelion Sol": (cost_level_4, quantity_level_4),
            "Brand": (cost_level_4, quantity_level_4),
            "Cho'Gath": (cost_level_4, quantity_level_4),
            "Draven": (cost_level_4, quantity_level_4),
            "Gnar": (cost_level_4, quantity_level_4),
            "Kindred": (cost_level_4, quantity_level_4),
            "Leona": (cost_level_4, quantity_level_4),
            "Sejuani": (cost_level_4, quantity_level_4),

            "Anivia": (cost_level_5, quantity_level_5),
            "Karthus": (cost_level_5, quantity_level_5),
            "Kayle": (cost_level_5, quantity_level_5),
            "Miss Fortune": (cost_level_5, quantity_level_5),
            "Swain": (cost_level_5, quantity_level_5),
            "Yasuo": (cost_level_5, quantity_level_5),
        }
