obs = obslua

-- Define the source name
source_name = "Prism Mobile Source"

-- Function to set the visibility of the source
function set_source_visibility(visible)
    local source = obs.obs_get_source_by_name(source_name)
    if source then
        local scene_item = obs.obs_scene_find_source(obs.obs_scene_from_source(obs.obs_frontend_get_current_scene()), source_name)
        if scene_item then
            obs.obs_sceneitem_set_visible(scene_item, visible)
        end
        obs.obs_source_release(source)
    end
end

-- Function to check if the source is broadcasting
function is_broadcasting()
    local source = obs.obs_get_source_by_name(source_name)
    if source then
        -- Check if the source is active
        local is_active = obs.obs_source_active(source)
        obs.obs_source_release(source)
        return is_active
    end
    return false
end

-- Timer callback to monitor broadcasting status
function monitor_broadcasting()
    if is_broadcasting() then
        set_source_visibility(true)
    else
        set_source_visibility(false)
    end
end

-- Script load function
function script_load(settings)
    -- Set a timer to check the broadcasting status every second
    obs.timer_add(monitor_broadcasting, 1000)
end

-- Script unload function
function script_unload()
    -- Remove the timer when the script is unloaded
    obs.timer_remove(monitor_broadcasting)
end