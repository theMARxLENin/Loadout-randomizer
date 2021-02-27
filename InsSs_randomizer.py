import random

#add custom supply points in future

def inputHandler(number):
    while True:
        try:
            num = int(input())
        except ValueError:
            print("Invalid input. Try again")
            continue
        if num < 0 or num > number:
            print("Invalid input. Try again")
            continue
        else: break
    return num

# func for choosing random item
def ChooseItem(dict, supply):
    temp = [key for key, sp in dict.items() if sp <= supply]
    choice = random.choice(temp)
    supply -= dict[choice]
    return choice, supply

#Choosing game mode
playmodes = ["Co-op", "PvP", "Competitive"]
print("Choose playing mode: 0. Co-op, 1. PvP, 2.Competitive")
mode = inputHandler(2)
print("You chose", playmodes[mode])

supply = 15
if mode == 0:
    supply += 5
print("Supply points", supply)

# Choosing side
sides = ["Insurgent", "Security"]
print("Choose your side: 0." + sides[0]+", 1." + sides[1])
Side = inputHandler(1)
print("You are", sides[Side])

night = False
print("Day or Night? 0. Day, 1. Night")
if inputHandler(1) == 1:
    night = True

# choosing class
if mode == 0 or mode == 1:
    fighters = ["Random", "Rifleman", "Breacher", "Advisor", "Demolitions", "Marksman", "Gunner", "Observer", "Commander"]
    print("Choose your class:")
    for i in range(len(fighters)):
        print(i, fighters[i])
    fighter = inputHandler(8)
    if fighter == 0:
        fighter = random.randint(1, 8)
    print("Your class is", fighters[fighter])
elif mode == 2:
    fighters = ["Assaulter", "Flanker", "Sharpshooter"]
    print("Choose your class: 0. Assaulter, 1. Flanker, 2. Sharpshooter")
    fighter = inputHandler(2)
    print("You class is", fighters[fighter])

# All 40 primary weapons
allPW = [None, "MP7", "MP5A5", "Grease Gun", "Uzi", "MP5A2",
         "Sterling", "G36K", "Mk 18 CQBR", "M4A1", "SKS",
         "AKS-74U", "M16A4", "L85A2", "VHS-2", "Galil SAR",
         "Honey Badger", "AKM", "M16A2", "AK-74", "Alpha AK",
         "QBZ-03", "Galil", "AS Val", "Mk 17 Mod 0", "G3A3",
         "Mk 14 EBR", "Tavor 7", "FAL", "ACE 52", "M249",
         "M240B", "PKM", "MG3", "M870", "TOZ-194",
         "M24", "Mosin-Nagant", "SVD", "M82A1 CQ", "M99",
         "FAMAS F1", "AUG A3", "M1 Garand", "M110 SASS", "QBZ-97",
         "QTS-11"]

# All secondary weapons
allSW = [None, "Tariq", "M45", "L106A1", "PF940", "M9", "Makarov", "Browning HP", "M1911", "Welrod"]

# All attachments
Optics = [None, "1x Flip Up Sights", "1x Holographic", "1x Kobra", "1x MARS", "1x MRO",
          "1x OKP-7", "1x Red Dot", "1.5x PK-AS", "2x-1x Holographic", "2x-1x Kobra",
          "2x-1x Red Dot", "3x A2 Scope", "3x Type 03 Scope", "4x-1x C79", "4x M150",
          "4x-1x SU230", "4x ISM", "4x PU Scope", "4x PSO-1", "4x-1x SUSAT",
          "7x Hunting Scope", "7x Sniper Scope", "7x Type 99 Scope", "1.5x-1x A1 Scope", "3x A3 Scope",
          "4x-1x M150 Bus", "2x-1x MARS", "2x-1x OKP-7", "4x-1x SU230 Bus", "6x-3x Red Ring Scope",
          "6x-3x T Scope", "2.5x-1x M1C Scope", "1.5x-1x CH Sight", "3x-1x CH Sight Bus", "6x-3x DOS Scope",
          "3x YMA95-1 Scope", "4x-1x Type 11 Scope"]
Primary_optics = Secondary_optics = Underbarrel = Secondary_underbarrel = Primary_barrel = Secondary_barrel = Magazine = \
    Secondary_Magazine = Siderail = Secondary_siderail = Chamber = Secondary_chamber = Ammo = Secondary_Ammo = Stock = \
    Miscellaneous = Primary_training = Secondary_training = None

