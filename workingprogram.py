# import pygal library
import pygal

# create a world map
worldmap = pygal.maps.world.World()

# set the title of the map
worldmap.title = 'Countries'

worldmap.tooltip_font_size = 14
worldmap.tooltip_border_radius = 10

worldmap.value_formatter = lambda x: {
    'aq': 'lol',
    'cd': 'Kinshasa',
    'de': 'Berlin',
    'eg': 'Cairo',
    'ga': 'Libreville',
    'hk': 'Hong Kong',
    'in': 'New Delhi',
    'jp': 'Tokyo',
    'nz': 'Wellington',
    'kz': 'Astana',
    'us': 'Washington DC'
}[x]

# adding the countries
worldmap.add('Random Data', {
        'aq' : 69,
        'cd' : 30,
        'de' : 40,
        'eg' : 50,
        'ga' : 45,
        'hk' : 23,
        'in' : 0,
        'jp' : 65,
        'nz' : 41,  
        'kz' : 32,
        'us' : 66
})

# save into the file
worldmap.render_to_file('worldmapresult.svg')
open('worldmapresult.svg')
print("Success")