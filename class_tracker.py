from deep_sort_realtime import deepsort, generate_detections

class ObjectTracker:
    def __init__(self, model_path):
        self.tracker = deepsort.deepsort()
        self.encoder = generate_detections.create_box_encoder(model_path)

    def update_bbox(self, tracker_id, bbox):
        self.tracker.update(tracker_id, bbox)

    def get_bbox_position(self, tracker_id):
        position = self.tracker.get_position(tracker_id)
        return position