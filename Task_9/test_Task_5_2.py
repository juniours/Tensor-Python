import Task_5_2

def test_avg_1_2():
    assert Task_5_2.avg(1, 2) == 3

def test_avg_5_3_4():
    assert Task_5_2.avg(5, 3, 4) == 12

def test_avg_text_txt():
    assert Task_5_2.avg("text", ".txt") == "text.txt"