def vb(lijstje):
    lijstje[1] = "lala"


items = ["bla", "blabla"]
if len(items) < 5:
    vb(items)
else:
    print("Nope niet kleiner dan 5...")