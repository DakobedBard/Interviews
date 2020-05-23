

def partitionLabels(s):
    if not s or len(s) ==0:
        return None
    lastindics = [0] * 26

    output_arr = []

    for i,char in enumerate(s):
        lastindics[ord(char)- ord('a')] = i
    start = 0
    end = 0
    for i, c in enumerate(s):
        end= max(end, lastindics[ord(c) - ord('a')])
        if i == end:
            output_arr.append(end-start+1)
            start = end+1
    return output_arr

s = "ababcbacadefegdehijhklij"
a  = partitionLabels(s)