if mode == 0 or mode == 1:
    AmmoCarrier_SP = {None: 0, "Light Carrier": 1, "Heavy Carrier": 3}
    Armor_SP = {None: 0, "Light Armor": 1, "Heavy Armor": 3}
    if Side == 0:
        Secondary_weapons_SP = {None: 0, allSW[6]: 0, allSW[9]: 0, allSW[7]: 1, allSW[8]: 2, allSW[5]: 2}
        if mode == 0:
            Secondary_weapons_SP.update({allSW[1]: 1, allSW[3]: 2, allSW[2]: 2, allSW[4]: 3})
        Accessory_SP = {None: 0, "Gas Mask": 0}
        if night:
            Accessory_SP.update({"Civilian NVG AM": 2, "Civilian NVG GN": 2, "Military NVG AM": 3, "Military NVG GN": 3, "Military NVG WP": 3})
        if fighter == 1 or fighter == 7 or fighter == 8:
            Primary_weapons_SP = {None: 0, allPW[18]: 1, allPW[17]: 3, allPW[19]: 4, allPW[28]: 5, allPW[21]: 4, allPW[41]: 6, allPW[45]: 3}
            Explosives_SP = {None: 0, "M83 Smoke": 1, "F1 Frag": 2, "Molotov": 2}
            if mode == 0:
                Primary_weapons_SP.update({allPW[12]: 2, allPW[7]: 3, allPW[25]: 4, allPW[9]: 5, allPW[14]: 5, allPW[42]: 3, allPW[46]: 4})
                Explosives_SP.update({"M84 Flash": 1, "AN-M14 Incendiary": 2, "M67 Frag": 2})
        elif fighter == 2:
            Primary_weapons_SP = {None: 0, allPW[6]: 1, allPW[35]: 2, allPW[4]: 2, allPW[5]: 3, allPW[23]: 6}
            Explosives_SP = {None: 0, "M83 Smoke": 1, "M84 Flash": 1, "TM-62 Mine": 1, "F1 Frag": 2, "Molotov": 2, "IED": 3}
            if mode == 0:
                Primary_weapons_SP.update({allPW[3]: 2, allPW[34]: 2, allPW[2]: 3, allPW[1]: 4, allPW[16]: 5})
                Explosives_SP.update({"M19 Mine": 1, "AN-M14 Incendiary": 2, "M67 Frag": 2, "C-4": 3})
        elif fighter == 3:
            Primary_weapons_SP = {None: 0, allPW[10]: 2, allPW[11]: 3, allPW[20]: 4, allPW[29]: 5}
            Explosives_SP = {None: 0, "M83 Smoke": 1, "M84 Flash": 1, "F1 Frag": 2, "Molotov": 2}
            if mode == 0:
                Primary_weapons_SP.update({allPW[24]: 3, allPW[13]: 4, allPW[8]: 4, allPW[27]: 5})
                Explosives_SP.update({"AN-M14 Incendiary": 2, "M67 Frag": 2})
        elif fighter == 4:
            Primary_weapons_SP = {None: 0, allPW[18]: 1, allPW[17]: 3, allPW[19]: 4, allPW[28]: 5, allPW[21]: 4, allPW[41]: 6, allPW[45]: 3}
            Explosives_SP = {None: 0, "M83 Smoke": 1, "TM-62 Mine": 1, "F1 Frag": 2, "Molotov": 2, "IED": 3, "Panzerfaust 3": 3, "RPG-7": 4}
            if mode == 0:
                Primary_weapons_SP.update({allPW[12]: 2, allPW[7]: 3, allPW[25]: 4, allPW[9]: 5, allPW[14]: 5, allPW[42]: 3, allPW[46]: 4})
                Explosives_SP.update({"M84 Flash": 1, "M19 Mine": 1, "AN-M14 Incendiary": 2, "M67 Frag": 2, "C-4": 3, "AT4": 3, "M3 MAAWS": 4})
        elif fighter == 5:
            Primary_weapons_SP = {None: 0, allPW[37]: 1, allPW[43]: 2, allPW[40]: 3, allPW[38]: 4}
            Explosives_SP = {None: 0, "M83 Smoke": 1, "F1 Frag": 2, "Molotov": 2}
            if mode == 0:
                Primary_weapons_SP.update({allPW[36]: 1, allPW[39]: 3, allPW[44]: 4, allPW[26]: 5})
                Explosives_SP.update({"M84 Flash": 1, "AN-M14 Incendiary": 2, "M67 Frag": 2})
        elif fighter == 6:
            Primary_weapons_SP = {None: 0, allPW[22]: 2, allPW[32]: 3, allPW[33]: 4}
            Explosives_SP = {None: 0, "M83 Smoke": 1, "TM-62 Mine": 1, "F1 Frag": 2, "Molotov": 2}
            if mode == 0:
                Primary_weapons_SP.update({allPW[15]: 2, allPW[30]: 3, allPW[31]: 4})
                Explosives_SP.update({"M84 Flash": 1, "M19 Mine": 1, "AN-M14 Incendiary": 2, "M67 Frag": 2})
    elif Side == 1:
        Secondary_weapons_SP = {None: 0, allSW[1]: 1, allSW[3]: 2, allSW[2]: 2, allSW[4]: 3}
        if mode == 0:
            Secondary_weapons_SP.update({allSW[6]: 0, allSW[9]: 0, allSW[7]: 1, allSW[8]: 2, allSW[5]: 2})
        Accessory_SP = {None: 0, "Gas Mask": 1}
        if night:
            Accessory_SP.update({"Mil-Spec NVG AM": 2, "Mil-Spec NVG GN": 2, "Mil-Spec NVG WP": 2, "SOF NVG AM": 3, "SOF NVG GN": 3, "SOF NVG WP": 3, "SOF NVG MC": 4})
        if fighter == 1 or fighter == 4 or fighter == 7 or fighter == 8:
            Primary_weapons_SP = {None: 0, allPW[12]: 2, allPW[7]: 3, allPW[25]: 4, allPW[9]: 5, allPW[14]: 5, allPW[42]: 3, allPW[46]: 4}
            Explosives_SP = {None: 0, "M83 Smoke": 1, "AN-M14 Incendiary": 2, "M67 Frag": 2}
            if mode == 1 and fighter == 4:
                Explosives_SP = {None: 0, "M83 Smoke": 1, "M84 Flash": 1, "M19 Mine": 1, "AN-M14 Incendiary": 2, "M67 Frag": 2, "C-4": 3, "AT4": 3, "M3 MAAWS": 4}
            if mode == 0:
                Primary_weapons_SP.update({allPW[18]: 1, allPW[17]: 3, allPW[19]: 4, allPW[28]: 5, allPW[21]: 4, allPW[41]: 6, allPW[45]: 3})
                Explosives_SP.update({"M84 Flash": 1, "F1 Frag": 2, "Molotov": 2})
                if fighter == 4:
                    Explosives_SP.update({"TM-62 Mine": 1, "IED": 3, "Panzerfaust 3": 3, "RPG-7": 4})
        elif fighter == 2:
            Primary_weapons_SP = {None: 0, allPW[3]: 2, allPW[34]: 2, allPW[2]: 3, allPW[1]: 4, allPW[16]: 5}
            Explosives_SP = {None: 0, "M83 Smoke": 1, "M84 Flash": 1, "M19 Mine": 1, "AN-M14 Incendiary": 2, "M67 Frag": 2, "C-4": 3}
            if mode == 0:
                Primary_weapons_SP.update({allPW[6]: 1, allPW[35]: 2, allPW[4]: 2, allPW[5]: 3, allPW[23]: 6})
                Explosives_SP.update({"TM-62 Mine": 1, "F1 Frag": 2, "Molotov": 2, "IED": 3})
        elif fighter == 3:
            Primary_weapons_SP = {None: 0, allPW[24]: 3, allPW[13]: 4, allPW[8]: 4, allPW[27]: 5}
            Explosives_SP = {None: 0, "M83 Smoke": 1, "M84 Flash": 1, "AN-M14 Incendiary": 2, "M67 Frag": 2}
            if mode == 0:
                Primary_weapons_SP.update({allPW[10]: 2, allPW[11]: 3, allPW[20]: 4, allPW[29]: 5})
                Explosives_SP.update({"F1 Frag": 2, "Molotov": 2})
        elif fighter == 5:
            Primary_weapons_SP = {None: 0, allPW[36]: 1, allPW[39]: 3, allPW[44]: 4, allPW[26]: 5}
            Explosives_SP = {None: 0, "M83 Smoke": 1, "AN-M14 Incendiary": 2, "M67 Frag": 2}
            if mode == 0:
                Primary_weapons_SP.update({allPW[37]: 1, allPW[43]: 2, allPW[40]: 3, allPW[38]: 4})
                Explosives_SP.update({"M84 Flash": 1, "F1 Frag": 2, "Molotov": 2})
        elif fighter == 6:
            Primary_weapons_SP = {None: 0, allPW[15]: 2, allPW[30]: 3, allPW[31]: 4}
            Explosives_SP = {None: 0, "M83 Smoke": 1, "M19 Mine": 1, "AN-M14 Incendiary": 2, "M67 Frag": 2}
            if mode == 0:
                Primary_weapons_SP.update({allPW[22]: 2, allPW[32]: 3, allPW[33]: 4})
                Explosives_SP.update({"M84 Flash": 1, "TM-62 Mine": 1, "F1 Frag": 2, "Molotov": 2})
