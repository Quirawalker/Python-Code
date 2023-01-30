"""This is just basicly a text file

THIS IS ENTIRELY FICTIONAL: Fool a friend and have fun
"""

import time, random 
ratio = random.randint(50,100)
def Global_Thermonuclear_War():
    print("~~~You are about to open GLOBAL THERMONUCLEAR WAR~~~\n")
    time.sleep(1.0)
    answer = input("Are you sure you wish to contine: CONFIRM or ABORT\n")
    if answer == "ABORT":
        time.sleep(2.0)
        print(
            """
            This has been a drill.
            System going off-line.
            """
            )

    elif answer == "CONFIRM":
        time.sleep(2.0)
        print(
            """
            This is not a drill...
                !!!Code Red Activated!!!\n
            """
            )
        time.sleep(2.0)
        print(
            """
            Thermonuclear Missiles have just been launched on a gloabl scale.

            Please wait for time till impact telemetry to come online.\n
            """
            )
        print("The computer estimates a total global percentage kill ratio of: ")
        print(ratio)
        time.sleep(5.0)
        print("Time Till Impact: 5...")
        time.sleep(1.0)
        print("Time Till Impact: 4...")
        time.sleep(1.0)
        print("Time Till Impact: 3...")
        time.sleep(1.0)
        print("Time Till Impact: 2...")
        time.sleep(1.0)
        print("Time Till Impact: 1...")
        time.sleep(1.0)
        print("!!!IMPACT!!!\n\n")

        time.sleep(2.0)
        print("This has been a fictional rendition and is strictly for fun!")

if __name__ == '__main__':
    Global_Thermonuclear_War()