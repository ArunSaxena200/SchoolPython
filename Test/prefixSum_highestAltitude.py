def largestAltitude(self, gain) -> int:
        """
        gain = [-5,1,5,0,-7]
        curr_altitude = 0
        highest_point = curr_altitude
        for i in range(len(gain)):

        """
        curr_altitude = 0
        highest_point = curr_altitude
        for i in range(len(gain)):
            curr_altitude = curr_altitude+ gain[i]
            highest_point  = max(highest_point,curr_altitude)
        return highest_point