'''
Given two rectangles whose sides are parallel to the X-axis and Y-axis, 
check if they have a non-empty intersection.
If the intersection is non-empty, return the rectangle defined by 
their intersection.

Ideas:
Assume a rectangle is defined by its top left and bottom right corner
Compare the top left corners of both rectangles to find how they are
oriented relative to each other.

4 possible scenarios.
1. Rectangle A is to the top left of rectangle B. 
    -> compare bottom right corner of rectangle A and top left corner of rectangle B

2. Rectangle A is to the top right of rectangle B.
    -> compare bottom left corner of rectangle A and top right corner of rectangle B

3. Rectangle A is to the bottom left corner of rectangle B.
    -> compare top right corner of rectangle A with bottom left corner of rectangle B

4. Rectangle A is to the bottom right corner of rectangle B.
    -> compare top left corner of rectangle A with bottom right corner of rectangle B

Compares in constant time

PROBLEM: Need to add in a lot of checks to handle all the cases.

Can be simplified more to just compare the largest x of one rectangle to the smallest x of the other
and vice-versa, to see if the largest x is greater than the smallest x.

If it is true, then do the same for the y values
'''

def find_intersection(rec1, rec2):

    rec1_top_x = rec1[0][0]
    rec1_top_y = rec1[0][1]
    rec1_bot_x = rec1[1][0]
    rec1_bot_y = rec1[1][1]

    rec2_top_x = rec2[0][0]
    rec2_top_y = rec2[0][1]
    rec2_bot_x = rec2[1][0]
    rec2_bot_y = rec2[1][1]
    
    if rec1_bot_x > rec2_top_x:
        if rec1_top_y > rec2_bot_y:
            return [[rec2_top_x, rec1_top_y], [rec1_bot_x, rec2_bot_y]]
        
        if rec1_bot_y < rec2_top_y:
            return [[rec2_top_x, rec2_top_y], [rec1_bot_x, rec1_bot_y]]
        
    elif rec1_top_x < rec2_bot_x:
        if rec1_bot_y < rec2_top_y:
            return [[rec1_top_x, rec2_top_y], [rec2_bot_x, rec1_bot_y]]
        
        if rec1_top_y > rec2_bot_y:
            return [[rec1_top_x, rec1_top_y], [rec2_bot_x, rec2_bot_y]]
    
    return 0