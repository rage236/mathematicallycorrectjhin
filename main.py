import itertools

class itemBase():
    AD: int
    crit: int
    AS: int

class InfinityEdge(itemBase):
    AD = 65
    crit = 20
    AS = 0

class LDR(itemBase):
    AD = 40
    crit = 20
    AS = 0

class Stormrazor(itemBase):
    AD = 60
    crit = 20
    AS = 15

class RFC(itemBase):
    AD = 30
    crit = 20
    AS = 20

class BT(itemBase):
    AD = 95
    crit = 20
    AS = 0

class GA(itemBase):
    AD = 55
    crit = 0
    AS = 0

class Collector(itemBase):
    AD = 55
    crit = 20
    AS = 0

class EssenceReaver(itemBase):
    AD = 60
    crit = 20
    AS = 0

class ShouldntAppear(itemBase):
    AD = 0
    crit = 0
    AS = 0

class Eclipse(itemBase):
    AD = 70
    crit = 0
    AS = 0

class Hubris(itemBase):
    AD = 65
    crit = 0
    AS = 0

class Hexplate(itemBase):
    AD = 55
    crit = 0
    AS = 25

class StatikkShiv(itemBase):
    AD = 50
    crit = 20
    AS = 30

class KrakenSlayer(itemBase):
    AD = 40
    crit = 20
    AS = 35

class Manamune(itemBase):
    AD = 85
    crit = 0
    AS = 0

class Bezerker(itemBase):
    AD = 0
    crit = 0
    AS = 35

class WitsEnd(itemBase):
    AD = 0
    crit = 0
    AS = 55

class Nashors(itemBase):
    AD = 0
    crit = 0
    AS = 50

class Runaans(itemBase):
    AD = 0
    crit = 20
    AS = 40

class PD(itemBase):
    AD = 20
    crit = 20
    AS = 30

class BORK(itemBase):
    AD = 40
    crit = 0
    AS = 25

class Steraks(itemBase):
    AD = 69
    crit = 0
    AS = 0

def main():
    items: list[itemBase] = [Steraks, WitsEnd, Nashors, Runaans, PD, BORK, GA, BT, EssenceReaver, Collector, LDR, InfinityEdge, RFC, Stormrazor, Eclipse, Hubris, Hexplate, StatikkShiv, KrakenSlayer, Manamune, Bezerker]
    #Rune Options, GatheringStorm is in minutes, not stacks (10 mins is one stack, 20 is 2, etc.)
    HOB: bool = False
    EyeballCollection: bool = False
    GatheringStormTime: int = 30
    AbsoluteFocus: bool = True
    secondaryForce: int = 9
    secondaryAS: int = 10
    conqueror: bool = True
    Alacrity: bool = True

    #forces Infinity Edge and LDR to appear in the build path, for a more reasonable max AD jhin build
    requireImportantItems = False
    maxAD = 0
    maxBootAD = 0
    maxItems: list[itemBase] = []
    maxBootItems: list[itemBase] = []
    builds = []
    if(requireImportantItems):
        items.remove(InfinityEdge)
        items.remove(LDR)
        reducedBuild = list(itertools.combinations(items, 4))
        for build in reducedBuild:
            build = list(build)
            build.append(InfinityEdge)
            build.append(LDR)
            builds.append(build)
    else:
        builds = list(itertools.combinations(items, 6))
    for build in builds:
        totalAS = 0
        totalCrit = 0
        totalAD = 138.9
        if(HOB):
            totalAS += 110
        if(EyeballCollection):
            totalAD += 18
        totalAD += (((4*int(GatheringStormTime/10)*int(GatheringStormTime/10)) + 4*int(GatheringStormTime/10))*.6)
        if(AbsoluteFocus):
            totalAD += 18
        totalAD += secondaryForce*.6
        totalAS += secondaryAS
        if(conqueror):
            totalAD += (48*.6)
        if(Alacrity):
            totalAS += 18
        for item in build:
            totalAS += item.AS
            if totalCrit != 100:
                totalCrit += item.crit
            totalAD += item.AD
        passive = 44 + .3*(totalCrit) + .25*(totalAS)
        totalAD = totalAD + totalAD*passive/100
        if(totalAD > maxAD):
            maxAD = totalAD
            maxItems = []
            for item in build:
                maxItems.append(item)
    print(maxItems, maxAD)
    print("\n")

    bootBuilds = []
    if(requireImportantItems):
        maxItems.remove(InfinityEdge)
        maxItems.remove(LDR)
        reducedBootBuilds = list(itertools.combinations(maxItems, 3))
        for build in reducedBootBuilds:
            build = list(build)
            build.append(InfinityEdge)
            build.append(LDR)
            build.append(Bezerker)
            bootBuilds.append(build)
    else:
        tempBootBuilds =  list(itertools.combinations(maxItems, 5))
        for item in tempBootBuilds:
            item = list(item)
            item.append(Bezerker)
            bootBuilds.append(item)
        #print(item)
    for build in bootBuilds:
        totalBootAS = 0
        totalBootCrit = 0
        totalBootAD = 138.9
        if(HOB):
            totalBootAS += 110
        if(EyeballCollection):
            totalBootAD += 18
        totalBootAD += (((4*int(GatheringStormTime/10)*int(GatheringStormTime/10)) + 4*int(GatheringStormTime/10))*.6)
        if(AbsoluteFocus):
            totalBootAD += 18
        totalBootAD += (secondaryForce*.6)
        totalBootAS += secondaryAS
        if(conqueror):
            totalBootAD += (48*.6)
        if(Alacrity):
            totalBootAS += 18
        for item in build:
            totalBootAS += item.AS
            if totalBootCrit != 100:
                totalBootCrit += item.crit
            totalBootAD += item.AD
        passive = 44 + .3*(totalBootCrit) + .25*(totalBootAS)
        totalBootAD = totalBootAD + totalBootAD*passive/100
        if(totalBootAD > maxBootAD):
            maxBootAD = totalBootAD
            maxBootItems = []
            for item in build:
                maxBootItems.append(item)
    print(maxBootItems, maxBootAD)
if __name__ == "__main__":
    main()
