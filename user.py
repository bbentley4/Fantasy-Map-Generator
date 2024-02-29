import subprocess
import math

letter_values = {'A': 0, 'B': 10, 'C': 20, 'D': 30, 'E': 40, 'F': 50, 'G': 60, 'H': 70, 'I': 80, 'J': 90, 'K': 100, 'L': 110, 'M': 120, 'N': 130, 'O': 140, 'P': 150, 'Q': 160, 'R': 170, 'S': 180, 'T': 190, 'U': 200}
number_values = {'01': -70, '02': -60, '03': -50, '04': -40, '05': -30, '06': -20, '07': -10, '08': 0, '09': 10, '10': 20, '11': 30, '12': 40, '13': 50, '14': 60, '15': 70}
    
def main():

    output_jgr = "map.jgr"
    output_jgr = open(output_jgr, "w")
    output_jgr.write("""newgraph
xaxis min -0 max 200 nodraw
yaxis min -70 max 70 nodraw
                     
""")

    print("Fantasy Map Generator")
    print("Open Grid.jpg to see what you'll be starting with. Each gridline is spaced 10 units apart.")
    print("Don't stress, the gridlines will not appear on the final result :)\n")

    input()

    print("First, pick a landscape:")
    print("1: Grassland")
    print("2: Desert")
    print("3: Islands")

    landscape = input()
    
    if landscape == '1':
        output_jgr.write("""newcurve poly color 0.45 0.6 0.41 marktype none linetype solid color 0.45 0.6 0.41
    pts 0 -70  200 -70  200 70  0 70
    """)
        
        print ("Let's start by defining the territories.")
        
        print("Next, we'll place the lakes.")
        print("Enter the coordinate (e.g. E05), as well as the width and height (e.g. 10).")
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
            else:
                print("Invalid coordinate\n")
                continue
            
            width = int(input("Width: "))
            height = int(input("Height: "))
            
            if width > 0 and height > 0:
                output_jgr.write(f"newcurve eps ./Lake.ps marksize {width} {height} pts {x} {y}")
                output_jgr.write("""
                """)
            else:
                print("Width and height should be greater than 0.\n")
                continue

        print("Next, we'll add mountains.")
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
            
            output_jgr.write("newcurve eps ./G_Mountains.ps marksize 15 15 pts ")
            
            mountain_size = 10
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            num_points = distance/mountain_size + 1
            add_to_x = (x2 - x1) / num_points
            add_to_y = (y2 - y1) / num_points

            for i in range(num_points):
                output_jgr(f"{x1 + i * add_to_x} {y1 + i * add_to_y}  ")
            output_jgr(f"{x2} {y2}")
            output_jgr("""
                       """)
            
        print("Next, we'll add forests.")
        print("Enter the coordinate where you'd like a cluster of trees.")
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
                output_jgr.write(f"newcurve eps ./Forest.ps marksize 15 15 pts {x} {y}")
                output_jgr.write("""
                """)
            else:
                print("Invalid coordinate\n")
                continue

        print("Next, we'll add rivers.")
        print("Enter the coordinates for the beginning and end of the river and how wide you'd like the river.")
        print("Additionally, enter the direction the river is running.")
        print("When you're done, simply type X when prompted for the coordinate.\n")

        while 1:
            x1 = None
            x2 = None
            y1 = None
            y2 = None
            width = None

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

            width = input("Width: ")
            if (width < 0):
                print ("Invalid width (must be greater than 0)")
                continue
            
            print("1: Northeast-Southwest")
            print("2: Northwest-SouthEast")
            print("3: East-West")
            print("4: North-South")

            direction = input()
            if direction == '1':
                output_jgr.write("newcurve eps ./RiverNE.ps marksize ")
            if direction == '2':
                output_jgr.write("newcurve eps ./RiverNW.ps marksize ")
            if direction == '3':
                output_jgr.write("newcurve eps ./RiverEW.ps marksize ")
            if direction == '4':
                output_jgr.write("newcurve eps ./RiverNS.ps marksize ")
        
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            #River stretches both ways so I have to plot it at the midpoint
            midpoint_x = (x1 + x2) / 2
            midpoint_y = (y1 + y2) / 2

            output_jgr(f"{width} {distance} pts {midpoint_x} {midpoint_y}")
            output_jgr("""
                       """)

    
    
    
    
    output_jgr.close()

if __name__ == "__main__":
    main()