elif mode == 2:
    #AmmoCarrier_SP = {None: 0, "Light Carrier": 3, "Heavy Carrier": 4}
    AmmoCarrier_SP = {None: 0}
    Armor_SP = {None: 0, "Light Armor": 2, "Heavy Armor": 4}
    if Side == 0:
        Secondary_weapons_SP = {None: 0, allSW[6]: 0, allSW[9]: 0, allSW[7]: 1, allSW[8]: 2, allSW[5]: 2}
        Accessory_SP = {None: 0, "Gas Mask": 0}
        Explosives_SP = {None: 0, "M83 Smoke": 1, "F1 Frag": 2, "Molotov": 2}
        if fighter == 0:
            Primary_weapons_SP = {None: 0, allPW[10]: 3, allPW[18]: 3, allPW[20]: 4, allPW[43]: 4, allPW[17]: 5, allPW[28]: 6,
                                  allPW[19]: 6, allPW[21]: 6, allPW[38]: 6, allPW[29]: 7, allPW[41]: 8}
        elif fighter == 1:
            Primary_weapons_SP = {None: 0, allPW[6]: 3, allPW[35]: 3, allPW[4]: 4, allPW[11]: 6, allPW[5]: 6, allPW[23]: 8}
            Explosives_SP.update({"M84 Flash": 1})
        elif fighter == 2:
            Primary_weapons_SP = {None: 0, allPW[37]: 1, allPW[40]: 5}
    elif Side == 1:
        Secondary_weapons_SP = {None: 0, allSW[1]: 1, allSW[3]: 2, allSW[2]: 2, allSW[4]: 3}
        Accessory_SP = {None: 0, "Gas Mask": 1}
        Explosives_SP = {None: 0, "M83 Smoke": 1, "M67 Frag": 2, "AN-M14 Incendiary": 2}
        if fighter == 0:
            Primary_weapons_SP = {None: 0, allPW[12]: 4, allPW[24]: 4, allPW[7]: 5, allPW[13]: 5, allPW[25]: 6,
                                  allPW[9]: 7, allPW[26]: 7, allPW[27]: 7, allPW[14]: 8, allPW[42]: 5, allPW[44]: 6}
        if fighter == 1:
            Primary_weapons_SP = {None: 0, allPW[34]: 3, allPW[3]: 4, allPW[2]: 6, allPW[1]: 6, allPW[16]: 7, allPW[8]: 7}
            Explosives_SP.update({"M84 Flash": 1})
        if fighter == 2:
            Primary_weapons_SP = {None: 0, allPW[36]: 1, allPW[39]: 5}

#Choosing primary weapon
primary_weapons = list(Primary_weapons_SP.keys())
print("Choose your primary weapon:")
print("0 Random")
for i in range(1, len(primary_weapons)):
    print(i, primary_weapons[i], "(", Primary_weapons_SP[primary_weapons[i]], ")")
choice = inputHandler(len(primary_weapons)-1)
if choice == 0:
    # 5% chance of getting no weapon
    if random.random() <= 0.05:
        choice = 0
    else:
        choice = random.randint(1, len(primary_weapons) - 1)
    # print(choice)
PrimW = primary_weapons[choice]
print("Your primary weapon is", PrimW, "(", Primary_weapons_SP[PrimW], ")")
if PrimW == None:
    print("That's right! Challenge yourself")
supply -= Primary_weapons_SP[PrimW]
#print("supply points", supply)

x = ["Secondary_weapons_SP", "Explosives_SP", "Armor_SP", "AmmoCarrier_SP", "Accessory_SP"]
random.shuffle(x)
for dict in x:
    if dict == "Secondary_weapons_SP":
        # Choosing random secondary weapon
        SecW, supply = ChooseItem(Secondary_weapons_SP, supply)
        if SecW: print("Secondary is", SecW, "(", Secondary_weapons_SP[SecW], ")")
        # print("supply points", supply)
    elif dict == "Explosives_SP":
        #Choosing random first explosive
        expl1, supply = ChooseItem(Explosives_SP, supply)
        exSp = Explosives_SP[expl1]
        if expl1 == "C-4" or expl1 == "IED":
            del Explosives_SP[expl1]
            if mode == 0:
                Explosives_SP.pop("M3 MAAWS", None)
                Explosives_SP.pop("RPG-7", None)
        if any(expl1 == i for i in ["Panzerfaust 3", "RPG-7", "AT4", "M3 MAAWS"]):
            Explosives_SP.pop("Panzerfaust 3", None)
            Explosives_SP.pop("RPG-7", None)
            Explosives_SP.pop("AT4", None)
            Explosives_SP.pop("M3 MAAWS", None)
            if mode == 0 and any(expl1 == j for j in ["RPG-7", "M3 MAAWS"]):
                Explosives_SP.pop("C-4", None)
        if expl1: print("First explosive is", expl1, "(", exSp, ")")
        #print("supply points", supply)
    elif dict == "Armor_SP":
        # Choosing random armor
        armor, supply = ChooseItem(Armor_SP, supply)
        if armor: print("Armor is", armor, "(", Armor_SP[armor], ")")
        # print("supply points", supply)
    elif dict == "AmmoCarrier_SP":
        # Choosing random ammo carrier
        carrier, supply = ChooseItem(AmmoCarrier_SP, supply)
        if carrier: print("Ammo carrier is", carrier, "(", AmmoCarrier_SP[carrier], ")")
        # print("supply points", supply)
    elif dict == "Accessory_SP":
        item, supply = ChooseItem(Accessory_SP, supply)
        if item: print("Accessory is", item, "(", Accessory_SP[item], ")")

