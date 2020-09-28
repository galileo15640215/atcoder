a, b, c, d = map(int, input().split())
if b < c or d < a:
    print("No")
else:
    print("Yes")

keiyou_week_df = pd.read_csv("keiyou_0.csv")
keiyou_week_df = keiyou_week_df.append(pd.read_csv("keiyou_2.csv"))
keiyou_holi_df = pd.read_csv("keiyou_1.csv")
keiyou_holi_df = keiyou_holi_df.append(pd.read_csv("keiyou_3.csv"))