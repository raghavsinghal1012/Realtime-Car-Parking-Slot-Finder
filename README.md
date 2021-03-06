
# Realtime Car Parking Slot Finder

I made a project which is a **Real-Time Car Parking Slot Finder**. In which the mall/restaurant owners, stadium management, etc. can find the empty parking spots in their parking area. With the count of empty parking spots. This will help them in-crowd and time management. This project shows the real-time occupancies of the parking slots and can be used via their surveillance camera.

I made this compiled project in python using **OpenCV, NumPy, Pickle, CVzone, and many more python libraries**. In this project we are going to see two types of views first is the **Side Camera view** and the other is **Bird Eye camera view**.

The main idea to solve this problem is to convert the video into a binary image and count the white pixels of a frame which will be created around a single slot. The slots which will have white pixels less than the threshold white pixels count will be termed as an empty parking slot.

For the side camera view being all the parking slots in a random shape, we will start by marking the pixel coordinates around the slot and make a closed frame around it. Each frame will have its own white pixel count. After marking all the visible parking slots in the video we will warp each and every selected frame and convert the random closed shapes to a rectangle, as in a regular closed shape counting of pixels are more accurate than a random closed shape. After setting the threshold count of white pixels in a frame by try and error method now we can finally see how our video would look.

For bird-eye camera view being all the parking slots in a symmetrical shape and will look identical from the top we will make a rectangular frame. The counting of white pixels of the frames will be done in the same way we did in the side camera view. Being another angle of view threshold frequency of white pixels will differ, and will be set again in the same way it was done earlier. After that, we can see the final output of our project which is empty parking slots.




## How to run the Project
1. Clone/Download this Repository.
2. Download Python 3.7 or above in your system.
3. Open cmd and type `pip install virtualenv`. After running successfully close the cmd window.<br /> 
![Image](https://github.com/raghavsinghal1012/Realtime-Car-Parking-Slot-Finder/blob/main/Images/7.png)
4. Open cmd in the downloaded folder.
![Image](https://github.com/raghavsinghal1012/Realtime-Car-Parking-Slot-Finder/blob/main/Images/11.png)
5. Create a virtual environment in the downloaded folder.
6. Type the following in cmd in order.
    
    - `virtualenv env`
    - ```env\Scripts\activate.bat```
    - `pip install -r requirements.txt`
    
    ![Image](https://github.com/raghavsinghal1012/Realtime-Car-Parking-Slot-Finder/blob/main/Images/12.png)
### Side Camera view
1. In the same cmd window type the following
```
python "parking side view camera\sidecamera.py"
```
![Image](https://github.com/raghavsinghal1012/Realtime-Car-Parking-Slot-Finder/blob/main/Images/13.png)
2. Press `ctrl+c` in the terminal to stop the program

### Bird Eye Camera view
1. In the same cmd window type the following
```
python "parking bird eye view camera\birdeyeview.py"
```
![Image](https://github.com/raghavsinghal1012/Realtime-Car-Parking-Slot-Finder/blob/main/Images/14.png)
2. Press `ctrl+c` in the terminal to stop the program
