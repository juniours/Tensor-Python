import Task_5_1

def test_check_passwd_Password():
    assert Task_5_1.check_passwd("Password") == False

def test_check_passwd_Password123():
    assert Task_5_1.check_passwd("Password123") == False

def test_check_passwd_admins():
    assert Task_5_1.check_passwd("admins") == False

def test_check_passwd_adm1ns():
    assert Task_5_1.check_passwd("adm1ns") == True