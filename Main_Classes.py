##
##
##Player
##
##

##WIP
##Stats such total hp,armor class,total mana and whatever can be calculated based on level,armor,class and race stats
class Player():
    def __init__(self,player_name,player_class,player_race,level,inventory,known_spells,equiped_weapon,equiped_armor):
        self.__name = player_name
        self.__player_class = player_class
        self.__player_race = player_race
        self.__level = level
        self.__inventory = inventory
        self.__known_spells = known_spells
        self.__equiped_weapon = equiped_weapon
        self.__equiped_armor = equiped_armor

    def __init__(self,player_name,player_class,player_race):
        self.__name = player_name
        self.__player_class = player_class
        self.__player_race = player_race
        self.__level = 0
        self.__inventory = {}
        self.__known_spells = {}

    def do_action(self):
        self.__player_class.action("test")




##
##
##Races
##
##
##Race Interface
class IPlayer_Race():
    #name of the race
    _name = None
    #base hp of the race
    _base_hp = None
    #armor class of the race
    _armor_class = None
    #base initiative of the race
    _base_initiative = None

    @classmethod
    def get_race_name(cls):
        return cls._name


    @classmethod
    def get_base_hp(cls):
        return cls._base_hp

    @classmethod
    def get_armor_class(cls):
        return cls._armor_class

    @classmethod
    def get_base_initiative(cls):
        return cls._base_initiative


##
##
##Classes
##
##
##Class interface
class IPlayer_Class():

    #name of the class
    _name = None
    #base class hp
    _base_hp = None
    #stat that determines how much hp scales with level
    _constitution = None
    #stat to determine this classes resistance to damage
    _armor_class = None
    #stat that determines how quickly the player can act in a turn
    _base_initiative = None
    #stat that determines ho much initiative scales with level
    _dexterity = None
    #the base mana of the class
    _base_mana = None
    #how much the mana increases based on level
    _intelligence= None
    #what spells can this class use
    _usable_spells = []
    #what weapons this class can use
    _usable_weapons = []


    @classmethod
    def get_class_name(cls):
        return cls._name

    @classmethod
    def get_armor_class(cls):
        return cls._armor_class

    @classmethod
    def get_base_hp(cls):
        return cls._base_hp

    @classmethod
    def get_constitution(cls):
        return cls._constitution

    @classmethod
    def get_base_initiative(cls):
        return cls._base_initiative

    @classmethod
    def get_dexterity(cls):
        return cls._dexterity

    @classmethod
    def get_base_mana(cls):
        return cls._base_mana

    @classmethod
    def get_intelligence(cls):
        return cls._intelligence

    @classmethod
    def get_usable_spells(cls):
        return cls._usable_spells

    @classmethod
    def get_usable_weapons(cls):
        return cls._usable_weapons



##
##
##Items
##
##


#Item Interface
#NO ACTUAL ITEM SHOULD INHERIT THIS DIRECTLY!!!!
class IItem():
    #name of the item
    _name = None
    #value of the item
    _value = None
    #type of the item
    _type = None

    @classmethod
    def get_name(cls):
        return cls._name

    @classmethod
    def get_value(cls):
        return cls._value

    @classmethod
    def get_type(cls):
        return cls._type

#Trinket interface
class ITrinket(IItem):
    #modifier that can increase the value
    _uniqueness = None
    _type = 'Trinket'

    @classmethod
    def get_uniqueness(cls):
        return cls._uniqueness


#Weapon interface
class IWeapon(IItem):
    #damage range of the weapon
    _type = 'Weapon'
    _damage_range = (None,None)

    @classmethod
    def get_damage_range(cls):
        return cls._damage_range


# Armor interface
class IArmor(IItem):
    # how much armor this gives the player
    _ac = None
    _type = 'Armor'
    @classmethod
    def get_ac(cls):
        return cls._ac


##
##
##Spells
##
##


class ISpell():
    #How much the spell costs to cast
    _mana_cost = None
    #How much damage does the spell do.Negative values for healing spells
    _damage_range = (None,None)
    #How many targets does the spell attack
    _number_of_targets = None
    #Effects added on the target
    _added_effects = []

    @classmethod
    def get_mana_cost(cls):
        return cls._mana_cost

    @classmethod
    def get_damage_range(cls):
        return cls._damage_range

    @classmethod
    def get_number_of_targets(cls):
        return cls._number_of_targets

    @classmethod
    def get_added_effects(cls):
        return cls._added_effects