# Setting attachments for primary
if PrimW:
    if PrimW == "MP7":
        Primary_optics = {Optics[0]: 0, Optics[1]: 1, Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Magazine = {None: 0, "Extended Magazine": 4}
        Siderail = {None: 0, "Laser sight": 2}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2,
                                   Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[1]: 1, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2,
                              Optics[5]: 2, Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2,
                              Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Magazine = {None: 0, "Extended Magazine": 5}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "MP5A5":
        Primary_optics = {Optics[0]: 0, Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Magazine = {None: 0, "Extended Magazine": 3}
        Siderail = {None: 0, "Laser sight": 2}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2,
                                   Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "Grease Gun":
        Primary_optics = {Optics[0]: 0, Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2}
        # Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Suppressor": 3, "Advanced suppressor": 6}
        Siderail = {None: 0, "Laser sight": 2}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2,
                                   Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Primary_barrel = {None: 0, "Flash Hider": 1, "Suppressor": 4, "Advanced suppressor": 7}
    elif PrimW == "Uzi":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Magazine = {None: 0, "Extended Magazine": 1}
        Siderail = {None: 0, "Laser sight": 2}
        if mode == 0:
            Primary_optics.update({Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2,
                                   Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4})
            Magazine.update({"Drum Magazine": 3})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
            Magazine = {None: 0, "Extended Magazine": 2}
    elif PrimW == "MP5A2":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Magazine = {None: 0, "Extended Magazine": 3}
        Siderail = {None: 0, "Laser sight": 2}
        if mode == 0:
            Primary_optics.update({Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2,
                                   Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "Sterling":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Suppressor": 3}
        Magazine = {None: 0, "Extended Magazine": 3}
        Siderail = {None: 0, "Laser sight": 2}
        if mode == 0:
            Primary_optics.update({Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2,
                                   Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
    elif PrimW == "G36K":
        Primary_optics = {Optics[0]: 0, Optics[33]: 1, Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2,
                          Optics[11]: 2, Optics[34]: 2, Optics[14]: 3, Optics[16]: 3, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Magazine = {None: 0, "Extended Magazine": 1}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if fighter == 1:
            Underbarrel.update({"Smoke Launcher": 1, "Bipod": 2, "Recoil grip Bipod": 4})
        if fighter == 4:
            Underbarrel.update({"Explosive Launcher": 3})
        if fighter == 7 or fighter == 8:
            Underbarrel.update({"Smoke Launcher": 1})
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 3})
            Primary_barrel.update({"Suppressor": 3})
            if fighter == 7 or fighter == 8:
                Underbarrel.update({"Bipod": 2, "Recoil grip Bipod": 4})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Underbarrel.update({"Recoil grip Bipod": 5})
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "Mk 18 CQBR":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[6]: 1,
                          Optics[7]: 1, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2,
                          Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Magazine = {None: 0, "Extended Magazine": 1}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Underbarrel.update({"Recoil grip Bipod": 4})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Underbarrel.update({"Recoil grip Bipod": 5})
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "M4A1":
        Primary_optics = {Optics[0]: 0, Optics[1]: 1, Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2,
                          Optics[14]: 3, Optics[16]: 3, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3,
                       "Recoil grip": 3, "M26 MASS": 3, "Masterkey": 4}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Magazine = {None: 0, "Extended Magazine": 1}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        # Miscellaneous = {None: 0, "Flat Top": 1}
        if fighter == 1:
            Underbarrel.update({"Smoke Launcher": 1, "Recoil grip Bipod": 4})
        if fighter == 4:
            Underbarrel.update({"Explosive Launcher": 3})
        if fighter == 7 or fighter == 8:
            Underbarrel.update({"Smoke Launcher": 1})
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 4})
            Primary_barrel.update({"Suppressor": 3})
            Magazine.update({"Drum Magazine": 3})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[1]: 1, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Underbarrel.update({"Recoil grip Bipod": 5})
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "SKS":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[6]: 1,
                          Optics[7]: 1, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2,
                          Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Magazine = {None: 0, "Extended Magazine": 2}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[21]: 2, Optics[22]: 2, Optics[30]: 3, Optics[31]: 3})
            Underbarrel.update({"Bipod": 2})
            Magazine.update({"Drum Magazine": 3})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "AKS-74U":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[6]: 1,
                          Optics[7]: 1, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2,
                          Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Magazine = {None: 0, "Extended Magazine": 1}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Magazine.update({"Drum Magazine": 3})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 3, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "M16A4":
        Primary_optics = {Optics[0]: 0, Optics[1]: 1, Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2,
                          Optics[14]: 3, Optics[16]: 3, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3, "M26 MASS": 3, "Masterkey": 4}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Magazine = {None: 0, "Extended Magazine": 1}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        #Miscellaneous = {None: 0, "Flat Top": 1}
        if fighter == 1:
            Underbarrel.update({"Smoke Launcher": 1, "Bipod": 2, "Recoil grip Bipod": 4})
        elif fighter == 4:
            Underbarrel.update({"Explosive Launcher": 3})
        elif fighter == 7 or fighter == 8:
            Underbarrel.update({"Smoke Launcher": 1})
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 4})
            Primary_barrel.update({"Suppressor": 3})
            Magazine.update({"Drum Magazine": 3})
            if fighter == 7 or fighter == 8:
                Underbarrel.update({"Smoke Launcher": 1, "Bipod": 2, "Recoil grip Bipod": 4})
        elif mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[1]: 1, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Underbarrel.update({"Recoil grip Bipod": 5})
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "L85A2":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[6]: 1,
                          Optics[7]: 1, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2, Optics[20]: 2,
                          Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Magazine = {None: 0, "Extended Magazine": 1}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Underbarrel.update({"Bipod": 2, "Recoil grip Bipod": 4})
            Magazine.update({"Drum Magazine": 3})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[20]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Underbarrel.update({"Recoil grip Bipod": 5})
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "VHS-2":
        Primary_optics = {Optics[0]: 0, Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2, Optics[14]: 3, Optics[16]: 3, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Magazine = {None: 0, "Extended Magazine": 1}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if fighter == 1:
            Underbarrel.update({"Smoke Launcher": 1, "Recoil grip Bipod": 4})
        if fighter == 4:
            Underbarrel.update({"Explosive Launcher": 3})
        if fighter == 7 or fighter == 8:
            Underbarrel.update({"Smoke Launcher": 1})
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 4})
            Primary_barrel.update({"Suppressor": 3})
            Magazine.update({"Drum Magazine": 3})
            if fighter == 7 or fighter == 8:
                Underbarrel.update({"Recoil grip Bipod": 4})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Underbarrel.update({"Recoil grip Bipod": 5})
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "Galil SAR":
        Primary_optics = {Optics[0]: 0, Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2, Optics[14]: 3, Optics[16]: 3, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3, "Recoil grip Bipod": 4}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Magazine = {None: 0, "Drum Magazine": 3}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 4})
            Primary_barrel.update({"Suppressor": 3})
    elif PrimW == "Honey Badger":
        Primary_optics = {Optics[0]: 0, Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2,
                                   Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 5}
    elif PrimW == "AKM":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2,
                          Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Smoke Launcher": 1, "Loading grip": 2, "Buckshot Launcher": 2,
                       "Aiming grip": 3, "Recoil grip": 3, "Masterkey": 4}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Magazine = {None: 0, "Extended Magazine": 1}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2, Optics[16]: 3, Optics[29]: 4})
            Primary_barrel.update({"Suppressor": 3})
            Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Buckshot Launcher": 2, "Aiming grip": 3, "Recoil grip": 4, "Masterkey": 4}
            Magazine.update({"Drum Magazine": 3})
        if fighter == 4:
            Underbarrel = {None: 0, "Quick draw grip": 1, "Explosive Launcher": 3, "Loading grip": 2, "Buckshot Launcher": 2, "Aiming grip": 3, "Recoil grip": 3, "Masterkey": 4}
        if fighter == 1 or (mode == 0 and (fighter == 7 or fighter == 8)):
            Underbarrel.update({"Bipod": 2})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Buckshot Launcher": 2, "Aiming grip": 3, "Recoil grip": 3, "Masterkey": 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "M16A2":
        Primary_optics = {Optics[0]: 0, Optics[12]: 2, Optics[15]: 3, Optics[26]: 4}
        Underbarrel = {None: 0, "Smoke Launcher": 1, "Recoil grip": 3, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Masterkey": 4}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Magazine = {None: 0, "Extended Magazine": 1}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_barrel.update({"Suppressor": 3})
            Magazine.update({"Drum Magazine": 3})
        if fighter == 1 or (mode == 0 and (fighter == 7 or fighter == 8)):
            Underbarrel.update({"Bipod": 2})
        if fighter == 4:
            Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Explosive Launcher": 3, "Recoil grip": 3, "Masterkey": 4}
        if mode == 2:
            Underbarrel = {None: 0, "Recoil grip": 3, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Masterkey": 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "AK-74":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2,
                          Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Smoke Launcher": 1, "Loading grip": 2, "Buckshot Launcher": 2, "Aiming grip": 3, "Recoil grip": 3, "Masterkey": 4}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Magazine = {None: 0, "Extended Magazine": 1}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2, Optics[16]: 3, Optics[29]: 4})
            Primary_barrel.update({"Suppressor": 3})
            Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Buckshot Launcher": 2, "Aiming grip": 3, "Recoil grip": 4, "Masterkey": 4}
            Magazine.update({"Drum Magazine": 3})
        if fighter == 4:
            Underbarrel = {None: 0, "Quick draw grip": 1, "Explosive Launcher": 3, "Loading grip": 2, "Buckshot Launcher": 2, "Aiming grip": 3, "Recoil grip": 3, "Masterkey": 4}
        if fighter == 1 or (mode == 0 and (fighter == 7 or fighter == 8)):
            Underbarrel.update({"Bipod": 2})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Buckshot Launcher": 2, "Aiming grip": 3, "Recoil grip": 3, "Masterkey": 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "Alpha AK":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[6]: 1,
                          Optics[7]: 1, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2,
                          Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Magazine = {None: 0, "Extended Magazine": 1}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[21]: 2, Optics[22]: 2, Optics[30]: 3, Optics[31]: 3})
            Magazine.update({"Drum Magazine": 3})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "QBZ-03":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2,
                          Optics[27]: 2, Optics[28]: 2, Optics[13]: 2, Optics[15]: 3, Optics[26]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Magazine = {None: 0, "Extended Magazine": 1}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if fighter == 1:
                Underbarrel = {None: 0, "Bipod": 2, "Recoil grip": 3}
        if mode == 0:
            Primary_optics.update({Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2, Optics[14]: 3, Optics[16]: 3, Optics[29]: 4})
            Primary_barrel.update({"Suppressor": 3})
            Magazine.update({"Drum Magazine": 3})
        if fighter == 1 or (mode == 0 and (fighter == 7 or fighter == 8)):
            Underbarrel.update({"Bipod": 2})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[13]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "Galil":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Magazine = {None: 0, "Drum Magazine": 3}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2, Optics[14]: 3, Optics[16]: 3, Optics[29]: 4})
            Underbarrel.update({"Recoil grip Bipod": 4})
            Primary_barrel.update({"Suppressor": 3})
    elif PrimW == "AS Val":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Magazine = {None: 0, "Extended Magazine": 2}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[19]: 1, Optics[9]: 2, Optics[11]: 2, Optics[14]: 3,
                                   Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[19]: 1, Optics[8]: 3, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
    elif PrimW == "Mk 17 Mod 0":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[6]: 1,
                          Optics[7]: 1, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2,
                          Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Magazine = {None: 0, "Extended Magazine": 2}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[21]: 2, Optics[22]: 2, Optics[30]: 3, Optics[31]: 3})
            Underbarrel.update({"Bipod": 2, "Recoil grip Bipod": 4})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Underbarrel.update({"Recoil grip Bipod": 5})
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "G3A3":
        Primary_optics = {Optics[0]: 0, Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2, Optics[14]: 3, Optics[16]: 3, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if fighter == 1:
            Underbarrel.update({"Bipod": 2, "Recoil grip Bipod": 4})
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 4})
            Primary_barrel.update({"Suppressor": 3})
            Magazine = {None: 0, "Extended Magazine": 2}
            if fighter == 7 or fighter == 8:
                Underbarrel.update({"Bipod": 2, "Recoil grip Bipod": 4})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Underbarrel.update({"Recoil grip Bipod": 5})
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "Mk 14 EBR":
        Primary_optics = {Optics[0]: 0, Optics[22]: 2, Optics[14]: 3, Optics[16]: 3, Optics[30]: 3, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Bipod": 2, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3, "Recoil grip Bipod": 4}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[6]: 1, Optics[7]: 1,
                                   Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[31]: 3, Optics[26]: 4})
            Siderail = {None: 0, "Laser sight": 2}
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Underbarrel.update({"Recoil grip Bipod": 5})
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
            Siderail = {None: 0, "Laser sight": 2}
    elif PrimW == "Tavor 7":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[6]: 1,
                          Optics[7]: 1, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2,
                          Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Magazine = {None: 0, "Extended Magazine": 2}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "FAL":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2, Optics[14]: 3, Optics[16]: 3, Optics[29]: 4})
            Primary_barrel.update({"Suppressor": 3})
            Magazine = {None: 0, "Extended Magazine": 2}
        if fighter == 1 or (mode == 0 and (fighter == 7 or fighter == 8)):
            Underbarrel.update({"Bipod": 2})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "ACE 52":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[6]: 1,
                          Optics[7]: 1, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2,
                          Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Magazine = {None: 0, "Extended Magazine": 2}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[21]: 2, Optics[22]: 2, Optics[30]: 3, Optics[31]: 3})
            Underbarrel.update({"Bipod": 2})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "M249":
        Primary_optics = {Optics[0]: 0, Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2, Optics[14]: 3, Optics[16]: 3, Optics[29]: 4}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Siderail = {None: 0, "Laser sight": 2}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 4})
            Primary_barrel.update({"Suppressor": 3})
    elif PrimW == "M240B":
        Primary_optics = {Optics[0]: 0, Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2, Optics[14]: 3, Optics[16]: 3, Optics[29]: 4}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Magazine = {None: 0, "Extended Magazine": 3}
        Siderail = {None: 0, "Laser sight": 2}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 4})
            Primary_barrel.update({"Suppressor": 3})
    elif PrimW == "PKM":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 4}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Siderail = {None: 0, "Laser sight": 2}
        if mode == 0:
            Primary_optics.update({Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2, Optics[16]: 3, Optics[29]: 4})
            Primary_barrel.update({"Suppressor": 3})
    elif PrimW == "MG3":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 4}
        Magazine = {None: 0, "Extended Magazine": 3}
        Siderail = {None: 0, "Laser sight": 2}
        if mode == 0:
            Primary_optics.update({Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2, Optics[14]: 3, Optics[16]: 3, Optics[29]: 4})
            Primary_barrel = {"Suppressor": 3}
    elif PrimW == "M870":
        Primary_optics = {Optics[0]: 0, Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Compensator": 3, "Suppressor": 3}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Flechette Rounds": 1, "Slug Rounds": 1}
        if mode == 0:
            Primary_optics.update({Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[16]: 3, Optics[29]: 4})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2, Optics[6]: 2,
                              Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2, Optics[16]: 3}
            Primary_barrel = {None: 0, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "TOZ-194":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Compensator": 3, "Suppressor": 3}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Flechette Rounds": 1, "Slug Rounds": 1}
        if mode == 0:
            Primary_optics.update({Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2, Optics[16]: 3, Optics[29]: 4})
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2, Optics[6]: 2,
                              Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2, Optics[16]: 3}
            Primary_barrel = {None: 0, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "M24":
        Primary_optics = {Optics[0]: 0, Optics[22]: 2, Optics[14]: 3, Optics[16]: 3, Optics[30]: 3, Optics[29]: 4}
        Chamber = {None: 0, "Greased bolt": 2}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Bipod": 2, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[7]: 1,
                                   Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[31]: 3, Optics[26]: 4})
            Siderail = {None: 0, "Laser sight": 2}
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[7]: 2, Optics[9]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2, Optics[14]: 2,
                              Optics[22]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[30]: 3, Optics[31]: 3, Optics[26]: 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
            Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
    elif PrimW == "Mosin-Nagant":
        Primary_optics = {Optics[0]: 0, Optics[18]: 1, Optics[21]: 2, Optics[15]: 3, Optics[31]: 3, Optics[26]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Bipod": 2, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Magazine = {None: 0, "Stripper Clip": 1}
        Ammo = {None: 0, "Tracer Rounds": 0}
        Chamber = {None: 0, "Greased bolt": 2}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[6]: 1,
                                   Optics[7]: 1, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2,
                                   Optics[22]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[30]: 3, Optics[29]: 4})
            Siderail = {None: 0, "Laser sight": 2}
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[18]: 1, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2, Optics[6]: 2,
                              Optics[7]: 2, Optics[9]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2, Optics[14]: 2,
                              Optics[22]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[30]: 3, Optics[31]: 3, Optics[26]: 4}
            Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "M1 Garand":
        Primary_optics = {Optics[0]: 0, Optics[32]: 2, Optics[21]: 2, Optics[15]: 3, Optics[31]: 3, Optics[26]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Smoke Launcher": 1, "Bipod": 2, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3, "Explosive Launcher": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Suppressor": 3}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[6]: 1,
                                   Optics[7]: 1, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2,
                                   Optics[22]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[30]: 3, Optics[29]: 4})
            Siderail = {None: 0, "Laser sight": 2}
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2, Optics[6]: 2,
                              Optics[7]: 2, Optics[32]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2, Optics[14]: 2,
                              Optics[22]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
    elif PrimW == "SVD":
        Primary_optics = {Optics[0]: 0, Optics[19]: 1, Optics[21]: 2, Optics[15]: 3, Optics[31]: 3, Optics[26]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Bipod": 2, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Magazine = {None: 0, "Extended Magazine": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[6]: 1,
                                   Optics[7]: 1, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2,
                                   Optics[22]: 2, Optics[14]: 3, Optics[16]: 3, Optics[30]: 3, Optics[29]: 4})
            Siderail = {None: 0, "Laser sight": 2}
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[19]: 1, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Siderail = {None: 0, "Laser sight": 2}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
            Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
    elif PrimW == "M82A1 CQ":
        Primary_optics = {Optics[0]: 0, Optics[22]: 2, Optics[14]: 3, Optics[16]: 3, Optics[30]: 3, Optics[29]: 4}
        Magazine = {None: 0, "Extended Magazine": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[6]: 1, Optics[7]: 1,
                                   Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[31]: 3, Optics[26]: 4})
            Siderail = {None: 0, "Laser sight": 2}
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2,
                              Optics[22]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[30]: 3, Optics[31]: 3, Optics[26]: 4}
    elif PrimW == "M110 SASS":
        Primary_optics = {Optics[0]: 0, Optics[22]: 2, Optics[14]: 3, Optics[16]: 3, Optics[35]: 3, Optics[30]: 3, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Bipod": 2, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3, "Recoil grip bipod": 4}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3, "Suppressor": 3}
        Magazine = {None: 0, "Extended Magazine": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[6]: 1, Optics[7]: 1,
                                   Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2, Optics[21]: 2, Optics[15]: 3, Optics[31]: 3, Optics[26]: 4})
            Siderail = {None: 0, "Laser sight": 2}
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[35]: 3, Optics[26]: 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 3}
    elif PrimW == "M99":
        Primary_optics = {Optics[0]: 0, Optics[23]: 1, Optics[21]: 2, Optics[15]: 3, Optics[31]: 3, Optics[26]: 4}
        Magazine = {None: 0, "Extended Magazine": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[2]: 1, Optics[3]: 1, Optics[4]: 1, Optics[5]: 1, Optics[6]: 1,
                                   Optics[7]: 1, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2,
                                   Optics[14]: 3, Optics[16]: 3, Optics[30]: 3, Optics[29]: 4})
            Siderail = {None: 0, "Laser sight": 2}
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[23]: 1, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[11]: 2, Optics[27]: 2, Optics[28]: 2,
                              Optics[22]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[30]: 3, Optics[31]: 3, Optics[26]: 4}
            Underbarrel = {None: 0, "Bipod": 2}
    elif PrimW == "FAMAS F1":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Smoke Launcher": 1, "Bipod": 2, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3, "Masterkey": 4}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if fighter == 4:
            Underbarrel = {None: 0, "Quick draw grip": 1, "Bipod": 2, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3, "Explosive Launcher": 3, "Masterkey": 4}
        if mode == 0:
            Primary_optics.update({Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2, Optics[14]: 3, Optics[16]: 3, Optics[29]: 4})
            Primary_barrel.update({"Suppressor": 3})
            Magazine = {None: 0, "Extended Magazine": 1}
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3, "Masterkey": 4}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "AUG A3":
        Primary_optics = {Optics[0]: 0, Optics[24]: 1, Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2,
                          Optics[11]: 2, Optics[25]: 2, Optics[14]: 3, Optics[16]: 3, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Smoke Launcher": 1, "Loading grip": 2, "Aiming grip": 3,
                       "Recoil grip": 3, "M26 MASS": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if fighter == 4:
            Underbarrel = {None: 0, "Quick draw grip": 1, "Explosive Launcher": 3, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3, "M26 MASS": 3}
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 3})
            Primary_barrel.update({"Suppressor": 3})
            Magazine = {None: 0, "Extended Magazine": 1}
        if mode == 2:
            Primary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[2]: 2, Optics[3]: 2, Optics[4]: 2, Optics[5]: 2,
                              Optics[6]: 2, Optics[7]: 2, Optics[9]: 2, Optics[10]: 2, Optics[11]: 2, Optics[27]: 2,
                              Optics[28]: 2, Optics[14]: 3, Optics[15]: 3, Optics[16]: 3, Optics[26]: 4}
            Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3, "M26 MASS": 3}
            Primary_barrel = {None: 0, "Flash Hider": 2, "Compensator": 4, "Suppressor": 4}
    elif PrimW == "QBZ-97":
        Primary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[36]: 1, Optics[10]: 2,
                          Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Buckshot Launcher": 2,
                       "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Magazine = {None: 0, "Extended Magazine": 1}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if fighter == 1:
            Underbarrel.update({"Smoke Launcher": 1, "Bipod": 2})
        if fighter == 4:
            Underbarrel.update({"Explosive Launcher": 3})
        if fighter == 7 or fighter == 8:
            Underbarrel.update({"Smoke Launcher": 1})
        if mode == 0:
            Primary_optics.update({Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2, Optics[11]: 2, Optics[14]: 3, Optics[16]: 3, Optics[29]: 4})
            Primary_barrel.update({"Suppressor": 3})
            Magazine = {None: 0, "Drum Magazine": 3}
            if fighter == 7 or fighter == 8:
                Underbarrel.update({"Bipod": 2})
    elif PrimW == "QTS-11":
        Primary_optics = {Optics[0]: 0, Optics[37]: 1, Optics[2]: 1, Optics[5]: 1, Optics[7]: 1, Optics[9]: 2,
                          Optics[11]: 2, Optics[14]: 3, Optics[16]: 3, Optics[29]: 4}
        Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        Primary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 3}
        Magazine = {None: 0, "Extended Magazine": 1}
        Siderail = {None: 0, "Laser sight": 2}
        Ammo = {None: 0, "Tracer Rounds": 0}
        if fighter == 1:
            Underbarrel.update({"Smoke Launcher": 1, "Bipod": 2, "Recoil grip Bipod": 4})
        if fighter == 4:
            Underbarrel.update({"Explosive Launcher": 3})
        if fighter == 7 or fighter == 8:
            Underbarrel.update({"Smoke Launcher": 1})
        if mode == 0:
            Primary_optics.update({Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1, Optics[10]: 2, Optics[27]: 2, Optics[28]: 2, Optics[15]: 3, Optics[26]: 3})
            Primary_barrel.update({"Suppressor": 3})
            if fighter == 7 or fighter == 8:
                Underbarrel.update({"Bipod": 2, "Recoil grip Bipod": 4})

