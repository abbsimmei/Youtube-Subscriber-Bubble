
from functions.loadSubscriberSubscribers import fetchSecondarySubs
from functions.loadSubscribers import fetchSubs
from functions.amountCalculator import countSubs
from functions.graphFunctions.starGraph.starGraphGenerator import starGraph
from functions.graphFunctions.starGraph.starGraphRatioGenerator import starRatioGraph
from functions.graphFunctions.completeGraph.completeGraph import compGraph1
from functions.graphFunctions.completeGraph.completeGraphGenerator import compGraph2
from functions.graphFunctions.completeGraph.edgeCleaner import compEdgeClean
from functions.subscriberRatio import subRatioFunc

from colorama import init, Fore, Back, Style
import os

os.system('cls')

# Initialize colorama
init()

"""
print(Fore.RED + "This text is red")
print(Fore.GREEN + "This text is green")
print(Fore.BLUE + "This text is blue")
print(Fore.YELLOW + "This text is yellow")

print(Style.BRIGHT + "Bright text")
print(Style.DIM + "Dim text")
print(Style.NORMAL + "Normal text")
print(Style.RESET_ALL + "Style reset")
"""

width = 80

ratioSubMinimum = 10
subLimit = 500
subMinimum = 50
ratioAmount = 200
channelName = "Swinceball"

def emptyBoxLine():
    print("#" + " " * (width - 2) + "#")

def textLine(text, width1, width2):
    print(Fore.YELLOW + "#" + " "*width1 + text + " "*width2 + "#")

def infoBox():
    print((Fore.YELLOW + "#" * width))
    emptyBoxLine()
    textLine("Welcome to the youtube graph generator!", 20, 19)
    emptyBoxLine()
    print
    print(("#" * width))

    print(Style.RESET_ALL + "")

    print(Fore.RED + Style.BRIGHT + "Fetch Data")
    print(Style.RESET_ALL + "'fetchPrimary' | fp - Fetch primary subscribers.")
    print("'fetchSecondary | fs' - Fetch secondary subscribers.")
    print("'fetchRatio | fr' - Fetch subscriber ratios.")

    print(Style.RESET_ALL + "")

    print(Fore.GREEN + Style.BRIGHT + "Generate Graphs")
    print(Style.RESET_ALL + "'star | s' - Generates a star graph.")
    print("'complete | c' - Generates complete graph.")
    print("'ratio | r' - Generates star ratio graph.")

    print(Style.RESET_ALL + "")

    print(Fore.MAGENTA + Style.BRIGHT + "Edit Graphs")
    print(Style.RESET_ALL + "'compEdge | ce' - Edit the edges on the complete graph.")

    print(Style.RESET_ALL + "" )

    print(Fore.CYAN + Style.BRIGHT + "Assign graph settings")
    print(Style.RESET_ALL + "'sublimit | sl' - What is the maximum amount of channels a person can be subscribed to, to count. (Max 1000)")
    print("'subminimum | sm' - What is the minimum amount of shared subs a channel needs to be shown in the graphs (not relevant for ratio graph):")
    print("'ratiosubminimum | rsm' - What is the minimum amount of shared subs a channel needs to be calculated with subscriber ratio?")
    print("'ratioamount | ra' - How many channels do you want to show in the ratio graph?")
    print("'channelname | cn' - What is your channel name?")

    print(Style.RESET_ALL + "")

    print((Fore.YELLOW + Style.BRIGHT + "Program Control"))
    print (Style.RESET_ALL + "'cls' - clear screen")
    print("'exit' - leave program")

    print(Style.RESET_ALL + "")

    print(Fore.CYAN + "Current graph settings:")
    print(Style.RESET_ALL + "subLimit: " + str(subLimit))
    print("subMinimum: " + str(subMinimum))
    print("ratioSubMininum: " + str(ratioSubMinimum))
    print("ratioAmount: " + str(ratioAmount))
    print("ChannelName: " + channelName)

infoBox()

while True:

    print(Style.RESET_ALL + "")

    command = input("Input command > ").strip().lower()

    if command in ["fetchprimary", "fp"]:
        fetchSubs()
    elif command in ["fetchsecondary", "fs"]:
        fetchSecondarySubs()
        countSubs(subLimit)
    elif command in ["fetchratio", "fr"]:
        subRatioFunc(int(ratioSubMinimum))
    elif command in ["star", "s"]:
        countSubs(subLimit)
        starGraph(subMinimum, channelName)
        print("You can now find the generated files in /generatedGephiFiles/star")
    elif command in ["complete", "c"]:
        countSubs(subLimit)
        compGraph1(subMinimum, subLimit, channelName)
        compGraph2(subMinimum, channelName)
        print("You can now find the generated files in /generatedGephiFiles/complete")
    elif command in ["ratio", "r"]:
        starRatioGraph(channelName)
        print("You can now find the generated files in /generatedGephiFiles/ratio")
    elif command in ["compedge", "ce"]:
        minWeigth = input("What do you want to be the minimum weight?")
        compEdgeClean(minWeigth)
    elif command in ["sublimit", "sl"]:
        subLimit = int(input("Enter new subLimit (max 1000): "))
        os.system('cls')
        infoBox()
    elif command in ["subminimum", "sm"]:
        subMinimum = int(input("Enter new subMinimum: "))
        os.system('cls')
        infoBox()
    elif command in ["ratiosubminimum", "rsm"]:
        ratioSubMinimum = int(input("Enter new ratioSubMinimum: "))
        os.system('cls')
        infoBox()
    elif command in ["ratioamount", "ra"]:
        ratioAmount = int(input("Enter new ratioAmount: "))
        os.system('cls')
        infoBox()
    elif command in ["channelname", "cn"]: 
        cn = input("What is your channel name: ")
        channelName = cn
        os.system('cls')
        infoBox()      
    elif command == "exit":
        break
    elif command == "cls":
        os.system('cls')
        infoBox()
    else:
        print("Unknown command. Please try again.")
