
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        if veganFriendly==1:
            restaurants=list(filter(lambda x:x[2]==1,restaurants))
            # print(restaurants)
        restaurants=list(filter(lambda x:x[3]<=maxPrice,restaurants))
        restaurants=list(filter(lambda x:x[4]<=maxDistance,restaurants))
        newrestro=[]
        for i in range(len(restaurants)):
            newrestro.append([restaurants[i][0],restaurants[i][1]]) 
        newrestro.sort(key=lambda x:(x[1],x[0]),reverse=True)
        
        return list(map(lambda x:x[0],newrestro))