# Setting attachments for secondary
if SecW == "Welrod":
    Secondary_optics = {Optics[0]: 0, Optics[8]: 1, Optics[3]: 1, Optics[4]: 1, Optics[6]: 1}
    Secondary_chamber = {None: 0, "Greased bolt": 2}
    Secondary_underbarrel = {None: 0, "Recoil grip": 3}
    Secondary_siderail = {None: 0, "Laser sight": 2}
    Secondary_Ammo = {None: 0, "Tracer Rounds": 0, "AP Rounds": 3, "AP Tracer Rounds": 3}
    Stock = {None: 0, "Quick Draw Holster": 1}
    if mode == 0 or fighter == 3:
        Secondary_optics.update({Optics[2]: 1, Optics[5]: 1, Optics[7]: 1})
    if mode == 1 and fighter == 5:
        Secondary_optics == None
        Secondary_siderail = None
    if mode == 2:
        Secondary_optics = {Optics[0]: 0, Optics[8]: 2, Optics[3]: 2, Optics[4]: 2, Optics[6]: 2, Optics[2]: 2, Optics[5]: 2, Optics[7]: 2}
        Stock = {None: 0, "Quick Draw Holster": 2}
        if fighter == 2:
            Secondary_siderail = None
    if fighter == 1 or fighter == 5 or (mode == 0 and fighter != 2 and fighter != 4):
        Secondary_underbarrel.update({None: 0, "Bipod": 2, "Recoil grip": 3, "Recoil grip Bipod": 4})
