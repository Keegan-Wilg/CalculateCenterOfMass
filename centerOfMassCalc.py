from pyfiglet import Figlet

f = Figlet(font='big')
print('\n' + f.renderText('CenterOfMass'))

def calc_center_of_mass(object_count, object_mass_list, object_location_list):
    if object_mass_list.len() or object_location_list.len() != object_count:
        raise Exception("Lists must be the same length as the amount of objects")

    total_mass = 0
    buffer_list = []
    iteration = 0
    numerator_num = 0

    for item in object_mass_list:
        try:
            total_mass += item
            buffer_list.append(object_mass_list[iteration] * object_location_list[iteration])
            iteration += 1
        except:
            raise Exception("Lists must only contain numbers")
        
    for item in object_location_list:
        try:
            item + 1
        except:
            raise Exception("Lists must only contain numbers")

    for item in buffer_list:
        numerator_num = numerator_num + item

    return numerator_num/total_mass