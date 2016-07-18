import operator
import computeDistance

def get_closest_neighbours(users, user_1, dist_type):
    try:
        if dist_type == 'Manhattan':
            r = 1.0
        elif dist_type == 'Euclidean':
            r = 2.0
        else:
            r = float(dist_type)
        user_1_dict = users[str(user_1)]
    except:
        return None
    if r <= 0:
        return None
    dist = 0
    dist_dict = {}
    for key_1, value_1 in users.iteritems():
        if user_1 != key_1:
            dist_dict[key_1] = computeDistance.get_minkowski_dist(users, key_1, user_1, dist_type)
    return sorted(dist_dict.items(), key=operator.itemgetter(1))

def main():
    users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0}, "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0}, "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0}, "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0,"Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0}, "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0}, "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0}, "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0}, "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}}

    print "From following users " + str(users.keys()) + ", type a user to get nearest neighbours."
    user_1 = raw_input("First User : ")
    dist_type = raw_input("Type Manhattan to compute Manhattan distance. Type Euclidean to compute Euclidean distance or enter value of r to compute Minkowski distance specific to r : ")
    nearest_neighbours = get_closest_neighbours(users, user_1, dist_type)
    print "Nearest neighbours are : " + str(nearest_neighbours)

if __name__ == '__main__':
    main()

