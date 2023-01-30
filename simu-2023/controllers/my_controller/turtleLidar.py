from controller import Lidar

class Lidar_Controller():
    def __init__(self, robot) -> None:
        self. timestep = int(robot.getBasicTimeStep())
        self.front_lidar =robot.getDevice('lidar')
        self.front_lidar.enable(self.timestep)
        self.front_lidar.enablePointCloud()





""" from controller import Lidar

class TurtleLidar(Lidar):
    def __init__(self):
        super().__init__("LDS-01")
        self.enable(timestep)


        



        
        range_image = self.getRangeImage()
        print("{}".format(range_image))

        timestep = int(self.getBasicTimeStep())

        
        Lidar.enablePointCloud(); # Enable the point cloud computation

        while self.step(timestep) != -1:
            
            lidarPoints = Lidar.getPointCloud(); # Get the point cloud

            # Print out the x, y, z, and layer information for the first point in the point cloud    
            print("x: " + str(lidarPoints[0].x) + " y: " + str(lidarPoints[0].y) + " z: " + str(lidarPoints[0].z) + " layer: " + str(lidarPoints[0].layer_id))



        







 self.__tracked_name = None
        self.__recognized_object = None

    @property
    def recognized_object(self):
        return self.__recognized_object

    def track_object(self, object_name):
        self.__tracked_name = object_name

    def is_tracked_object_on_left(self):
        obj = self.__recognized_object
        if not obj:
            return None

        obj_centos_pos = obj.get_position_on_image()[0] + int(obj.get_size_on_image()[0]/2)
        if obj_centos_pos < int(self.getWidth()/2):
            return True
        else:
            return False

    def is_tracked_object_on_right(self):
        return self.is_tracked_object_on_left() == False

    def is_tracked_object_present(self):
        objs = self.getRecognitionObjects()
        for obj in objs:
            if self.__tracked_name == obj.get_model().decode("utf-8"):
                self.__recognized_object = obj
                return True
        return False """ 