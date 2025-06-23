import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class ScanRelay(Node):
    def __init__(self):
        super().__init__('scan_relay')
        self.sub = self.create_subscription(
            LaserScan,
            '/world/warehouse/model/turtlebot4/link/rplidar_link/sensor/rplidar/scan',
            self.relay_callback,
            10)
        self.pub = self.create_publisher(LaserScan, '/scan', 10)
        self.get_logger().info('🚀 Scan relay with frame fix started')

    def relay_callback(self, msg):
        msg.header.frame_id = 'base_scan'  # 👈 change the frame to something valid
        self.pub.publish(msg)
        self.get_logger().info('📡 Relayed with fixed frame_id: base_scan')

def main(args=None):
    rclpy.init(args=args)
    node = ScanRelay()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