elif SecW:
    Secondary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 1}
    Secondary_Magazine = {None: 0, "Extended Magazine": 1}
    Secondary_siderail = {None: 0, "Laser sight": 1}
    Stock = {None: 0, "Quick Draw Holster": 1}
    if mode == 0:
        Secondary_barrel.update({"Suppressor": 2})
    if mode == 2:
        Secondary_barrel = {None: 0, "Flash Hider": 1, "Compensator": 2, "Suppressor": 2}
        if Side == 0 and fighter == 2:
            Secondary_Magazine = {None: 0, "Extended Magazine": 1}
        else:
            Secondary_Magazine = {None: 0, "Extended Magazine": 2}
        Stock = {None: 0, "Quick Draw Holster": 2}

if night:
    if Secondary_siderail:
        Secondary_siderail.update({"Flashlight": 1, "IR Flashlight": 1, "IR Laser Sight": 1})
    if Siderail:
        Siderail.update({"Flashlight": 1, "IR Flashlight": 1, "IR Laser Sight": 1})
    if any(PrimW == i for i in ["AKM", "AK-74", "QBZ-03", "FAL", "FAMAS F1", "Galil", "PKM", "MG3"]):
        Primary_optics.update({"4x M150 NV": 3})
        if mode == 0:
            if any(PrimW == i for i in ["AKM", "AK-74", "PKM"]):
                Primary_optics.update({"4x SU230 NV": 3})
            else:
                Primary_optics.update({"4x C79 NV": 3, "4x SU230 NV": 3})
    elif any(PrimW == i for i in ["Mosin-Nagant", "M1 Garand", "M99", "SVD"]):
        Primary_optics.update({"7x Hunting Scope NV": 2, "4x M150 NV": 3})
        if mode == 0 and (PrimW == "Mosin-Nagant" or PrimW == "SVD"):
            Primary_optics.update({"7x Sniper Scope NV": 2})
    elif any(PrimW == i for i in ["SKS", "AKS-74U", "Alpha AK", "ACE 52", "Mk 17 Mod 0", "L85A2", "Mk 18 CQBR", "Tavor 7"]):
        Primary_optics.update({"4x C79 NV": 3, "4x M150 NV": 3, "4x SU230 NV": 3})
        if mode == 0 and any(PrimW == i for i in ["SKS", "Alpha AK", "ACE 52", "Mk 17 Mod 0"]):
            Primary_optics.update({"7x Hunting Scope NV": 2, "7x Sniper Scope NV": 2})
    elif mode == 0 and any(PrimW == i for i in ["Sterling", "Uzi", "MP5A2", "AS Val"]):
        Primary_optics.update({"4x C79 NV": 3, "4x M150 NV": 3, "4x SU230 NV": 3})
    elif mode == 0 and (PrimW == "TOZ-194" or PrimW == "M870"):
        Primary_optics.update({"4x SU230 NV": 3})
    elif any(PrimW == i for i in ["M16A4", "AUG A3", "G36K", "G3A3", "M4A1", "VHS-2", "Galil SAR", "M249", "M240B"]):
        Primary_optics.update({"4x C79 NV": 3, "4x SU230 NV": 3})
        if mode == 0:
            Primary_optics.update({"4x M150 NV": 3})
    elif any(PrimW == i for i in ["M24", "M82A1 CQ", "M110 SASS", "Mk 14 EBR"]):
        Primary_optics.update({"7x Sniper Scope NV": 2, "4x C79 NV": 3, "4x SU230 NV": 3})
        if PrimW == "M110 SASS":
            Primary_optics.update({"7x Hunting Scope NV": 2})
        if mode == 0:
            Primary_optics.update({"4x M150 NV": 3})
    elif mode == 0 and any(PrimW == i for i in ["Grease Gun", "MP5A5", "MP7", "Honey Badger"]):
        Primary_optics.update({"4x C79 NV": 3, "4x M150 NV": 3, "4x SU230 NV": 3})

