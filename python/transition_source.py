import obspython as obs

class TransitionSource:
    def __init__(self, source_name):
        self.source_name = source_name
        self.scene_item = None

    def find_source(self):
        """Finds the source in the current scene."""
        current_scene = obs.obs_frontend_get_current_scene()
        scene = obs.obs_scene_from_source(current_scene)
        self.scene_item = obs.obs_scene_find_source(scene, self.source_name)
        obs.obs_source_release(current_scene)

    def on_event(self, event):
        """Handles OBS events to show/hide or move the source."""
        if event == obs.OBS_FRONTEND_EVENT_STREAMING_STARTED or event == obs.OBS_FRONTEND_EVENT_RECORDING_STARTED:
            self.transition_on_screen()
        elif event == obs.OBS_FRONTEND_EVENT_STREAMING_STOPPED or event == obs.OBS_FRONTEND_EVENT_RECORDING_STOPPED:
            self.transition_off_screen()

    def transition_on_screen(self):
        """Transitions the source onto the screen."""
        if self.scene_item:
            obs.obs_sceneitem_set_visible(self.scene_item, True)
            print(f"{self.source_name} transitioned on screen.")

    def transition_off_screen(self):
        """Transitions the source off the screen."""
        if self.scene_item:
            obs.obs_sceneitem_set_visible(self.scene_item, False)
            print(f"{self.source_name} transitioned off screen.")

def script_load(settings):
    source_name = "Your Source Name Here"  # Replace with your source's name
    transition_source = TransitionSource(source_name)
    transition_source.find_source()

    # Register the event callback for streaming and recording
    obs.obs_frontend_add_event_callback(transition_source.on_event)

    print("Script loaded and event callbacks set.")