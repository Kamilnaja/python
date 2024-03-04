"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    return azara_record[1] == str(rui_record[1][0] + str(rui_record[1][1]))


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return 'not a match'


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """

    res = ''
    for _, item in enumerate(combined_record_group):
        res += (f"('{item[0]}', '{item[2]}', {item[3]}, '{item[4]}')\n")
    return res


print(
    clean_up((
        ('Scrimshawed Whale Tooth', '2A', 'Deserted Docks', ('2', 'A'), 'Blue'),
        ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'),
        ('Robot Parrot', '1C', 'Seaside Cottages', ('1', 'C'), 'Blue'),
        ('Glass Starfish', '6D', 'Tangled Seaweed Patch', ('6', 'D'), 'Orange'),
        ('Vintage Pirate Hat', '7E',
         'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'),
        ('Pirate Flag', '7F', 'Windswept Hilltop (Island of Mystery)',
         ('7', 'F'), 'Orange'),
        ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'),
        ('Model Ship in Large Bottle', '8A',
         'Harbor Managers Office', ('8', 'A'), 'Purple'),
        ('Angry Monkey Figurine', '5B',
         'Stormy Breakwater', ('5', 'B'), 'Purple'),
        ('Carved Wooden Elephant', '8C',
         'Foggy Seacave', ('8', 'C'), 'Purple'),
        ('Amethyst  Octopus', '1F',
         'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow'),
        ('Antique Glass Fishnet Float', '3D',
         'Spiky Rocks', ('3', 'D'), 'Yellow'),
        ('Silver Seahorse', '4E',
         'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')
    ))
)


input_data = (
    ('Scrimshawed Whale Tooth', '2A', 'Deserted Docks', ('2', 'A'), 'Blue'),
    ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'),
    ('Robot Parrot', '1C', 'Seaside Cottages', ('1', 'C'), 'Blue'),
    ('Glass Starfish', '6D', 'Tangled Seaweed Patch', ('6', 'D'), 'Orange'),
    ('Vintage Pirate Hat', '7E',
     'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'),
    ('Pirate Flag', '7F', 'Windswept Hilltop (Island of Mystery)',
     ('7', 'F'), 'Orange'),
    ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'),
    ('Model Ship in Large Bottle', '8A',
     'Harbor Managers Office', ('8', 'A'), 'Purple'),
    ('Angry Monkey Figurine', '5B',
     'Stormy Breakwater', ('5', 'B'), 'Purple'),
    ('Carved Wooden Elephant', '8C',
     'Foggy Seacave', ('8', 'C'), 'Purple'),
    ('Amethyst  Octopus', '1F',
     'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow'),
    ('Antique Glass Fishnet Float', '3D',
     'Spiky Rocks', ('3', 'D'), 'Yellow'),
    ('Silver Seahorse', '4E',
     'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')
)

result_data = """('Scrimshawed Whale Tooth', 'Deserted Docks', ('2', 'A'), 'Blue')\n\
('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')\n\
('Robot Parrot', 'Seaside Cottages', ('1', 'C'), 'Blue')\n\
('Glass Starfish', 'Tangled Seaweed Patch', ('6', 'D'), 'Orange')\n\
('Vintage Pirate Hat', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')\n\
('Pirate Flag', 'Windswept Hilltop (Island of Mystery)', ('7', 'F'), 'Orange')\n\
('Crystal Crab', 'Old Schooner', ('6', 'A'), 'Purple')\n\
('Model Ship in Large Bottle', 'Harbor Managers Office', ('8', 'A'), 'Purple')\n\
('Angry Monkey Figurine', 'Stormy Breakwater', ('5', 'B'), 'Purple')\n\
('Carved Wooden Elephant', 'Foggy Seacave', ('8', 'C'), 'Purple')\n\
('Amethyst  Octopus', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')\n\
('Antique Glass Fishnet Float', 'Spiky Rocks', ('3', 'D'), 'Yellow')\n\
('Silver Seahorse', 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')\n"""

assert clean_up(input_data) == result_data
