import codebug_tether
import time


def default_phase():
    codebug.set_row(4, 0b11111)
    codebug.set_row(3, 0b11111)
    codebug.set_row(2, 0b11111)
    codebug.set_row(1, 0b00000)
    codebug.set_row(0, 0b00000)


def A_1_phase():
    codebug.set_row(4, 0b11111)
    codebug.set_row(3, 0b11111)
    codebug.set_row(2, 0b11100)
    codebug.set_row(1, 0b11000)
    codebug.set_row(0, 0b00000)


def A_2_phase():
    number = 31
    for index in range(5):
        codebug.set_row(4-index, number)
        number -= 2 ** index


    # codebug.set_row(4, 0b11111) #31
    # codebug.set_row(3, 0b11110) #30 1 
    # codebug.set_row(2, 0b11100) #28 2
    # codebug.set_row(1, 0b11000) #24 4
    # codebug.set_row(0, 0b10000) #16 8




codebug = codebug_tether.CodeBug()


def main():


    codebug.clear()
    default_phase()
    SLEEPING_TIME = 0.15

    while True:
        if codebug.get_input('A'):
            A_1_phase()
            time.sleep(SLEEPING_TIME)
            A_2_phase()
            time.sleep(SLEEPING_TIME)
            A_1_phase()
            time.sleep(SLEEPING_TIME)
            default_phase()
    
main()