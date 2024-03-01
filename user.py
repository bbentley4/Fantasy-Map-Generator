import subprocess
import math

letter_values = {'A': 0, 'B': 10, 'C': 20, 'D': 30, 'E': 40, 'F': 50, 'G': 60, 'H': 70, 'I': 80, 'J': 90, 'K': 100, 'L': 110, 'M': 120, 'N': 130, 'O': 140, 'P': 150, 'Q': 160, 'R': 170, 'S': 180, 'T': 190, 'U': 200}
number_values = {'01': -70, '02': -60, '03': -50, '04': -40, '05': -30, '06': -20, '07': -10, '08': 0, '09': 10, '10': 20, '11': 30, '12': 40, '13': 50, '14': 60, '15': 70}

def main():

    output_jgr = open("map.jgr", "w")
    output_jgr.write("newgraph\nxaxis min 0 max 200 nodraw\nyaxis min -70 max 70 nodraw\n")

    print("Fantasy Map Generator")
    print("Open Grid.jpg to see what you'll be starting with. Each gridline is spaced 10 units apart.")
    print("Don't stress, the gridlines will not appear on the final result :)\n")

    input()

    print("First, pick a landscape:")
    print("1: Grassland")
    print("2: Desert")
    print("3: Islands")

    landscape = input("\t")
    
    # ---------------------------------------------------------------------------- #
    #                               GRASSLAND OPTION                               #
    # ---------------------------------------------------------------------------- #
    if landscape == '1':
        output_jgr.write("newcurve poly color 0.45 0.6 0.41 marktype none linetype solid color 0.45 0.6 0.41\npts 0 -70  200 -70  200 70  0 70")
        
        print("Lakes:")
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
            if width < 0:
                print("Width should be greater than 0.\n")
                continue

            height = int(input("Height: "))
            if height < 0: 
                print("Height should be greater than 0.\n")
                continue

            output_jgr.write(f"newcurve eps ./Lake.ps marksize {width} {height} pts {x} {y}\n")

        print("Mountains:")
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

            letter = coordinate1[0].upper()
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
            
            output_jgr.write("newcurve eps ./G_Mountains.ps marksize 15 15 pts ")
            
            mountain_size = 10
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            num_points = int(distance/mountain_size) + 1
            add_to_x = ((x2 - x1) / num_points)
            add_to_y = ((y2 - y1) / num_points)

            for i in range(num_points):
                plot_x = x1 + i * add_to_x
                plot_y = y1 + i * add_to_y
                output_jgr.write(f"{plot_x} {plot_y}  ")
            output_jgr.write(f"{x2} {y2}\n")
            
        print("Forests:")
        print("Enter the coordinate where you'd like a cluster of trees.")
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
                output_jgr.write(f"newcurve eps ./Forest.ps marksize 15 15 pts {x} {y}\n")
            else:
                print("Invalid coordinate\n")
                continue

    # ---------------------------------------------------------------------------- #
    #                                 DESERT OPTION                                #
    # ---------------------------------------------------------------------------- #
    if landscape == '2':
        output_jgr.write("newcurve poly color 0.93 0.79 0.69 marktype none linetype solid color 0.93 0.79 0.69\n\tpts 0 -70  200 -70  200 70  0 70\n")

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
            height = int(input("Height: "))
            
            if width > 0 and height > 0:
                output_jgr.write(f"newcurve eps ./Lake.ps marksize {width} {height} pts {x} {y}\n")
            else:
                print("Width and height should be greater than 0.\n")
                continue

        print("Mountains:")
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

            letter = coordinate1[0].upper()
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
            
            output_jgr.write("newcurve eps ./R_Mountains.ps marksize 15 15 pts ")
            
            mountain_size = 10
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            num_points = int(distance/mountain_size) + 1
            add_to_x = ((x2 - x1) / num_points)
            add_to_y = ((y2 - y1) / num_points)

            for i in range(num_points):
                plot_x = x1 + i * add_to_x
                plot_y = y1 + i * add_to_y
                output_jgr.write(f"{plot_x} {plot_y}  ")
            output_jgr.write(f"{x2} {y2}\n")
            
        print("Cacti:")
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
                output_jgr.write(f"newcurve eps ./Cactus.ps marksize 10 10 pts {x} {y}\n")
            else:
                print("Invalid coordinate\n")
                continue

        print("Oases:")
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
            if width < 0:
                print("Width should be greater than 0.\n")
                continue

            height = int(input("Height: "))
            if height < 0: 
                print("Height should be greater than 0.\n")
                continue

            output_jgr.write(f"newcurve eps ./Lake.ps marksize {width} {height} pts {x} {y}\n")

    # ---------------------------------------------------------------------------- #
    #                                 OCEAN OPTION                                 #
    # ---------------------------------------------------------------------------- #
    if landscape == '3':
        output_jgr.write("newcurve poly color 0.3 0.5 0.7 marktype none linetype solid color 0.3 0.5 0.7\n\tpts 0 -70  200 -70  200 70  0 70\n")

    # ---------------------------------------------------------------------------- #
    #                                  CLEANING UP                                 #
    # ---------------------------------------------------------------------------- #
        
    # ---------------------------------- Compile --------------------------------- #
    # Compile Command 1
    command1 = "jgraph -P map.jgr > map.ps"
    subprocess.run(command1, shell=True, check=True)

    # Compile Command 2
    command2_part1 = "jgraph map.jgr"
    command2_part2 = "convert -density 300 - -quality 100 map.jpg"
    process1 = subprocess.Popen(command2_part1.split(), stdout=subprocess.PIPE)
    process2 = subprocess.Popen(command2_part2.split(), stdin=process1.stdout, stdout=subprocess.PIPE)
    process1.stdout.close()  
    output, error = process2.communicate()

    # Error Check
    if error:
        print("Error in saving map:", error.decode())

    # -------------------------- Exit Message and Close -------------------------- #
    print("Your map is complete! Open map.jpg to see your finished result!\n")
    output_jgr.close()

if __name__ == "__main__":
    main()

