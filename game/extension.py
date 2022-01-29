class ExttensionDatas:
    BASE_WIDTH = 320
    BASE_HEIGHT  = 180
    
    def __init__(self):
        self.ext_list = [
            "1024x768 (4:3)",
            "1200x600 (2:1)",
            "1280x800 (8:5)",
            "1440x900 (8:5)",
            "1400x1050 (4:3)",
            "1600x900 (16:9)",
            "1600x1024 (25:16)",
            "1680x1050 (8:5)",
            "1920x1200 (16:10)",
            "1366x768 (16:9)"
        ]

    def calculate(self):
        for item in self.ext_list:
            wh, r = item.split()

            w, h = wh.split("x")

            w_res = int(w) // ExttensionDatas.BASE_WIDTH
            h_res = int(h) // ExttensionDatas.BASE_HEIGHT

            if w_res == h_res:
                print(f"\t[+] {item}")
            else:
                print(f"{item}")



ExttensionDatas().calculate()