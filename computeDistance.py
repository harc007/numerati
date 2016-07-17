import math

def get_minkowski_dist(users, user_1, user_2, dist_type):
    try:
        if dist_type == 'Manhattan':
            r = 1.0
        elif dist_type == 'Euclidean':
            r = 2.0
        else:
            r = float(dist_type)
        user_1_dict = users[str(user_1)]
        user_2_dict = users[str(user_2)]
    except:
        return None
    if r <= 0:
        return None
    dist = 0
    for key_1, value_1 in user_1_dict.iteritems():
        for key_2, value_2 in user_2_dict.iteritems():
            if(key_1 == key_2):
                dist += math.pow(abs(value_1 - value_2), r)
                break
    dist = math.pow(dist, 1.0/r)
    return dist

def main():
    users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0}, "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0}, "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0}, "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0,"Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0}, "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0}, "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0}, "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0}, "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}}

    print "From following users " + str(users.keys()) + ", type two users to compute distance between them."
    user_1 = raw_input("First User : ")
    user_2 = raw_input("Second User : ")
    dist_type = raw_input("Type Manhattan to compute Manhattan distance. Type Euclidean to compute Euclidean distance or enter value of r to compute Minkowski distance specific to r : ")
    if type(dist_type) is str and (dist_type == 'Manhattan' or dist_type == 'Euclidean'):
        dist = get_minkowski_dist(users, user_1, user_2, dist_type = dist_type)
    else:
        dist = get_minkowski_dist(users, user_1, user_2, dist_type)
    if dist is not None:
        print "Distance is : " + str(dist)
    else:
        print "Cannot compute distance due to invalid input data"

if __name__ == '__main__':
    main()

