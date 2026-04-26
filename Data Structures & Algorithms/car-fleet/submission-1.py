class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(key=lambda x: x[0], reverse=True)

        stack = [cars[0]]
        for car in cars[1:]:
            t1 = (target - car[0]) / car[1]
            t2 = (target - stack[-1][0]) / stack[-1][1]
            print(t1, t2)
            if t1 > t2:
                stack.append(car)
        
        return len(stack)