#!/usr/bin/env python


actI = [
    'Lioneye\'s Watch',
    'Twilight Strand', 'Coast', 'Tidal Island', 'Mud Flats', 'Fetid Pool',
    'Lower Submerged Passage', 'Flooded Depths', 'Upper Submerged Passage',
    'Ledge', 'Climb', 'Lower Prison', 'Upper Prison', 'Prisoner\'s Gate',
    'Ship Graveyard', 'Ship Graveyard Cave', 'Coves',
    'Cavern of Wrath', 'Cavern of Anger',
]
actII = [
    'Forest Encampment',
    'Southern Forest', 'Old Fields ', 'Riverways', 'Crossroads ', 'Den',
    'Fellshrine Ruins', 'Chamber of Sins Level 1', 'Chamber of Sins Level 2',
    'Chamber of Sins Level 3', 'Blackwood', 'Weaver\'s Chambers',
    'Crypt Level 1', 'Crypt Level 2', 'Broken Bridge', 'Western Forest',
    'Vaal Ruins Level 1 ', 'Vaal Ruins Level 2', 'Wetlands', 'Dread Thicket',
    'Caverns Level 1', 'Caverns Level 2', 'Ancient Pyramid',
]
actIII = [
    'Sarn Encampment',
    'City of Sarn', 'Slums', 'Crematorium', 'Slums Sewers', 'Marketplace',
    'Warehouse Sewers', 'Warehouse District ', 'Market Sewers', 'Battlefront',
    'Solaris Temple Level 1', 'Solaris Temple Level 2', 'Catacombs', 'Docks',
    'Sewer Waterway', 'Ebony Barracks', 'Lunaris Temple Level 1',
    'Lunaris Temple Level 2', 'Lunaris Temple Level 3', 'Imperial Garden',
    'Library', 'Archives', 'Hedge Maze ', 'Sceptre of God',
    'Upper Sceptre of God', 'Eternal Laboratory',
]
zonelist = ['Menu'] + actI + actII + actIII

zones = {
    'Menu': {
        'song': '',
        'pixels': [],}
    'Lioneye\'s Watch': {
        'song': '',
        'pixels': [],}
    'Twilight Strand': {
        'song': '',
        'pixels': [],}
    'Coast': {
        'song': '',
        'pixels': [],}
    'Tidal Island': {
        'song': '',
        'pixels': [],}
    'Mud Flats': {
        'song': '',
        'pixels': [],}
    'Lower Submerged Passage': {
        'song': '',
        'pixels': [],}
    'Fetid Pool ': {
        'song': '',
        'pixels': [],}
    'Upper Submerged Passage': {
        'song': '',
        'pixels': [],}
    'Flooded Depths': {
        'song': '',
        'pixels': [],}
    'Ledge': {
        'song': '',
        'pixels': [],}
    'Climb': {
        'song': '',
        'pixels': [],}
    'Lower Prison': {
        'song': '',
        'pixels': [],}
    'Upper Prison': {
        'song': '',
        'pixels': [],}
    'Prisoner\'s Gate': {
        'song': '',
        'pixels': [],}
    'Ship Graveyard': {
        'song': '',
        'pixels': [],}
    'Coves': {
        'song': '',
        'pixels': [],}
    'Ship Graveyard Cave': {
        'song': '',
        'pixels': [],}
    'Cavern of Wrath': {
        'song': '',
        'pixels': [],}
    'Cavern of Anger': {
        'song': '',
        'pixels': [],}
    'Southern Forest': {
        'song': '',
        'pixels': [],}
    'Old Fields ': {
        'song': '',
        'pixels': [],}
    'Riverways': {
        'song': '',
        'pixels': [],}
    'Crossroads ': {
        'song': '',
        'pixels': [],}
    'Den': {
        'song': '',
        'pixels': [],}
    'Fellshrine Ruins': {
        'song': '',
        'pixels': [],}
    'Chamber of Sins Level 1': {
        'song': '',
        'pixels': [],}
    'Chamber of Sins Level 2': {
        'song': '',
        'pixels': [],}
    'Chamber of Sins Level 3': {
        'song': '',
        'pixels': [],}
    'Blackwood': {
        'song': '',
        'pixels': [],}
    'Weaver\'s Chambers': {
        'song': '',
        'pixels': [],}
    'Crypt Level 1': {
        'song': '',
        'pixels': [],}
    'Crypt Level 2': {
        'song': '',
        'pixels': [],}
    'Broken Bridge': {
        'song': '',
        'pixels': [],}
    'Western Forest': {
        'song': '',
        'pixels': [],}
    'Vaal Ruins Level 1 ': {
        'song': '',
        'pixels': [],}
    'Vaal Ruins Level 2': {
        'song': '',
        'pixels': [],}
    'Wetlands': {
        'song': '',
        'pixels': [],}
    'Dread Thicket': {
        'song': '',
        'pixels': [],}
    'Caverns Level 1': {
        'song': '',
        'pixels': [],}
    'Caverns Level 2': {
        'song': '',
        'pixels': [],}
    'Ancient Pyramid': {
        'song': '',
        'pixels': [],}
    'City of Sarn': {
        'song': '',
        'pixels': [],}
    'Slums': {
        'song': '',
        'pixels': [],}
    'Crematorium': {
        'song': '',
        'pixels': [],}
    'Slums Sewers': {
        'song': '',
        'pixels': [],}
    'Marketplace': {
        'song': '',
        'pixels': [],}
    'Warehouse Sewers': {
        'song': '',
        'pixels': [],}
    'Warehouse District ': {
        'song': '',
        'pixels': [],}
    'Market Sewers': {
        'song': '',
        'pixels': [],}
    'Battlefront': {
        'song': '',
        'pixels': [],}
    'Solaris Temple Level 1': {
        'song': '',
        'pixels': [],}
    'Solaris Temple Level 2': {
        'song': '',
        'pixels': [],}
    'Catacombs': {
        'song': '',
        'pixels': [],}
    'Docks': {
        'song': '',
        'pixels': [],}
    'Sewer Waterway': {
        'song': '',
        'pixels': [],}
    'Ebony Barracks': {
        'song': '',
        'pixels': [],}
    'Lunaris Temple Level 1': {
        'song': '',
        'pixels': [],}
    'Lunaris Temple Level 2': {
        'song': '',
        'pixels': [],}
    'Lunaris Temple Level 3': {
        'song': '',
        'pixels': [],}
    'Imperial Garden': {
        'song': '',
        'pixels': [],}
    'Library': {
        'song': '',
        'pixels': [],}
    'Archives': {
        'song': '',
        'pixels': [],}
    'Hedge Maze ': {
        'song': '',
        'pixels': [],}
    'Sceptre of God': {
        'song': '',
        'pixels': [],}
    'Upper Sceptre of God': {
        'song': '',
        'pixels': [],}
    'Eternal Laboratory': {
        'song': '',
        'pixels': [],}
}
