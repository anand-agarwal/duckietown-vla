#!/usr/bin/env python3

import os

import rospy
from cv_bridge import CvBridge

from duckietown.dtros import DTROS, NodeType
from sensor_msgs.msg import CompressedImage


class CameraCheckNode(DTROS):

    def __init__(self):
        super().__init__(
            node_name="camera_check_node",
            node_type=NodeType.PERCEPTION,
        )

        self.vehicle_name = os.environ["VEHICLE_NAME"]

        self.camera_topic = (
            f"/{self.vehicle_name}/camera_node/image/compressed"
        )

        self.bridge = CvBridge()

        self.subscriber = rospy.Subscriber(
            self.camera_topic,
            CompressedImage,
            self.image_callback,
            queue_size=1,
            buff_size=2**24,
        )

        rospy.loginfo(
            f"DriveVLA camera bridge listening on {self.camera_topic}"
        )

    def image_callback(self, msg):
        try:
            image = self.bridge.compressed_imgmsg_to_cv2(
                msg,
                desired_encoding="bgr8",
            )

            height, width = image.shape[:2]

            rospy.loginfo_throttle(
                2.0,
                f"Camera received: {width}x{height}, "
                f"{len(msg.data)} compressed bytes",
            )

        except Exception as exc:
            rospy.logerr_throttle(
                2.0,
                f"Could not decode camera frame: {exc}",
            )


if __name__ == "__main__":
    node = CameraCheckNode()
    rospy.spin()