x = ["explosive2", "explosive3", "Primary_optics", "Underbarrel", "Primary_barrel", "Magazine", "Siderail", "Chamber",
     "Ammo", "Miscellaneous", "Secondary_optics", "Secondary_underbarrel", "Secondary_barrel", "Secondary_Magazine",
     "Secondary_siderail", "Secondary_chamber", "Secondary_Ammo", "Stock", "Primary_training", "Secondary_training"]
random.shuffle(x)
for stuff in x:
    # Choosing random second explosive
    if stuff == "explosive2" and carrier:
        expl2, supply = ChooseItem(Explosives_SP, supply)
        exSp = Explosives_SP[expl2]
        if expl2 == "C-4" or expl2 == "IED":
            del Explosives_SP[expl2]
            if mode == 0:
                Explosives_SP.pop("M3 MAAWS", None)
                Explosives_SP.pop("RPG-7", None)
        if any(expl2 == i for i in ["Panzerfaust 3", "RPG-7", "AT4", "M3 MAAWS"]):
            Explosives_SP.pop("Panzerfaust 3", None)
            Explosives_SP.pop("RPG-7", None)
            Explosives_SP.pop("AT4", None)
            Explosives_SP.pop("M3 MAAWS", None)
            if mode == 0 and any(expl2 == j for j in ["RPG-7", "M3 MAAWS"]):
                Explosives_SP.pop("C-4", None)
        if expl2: print("Second explosive is", expl2, "(", exSp, ")")
        #print("supply points", supply)

    # Choosing random third explosive
    elif stuff == "explosive3" and carrier == "Heavy Carrier":
        expl3, supply = ChooseItem(Explosives_SP, supply)
        if expl3: print("Third explosive is", expl3, "(", Explosives_SP[expl3], ")")
        #print("supply points", supply)

    # Choosing attachments
    elif stuff == "Primary_optics" and Primary_optics:
        item, supply = ChooseItem(Primary_optics, supply)
        if PrimW == "Mosin-Nagant" and any(item == i for i in ["4x PU Scope", "2x-1x Holographic", "2x-1x Kobra", "2x-1x Red Dot",
                                                               "2x-1x MARS", "2x-1x OKP-7", "6x-3x Red Ring Scope", "7x Hunting Scope",
                                                               "7x Sniper Scope", "7x Hunting Scope NV", "7x Sniper Scope NV"]):
            Magazine = None
        if item and (PrimW == "M4A1" or PrimW == "M16A4") and item != "1x Flip Up Sights" and item != "4x C79 NV" and item !="4x M150 NV" and item != "4x SU230 NV":
            Miscellaneous = {None: 0, "Flat Top": 1}
        if item: print("Optics for main is", item, "(", Primary_optics[item], ")")
        #print("supply points", supply)

    elif stuff == "Underbarrel" and Underbarrel:
        item, supply = ChooseItem(Underbarrel, supply)
        if PrimW == "M1 Garand" and (item == "Smoke Launcher" or item == "Explosive Launcher"):
            Primary_barrel = None
        if item: print("Underbarrel for main is", item, "(", Underbarrel[item], ")")
        #print("supply points", supply)

    elif stuff == "Primary_barrel" and Primary_barrel:
        item, supply = ChooseItem(Primary_barrel, supply)
        if PrimW == "Grease Gun" and (item == "Suppressor" or item == "Advanced suppressor"):
            Underbarrel = {None: 0, "Quick draw grip": 1, "Loading grip": 2, "Aiming grip": 3, "Recoil grip": 3}
        if PrimW == "M1 Garand" and (item == "Flash Hider" or item == "Suppressor"):
            Underbarrel.pop("Smoke Launcher", None)
            Underbarrel.pop("Explosive Launcher", None)
        if item: print("Barrel for main is", item, "(", Primary_barrel[item], ")")
        #print("supply points", supply)

    elif stuff == "Magazine" and Magazine:
        item, supply = ChooseItem(Magazine, supply)
        if item == "Stripper Clip":
            for optic in ["4x PU Scope", "2x-1x Holographic", "2x-1x Kobra", "2x-1x Red Dot", "2x-1x MARS", "2x-1x OKP-7",
                          "6x-3x Red Ring Scope", "7x Hunting Scope", "7x Sniper Scope", "7x Hunting Scope NV", "7x Sniper Scope NV"]:
                Primary_optics.pop(optic, None)
        if item: print("Magazine for main is", item, "(", Magazine[item], ")")
        #print("supply points", supply)

    elif stuff == "Siderail" and Siderail:
        item, supply = ChooseItem(Siderail, supply)
        if item:
            print("Siderail for main is", item, "(", Siderail[item], ")")
            if night:
                Primary_training = {None: 0, "NVG point shooting": 0}
        #print("supply points", supply)

    elif stuff == "Chamber" and Chamber:
        item, supply = ChooseItem(Chamber, supply)
        if item: print("Chamber for main is", item, "(", Chamber[item], ")")
        #print("supply points", supply)

    elif stuff == "Ammo" and Ammo:
        item, supply = ChooseItem(Ammo, supply)
        if item: print("Ammo for main is", item, "(", Ammo[item], ")")
        #print("supply points", supply)

    elif stuff == "Miscellaneous" and Miscellaneous:
        item, supply = ChooseItem(Miscellaneous, supply)
        if item == "Flat Top":
            Optics.pop("1x Flip Up Sights", None)
            Optics.pop("4x C79 NV", None)
            Optics.pop("4x M150 NV", None)
            Optics.pop("4x SU230 NV", None)
        if item: print("Miscellaneous for main is", item, "(", Miscellaneous[item], ")")

    elif stuff == "Secondary_optics" and Secondary_optics:
        item, supply = ChooseItem(Secondary_optics, supply)
        if item: print("Optics for secondary is", item, "(", Secondary_optics[item], ")")
        #print("supply points", supply)

    elif stuff == "Secondary_underbarrel" and Secondary_underbarrel:
        item, supply = ChooseItem(Secondary_underbarrel, supply)
        if item: print("Underbarrel for secondary is", item, "(", Secondary_underbarrel[item], ")")
        #print("supply points", supply)

    elif stuff == "Secondary_barrel" and Secondary_barrel:
        item, supply = ChooseItem(Secondary_barrel, supply)
        if item: print("Barrel for secondary is", item, "(", Secondary_barrel[item], ")")
        #print("supply points", supply)

    elif stuff == "Secondary_Magazine" and Secondary_Magazine:
        item, supply = ChooseItem(Secondary_Magazine, supply)
        if item: print("Magazine for secondary is", item, "(", Secondary_Magazine[item], ")")
        #print("supply points", supply)

    elif stuff == "Secondary_siderail" and Secondary_siderail:
        item, supply = ChooseItem(Secondary_siderail, supply)
        if item:
            print("Siderail for secondary is", item, "(", Secondary_siderail[item], ")")
            if night:
                Secondary_training = {None: 0, "NVG point shooting": 0}
        #print("supply points", supply)

    elif stuff == "Secondary_chamber" and Secondary_chamber:
        item, supply = ChooseItem(Secondary_chamber, supply)
        if item: print("Chamber for secondary is", item, "(", Secondary_chamber[item], ")")
        #print("supply points", supply)

    elif stuff == "Secondary_Ammo" and Secondary_Ammo:
        item, supply = ChooseItem(Secondary_Ammo, supply)
        if item: print("Ammo for secondary is", item, "(", Secondary_Ammo[item], ")")

    elif stuff == "Stock" and Stock:
        item, supply = ChooseItem(Stock, supply)
        if item: print("Stock for secondary is", item, "(", Stock[item], ")")

    elif stuff == "Primary_training" and Primary_training:
        item, supply = ChooseItem(Primary_training, supply)
        if item: print("Training for primary is", item, "(", Primary_training[item], ")")

    elif stuff == "Secondary_training" and Secondary_training:
        item, supply = ChooseItem(Secondary_training, supply)
        if item: print("Training for secondary is", item, "(", Secondary_training[item], ")")

print("Supply points left:", supply)
