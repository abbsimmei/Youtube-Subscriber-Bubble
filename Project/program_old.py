
from functions.loadSubscriberSubscribers import fetchSecondarySubs
from functions.loadSubscribers import fetchSubs
from functions.amountCalculator import countSubs
from functions.graphFunctions.starGraph.starGraphGenerator import starGraph
from functions.graphFunctions.starGraph.starGraphRatioGenerator import starRatioGraph
from functions.graphFunctions.completeGraph.completeGraph import compGraph1
from functions.graphFunctions.completeGraph.completeGraphGenerator import compGraph2
from functions.graphFunctions.completeGraph.edgeCleaner import compEdgeClean
from functions.subscriberRatio import subRatioFunc

skipVar = input("Do you want to skip fetching primarySubscribers? Write 'skip': ")
if skipVar != "skip":
    fetchSubs()
else:
    print("Skipped loading primary subscribers")

skipVarSec = input("Do you want to skip fetching secondarySubscribers? Write 'skip': ")
if skipVarSec != "skip":
    fetchSecondarySubs()
else:
    print("Skipped loading secondary subscribers")

subRatioBool = input("Do you want to skip fetching subscriber ratios? Write 'skip': ")
if subRatioBool != "skip":
    subRatioSubMinimum = input("What is the minimum amount of shared subs a channel needs to be calculated with subscriber ratio? ")
    print("Generating subscriber ratios")
    subRatioFunc(int(subRatioSubMinimum))
else:
    print("skipped generating subscriber ratios")


graphBool = input("Do you want to generate graphs? Write 'yes': ")
if graphBool == "yes":
    subLimit = input("What is the maximum amount of channels a person can be subscribed to, to count. (Max 1000), (else: skip): ")
    if subLimit != "skip":
        countSubs(subLimit)

    subMinimum = input("What is the minimum amount of shared subs a channel needs to be shown in the graphs (not relevant for ratio graph): ")

    starBool = input("Do you want to skip creating star graph? Write 'skip': ")
    if starBool != "skip":
        print("Generating star Graph")
        starGraph(subMinimum)
    else:
        print("Skipped star graph")

    compBool = input("Do you want to skip creating complete graph? Write 'skip': ")
    if compBool != "skip":
        print("Generating Complete Graph")
        compGraph1(subMinimum, subLimit)
        compGraph2(subMinimum)

        cleanerBool = input("Do you want to edit the edges on the complete graph? Write 'yes': ")
        if cleanerBool == "yes":
            minWeigth = input("What do you want to be the minimum weight?")
            compEdgeClean(minWeigth)
    else:
        print("skipped graph generation")
    
    starRatioBool = input("Do you want to skip creating complete graph? Write 'skip': ")
    if starRatioBool != "skip":
        starRatioGraph()
        



