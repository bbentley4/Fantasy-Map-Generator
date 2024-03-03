import subprocess
import math

letter_values = {'A': 0, 'B': 10, 'C': 20, 'D': 30, 'E': 40, 'F': 50, 'G': 60, 'H': 70, 'I': 80, 'J': 90, 'K': 100, 'L': 110, 'M': 120, 'N': 130, 'O': 140, 'P': 150, 'Q': 160, 'R': 170, 'S': 180, 'T': 190, 'U': 200}
number_values = {'01': -70, '02': -60, '03': -50, '04': -40, '05': -30, '06': -20, '07': -10, '08': 0, '09': 10, '10': 20, '11': 30, '12': 40, '13': 50, '14': 60, '15': 70}

def initialize_map(file):
    file.write("""newgraph
xaxis min 0 max 200 no_auto_hash_labels hash 20 grid_lines
    hash_label at 0 : A
    hash_label at 10 : B
    hash_label at 20 : C
    hash_label at 30 : D
    hash_label at 40 : E
    hash_label at 50 : F
    hash_label at 60 : G
    hash_label at 70 : H
    hash_label at 80 : I
    hash_label at 90 : J
    hash_label at 100 : K
    hash_label at 110 : L
    hash_label at 120 : M
    hash_label at 130 : N
    hash_label at 140 : O
    hash_label at 150 : P
    hash_label at 160 : Q
    hash_label at 170 : R
    hash_label at 180 : S
    hash_label at 190 : T
    hash_label at 200 : U

yaxis min -70 max 70 no_auto_hash_labels hash 20 grid_lines
    hash_label at -70 : 1
    hash_label at -60 : 2
    hash_label at -50 : 3
    hash_label at -40 : 4
    hash_label at -30 : 5
    hash_label at -20 : 6
    hash_label at -10 : 7
    hash_label at 0 : 8
    hash_label at 10 : 9
    hash_label at 20 : 10
    hash_label at 30 : 11
    hash_label at 40 : 12
    hash_label at 50 : 13
    hash_label at 60 : 14
    hash_label at 70 : 15\n""")

