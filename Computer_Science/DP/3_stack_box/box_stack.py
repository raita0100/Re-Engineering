def tallestStack(Boxes):

    # sort according to the length
    Boxes.sort(key = lambda x: x[0])
    # map according to the heights
    heights = {box:box[2] for box in Boxes}

    for i in range(1, len(Boxes)):
        # current box
        box = Boxes[i]
        # find set of all boxes which can be stacked on box
        S = [Boxes[j] for j in range(i) if canBeStacked(Boxes[j], box)]

        # calculate maximum height among the sets
        heights[box] = box[2] + max([heights[boxi] for boxi in S], default=0)

    return (max(heights.values(), default=0), heights)

def canBeStacked(top, bottom):
    # return true if Length and width of
    # top box are less than bottom box
    return top[0] < bottom[0] and top[1] < bottom[1]
