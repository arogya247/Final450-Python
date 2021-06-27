def merge(self, intervals):
        intervals.sort()
        
        arr = []
        
        for i in intervals:
            if len(arr)==0 or arr[-1][1] < i[0]:
                arr.append(i)
            else:
                arr[-1][1] = max(arr[-1][1], i[1])
                
        return arr