def main():

    print("\n\tFantasy Map Generator\n")
    print("Are you starting a new map or editing an existing one?")
    print("1: New\n2: Edit")

    output_jgr = None
    file_choice = None
    while 1:
        file_choice = input()
        if file_choice == '1':
            output_jgr = open("map.jgr", "w")
            initialize_map(output_jgr)
            print("\nOpen Grid.jpg to see what you'll be starting with. Each gridline is spaced 10 units apart.")
            print("Don't stress, the gridlines will not appear on the final result :)\n")
            break
        elif file_choice == '2':
            print("\nOkay, we'll edit map.jgr!")
            output_jgr = open("map.jgr", "a")
            break
        else:
            print("Invalid option")
            print("1: New\n2: Edit")

    input()
    
    while 1:
        if file_choice == '1':
            print("\nFirst, pick a landscape:")
        else:
            print ("\nWhich type were you working on?")
        print("1: Grassland")
        print("2: Desert")
        print("3: Islands")

        landscape = input()
        
        # ---------------------------------------------------------------------------- #
        #                               GRASSLAND OPTION                               #
        # ---------------------------------------------------------------------------- #
        if landscape == '1':
           
            if file_choice == '1':
                output_jgr.write("\nnewcurve poly color 0.45 0.6 0.41 marktype none linetype solid color 0.45 0.6 0.41\npts 0 -70  200 -70  200 70  0 70\n")
            
            print("\n\tLakes:")
            print("Enter the coordinate, as well as the width and height.")
            print("When you're done, type X when prompted for the coordinate.\n")

            while 1:
                coordinate = input("Coordinate: ")

                if coordinate == 'X' or coordinate == 'x':
                    break

                if len(coordinate) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate[0].upper()
                number = coordinate[1:]

                if letter in letter_values and number in number_values:
                    x = letter_values[letter]
                    y = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue
                
                width = int(input("Width: "))
                if width < 0 and width > 200:
                    print("Width should be greater than 0 & less than 200.\n")
                    continue

                height = int(input("Height: "))
                if height < 0 and height > 140: 
                    print("Height should be greater than 0 and less than 140.\n")
                    continue

                output_jgr.write(f"\nnewcurve eps ./Icons/Lake.ps marksize {width} {height} pts {x} {y}\n")

            print("\n\tMountains:")
            print("Enter the coordinates for the beginning and end of the mountain range.")
            print("When you're done, type X when prompted for the first coordinate.\n")

            while 1:
                x1 = None
                x2 = None
                y1 = None
                y2 = None
                coordinate1 = input("Coordinate 1: ")

                if coordinate1 == 'X' or coordinate1 == 'x':
                    break

                if len(coordinate1) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate1[0]
                number = coordinate1[1:]

                if letter in letter_values and number in number_values:
                    x1 = letter_values[letter]
                    y1 = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue
                
                coordinate2 = input("Coordinate 2: ")

                if len(coordinate2) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate2[0]
                number = coordinate2[1:]

                if letter in letter_values and number in number_values:
                    x2 = letter_values[letter]
                    y2 = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue
                
                mountain_size = 10
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                num_points = int(distance/mountain_size) + 1
                add_to_x = ((x2 - x1) / num_points)
                add_to_y = ((y2 - y1) / num_points)

                for i in range(num_points):
                    plot_x = x1 + i * add_to_x
                    plot_y = y1 + i * add_to_y
                    output_jgr.write(f"\nnewcurve eps ./Icons/G_Mountains.ps marksize 15 15 pts {plot_x} {plot_y}")
                output_jgr.write(f"\nnewcurve eps ./Icons/G_Mountains.ps marksize 15 15 pts {x2} {y2}\n")
                
            print("\n\tForests:")
            print("Enter the coordinate where you'd like a cluster of trees.")
            print("When you're done, type X when prompted for the coordinate.\n")

            while 1:
                coordinate = input("Coordinate: ")

                if coordinate == 'X' or coordinate == 'x':
                    break

                if len(coordinate) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate[0]
                number = coordinate[1:]

                if letter in letter_values and number in number_values:
                    x = letter_values[letter]
                    y = number_values[number] 
                    output_jgr.write(f"\nnewcurve eps ./Icons/Forest.ps marksize 15 15 pts {x} {y}\n")
                else:
                    print("Invalid coordinate\n")
                    continue
            
            print ("\n\tTerritories:")
            print("For now, we'll just draw lines, and label when we're done.")
            print("Enter the coordinates (e.g. E05) for the beginning and end of each line.")
            print("If necessary, draw the lines, quit the program, look at your map, then come back to edit!")

            while 1:
                x1 = None
                x2 = None
                y1 = None
                y2 = None
                coordinate1 = input("Coordinate 1: ")

                if coordinate1 == 'X' or coordinate1 == 'x':
                    break

                if len(coordinate1) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate1[0]
                number = coordinate1[1:]

                if letter in letter_values and number in number_values:
                    x1 = letter_values[letter]
                    y1 = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue
                
                coordinate2 = input("Coordinate 2: ")

                if len(coordinate2) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate2[0]
                number = coordinate2[1:]

                if letter in letter_values and number in number_values:
                    x2 = letter_values[letter]
                    y2 = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue
                
                output_jgr.write(f"\nnewcurve marktype none linetype solid linethickness 1 pts {x1} {y1}  {x2} {y2}\n")

            print("\n\tLabels:")
            print("Enter the coordinate that you want the label to begin and the label.")
            print("Keep in mind, the character in the middle of the string will be placed at the coordinate you select.")
            print("When you're done, type X when prompted for the coordinate.\n")

            while 1:
                coordinate = input("Coordinate: ")

                if coordinate == 'X' or coordinate == 'x':
                    break

                if len(coordinate) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate[0]
                number = coordinate[1:]

                if letter in letter_values and number in number_values:
                    x = letter_values[letter]
                    y = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue

                # New while loop so user doesn't have to redo coordinate if they mess up label
                while 1:
                    font_size = int(input("Font Size: "))
                    if font_size < 3 or font_size > 12:
                        print("5 is the minimum; 12 is the maximum.\n")
                        continue

                    label = input("Label: ")
                    if (len(label) > 30):
                        print("Please keep label under 30 characters.\n")
                        continue
                    break

                output_jgr.write(f"\nnewstring hjc vjc x {x} y {y}\nfontsize {font_size} font Courier : {label}\n")
                    
            break
        # ---------------------------------------------------------------------------- #
        #                                 DESERT OPTION                                #
        # ---------------------------------------------------------------------------- #
        elif landscape == '2':
            
            if file_choice == '1':
                output_jgr.write("\nnewcurve poly color 0.93 0.79 0.69 marktype none linetype solid color 0.93 0.79 0.69\n\tpts 0 -70  200 -70  200 70  0 70\n")

            print("\n\tMountains:")
            print("Enter the coordinates for the beginning and end of the mountain range.")
            print("When you're done, simply type X when prompted for the first coordinate.\n")

            while 1:
                x1 = None
                x2 = None
                y1 = None
                y2 = None
                coordinate1 = input("Coordinate 1: ")

                if coordinate1 == 'X' or coordinate1 == 'x':
                    break

                if len(coordinate1) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate1[0]
                number = coordinate1[1:]

                if letter in letter_values and number in number_values:
                    x1 = letter_values[letter]
                    y1 = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue
                
                coordinate2 = input("Coordinate 2: ")

                if len(coordinate2) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate2[0].upper()
                number = coordinate2[1:]

                if letter in letter_values and number in number_values:
                    x2 = letter_values[letter]
                    y2 = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue
                
                mountain_size = 10
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                num_points = int(distance/mountain_size) + 1
                add_to_x = ((x2 - x1) / num_points)
                add_to_y = ((y2 - y1) / num_points)

                for i in range(num_points):
                    plot_x = x1 + i * add_to_x
                    plot_y = y1 + i * add_to_y
                    output_jgr.write(f"\nnewcurve eps ./Icons/R_Mountains.ps marksize 15 15 pts {plot_x} {plot_y}")
                output_jgr.write(f"\nnewcurve eps ./Icons/R_Mountains.ps marksize 15 15 pts {x2} {y2}\n")
                
            print("\n\tCacti:")
            print("Enter the coordinate where you'd like a cactus.")
            print("When you're done, simply type X when prompted for the coordinate.\n")

            while 1:
                coordinate = input("Coordinate: ")

                if coordinate == 'X' or coordinate == 'x':
                    break

                if len(coordinate) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate[0].upper()
                number = coordinate[1:]

                if letter in letter_values and number in number_values:
                    x = letter_values[letter]
                    y = number_values[number] 
                    output_jgr.write(f"\nnewcurve eps ./Icons/Cactus.ps marksize 5 5 pts {x} {y}\n")
                else:
                    print("Invalid coordinate\n")
                    continue

            print("\n\tOases:")
            print("Enter the coordinate, as well as the width and height.")
            print("When you're done, type X when prompted for the coordinate.\n")

            while 1:
                coordinate = input("Coordinate: ")

                if coordinate == 'X' or coordinate == 'x':
                    break

                if len(coordinate) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate[0]
                number = coordinate[1:]

                if letter in letter_values and number in number_values:
                    x = letter_values[letter]
                    y = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue
                
                width = int(input("Width: "))
                if width < 0:
                    print("Width should be greater than 0.\n")
                    continue

                height = int(input("Height: "))
                if height < 0: 
                    print("Height should be greater than 0.\n")
                    continue

                output_jgr.write(f"\nnewcurve eps ./Icons/Lake.ps marksize {width} {height} pts {x} {y}\n")

            print ("\n\tTerritories:")
            print("For now, we'll just draw lines, and label when we're done.")
            print("Enter the coordinates (e.g. E05) for the beginning and end of each line.")
            print("If necessary, draw the lines, quit the program, look at your map, then come back to edit!")

            while 1:
                x1 = None
                x2 = None
                y1 = None
                y2 = None
                coordinate1 = input("Coordinate 1: ")

                if coordinate1 == 'X' or coordinate1 == 'x':
                    break

                if len(coordinate1) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate1[0]
                number = coordinate1[1:]

                if letter in letter_values and number in number_values:
                    x1 = letter_values[letter]
                    y1 = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue
                
                coordinate2 = input("Coordinate 2: ")

                if len(coordinate2) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate2[0]
                number = coordinate2[1:]

                if letter in letter_values and number in number_values:
                    x2 = letter_values[letter]
                    y2 = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue
                
                output_jgr.write("\nnewcurve marktype none linetype solid linethickness 1 pts {x1} {y1}  {x2} {y2}\n")

            print("\n\tLabels:")
            print("Enter the coordinate that you want the label to begin and the label.")
            print("Keep in mind, the leftmost character of the string will be placed at the coordinate you select.")
            print("When you're done, type X when prompted for the coordinate.\n")

            while 1:
                coordinate = input("Coordinate: ")

                if coordinate == 'X' or coordinate == 'x':
                    break

                if len(coordinate) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate[0]
                number = coordinate[1:]

                if letter in letter_values and number in number_values:
                    x = letter_values[letter]
                    y = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue

                # New while loop so user doesn't have to redo coordinate if they mess up label
                while 1:
                    font_size = int(input("Font Size: "))
                    if font_size < 3 or font_size > 12:
                        print("5 is the minimum; 12 is the maximum.\n")
                        continue

                    label = input("Label: ")
                    if (len(label) > 30):
                        print("Please keep label under 30 characters.\n")
                        continue
                    break

                output_jgr.write(f"\nnewstring hjl vjc x {x} y {y}\nfontsize {font_size} font Courier : {label}\n")
            
            break
        # ---------------------------------------------------------------------------- #
        #                                 OCEAN OPTION                                 #
        # ---------------------------------------------------------------------------- #
        elif landscape == '3':
            
            if file_choice == '1':
                output_jgr.write("\nnewcurve poly color 0.3 0.5 0.7 marktype none linetype solid color 0.3 0.5 0.7\n\tpts 0 -70  200 -70  200 70  0 70\n")
            
            print("\n\tIslands:")
            print("Enter the coordinate (e.g. E05), as well as the width and height.")
            print("When you're done, type X when prompted for the coordinate.\n")

            while 1:
                coordinate = input("Coordinate: ")

                if coordinate == 'X' or coordinate == 'x':
                    break

                if len(coordinate) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate[0].upper()
                number = coordinate[1:]

                if letter in letter_values and number in number_values:
                    x = letter_values[letter]
                    y = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue
                
                width = int(input("Width: "))
                if width < 0 and width > 200:
                    print("Width should be greater than 0 & less than 200.\n")
                    continue

                height = int(input("Height: "))
                if height < 0 and height > 140: 
                    print("Height should be greater than 0 and less than 140.\n")
                    continue

                output_jgr.write(f"\nnewcurve eps ./Icons/Island.ps marksize {width} {height} pts {x} {y}\n")

            print("\n\tLakes:")
            print("Enter the coordinate, as well as the width and height.")
            print("When you're done, type X when prompted for the coordinate.\n")

            while 1:
                coordinate = input("Coordinate: ")

                if coordinate == 'X' or coordinate == 'x':
                    break

                if len(coordinate) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate[0].upper()
                number = coordinate[1:]

                if letter in letter_values and number in number_values:
                    x = letter_values[letter]
                    y = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue
                
                width = int(input("Width: "))
                if width < 0 and width > 200:
                    print("Width should be greater than 0 & less than 200.\n")
                    continue

                height = int(input("Height: "))
                if height < 0 and height > 140: 
                    print("Height should be greater than 0 and less than 140.\n")
                    continue

                output_jgr.write(f"\nnewcurve eps ./Icons/Lake.ps marksize {width} {height} pts {x} {y}\n")

            print("\n\tPalm Trees:")
            print("Enter the coordinate where you'd like a cactus.")
            print("When you're done, simply type X when prompted for the coordinate.\n")

            while 1:
                coordinate = input("Coordinate: ")

                if coordinate == 'X' or coordinate == 'x':
                    break

                if len(coordinate) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate[0].upper()
                number = coordinate[1:]

                if letter in letter_values and number in number_values:
                    x = letter_values[letter]
                    y = number_values[number] 
                    output_jgr.write(f"\nnewcurve eps ./Icons/PalmTree.ps marksize 5 5 pts {x} {y}\n")
                else:
                    print("Invalid coordinate\n")
                    continue
            
            print("\n\tMountains:")
            print("Enter the coordinates for the beginning and end of the mountain range.")
            print("When you're done, type X when prompted for the first coordinate.\n")

            while 1:
                x1 = None
                x2 = None
                y1 = None
                y2 = None
                coordinate1 = input("Coordinate 1: ")

                if coordinate1 == 'X' or coordinate1 == 'x':
                    break

                if len(coordinate1) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate1[0]
                number = coordinate1[1:]

                if letter in letter_values and number in number_values:
                    x1 = letter_values[letter]
                    y1 = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue
                
                coordinate2 = input("Coordinate 2: ")

                if len(coordinate2) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate2[0]
                number = coordinate2[1:]

                if letter in letter_values and number in number_values:
                    x2 = letter_values[letter]
                    y2 = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue
                
                mountain_size = 10
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                num_points = int(distance/mountain_size) + 1
                add_to_x = ((x2 - x1) / num_points)
                add_to_y = ((y2 - y1) / num_points)

                for i in range(num_points):
                    plot_x = x1 + i * add_to_x
                    plot_y = y1 + i * add_to_y
                    output_jgr.write(f"\nnewcurve eps ./Icons/G_Mountains.ps marksize 15 15 pts {plot_x} {plot_y}")
                output_jgr.write(f"\nnewcurve eps ./Icons/G_Mountains.ps marksize 15 15 pts {x2} {y2}\n")
            
            print("\n\tLabels:")
            print("Enter the coordinate that you want the label to begin and the label.")
            print("Keep in mind, the character in the middle of the string will be placed at the coordinate you select.")
            print("When you're done, type X when prompted for the coordinate.\n")

            while 1:
                coordinate = input("Coordinate: ")

                if coordinate == 'X' or coordinate == 'x':
                    break

                if len(coordinate) != 3:
                    print("Invalid coordinate\n")
                    continue

                letter = coordinate[0]
                number = coordinate[1:]

                if letter in letter_values and number in number_values:
                    x = letter_values[letter]
                    y = number_values[number] 
                else:
                    print("Invalid coordinate\n")
                    continue

                # New while loop so user doesn't have to redo coordinate if they mess up label
                while 1:
                    font_size = int(input("Font Size: "))
                    if font_size < 3 or font_size > 12:
                        print("5 is the minimum; 12 is the maximum.\n")
                        continue

                    label = input("Label: ")
                    if (len(label) > 30):
                        print("Please keep label under 30 characters.\n")
                        continue
                    break

                output_jgr.write(f"\nnewstring hjc vjc x {x} y {y}\nfontsize {font_size} font Courier : {label}\n")

            break
        # ---------------------------------------------------------------------------- #
        #                                INVALID OPTION                                #
        # ---------------------------------------------------------------------------- #
        else:
            print ("Invalid Option\n")
            print("1: Grassland")
            print("2: Desert")
            print("3: Islands")
            continue
    # ---------------------------------------------------------------------------- #
    #                                     END                                      #
    # ---------------------------------------------------------------------------- #

    # -------------------------- Exit Message and Close -------------------------- #
    print("\nYour map is complete!\nCompile using this command:\n\n\tjgraph map.jgr |  convert -density 300 - -quality 100 map.jpg\n\nThen open map.jpg to see your finished result!\n")
    output_jgr.close()

if __name__ == "__main__":
    main()

