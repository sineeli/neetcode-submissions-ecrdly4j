class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_arr = [(p, s) for p, s in zip(position, speed)]

        cars_arr.sort(key=lambda x: x[0], reverse=True)
        print(cars_arr)
        time_taken = []

        for p, s in cars_arr:
            time_taken.append((target - p) / s)
        
        max_time = -1000000
        car_fleets = 0
        print(time_taken)
        for time in time_taken:
            if time > max_time:
                car_fleets += 1
                max_time = time
        
        return car_fleets


