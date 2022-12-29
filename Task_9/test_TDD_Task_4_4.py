import TDD_Task_4_4


def test_add_item_smth():
    assert TDD_Task_4_4.add_item({"elf": 97}, {"smth": 10}, "smth") == False

def test_add_item_thing():
    assert TDD_Task_4_4.add_item({"elf": 17, "dwarf": 14}, {"thing": 30}, "thing") == True

def test_del_item_elf():
    assert TDD_Task_4_4.del_item({"elf": 17, "dwarf": 14}, "elf") == True

def test_del_item_thing():
    assert TDD_Task_4_4.del_item({"elf": 17, "dwarf": 14}, "thing") == False