import prisoners_dilemma

####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Haxosaurus Rex' # Only 10 chars displayed.
strategy_name = 'The best strat'
# strategy_description = 'Betray the first 3 turns and after that Collude unless the other person has betrayed'
strategy_description = 'After ten moves, try and figure out what the other person is doing and copy them. Otherwise return B'

multiplyer = ""
s_id = ""

def all_same(items):
    return all(x == items[0] for x in items)

def graph_data(points):
    dist = []
    dist2 = []
    for x in range(0, len(points)-1):
        dist.append(points[x+1] - points[x])
    print dist
    dist = dist*80
    for x in range(len(points), 200):
        points.append(points[x-1] + dist[x])
    print points
    
    for x in range(0, len(points)-1):
        dist2.append(points[x+1] - points[x])
    
    if all_same(dist):
        return dist
    return "NONE"
    
    # print "Dist: " + str(dist)

def identify_trend(array, string):
    betray_index = []
    if 'b' in string:
        for x in range(len(array)):
            if array[x] is 'b':
                betray_index.append(x)
        dist = graph_data(betray_index)
        if dist is not "NONE":
            count = dist[0]
            return "LINEAR:" + str(count)
    return "UNKNOWN"
    # print "Indexs Betrayed:" + str(betray_index)
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    
    times_colluded = 0
    has_betrayed = False
    if len(my_history) >= 10 and has_betrayed is False:
        for x in range(len(my_history)):
            if their_history[x] is 'b':
                has_betrayed = True
	if has_betrayed == False: 
            return 'c'
    return 'b'
    
    
    '''
    first_ten = []
    first_ten_string = ""
   
    global s_id
    global multiplyer
    if len(their_history) >= 11:
        for x in their_history:
            first_ten.append(x)
            first_ten_string += x
        s_id = identify_trend(first_ten, first_ten_string)
        if "LINEAR" in s_id:
            colon_index = s_id.index(":")
            multiplyer = ""
            for x in range(colon_index+1, len(s_id)):
                multiplyer += s_id[x]
            multiplyer = int(float(multiplyer))
    if "LINEAR" in s_id:
        print "len: " + str(len(their_history))
        print "multi: " + str(multiplyer)
        print "div: " + str(len(their_history) % multiplyer)
        if len(their_history) % multiplyer == 0:
            print "Return b"
            return "b"
        return "c"    
    return "b"
    '''
	       
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
	#
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    print test_move(my_history='bbbbbbbbbbbb', their_history='bbcbbcbbcbbc', my_score=0, their_score=0, result='b')
    
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             